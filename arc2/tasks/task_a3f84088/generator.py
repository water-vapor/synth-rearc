from arc2.core import *


COLOR_CYCLE_A3F84088 = (TWO, FIVE, ZERO, FIVE)


def _layer_count_a3f84088(side: Integer) -> Integer:
    x0 = subtract(side, TWO)
    x1 = divide(add(x0, ONE), TWO)
    if x0 == SEVEN:
        return decrement(x1)
    return x1


def _frame_patch_a3f84088(
    top: Integer,
    left: Integer,
    side: Integer,
) -> Indices:
    x0 = subtract(side, ONE)
    x1 = astuple(top, left)
    x2 = astuple(add(top, x0), add(left, x0))
    x3 = frozenset({x1, x2})
    return box(x3)


def _render_output_a3f84088(
    gi: Grid,
    frame: Patch,
    side: Integer,
) -> Grid:
    x0 = gi
    x1 = frame
    x2 = _layer_count_a3f84088(side)
    for x3 in range(x2):
        x1 = inbox(x1)
        x4 = COLOR_CYCLE_A3F84088[x3 % FOUR]
        x0 = fill(x0, x4, x1)
    return x0


def generate_a3f84088(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    side = randint(6, 25)
    margin = randint(ZERO, min(5, 30 - side))
    top = randint(ZERO, margin)
    left = randint(ZERO, margin)
    n = add(side, margin)
    frame = _frame_patch_a3f84088(top, left, side)
    gi = canvas(ZERO, (n, n))
    gi = fill(gi, FIVE, frame)
    go = _render_output_a3f84088(gi, frame, side)
    return {"input": gi, "output": go}
