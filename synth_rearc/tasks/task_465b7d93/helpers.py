from synth_rearc.core import *


def resize_object_465b7d93(
    obj: Object,
    dimensions: tuple[int, int],
) -> Object:
    x0, x1 = dimensions
    x2 = normalize(obj)
    x3 = toindices(x2)
    x4 = height(x2)
    x5 = width(x2)
    x6 = color(x2)
    if len(x3) == ONE:
        x7 = frozenset((x8, x9) for x8 in range(x0) for x9 in range(x1))
        return recolor(x6, x7)
    x7 = lambda x8: ZERO if x4 == ONE else (x8 * (x0 - ONE)) // (x4 - ONE)
    x8 = lambda x9: ZERO if x5 == ONE else (x9 * (x1 - ONE)) // (x5 - ONE)
    x9 = set()
    for x10, x11 in x3:
        x9.add((x7(x10), x8(x11)))
        x12 = (x10 + ONE, x11)
        x13 = (x10, x11 + ONE)
        if x12 in x3:
            x9.update(connect((x7(x10), x8(x11)), (x7(x10 + ONE), x8(x11))))
        if x13 in x3:
            x9.update(connect((x7(x10), x8(x11)), (x7(x10), x8(x11 + ONE))))
    for x10 in range(x4 - ONE):
        for x11 in range(x5 - ONE):
            x12 = {(x10, x11), (x10 + ONE, x11), (x10, x11 + ONE), (x10 + ONE, x11 + ONE)}
            if x12.issubset(x3):
                for x13 in range(x7(x10), x7(x10 + ONE) + ONE):
                    for x14 in range(x8(x11), x8(x11 + ONE) + ONE):
                        x9.add((x13, x14))
    return recolor(x6, frozenset(x9))
