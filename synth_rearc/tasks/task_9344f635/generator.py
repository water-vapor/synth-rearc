from synth_rearc.core import *


BG_9344F635 = SEVEN
DIM_BOUNDS_9344F635 = (SEVEN, 12)
TOTAL_OBJECT_BOUNDS_9344F635 = (FOUR, SEVEN)
MAX_VERTICAL_OBJECTS_9344F635 = FOUR
MAX_HORIZONTAL_OBJECTS_9344F635 = FOUR
PALETTE_9344F635 = remove(BG_9344F635, interval(ZERO, TEN, ONE))


def _sample_separated_positions_9344f635(length: int, count: int) -> tuple[int, ...]:
    x0 = list(interval(ZERO, length, ONE))
    x1 = []
    while len(x1) < count:
        if not x0:
            return tuple()
        x2 = choice(x0)
        x1.append(x2)
        x0 = [x3 for x3 in x0 if abs(x3 - x2) > ONE]
    return tuple(x1)


def _touches_occupied_9344f635(
    cells: frozenset[tuple[int, int]],
    occupied: frozenset[tuple[int, int]],
) -> bool:
    for x0 in cells:
        if x0 in occupied:
            return True
        if dneighbors(x0) & occupied:
            return True
    return False


def _sample_horizontal_colors_9344f635(
    diff_lb: float,
    diff_ub: float,
    count: int,
) -> tuple[int, ...]:
    x0 = min(count, THREE)
    x1 = unifint(diff_lb, diff_ub, (ONE, x0))
    x2 = list(sample(PALETTE_9344F635, x1))
    while len(x2) < count:
        x2.append(choice(x2))
    shuffle(x2)
    return tuple(x2)


def _render_output_9344f635(
    dim: int,
    verticals: tuple[tuple[int, int], ...],
    horizontals: tuple[tuple[int, int], ...],
) -> Grid:
    x0 = canvas(BG_9344F635, (dim, dim))
    for x1, x2 in verticals:
        x0 = fill(x0, x2, vfrontier((ZERO, x1)))
    for x3, x4 in horizontals:
        x0 = fill(x0, x4, hfrontier((x3, ZERO)))
    return x0


def generate_9344f635(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, DIM_BOUNDS_9344F635)
        x1 = min(TOTAL_OBJECT_BOUNDS_9344F635[1], x0 - ONE, ((x0 + ONE) // TWO) + THREE)
        x2 = unifint(diff_lb, diff_ub, (TOTAL_OBJECT_BOUNDS_9344F635[0], x1))
        x3 = min(MAX_VERTICAL_OBJECTS_9344F635, (x0 + ONE) // TWO, x2 - ONE)
        x4 = max(ONE, x2 - MAX_HORIZONTAL_OBJECTS_9344F635)
        if x4 > x3:
            continue
        x5 = unifint(diff_lb, diff_ub, (x4, x3))
        x6 = x2 - x5
        x7 = _sample_separated_positions_9344f635(x0, x5)
        if len(x7) != x5:
            continue
        x8 = tuple(sample(interval(ZERO, x0, ONE), x6))
        x9 = tuple(sample(PALETTE_9344F635, x5))
        x10 = _sample_horizontal_colors_9344f635(diff_lb, diff_ub, x6)
        x11 = tuple(pair(x7, x9))
        x12 = tuple(pair(x8, x10))
        x13 = canvas(BG_9344F635, (x0, x0))
        x14 = frozenset()
        x15 = []
        x16 = list(x12)
        shuffle(x16)
        for x17, x18 in x16:
            x19 = []
            for x20 in interval(ZERO, x0 - ONE, ONE):
                x21 = frozenset({(x17, x20), (x17, x20 + ONE)})
                if _touches_occupied_9344f635(x21, x14):
                    continue
                x19.append(x21)
            if len(x19) == ZERO:
                break
            x22 = choice(x19)
            x15.append((x22, x18))
            x14 = combine(x14, x22)
        if len(x15) != x6:
            continue
        x23 = []
        x24 = list(x11)
        shuffle(x24)
        for x25, x26 in x24:
            x27 = []
            for x28 in interval(ZERO, x0 - ONE, ONE):
                x29 = frozenset({(x28, x25), (x28 + ONE, x25)})
                if _touches_occupied_9344f635(x29, x14):
                    continue
                x27.append(x29)
            if len(x27) == ZERO:
                break
            x30 = choice(x27)
            x23.append((x30, x26))
            x14 = combine(x14, x30)
        if len(x23) != x5:
            continue
        for x31, x32 in x15:
            x13 = fill(x13, x32, x31)
        for x33, x34 in x23:
            x13 = fill(x13, x34, x33)
        x35 = _render_output_9344f635(x0, x11, x12)
        if x13 == x35:
            continue
        from .verifier import verify_9344f635

        if verify_9344f635(x13) != x35:
            continue
        return {"input": x13, "output": x35}
