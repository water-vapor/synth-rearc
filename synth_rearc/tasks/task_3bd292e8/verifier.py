from collections import deque

from synth_rearc.core import *


def _region_graph_3bd292e8(
    I: Grid,
):
    x0 = objects(I, T, F, F)
    x1 = tuple(order(colorfilter(x0, SEVEN), ulcorner))
    x2 = {cell: idx for idx, obj in enumerate(x1) for cell in toindices(obj)}
    x3 = [set() for _ in x1]
    for x4 in ofcolor(I, TWO):
        x5 = {x2[x6] for x6 in dneighbors(x4) if x6 in x2}
        for x6 in x5:
            for x7 in x5:
                if x6 != x7:
                    x3[x6].add(x7)
    x4 = tuple(tuple(sorted(neighbors0)) for neighbors0 in x3)
    x5 = x2[(subtract(height(I), ONE), ZERO)]
    return x1, x4, x5


def verify_3bd292e8(
    I: Grid,
) -> Grid:
    x0, x1, x2 = _region_graph_3bd292e8(I)
    x3 = {x2: ZERO}
    x4 = deque((x2,))
    while len(x4) > ZERO:
        x5 = x4.popleft()
        for x6 in x1[x5]:
            if x6 not in x3:
                x3[x6] = increment(x3[x5])
                x4.append(x6)
    x5 = I
    for x6, x7 in enumerate(x0):
        x8 = branch(even(x3[x6]), FIVE, THREE)
        x5 = fill(x5, x8, x7)
    return x5
