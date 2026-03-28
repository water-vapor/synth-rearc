from arc2.core import *


def _segments_5a719d11(
    cuts: tuple[int, ...],
    limit: Integer,
) -> tuple[tuple[int, int], ...]:
    x0 = set(cuts)
    x1 = []
    x2 = ZERO
    while x2 < limit:
        if x2 in x0:
            x2 = increment(x2)
            continue
        x3 = x2
        while x2 < limit and x2 not in x0:
            x2 = increment(x2)
        x1.append((x3, subtract(x2, x3)))
    return tuple(x1)


def _motif_patch_5a719d11(
    panel: Grid,
) -> Indices:
    x0 = mostcolor(panel)
    x1 = asindices(panel)
    x2 = ofcolor(panel, x0)
    return difference(x1, x2)


def verify_5a719d11(I: Grid) -> Grid:
    x0 = frontiers(I)
    x1 = sfilter(x0, hline)
    x2 = colorfilter(x1, ZERO)
    x3 = tuple(sorted(apply(uppermost, x2)))
    x4 = height(I)
    x5 = _segments_5a719d11(x3, x4)
    x6 = sfilter(x0, vline)
    x7 = colorfilter(x6, ZERO)
    x8 = tuple(sorted(apply(leftmost, x7)))
    x9 = width(I)
    x10 = _segments_5a719d11(x8, x9)
    x11, x12 = x10
    x13 = canvas(ZERO, shape(I))
    for x14, x15 in x5:
        x16 = crop(I, (x14, x11[0]), (x15, x11[1]))
        x17 = crop(I, (x14, x12[0]), (x15, x12[1]))
        x18 = mostcolor(x16)
        x19 = mostcolor(x17)
        x20 = _motif_patch_5a719d11(x16)
        x21 = _motif_patch_5a719d11(x17)
        x22 = fill(canvas(x18, shape(x16)), x19, x21)
        x23 = fill(canvas(x19, shape(x17)), x18, x20)
        x24 = shift(asobject(x22), (x14, x11[0]))
        x25 = shift(asobject(x23), (x14, x12[0]))
        x13 = paint(x13, x24)
        x13 = paint(x13, x25)
    return x13
