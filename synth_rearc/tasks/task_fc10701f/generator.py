from synth_rearc.core import *


def _rect_patch_fc10701f(
    top: int,
    left: int,
    height_: int,
    width_: int,
):
    x0 = interval(top, add(top, height_), ONE)
    x1 = interval(left, add(left, width_), ONE)
    return product(x0, x1)


def _choose_lines_fc10701f(
    total: int,
    excluded: tuple[int, ...],
    gap_start: int,
    gap_stop: int,
    diff_lb: float,
    diff_ub: float,
):
    x0 = frozenset(excluded)
    while True:
        x1 = choice((TWO, THREE))
        x2 = randint(ZERO, subtract(x1, ONE))
        x3 = tuple(i for i in range(x2, total, x1) if i not in x0)
        x4 = tuple(i for i in x3 if gap_start <= i < gap_stop)
        if len(x4) == ZERO:
            continue
        x5 = unifint(diff_lb, diff_ub, (ONE, len(x4)))
        x6 = tuple(sorted(sample(x4, x5)))
        x7 = x6
        x8 = tuple(i for i in x3 if i < gap_start)
        x9 = tuple(i for i in x3 if i >= gap_stop)
        if len(x8) > ZERO and choice((T, F)):
            x10 = unifint(diff_lb, diff_ub, (ONE, len(x8)))
            x7 = x7 + tuple(sorted(sample(x8, x10)))
        if len(x9) > ZERO and choice((T, F)):
            x11 = unifint(diff_lb, diff_ub, (ONE, len(x9)))
            x7 = x7 + tuple(sorted(sample(x9, x11)))
        x12 = tuple(sorted(set(x7)))
        return x12, x6


def _paint_vertical_markers_fc10701f(
    grid: Grid,
    rows: tuple[int, ...],
    left: int,
    size_: int,
    depth: int,
) -> Grid:
    x0 = grid
    x1 = interval(subtract(left, depth), left, ONE)
    x2 = interval(add(left, size_), add(add(left, size_), depth), ONE)
    for x3 in rows:
        x4 = product((x3,), x1)
        x5 = product((x3,), x2)
        x6 = combine(x4, x5)
        x0 = fill(x0, ZERO, x6)
    return x0


def _paint_horizontal_markers_fc10701f(
    grid: Grid,
    cols: tuple[int, ...],
    top: int,
    size_: int,
    depth: int,
) -> Grid:
    x0 = grid
    x1 = interval(subtract(top, depth), top, ONE)
    x2 = interval(add(top, size_), add(add(top, size_), depth), ONE)
    for x3 in cols:
        x4 = product(x1, (x3,))
        x5 = product(x2, (x3,))
        x6 = combine(x4, x5)
        x0 = fill(x0, ZERO, x6)
    return x0


def generate_fc10701f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x1 = TWO
        x2 = choice((T, F))
        if x2:
            x3 = unifint(diff_lb, diff_ub, (ZERO, SIX))
            x4 = unifint(diff_lb, diff_ub, (ZERO, SIX))
            x5 = unifint(diff_lb, diff_ub, (ZERO, SIX))
            x6 = unifint(diff_lb, diff_ub, (ZERO, SIX))
            x7 = unifint(diff_lb, diff_ub, (ONE, TEN))
            x8 = add(add(multiply(TWO, x0), x7), add(x3, x4))
            x9 = add(add(x0, multiply(TWO, x1)), add(x5, x6))
            x10 = add(x5, x1)
            x11 = x3
            x12 = add(add(x3, x0), x7)
            x13 = choice((T, F))
            x14 = branch(x13, x11, x12)
            x15 = branch(x13, x12, x11)
            x16 = canvas(SIX, (x8, x9))
            x17 = _rect_patch_fc10701f(x14, x10, x0, x0)
            x18 = _rect_patch_fc10701f(x15, x10, x0, x0)
            x19 = fill(x16, NINE, x17)
            x20 = fill(x19, SEVEN, x18)
            x21 = tuple(interval(x14, add(x14, x0), ONE) + interval(x15, add(x15, x0), ONE))
            x22 = add(minimum((x14, x15)), x0)
            x23 = maximum((x14, x15))
            x24, x25 = _choose_lines_fc10701f(x8, x21, x22, x23, diff_lb, diff_ub)
            x26 = _paint_vertical_markers_fc10701f(x20, x24, x10, x0, x1)
            x27 = product(x25, interval(x10, add(x10, x0), ONE))
            x28 = replace(x26, NINE, SEVEN)
            x29 = fill(x28, SIX, x18)
            x30 = fill(x29, TWO, x27)
            return {"input": x26, "output": x30}
        x3 = unifint(diff_lb, diff_ub, (ZERO, SIX))
        x4 = unifint(diff_lb, diff_ub, (ZERO, SIX))
        x5 = unifint(diff_lb, diff_ub, (ZERO, SIX))
        x6 = unifint(diff_lb, diff_ub, (ZERO, SIX))
        x7 = unifint(diff_lb, diff_ub, (ONE, TEN))
        x8 = add(add(x0, multiply(TWO, x1)), add(x3, x4))
        x9 = add(add(multiply(TWO, x0), x7), add(x5, x6))
        x10 = add(x3, x1)
        x11 = x5
        x12 = add(add(x5, x0), x7)
        x13 = choice((T, F))
        x14 = branch(x13, x11, x12)
        x15 = branch(x13, x12, x11)
        x16 = canvas(SIX, (x8, x9))
        x17 = _rect_patch_fc10701f(x10, x14, x0, x0)
        x18 = _rect_patch_fc10701f(x10, x15, x0, x0)
        x19 = fill(x16, NINE, x17)
        x20 = fill(x19, SEVEN, x18)
        x21 = tuple(interval(x14, add(x14, x0), ONE) + interval(x15, add(x15, x0), ONE))
        x22 = add(minimum((x14, x15)), x0)
        x23 = maximum((x14, x15))
        x24, x25 = _choose_lines_fc10701f(x9, x21, x22, x23, diff_lb, diff_ub)
        x26 = _paint_horizontal_markers_fc10701f(x20, x24, x10, x0, x1)
        x27 = product(interval(x10, add(x10, x0), ONE), x25)
        x28 = replace(x26, NINE, SEVEN)
        x29 = fill(x28, SIX, x18)
        x30 = fill(x29, TWO, x27)
        return {"input": x26, "output": x30}
