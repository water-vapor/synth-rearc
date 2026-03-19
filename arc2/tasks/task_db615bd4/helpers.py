from arc2.core import *


def solid_rectangle_db615bd4(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(top, top + h) for j in range(left, left + w))


def sparse_rectangle_db615bd4(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(top, top + h, TWO) for j in range(left, left + w, TWO))


def sparse_box_db615bd4(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    x0 = solid_rectangle_db615bd4(top, left, h, w)
    x1 = sparse_rectangle_db615bd4(top, left, h, w)
    x2 = intersection(box(x0), x1)
    return x2


def packed_rectangles_db615bd4(
    frame: Patch,
    dims: tuple[tuple[Integer, Integer], ...],
) -> tuple[Indices, ...]:
    x0 = uppermost(frame) + ONE
    x1 = leftmost(frame) + ONE
    x2 = height(frame) - TWO
    x3 = width(frame) - TWO
    if portrait(frame):
        x4 = sum(h for h, _ in dims)
        x5 = (x2 - x4) // (len(dims) + ONE)
        x6 = x1 + (x3 - max(w for _, w in dims)) // TWO
        x7 = x0 + x5
        out = []
        for h, w in dims:
            out.append(solid_rectangle_db615bd4(x7, x6, h, w))
            x7 += h + x5
        return tuple(out)
    x4 = sum(w for _, w in dims)
    x5 = (x3 - x4) // (len(dims) + ONE)
    x6 = x0 + (x2 - max(h for h, _ in dims)) // TWO
    x7 = x1 + x5
    out = []
    for h, w in dims:
        out.append(solid_rectangle_db615bd4(x6, x7, h, w))
        x7 += w + x5
    return tuple(out)
