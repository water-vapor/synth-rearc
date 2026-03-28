from synth_rearc.core import *


def _gap_runs_67c52801(
    row: tuple[int, ...],
) -> tuple[tuple[int, int], ...]:
    x0 = []
    x1 = ZERO
    x2 = len(row)
    while greater(x2, x1):
        if flip(equality(row[x1], ZERO)):
            x1 = increment(x1)
            continue
        x3 = x1
        while both(greater(x2, x1), equality(row[x1], ZERO)):
            x1 = increment(x1)
        x0.append((x3, subtract(x1, x3)))
    return tuple(x0)


def _orient_object_67c52801(
    obj: Object,
    target_width: int,
) -> Object | None:
    x0 = normalize(obj)
    x1 = width(x0)
    if equality(x1, target_width):
        return x0
    x2 = height(x0)
    if flip(equality(x2, target_width)):
        return None
    x3 = canvas(ZERO, shape(x0))
    x4 = paint(x3, x0)
    x5 = rot90(x4)
    x6 = asobject(x5)
    x7 = matcher(first, ZERO)
    x8 = compose(flip, x7)
    return sfilter(x6, x8)


def _assign_objects_67c52801(
    gaps: tuple[tuple[int, int], ...],
    objs: tuple[Object, ...],
) -> tuple[tuple[int, Object], ...] | None:
    if equality(len(gaps), ZERO):
        return ()
    x0 = first(gaps)
    x1, x2 = x0
    for x3, x4 in enumerate(objs):
        x5 = _orient_object_67c52801(x4, x2)
        if equality(x5, None):
            continue
        x6 = objs[:x3] + objs[increment(x3):]
        x7 = _assign_objects_67c52801(gaps[ONE:], x6)
        if flip(equality(x7, None)):
            return ((x1, x5),) + x7
    return None


def verify_67c52801(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = decrement(x0)
    x3 = decrement(x2)
    x4 = index(I, (x2, ZERO))
    x5 = crop(I, ORIGIN, (x3, x1))
    x6 = objects(x5, T, F, F)
    x7 = matcher(color, ZERO)
    x8 = compose(flip, x7)
    x9 = tuple(sorted(sfilter(x6, x8), key=lambda x10: (size(x10), height(x10), width(x10), color(x10))))
    x10 = tuple(index(I, (x3, x11)) for x11 in range(x1))
    x11 = _gap_runs_67c52801(x10)
    x12 = _assign_objects_67c52801(x11, x9)
    if equality(x12, None):
        raise ValueError("could not match upper objects to floor gaps")
    x13 = canvas(ZERO, shape(I))
    x14 = connect((x2, ZERO), (x2, decrement(x1)))
    x15 = fill(x13, x4, x14)
    x16 = frozenset((x3, x17) for x17 in range(x1) if equality(index(I, (x3, x17)), x4))
    x18 = fill(x15, x4, x16)
    for x19, x20 in x12:
        x21 = add(subtract(x3, height(x20)), ONE)
        x22 = shift(x20, (x21, x19))
        x18 = paint(x18, x22)
    return x18
