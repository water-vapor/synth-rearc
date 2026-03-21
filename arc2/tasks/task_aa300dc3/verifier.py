from arc2.core import *


def _diagonal_runs_aa300dc3(
    cells: Indices,
    anti: Boolean,
) -> tuple[Indices, ...]:
    if len(cells) == ZERO:
        return tuple()
    x0: dict[Integer, list[IntegerTuple]] = dict()
    for x1 in cells:
        x2, x3 = x1
        x4 = x2 + x3 if anti else x2 - x3
        if x4 not in x0:
            x0[x4] = []
        x0[x4].append(x1)
    x5 = tuple()
    for x6 in sorted(x0):
        x7 = sorted(x0[x6])
        x8 = [x7[ZERO]]
        for x9, x10 in x7[ONE:]:
            x11, x12 = x8[-ONE]
            x13 = (x11 + ONE, x12 - ONE) if anti else (x11 + ONE, x12 + ONE)
            if (x9, x10) == x13:
                x8.append((x9, x10))
                continue
            x5 = x5 + (frozenset(x8),)
            x8 = [(x9, x10)]
        x5 = x5 + (frozenset(x8),)
    return x5


def _run_sort_key_aa300dc3(
    run: Indices,
    cells: Indices,
    anti: Boolean,
) -> tuple[Integer, Integer, IntegerTuple]:
    x0 = uppermost(cells)
    x1 = lowermost(cells)
    x2 = leftmost(cells)
    x3 = rightmost(cells)
    x4, x5 = first(sorted(run))
    x6 = x4 + x5 if anti else x4 - x5
    x7 = x0 + x1 + x2 + x3 if anti else x0 + x1 - x2 - x3
    x8 = abs(double(x6) - x7)
    return (x8, x6, ulcorner(run))


def verify_aa300dc3(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, ZERO)
    x1 = _diagonal_runs_aa300dc3(x0, F)
    x2 = _diagonal_runs_aa300dc3(x0, T)
    x3 = valmax(x1, size)
    x4 = valmax(x2, size)
    x5 = tuple(x6 for x6 in x1 if size(x6) == x3)
    x6 = tuple(x7 for x7 in x2 if size(x7) == x4)
    x7 = first(sorted(x5, key=lambda x8: _run_sort_key_aa300dc3(x8, x0, F)))
    x8 = first(sorted(x6, key=lambda x9: _run_sort_key_aa300dc3(x9, x0, T)))
    x9 = _run_sort_key_aa300dc3(x7, x0, F)
    x10 = _run_sort_key_aa300dc3(x8, x0, T)
    if x3 > x4:
        x11 = x7
    elif x4 > x3:
        x11 = x8
    elif x9 <= x10:
        x11 = x7
    else:
        x11 = x8
    x12 = fill(I, EIGHT, x11)
    return x12
