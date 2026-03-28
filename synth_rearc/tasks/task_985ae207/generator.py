from synth_rearc.core import *


PALETTE_985AE207 = tuple(x0 for x0 in range(ONE, TEN) if x0 != EIGHT)
SHORT_SIDE_985AE207 = (TWO, TWO, THREE, THREE, THREE, FOUR, FOUR, FIVE, SIX)


def _rect_patch_985ae207(top: Integer, left: Integer, h: Integer, w: Integer) -> Indices:
    return frozenset((x0, x1) for x0 in range(top, top + h) for x1 in range(left, left + w))


def _motif_patch_985ae207(center: IntegerTuple) -> Indices:
    x0, x1 = center
    return frozenset((x0 + x2, x1 + x3) for x2 in range(-ONE, TWO) for x3 in range(-ONE, TWO))


def _expand_985ae207(
    patch: Indices,
    dims: IntegerTuple,
    radius: Integer = ONE,
) -> Indices:
    x0, x1 = dims
    x2 = set()
    for x3, x4 in patch:
        for x5 in range(-radius, radius + ONE):
            for x6 in range(-radius, radius + ONE):
                x7 = x3 + x5
                x8 = x4 + x6
                if ZERO <= x7 < x0 and ZERO <= x8 < x1:
                    x2.add((x7, x8))
    return frozenset(x2)


def _bridge_centers_985ae207(
    source: IntegerTuple,
    target: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = source
    x2, x3 = target
    if x0 == x2:
        x4 = THREE if x3 > x1 else -THREE
        return tuple((x0, x5) for x5 in range(x1, x3 + x4, x4))
    x4 = THREE if x2 > x0 else -THREE
    return tuple((x5, x1) for x5 in range(x0, x2 + x4, x4))


def _bridge_patch_985ae207(
    source: IntegerTuple,
    target: IntegerTuple,
) -> Indices:
    x0 = _bridge_centers_985ae207(source, target)
    return frozenset(merge(tuple(_motif_patch_985ae207(x1) for x1 in x0)))


def _apply_bridge_985ae207(
    grid: Grid,
    outer_color: Integer,
    center_color: Integer,
    source: IntegerTuple,
    target: IntegerTuple,
) -> Grid:
    x0 = _bridge_patch_985ae207(source, target)
    x1 = _bridge_centers_985ae207(source, target)
    x2 = fill(grid, outer_color, x0)
    x3 = fill(x2, center_color, frozenset(x1))
    return x3


def _weighted_candidates_985ae207(
    target: dict,
    dims: IntegerTuple,
    input_blocked: Indices,
    output_blocked: Indices,
) -> tuple[dict, ...]:
    x0, x1 = dims
    x2 = target["top"]
    x3 = target["bottom"]
    x4 = target["left"]
    x5 = target["right"]
    x6 = target["patch"]
    x7 = target["orientation"]
    x8 = []
    x9 = ("left", "right") if x7 == "v" else ("up", "down")
    if x7 == "s":
        x9 = ("left", "right", "up", "down")
    for x10 in x9:
        if x10 == "left":
            for x11 in range(x2, x3 + ONE):
                x12 = ONE
                while x4 - THREE * x12 - ONE >= ZERO:
                    x13 = (x11, x4 - THREE * x12)
                    x14 = (x11, x4)
                    x15 = _motif_patch_985ae207(x13)
                    x16 = _bridge_patch_985ae207(x13, x14)
                    if len(intersection(x15, input_blocked)) == ZERO and len(intersection(difference(x16, x6), output_blocked)) == ZERO:
                        x8.append({"center": x13, "edge": x14, "patch": x15, "bridge": x16, "weight": THREE})
                    x12 += ONE
        elif x10 == "right":
            for x11 in range(x2, x3 + ONE):
                x12 = ONE
                while x5 + THREE * x12 + ONE < x1:
                    x13 = (x11, x5 + THREE * x12)
                    x14 = (x11, x5)
                    x15 = _motif_patch_985ae207(x13)
                    x16 = _bridge_patch_985ae207(x13, x14)
                    if len(intersection(x15, input_blocked)) == ZERO and len(intersection(difference(x16, x6), output_blocked)) == ZERO:
                        x8.append({"center": x13, "edge": x14, "patch": x15, "bridge": x16, "weight": THREE})
                    x12 += ONE
        elif x10 == "up":
            for x11 in range(x4, x5 + ONE):
                x12 = ONE
                while x2 - THREE * x12 - ONE >= ZERO:
                    x13 = (x2 - THREE * x12, x11)
                    x14 = (x2, x11)
                    x15 = _motif_patch_985ae207(x13)
                    x16 = _bridge_patch_985ae207(x13, x14)
                    if len(intersection(x15, input_blocked)) == ZERO and len(intersection(difference(x16, x6), output_blocked)) == ZERO:
                        x8.append({"center": x13, "edge": x14, "patch": x15, "bridge": x16, "weight": THREE})
                    x12 += ONE
        else:
            for x11 in range(x4, x5 + ONE):
                x12 = ONE
                while x3 + THREE * x12 + ONE < x0:
                    x13 = (x3 + THREE * x12, x11)
                    x14 = (x3, x11)
                    x15 = _motif_patch_985ae207(x13)
                    x16 = _bridge_patch_985ae207(x13, x14)
                    if len(intersection(x15, input_blocked)) == ZERO and len(intersection(difference(x16, x6), output_blocked)) == ZERO:
                        x8.append({"center": x13, "edge": x14, "patch": x15, "bridge": x16, "weight": THREE})
                    x12 += ONE
    x17 = []
    for x18 in x8:
        x17.extend(repeat(x18, x18["weight"]))
    return tuple(x17)


def _sample_target_985ae207(
    dims: IntegerTuple,
    blocked: Indices,
    diff_lb: float,
    diff_ub: float,
) -> dict | None:
    x0, x1 = dims
    for _ in range(200):
        x2 = choice(("h", "v"))
        if x2 == "h":
            x3ub = min(SIX, max(TWO, x0 // THREE))
            x3 = unifint(diff_lb, diff_ub, (TWO, x3ub))
            x4lb = max(SIX, x3 + ONE)
            x4ub = max(x4lb, x1 - ONE)
            x4 = unifint(diff_lb, diff_ub, (x4lb, x4ub))
        else:
            x4ub = min(SIX, max(TWO, x1 // THREE))
            x4 = unifint(diff_lb, diff_ub, (TWO, x4ub))
            x3lb = max(SIX, x4 + ONE)
            x3ub = max(x3lb, x0 - ONE)
            x3 = unifint(diff_lb, diff_ub, (x3lb, x3ub))
        if x3 > x0 or x4 > x1:
            continue
        x5 = randint(ZERO, x0 - x3)
        x6 = randint(ZERO, x1 - x4)
        x7 = _rect_patch_985ae207(x5, x6, x3, x4)
        x8 = _expand_985ae207(x7, dims)
        if len(intersection(x8, blocked)) > ZERO:
            continue
        return {
            "top": x5,
            "bottom": x5 + x3 - ONE,
            "left": x6,
            "right": x6 + x4 - ONE,
            "patch": x7,
            "orientation": x2 if x3 != x4 else "s",
        }
    return None


def generate_985ae207(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    from .verifier import verify_985ae207

    while True:
        x0 = unifint(diff_lb, diff_ub, (20, 26))
        x1 = unifint(diff_lb, diff_ub, (20, 26))
        x2 = (x0, x1)
        x3 = choice(PALETTE_985AE207)
        x4 = tuple(x5 for x5 in PALETTE_985AE207 if x5 != x3)
        x5 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x6 = sample(x4, x5)
        x7 = []
        x8 = frozenset()
        for x9 in x6:
            x10 = _sample_target_985ae207(x2, x8, diff_lb, diff_ub)
            if x10 is None:
                break
            x10["color"] = x9
            x7.append(x10)
            x8 = combine(x8, _expand_985ae207(x10["patch"], x2))
        if len(x7) != x5:
            continue
        x11 = canvas(EIGHT, x2)
        for x12 in x7:
            x11 = fill(x11, x12["color"], x12["patch"])
        if mostcolor(x11) != EIGHT:
            continue
        x13 = frozenset(merge(tuple(x14["patch"] for x14 in x7)))
        x14 = frozenset(merge(tuple(_expand_985ae207(x15["patch"], x2) for x15 in x7)))
        x15 = x13
        x16 = []
        x17 = list(range(len(x7)))
        shuffle(x17)
        x18 = False
        for x19 in x17:
            x20 = x7[x19]
            x21 = _weighted_candidates_985ae207(x20, x2, x14, x15)
            if len(x21) == ZERO:
                x18 = True
                break
            x22 = choice(x21)
            x16.append((x20["color"], x22["center"], x22["edge"]))
            x14 = combine(x14, _expand_985ae207(x22["patch"], x2))
            x15 = combine(x15, x22["bridge"])
            x11 = fill(x11, x3, x22["patch"])
            x11 = fill(x11, x20["color"], initset(x22["center"]))
        if x18:
            continue
        x23 = choice((ZERO, ONE, ONE, TWO))
        for _ in range(x23):
            x24 = []
            for x25 in x7:
                if sum(ONE for x26, _, _ in x16 if x26 == x25["color"]) >= TWO:
                    continue
                x27 = _weighted_candidates_985ae207(x25, x2, x14, x15)
                x24.extend((x25, x28) for x28 in x27)
            if len(x24) == ZERO:
                break
            x29, x30 = choice(tuple(x24))
            x16.append((x29["color"], x30["center"], x30["edge"]))
            x14 = combine(x14, _expand_985ae207(x30["patch"], x2))
            x15 = combine(x15, x30["bridge"])
            x11 = fill(x11, x3, x30["patch"])
            x11 = fill(x11, x29["color"], initset(x30["center"]))
        if len(x16) < TWO:
            continue
        if mostcolor(x11) != EIGHT:
            continue
        x31 = x11
        for x32, x33, x34 in x16:
            x31 = _apply_bridge_985ae207(x31, x3, x32, x33, x34)
        if choice((T, F)):
            x11 = hmirror(x11)
            x31 = hmirror(x31)
        if choice((T, F)):
            x11 = vmirror(x11)
            x31 = vmirror(x31)
        if x11 == x31:
            continue
        if mostcolor(x11) != EIGHT:
            continue
        if verify_985ae207(x11) != x31:
            continue
        return {"input": x11, "output": x31}
