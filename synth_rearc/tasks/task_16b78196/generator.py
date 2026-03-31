from synth_rearc.core import *

from .helpers import (
    GROUP_SPECS_16B78196,
    make_object_16b78196,
    place_group_16b78196,
    template_group_16b78196,
)


def _group_colors_16b78196(
    spec_name: str,
    pool: list[Integer],
) -> tuple[Integer, ...]:
    if spec_name == "vertical_bottom_a" and choice((T, F)):
        x0 = pool.pop()
        x1 = pool.pop()
        return (x0, x1, x0)
    x2 = len(GROUP_SPECS_16B78196[spec_name]["templates"])
    return tuple(pool.pop() for _ in range(x2))


def _rectangle_cells_16b78196(
    upper_left: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = upper_left
    x2, x3 = dims
    return frozenset((i, j) for i in range(x0, add(x0, x2)) for j in range(x1, add(x1, x3)))


def _scatter_objects_16b78196(
    objs: tuple[Object, ...],
    forbidden: Indices,
    dims: IntegerTuple,
) -> tuple[Object, ...] | None:
    x0 = set(forbidden)
    x1 = set(forbidden)
    for x2 in forbidden:
        x1 |= neighbors(x2)
    x3 = list(objs)
    shuffle(x3)
    x4: list[Object] = []
    x5, x6 = dims
    for x7 in x3:
        x8 = normalize(x7)
        x9 = height(x8)
        x10 = width(x8)
        x11 = [(i, j) for i in range(add(x5, ONE - x9)) for j in range(add(x6, ONE - x10))]
        shuffle(x11)
        x12 = None
        for x13 in x11:
            x14 = shift(x8, x13)
            x15 = toindices(x14)
            if x15 & x1:
                continue
            x12 = x14
            break
        if x12 is None:
            return None
        x4.append(x12)
        x16 = toindices(x12)
        x0 |= x16
        for x17 in x16:
            x1.add(x17)
            x1 |= neighbors(x17)
    return tuple(x4)


def _distinct_offsets_16b78196(
    limit_a: Integer,
    limit_b: Integer,
    sep: Integer,
) -> tuple[Integer, Integer]:
    for _ in range(100):
        x0 = randint(ZERO, limit_a)
        x1 = randint(ZERO, limit_b)
        if abs(subtract(x0, x1)) >= sep:
            return x0, x1
    return randint(ZERO, limit_a), randint(ZERO, limit_b)


def _interval_overlaps_16b78196(
    start: Integer,
    span: Integer,
    reserved: tuple[tuple[Integer, Integer], ...],
) -> Boolean:
    x0 = add(start, span)
    for x1, x2 in reserved:
        x3 = add(x1, x2)
        if both(start < x3, x1 < x0):
            return T
    return F


def _boundary_noise_16b78196(
    axis: str,
    anchor_ul: IntegerTuple,
    anchor_dims: IntegerTuple,
    reserved: dict[str, tuple[tuple[Integer, Integer], ...]],
) -> Indices:
    x0, x1 = anchor_ul
    x2, x3 = anchor_dims
    x4 = set()
    if axis == "vertical":
        x5 = {
            "single": frozenset({(ZERO, ZERO)}),
            "hpair": frozenset({(ZERO, ZERO), (ZERO, ONE)}),
            "vpair": frozenset({(ZERO, ZERO), (ONE, ZERO)}),
        }
        for x6 in ("top", "bottom"):
            if reserved.get(x6):
                continue
            for _ in range(choice((ZERO, ONE, ONE, TWO))):
                x7 = choice(("single", "single", "hpair", "vpair"))
                x8 = x5[x7]
                x9 = max(j for _, j in x8)
                x10 = False
                for _ in range(40):
                    x11 = randint(ZERO, subtract(x3, increment(x9)))
                    if _interval_overlaps_16b78196(x11, increment(x9), reserved.get(x6, ())):
                        continue
                    x12 = set()
                    for i, j in x8:
                        x13 = add(x0, i) if x6 == "top" else subtract(add(x0, decrement(x2)), i)
                        x12.add((x13, add(x1, add(x11, j))))
                    if x12 & x4:
                        continue
                    x4 |= x12
                    x10 = True
                    break
                if not x10:
                    continue
        return frozenset(x4)
    x5 = {
        "single": frozenset({(ZERO, ZERO)}),
        "vpair": frozenset({(ZERO, ZERO), (ONE, ZERO)}),
        "hpair": frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    }
    for x6 in ("left", "right"):
        if reserved.get(x6):
            continue
        for _ in range(choice((ZERO, ONE, ONE, TWO))):
            x7 = choice(("single", "single", "vpair", "hpair"))
            x8 = x5[x7]
            x9 = max(i for i, _ in x8)
            x10 = False
            for _ in range(40):
                x11 = randint(ZERO, subtract(x2, increment(x9)))
                if _interval_overlaps_16b78196(x11, increment(x9), reserved.get(x6, ())):
                    continue
                x12 = set()
                for i, j in x8:
                    x13 = add(x1, j) if x6 == "left" else subtract(add(x1, decrement(x3)), j)
                    x12.add((add(x0, add(x11, i)), x13))
                if x12 & x4:
                    continue
                x4 |= x12
                x10 = True
                break
            if not x10:
                continue
    return frozenset(x4)


def generate_16b78196(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("vertical", "vertical", "horizontal"))
        x1 = list(range(ONE, TEN))
        shuffle(x1)
        x2 = x1.pop()
        if x0 == "vertical":
            x3 = choice(("vertical_bottom_a", "vertical_bottom_b"))
            x4 = choice((T, T, F)) if x3 == "vertical_bottom_a" else choice((T, F, F))
            x5 = [x3]
            if x4:
                x5.append("vertical_top")
        else:
            x5 = ["horizontal_left", "horizontal_right"]
        x6 = tuple(template_group_16b78196(name, _group_colors_16b78196(name, x1)) for name in x5)
        if x0 == "vertical":
            x7 = max(group["span"] for group in x6)
            x8 = max((subtract(group["length"], len(group["contact"])) for group in x6 if group["side"] == "top"), default=ZERO)
            x9 = max((subtract(group["length"], len(group["contact"])) for group in x6 if group["side"] == "bottom"), default=ZERO)
            x10 = randint(max(18, add(x7, 8)), 30)
            x11 = randint(5, 7)
            if add(x8, add(x11, x9)) > 30:
                continue
            x12 = randint(x8, subtract(subtract(30, x11), x9))
            x13 = randint(ZERO, subtract(30, x10))
            x14 = {}
            if both("vertical_top" in x5, x10 > 5):
                x14["vertical_top"] = randint(ZERO, subtract(x10, x6[x5.index("vertical_top")]["span"]))
            if x3 in x5:
                x15 = subtract(x10, x6[x5.index(x3)]["span"])
                if "vertical_top" in x14:
                    x16 = x14["vertical_top"]
                    for _ in range(100):
                        x17 = randint(ZERO, x15)
                        if abs(subtract(x17, x16)) >= 4:
                            break
                    else:
                        x17 = randint(ZERO, x15)
                    x14[x3] = x17
                else:
                    x14[x3] = randint(ZERO, x15)
            x18 = []
            x19 = frozenset()
            x20 = {"top": (), "bottom": ()}
            for x21 in x6:
                x22, x23 = place_group_16b78196(x21, (x12, x13), (x11, x10), x14[x21["name"]])
                x18.extend(x22)
                x19 |= x23
                x24 = x21["side"]
                x20[x24] = x20.get(x24, ()) + ((x14[x21["name"]], x21["span"]),)
            x19 |= _boundary_noise_16b78196("vertical", (x12, x13), (x11, x10), x20)
        else:
            x7 = max(group["span"] for group in x6)
            x8 = max((subtract(group["length"], len(group["contact"])) for group in x6 if group["side"] == "left"), default=ZERO)
            x9 = max((subtract(group["length"], len(group["contact"])) for group in x6 if group["side"] == "right"), default=ZERO)
            x10 = randint(22, 30)
            x11 = randint(max(6, add(x7, 1)), 7)
            if add(x8, add(x11, x9)) > 30:
                continue
            x12 = randint(ZERO, subtract(30, x10))
            x13 = randint(x8, subtract(subtract(30, x11), x9))
            x14, x15 = _distinct_offsets_16b78196(subtract(x10, x6[0]["span"]), subtract(x10, x6[1]["span"]), 5)
            x16 = {"horizontal_left": x14, "horizontal_right": x15}
            x18 = []
            x19 = frozenset()
            x20 = {"left": (), "right": ()}
            for x21 in x6:
                x22, x23 = place_group_16b78196(x21, (x12, x13), (x10, x11), x16[x21["name"]])
                x18.extend(x22)
                x19 |= x23
                x24 = x21["side"]
                x20[x24] = x20.get(x24, ()) + ((x16[x21["name"]], x21["span"]),)
            x19 |= _boundary_noise_16b78196("horizontal", (x12, x13), (x10, x11), x20)
        x23 = difference(_rectangle_cells_16b78196((x12, x13), (x11, x10) if x0 == "vertical" else (x10, x11)), x19)
        x24 = make_object_16b78196(x2, x23)
        x25 = _scatter_objects_16b78196(tuple(x18), toindices(x24), (30, 30))
        if x25 is None:
            continue
        x26 = paint(canvas(ZERO, (30, 30)), x24)
        for x27 in x25:
            x26 = paint(x26, x27)
        x28 = paint(canvas(ZERO, (30, 30)), x24)
        for x29 in x18:
            x28 = paint(x28, x29)
        if x26 == x28:
            continue
        return {"input": x26, "output": x28}
