from arc2.core import *


def _slide_row_9c56f360(row: tuple[int, ...]) -> tuple[int, ...]:
    out = []
    seg = []
    for value in row:
        if value == EIGHT:
            count = seg.count(THREE)
            out.extend((THREE,) * count)
            out.extend((ZERO,) * (len(seg) - count))
            out.append(EIGHT)
            seg = []
            continue
        seg.append(value)
    count = seg.count(THREE)
    out.extend((THREE,) * count)
    out.extend((ZERO,) * (len(seg) - count))
    return tuple(out)


def verify_9c56f360(I: Grid) -> Grid:
    x0 = tuple(_slide_row_9c56f360(x1) for x1 in I)
    return x0
