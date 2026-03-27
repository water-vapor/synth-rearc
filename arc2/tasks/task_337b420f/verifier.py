from arc2.core import *


def _inside_bounds_337b420f(
    obj: Patch,
    dims: tuple[int, int],
) -> bool:
    x0 = uppermost(obj) >= ZERO
    x1 = leftmost(obj) >= ZERO
    x2 = lowermost(obj) < dims[0]
    x3 = rightmost(obj) < dims[1]
    return x0 and x1 and x2 and x3


def _shift_candidates_337b420f(
    obj: Patch,
    dims: tuple[int, int],
) -> tuple[IntegerTuple, ...]:
    x0 = []
    if rightmost(obj) == dims[1] - ONE:
        x0.append(LEFT)
    if leftmost(obj) == ZERO:
        x0.append(RIGHT)
    if lowermost(obj) == dims[0] - ONE:
        x0.append(UP)
    if uppermost(obj) == ZERO:
        x0.append(DOWN)
    for x1 in (LEFT, RIGHT, UP, DOWN):
        if x1 not in x0:
            x0.append(x1)
    return tuple(x0)


def _place_object_337b420f(
    obj: Object,
    occupied: Indices,
    dims: tuple[int, int],
) -> Object:
    x0 = toindices(obj)
    x1 = len(intersection(x0, occupied)) == ZERO
    if x1:
        return obj
    x2 = _shift_candidates_337b420f(obj, dims)
    for x3 in x2:
        x4 = shift(obj, x3)
        x5 = toindices(x4)
        x6 = len(intersection(x5, occupied)) == ZERO
        x7 = _inside_bounds_337b420f(x4, dims)
        if x6 and x7:
            return x4
    return obj


def verify_337b420f(I: Grid) -> Grid:
    x0 = hsplit(I, THREE)
    x1 = first(x0)
    x2 = shape(x1)
    x3 = canvas(EIGHT, x2)
    x4 = rbind(objects, T)
    x5 = rbind(x4, F)
    x6 = rbind(x5, T)
    x7 = rbind(argmax, size)
    x8 = compose(x7, x6)
    x9 = apply(x8, x0)
    x10 = order(x9, size)
    x11 = last(x10)
    x12 = remove(x11, x10)
    x13 = last(x12)
    x14 = first(x12)
    x15 = (x11, x13, x14)
    x16 = x3
    x17 = frozenset()
    for x18 in x15:
        x19 = _place_object_337b420f(x18, x17, x2)
        x16 = paint(x16, x19)
        x17 = combine(x17, toindices(x19))
    return x16
