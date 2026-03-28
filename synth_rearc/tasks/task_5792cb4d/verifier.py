from synth_rearc.core import *


def _ordered_path_5792cb4d(
    x0: Grid,
) -> tuple[IntegerTuple, ...]:
    x1 = first(objects(x0, F, F, T))
    x2 = toindices(x1)
    x3 = {
        x4: tuple(x5 for x5 in dneighbors(x4) if x5 in x2)
        for x4 in x2
    }
    x4 = tuple(sorted(x5 for x5, x6 in x3.items() if len(x6) == ONE))
    x5 = x4[ZERO]
    x6 = None
    x7 = []
    while x5 is not None:
        x7.append(x5)
        x8 = tuple(x9 for x9 in x3[x5] if x9 != x6)
        x10 = x8[ZERO] if len(x8) > ZERO else None
        x6 = x5
        x5 = x10
    return tuple(x7)


def verify_5792cb4d(I: Grid) -> Grid:
    x0 = mostcolor(I)
    x1 = _ordered_path_5792cb4d(I)
    x2 = tuple(index(I, x3) for x3 in x1)
    x3 = tuple(reversed(x2))
    x4 = frozenset((x5, x6) for x5, x6 in zip(x3, x1))
    x5 = canvas(x0, shape(I))
    x6 = paint(x5, x4)
    return x6
