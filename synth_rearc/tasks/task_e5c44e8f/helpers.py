from synth_rearc.core import *


def spiral_path_e5c44e8f(
    start: IntegerTuple,
    dims: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    h, w = dims
    i, j = start
    maxdist = max(i, h - 1 - i, j, w - 1 - j)
    ncycles = (maxdist + 1) // 2
    run = TWO
    directions = (UP, RIGHT, DOWN, LEFT)
    cells = []
    for seg_idx in range(FOUR * ncycles):
        di, dj = directions[seg_idx % FOUR]
        for _ in range(run):
            i += di
            j += dj
            if 0 <= i < h and 0 <= j < w:
                cells.append((i, j))
        if seg_idx % TWO == ONE:
            run += TWO
    return tuple(cells)
