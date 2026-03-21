from arc2.core import *


def _infer_period_abbfd121(
    I: Grid,
    blocked: Indices,
    axis: Integer,
) -> Integer:
    x0 = height(I)
    x1 = width(I)
    x2 = x0 if axis == ZERO else x1
    for x3 in range(ONE, x2):
        x4 = F
        x5 = T
        if axis == ZERO:
            for x6 in range(x0 - x3):
                for x7 in range(x1):
                    x8 = astuple(x6, x7)
                    x9 = astuple(x6 + x3, x7)
                    if x8 in blocked or x9 in blocked:
                        continue
                    x4 = T
                    if index(I, x8) != index(I, x9):
                        x5 = F
                        break
                if not x5:
                    break
        else:
            for x6 in range(x0):
                for x7 in range(x1 - x3):
                    x8 = astuple(x6, x7)
                    x9 = astuple(x6, x7 + x3)
                    if x8 in blocked or x9 in blocked:
                        continue
                    x4 = T
                    if index(I, x8) != index(I, x9):
                        x5 = F
                        break
                if not x5:
                    break
        if x4 and x5:
            return x3
    return x2


def _reconstruct_crop_abbfd121(
    I: Grid,
    rects: Objects,
    target: Object,
) -> Grid:
    x0 = merge(rects)
    x1 = toindices(x0)
    x2 = _infer_period_abbfd121(I, x1, ZERO)
    x3 = _infer_period_abbfd121(I, x1, ONE)
    x4 = {}
    x5 = height(I)
    x6 = width(I)
    for x7 in range(x5):
        for x8 in range(x6):
            x9 = astuple(x7, x8)
            if x9 in x1:
                continue
            x10 = (x7 % x2, x8 % x3)
            x11 = index(I, x9)
            if x10 in x4 and x4[x10] != x11:
                raise ValueError("inconsistent periodic background")
            x4[x10] = x11
    x12 = frozenset(x4)
    x13 = interval(ZERO, x2, ONE)
    x14 = interval(ZERO, x3, ONE)
    x15 = product(x13, x14)
    x16 = difference(x15, x12)
    if size(x16) > ZERO:
        raise ValueError("missing periodic residues")
    x17 = ulcorner(target)
    x18 = first(x17)
    x19 = last(x17)
    x20 = height(target)
    x21 = width(target)
    x22 = tuple(
        tuple(x4[((x18 + x23) % x2, (x19 + x24) % x3)] for x24 in range(x21))
        for x23 in range(x20)
    )
    return x22


def verify_abbfd121(
    I: Grid,
) -> Grid:
    x0 = partition(I)
    x1 = fork(multiply, height, width)
    x2 = fork(equality, size, x1)
    x3 = sfilter(x0, x2)
    x4 = argmax(x3, size)
    x5 = _reconstruct_crop_abbfd121(I, x3, x4)
    return x5
