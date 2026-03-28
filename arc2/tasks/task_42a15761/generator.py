from arc2.core import *


def _block_42a15761(
    height_value: Integer,
    zero_rows: tuple[Integer, ...],
) -> Grid:
    x0 = canvas(TWO, astuple(height_value, THREE))
    x1 = frozenset((x2, ONE) for x2 in zero_rows)
    return fill(x0, ZERO, x1)


def _join_blocks_42a15761(
    blocks: tuple[Grid, ...],
    separator: Grid,
) -> Grid:
    x0 = first(blocks)
    for x1 in blocks[ONE:]:
        x0 = hconcat(x0, separator)
        x0 = hconcat(x0, x1)
    return x0


def generate_42a15761(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x1 = add(double(x0), ONE)
        x2 = interval(ONE, x1, TWO)
        x3 = interval(ONE, add(x0, ONE), ONE)
        x4 = tuple(sample(x3, x0))
        if x4 == x3:
            continue
        x5 = {}
        for x6 in x3:
            x7 = tuple(sorted(sample(x2, x6)))
            x8 = _block_42a15761(x1, x7)
            x5[x6] = x8
        x9 = tuple(x5[x10] for x10 in x4)
        x10 = tuple(x5[x11] for x11 in x3)
        x11 = canvas(ZERO, astuple(x1, ONE))
        x12 = _join_blocks_42a15761(x9, x11)
        x13 = _join_blocks_42a15761(x10, x11)
        return {"input": x12, "output": x13}
