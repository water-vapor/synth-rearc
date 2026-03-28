from synth_rearc.core import *


def _variable_column_85b81ff1(
    fg: Integer,
    black_count: Integer,
) -> Grid:
    x0 = set(sample(range(SIX), subtract(SIX, black_count)))
    x1 = []
    for x2 in range(13):
        x3 = even(x2)
        x4 = divide(subtract(x2, ONE), TWO)
        x5 = branch(either(x3, x4 in x0), fg, ZERO)
        x1.append((x5,))
    return tuple(x1)


def _solid_column_85b81ff1(
    fg: Integer,
) -> Grid:
    return canvas(fg, astuple(13, ONE))


def _join_blocks_85b81ff1(
    blocks: tuple[Grid, ...],
    separator: Grid,
) -> Grid:
    x0 = first(blocks)
    for x1 in blocks[ONE:]:
        x0 = hconcat(x0, separator)
        x0 = hconcat(x0, x1)
    return x0


def generate_85b81ff1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(ZERO, interval(ZERO, TEN, ONE))
    x1 = tuple(range(ONE, SEVEN))
    while True:
        x2 = choice(x0)
        x3 = tuple(sample(x1, FIVE))
        x4 = tuple(sorted(x3, reverse=True))
        if x3 == x4:
            continue
        x5 = _solid_column_85b81ff1(x2)
        x6 = tuple(_variable_column_85b81ff1(x2, x7) for x7 in x3)
        x7 = tuple(hconcat(x5, x8) for x8 in x6)
        x8 = canvas(ZERO, astuple(13, ONE))
        x9 = _join_blocks_85b81ff1(x7, x8)
        x10 = tuple(x7[x3.index(x11)] for x11 in x4)
        x11 = _join_blocks_85b81ff1(x10, x8)
        return {"input": x9, "output": x11}
