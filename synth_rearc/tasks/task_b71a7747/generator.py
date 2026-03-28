from synth_rearc.core import *


FAMILIES_B71A7747 = (
    ((FOUR, THREE), (TWO, ONE, TWO), ZERO, THREE),
    ((THREE, THREE), (FOUR, THREE, FOUR), ONE, TWO),
    ((FOUR, FIVE), (THREE, ONE, TWO), ZERO, TWO),
)


def _rectangle_b71a7747(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Indices:
    x0 = interval(top, add(top, height_), ONE)
    x1 = interval(left, add(left, width_), ONE)
    return product(x0, x1)


def _endpoint_b71a7747(
    point: IntegerTuple,
    size_: Integer,
    horizontal: Boolean,
) -> IntegerTuple:
    x0 = first(point)
    x1 = last(point)
    if horizontal:
        x2 = randint(ONE, subtract(size_, TWO))
        while x2 == x1:
            x2 = randint(ONE, subtract(size_, TWO))
        return astuple(x0, x2)
    x2 = randint(ONE, subtract(size_, TWO))
    while x2 == x0:
        x2 = randint(ONE, subtract(size_, TWO))
    return astuple(x2, x1)


def _draw_output_b71a7747(
    size_: Integer,
    background: Integer,
    foreground: Integer,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    while True:
        x0 = canvas(background, (size_, size_))
        x1 = unifint(diff_lb, diff_ub, (THREE, branch(greater(size_, 12), SIX, FIVE)))
        x2 = astuple(randint(ONE, subtract(size_, TWO)), randint(ONE, subtract(size_, TWO)))
        x3 = x0
        x4 = choice((True, False))
        for _ in range(x1):
            x5 = _endpoint_b71a7747(x2, size_, x4)
            x6 = connect(x2, x5)
            x3 = fill(x3, foreground, x6)
            if choice((True, False, False)):
                x7 = first(x5)
                x8 = last(x5)
                x9 = max(ONE, decrement(x7))
                x10 = max(ONE, decrement(x8))
                x11 = min(TWO, subtract(size_, x9))
                x12 = min(TWO, subtract(size_, x10))
                x13 = _rectangle_b71a7747(x9, x10, x11, x12)
                x3 = fill(x3, foreground, x13)
            if choice((True, False, False)):
                x14 = branch(x4, choice((UP, DOWN)), choice((LEFT, RIGHT)))
                x15 = add(x2, x14)
                x16 = add(x5, x14)
                x17 = both(
                    both(greater(first(x15), ZERO), greater(last(x15), ZERO)),
                    both(greater(size_, increment(first(x16))), greater(size_, increment(last(x16)))),
                )
                if x17:
                    x18 = connect(x15, x16)
                    x3 = fill(x3, foreground, x18)
            x2 = x5
            x4 = not x4
        x19 = colorcount(x3, foreground)
        x20 = add(size_, halve(size_))
        x21 = divide(multiply(size_, size_), THREE)
        if both(greater(x19, x20), greater(x21, x19)):
            return x3


def _keep_indices_b71a7747(
    blocks: Integer,
    group_size: Integer,
    margins: IntegerTuple,
) -> tuple[Tuple[Integer, ...], Integer]:
    x0 = first(margins)
    x1 = margins[1]
    x2 = last(margins)
    x3 = []
    x4 = x0
    for x5 in range(blocks):
        for x6 in range(group_size):
            x3.append(add(x4, x6))
        x4 = add(x4, group_size)
        if x5 != decrement(blocks):
            x4 = add(x4, x1)
    return tuple(x3), add(x4, x2)


def _scaffold_color_b71a7747(
    row: Integer,
    col: Integer,
    keep_rows: frozenset,
    keep_cols: frozenset,
    colors: Tuple[Integer, ...],
) -> Integer:
    x0 = contained(row, keep_rows)
    x1 = contained(col, keep_cols)
    if x0 != x1:
        return colors[1]
    if x0 and x1:
        return ZERO
    if len(colors) == TWO:
        return colors[(row + col) % TWO]
    return colors[(row + double(col)) % THREE]


def _embed_inner_b71a7747(
    output: Grid,
    blocks: Integer,
    group_size: Integer,
    margins: IntegerTuple,
    scaffold_colors: Tuple[Integer, ...],
) -> Grid:
    x0, x1 = _keep_indices_b71a7747(blocks, group_size, margins)
    x2 = frozenset(x0)
    x3 = frozenset(x0)
    x4 = {v: i for i, v in enumerate(x0)}
    x5 = []
    for x6 in range(x1):
        x7 = []
        for x8 in range(x1):
            x9 = both(contained(x6, x2), contained(x8, x3))
            if x9:
                x10 = x4[x6]
                x11 = x4[x8]
                x12 = output[x10][x11]
            else:
                x12 = _scaffold_color_b71a7747(x6, x8, x2, x3, scaffold_colors)
            x7.append(x12)
        x5.append(tuple(x7))
    return tuple(x5)


def _wrap_border_b71a7747(
    grid: Grid,
    color_: Integer,
    border: Integer,
) -> Grid:
    if border == ZERO:
        return grid
    x0 = add(height(grid), double(border))
    x1 = add(width(grid), double(border))
    x2 = [list(row) for row in canvas(color_, (x0, x1))]
    for x3, x4 in enumerate(grid):
        for x5, x6 in enumerate(x4):
            x2[add(x3, border)][add(x5, border)] = x6
    return tuple(tuple(row) for row in x2)


def generate_b71a7747(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(FAMILIES_B71A7747)
    x1 = first(x0)
    x2 = x0[1]
    x3 = x0[2]
    x4 = x0[3]
    x5 = first(x1)
    x6 = last(x1)
    x7 = multiply(x5, x6)
    x8 = sample(tuple(range(ONE, TEN)), add(x4, TWO))
    x9 = tuple(x8[:x4])
    x10 = x8[x4]
    x11 = x8[add(x4, ONE)]
    x12 = _draw_output_b71a7747(x7, x10, x11, diff_lb, diff_ub)
    x13 = _embed_inner_b71a7747(x12, x5, x6, x2, x9)
    x14 = _wrap_border_b71a7747(x13, first(x9), x3)
    return {"input": x14, "output": x12}
