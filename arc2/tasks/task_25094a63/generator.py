from arc2.core import *


COLORS = (ONE, TWO, THREE, SIX, EIGHT)
GRID_SHAPE = (30, 30)
RECT_COUNT_BOUNDS = (TWO, FOUR)
RECT_DIM_BOUNDS = (FOUR, TEN)
RECT_AREA_BOUNDS = (60, 180)


def _rectangle_patch(
    dims: tuple[int, int],
    loc: tuple[int, int],
) -> Indices:
    x0 = canvas(ZERO, dims)
    x1 = asindices(x0)
    x2 = shift(x1, loc)
    return x2


def _expanded_patch(
    dims: tuple[int, int],
    loc: tuple[int, int],
) -> Indices:
    h, w = dims
    i, j = loc
    return frozenset(
        (a, b)
        for a in range(max(ZERO, i - ONE), min(GRID_SHAPE[0], i + h + ONE))
        for b in range(max(ZERO, j - ONE), min(GRID_SHAPE[1], j + w + ONE))
    )


def generate_25094a63(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, RECT_COUNT_BOUNDS)
        x1 = sample(COLORS, x0)
        x2 = []
        x3 = ZERO
        for x4 in x1:
            x5 = unifint(diff_lb, diff_ub, RECT_DIM_BOUNDS)
            x6 = unifint(diff_lb, diff_ub, RECT_DIM_BOUNDS)
            x2.append((x5, x6, x4))
            x3 += x5 * x6
        if not (RECT_AREA_BOUNDS[0] <= x3 <= RECT_AREA_BOUNDS[1]):
            continue
        x7 = sorted(x2, key=lambda x8: (-(x8[0] * x8[1]), -x8[0], -x8[1]))
        x9 = frozenset({})
        x10 = []
        x11 = False
        for x12, x13, x14 in x7:
            x15 = []
            for x16 in range(GRID_SHAPE[0] - x12 + ONE):
                for x17 in range(GRID_SHAPE[1] - x13 + ONE):
                    x18 = _expanded_patch((x12, x13), (x16, x17))
                    if len(intersection(x18, x9)) == ZERO:
                        x15.append((x16, x17))
            if len(x15) == ZERO:
                x11 = True
                break
            x19 = choice(x15)
            x20 = _rectangle_patch((x12, x13), x19)
            x21 = outbox(x20)
            x10.append((x20, x21, x14))
            x9 = combine(x9, _expanded_patch((x12, x13), x19))
        if x11:
            continue
        x22 = {}
        x23 = {}
        for x24, x25, x26 in x10:
            for x27 in x24:
                x22[x27] = x26
            for x27 in x25:
                if not (ZERO <= x27[0] < GRID_SHAPE[0] and ZERO <= x27[1] < GRID_SHAPE[1]):
                    continue
                if x27 in x22:
                    continue
                x23.setdefault(x27, set()).add(x26)
        x28 = []
        for x29 in range(GRID_SHAPE[0]):
            x30 = []
            for x31 in range(GRID_SHAPE[1]):
                x32 = (x29, x31)
                if x32 in x22:
                    x30.append(x22[x32])
                    continue
                x33 = tuple(x34 for x34 in COLORS if x34 not in x23.get(x32, set()))
                x30.append(choice(x33))
            x28.append(tuple(x30))
        gi = tuple(x28)
        if numcolors(gi) != FIVE:
            continue
        x35 = tuple(x36 for x36, _, _ in x10)
        x36 = merge(x35)
        go = gi
        x37 = fill(go, FOUR, x36)
        return {"input": gi, "output": x37}
