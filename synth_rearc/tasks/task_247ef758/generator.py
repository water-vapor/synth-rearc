from synth_rearc.core import *

from .verifier import verify_247ef758


HEIGHT_RANGE_247EF758 = (10, 16)
LEFT_WIDTH_RANGE_247EF758 = (3, 5)
RIGHT_WIDTH_RANGE_247EF758 = (10, 15)
MOVABLE_COUNT_RANGE_247EF758 = (2, 3)
MARKER_COUNT_CHOICES_247EF758 = (ONE, ONE, ONE, TWO)
SHAPE_LIBRARY_247EF758 = (
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 1), (1, 0), (1, 2), (2, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}),
    frozenset({(0, 0), (1, 1), (2, 2)}),
    frozenset({(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)}),
    frozenset({(0, 1), (0, 2), (1, 1), (2, 0), (2, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 2)}),
)


def _shape_pool_247ef758(
    left_width: Integer,
) -> tuple[Indices, ...]:
    return tuple(x0 for x0 in SHAPE_LIBRARY_247EF758 if width(x0) <= left_width)


def _shape_halo_247ef758(
    obj: Object,
) -> frozenset[IntegerTuple]:
    x0 = set()
    for x1 in toindices(obj):
        x0.add(x1)
        x0.update(neighbors(x1))
    return frozenset(x0)


def _place_left_objects_247ef758(
    specs: tuple[tuple[Integer, Indices], ...],
    h: Integer,
    left_width: Integer,
) -> tuple[Object, ...] | None:
    x0 = set()
    x1 = []
    x2 = tuple(sorted(specs, key=lambda x3: (-height(x3[1]), -width(x3[1]))))
    for x3, x4 in x2:
        x5 = height(x4)
        x6 = width(x4)
        x7 = None
        for _ in range(80):
            x8 = randint(ZERO, subtract(h, x5))
            x9 = randint(ZERO, subtract(left_width, x6))
            x10 = shift(recolor(x3, x4), astuple(x8, x9))
            x11 = toindices(x10)
            if any(x12 in x0 for x12 in x11):
                continue
            x7 = x10
            x0.update(_shape_halo_247ef758(x10))
            x1.append(x10)
            break
        if x7 is None:
            return None
    return tuple(x1)


def _marker_slots_247ef758(
    obj: Object,
    h: Integer,
    right_width: Integer,
) -> tuple[tuple[Integer, ...], tuple[Integer, ...]]:
    x0, x1 = center(obj)
    x2 = subtract(x0, uppermost(obj))
    x3 = subtract(x1, leftmost(obj))
    x4 = subtract(lowermost(obj), x0)
    x5 = subtract(rightmost(obj), x1)
    x6 = tuple(range(add(ONE, x2), increment(subtract(subtract(h, TWO), x4))))
    x7 = tuple(range(add(ONE, x3), increment(subtract(subtract(right_width, TWO), x5))))
    return x6, x7


def _pick_markers_247ef758(
    candidates: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    if len(candidates) == ONE:
        return candidates
    x0 = min(choice(MARKER_COUNT_CHOICES_247EF758), len(candidates))
    return tuple(sorted(sample(candidates, x0)))


def _render_right_panel_247ef758(
    h: Integer,
    right_width: Integer,
    base_color: Integer,
    row_markers: dict[Integer, tuple[Integer, ...]],
    col_markers: dict[Integer, tuple[Integer, ...]],
) -> Grid:
    x0 = [[ZERO for _ in range(right_width)] for _ in range(h)]
    for x1 in range(right_width):
        x0[ZERO][x1] = base_color
        x0[decrement(h)][x1] = base_color
    for x2 in range(h):
        x0[x2][ZERO] = base_color
        x0[x2][decrement(right_width)] = base_color
    for x3, x4 in row_markers.items():
        for x5 in x4:
            x0[x5][ZERO] = x3
            x0[x5][decrement(right_width)] = x3
    for x6, x7 in col_markers.items():
        for x8 in x7:
            x0[ZERO][x8] = x6
            x0[decrement(h)][x8] = x6
    return tuple(tuple(x9) for x9 in x0)


def generate_247ef758(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(range(ONE, TEN))
    while True:
        x1 = unifint(diff_lb, diff_ub, HEIGHT_RANGE_247EF758)
        x2 = unifint(diff_lb, diff_ub, LEFT_WIDTH_RANGE_247EF758)
        x3 = unifint(diff_lb, diff_ub, RIGHT_WIDTH_RANGE_247EF758)
        x4 = _shape_pool_247ef758(x2)
        if len(x4) < TWO:
            continue
        x5 = unifint(diff_lb, diff_ub, MOVABLE_COUNT_RANGE_247EF758)
        x6 = randint(ZERO, ONE)
        x7 = randint(ZERO, TWO)
        if add(add(TWO, x5), add(x6, x7)) > NINE:
            continue
        x8 = list(sample(x0, add(add(TWO, x5), add(x6, x7))))
        x9 = x8.pop(ZERO)
        x10 = x8.pop(ZERO)
        x11 = tuple(x8.pop(ZERO) for _ in range(x5))
        x12 = tuple(x8.pop(ZERO) for _ in range(x6))
        x13 = tuple(x8.pop(ZERO) for _ in range(x7))
        x14 = tuple((x15, choice(x4)) for x15 in x11 + x12)
        x15 = _place_left_objects_247ef758(x14, x1, x2)
        if x15 is None:
            continue
        x16 = {color(x17): x17 for x17 in x15}
        x17 = tuple(
            sorted(
                x11,
                key=lambda x18: (
                    -height(x16[x18]),
                    -width(x16[x18]),
                    -size(x16[x18]),
                ),
            )
        )
        x18 = {}
        x19 = {}
        x20 = set()
        x21 = set()
        x22 = False
        for x23 in x17:
            x24, x25 = _marker_slots_247ef758(x16[x23], x1, x3)
            x26 = tuple(x27 for x27 in x24 if x27 not in x20)
            x27 = tuple(x28 for x28 in x25 if x28 not in x21)
            if len(x26) == ZERO or len(x27) == ZERO:
                x22 = True
                break
            x28 = _pick_markers_247ef758(x26)
            x29 = _pick_markers_247ef758(x27)
            x18[x23] = x28
            x19[x23] = x29
            x20.update(x28)
            x21.update(x29)
        if x22:
            continue
        x30 = {}
        x31 = {}
        x32 = tuple(x33 for x33 in range(ONE, decrement(x1)) if x33 not in x20)
        x33 = tuple(x34 for x34 in range(ONE, decrement(x3)) if x34 not in x21)
        for x34 in x13:
            x35 = bool(x32) and choice((T, F))
            x36 = bool(x33) and choice((T, F))
            if not x35 and not x36:
                x35 = bool(x32)
                x36 = not x35 and bool(x33)
            if x35:
                x37 = ONE if len(x32) == ONE else min(TWO, len(x32))
                x38 = tuple(sorted(sample(x32, randint(ONE, x37))))
                x30[x34] = x38
                x32 = tuple(x39 for x39 in x32 if x39 not in x38)
            if x36:
                x40 = ONE if len(x33) == ONE else min(TWO, len(x33))
                x41 = tuple(sorted(sample(x33, randint(ONE, x40))))
                x31[x34] = x41
                x33 = tuple(x42 for x42 in x33 if x42 not in x41)
        x34 = canvas(ZERO, astuple(x1, x2))
        for x35 in x15:
            x34 = paint(x34, x35)
        x36 = dict(x18)
        x36.update(x30)
        x37 = dict(x19)
        x37.update(x31)
        x38 = _render_right_panel_247ef758(x1, x3, x10, x36, x37)
        x39 = canvas(x9, astuple(x1, ONE))
        x40 = hconcat(hconcat(x34, x39), x38)
        x41 = tuple(sorted((x16[x42] for x42 in x11), key=lambda x43: (-uppermost(x43), -leftmost(x43))))
        x42 = x40
        for x43 in x41:
            x42 = fill(x42, ZERO, x43)
        for x44 in x41:
            x45 = color(x44)
            x46 = center(x44)
            for x47 in x18[x45]:
                for x48 in x19[x45]:
                    x49 = add(add(x2, ONE), x48)
                    x50 = shift(x44, subtract(astuple(x47, x49), x46))
                    x42 = paint(x42, x50)
        if verify_247ef758(x40) != x42:
            continue
        return {"input": x40, "output": x42}
