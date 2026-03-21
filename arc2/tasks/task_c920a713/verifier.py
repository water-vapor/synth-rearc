from collections import Counter

from arc2.core import *


def verify_c920a713(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = order(x0, color)
    x2 = tuple(color(x3) for x3 in x1)
    x3 = {color(x4): x4 for x4 in x1}
    x4 = {x5: Counter(x6 for x6, _ in toobject(box(x3[x5]), I) if x6 != x5) for x5 in x2}
    x5 = {x6: sum(x7.values()) for x6, x7 in x4.items()}
    x6 = {x7: height(x3[x7]) * width(x3[x7]) for x7 in x2}
    x7 = [min(x2, key=lambda x8: (x5[x8], x6[x8], x8))]
    x8 = set(x2) - set(x7)
    while len(x8) > ZERO:
        x9 = set(x7)
        x10 = min(
            x8,
            key=lambda x11: (
                sum(x12 for x13, x12 in x4[x11].items() if x13 not in x9),
                -sum(x12 for x13, x12 in x4[x11].items() if x13 in x9),
                x5[x11],
                x6[x11],
                x11,
            ),
        )
        x7.append(x10)
        x8.remove(x10)
    x11 = tuple(reversed(x7))
    x12 = subtract(double(len(x11)), ONE)
    x13 = canvas(first(x11), (x12, x12))
    for x14, x15 in enumerate(x11[1:], ONE):
        x16 = decrement(subtract(x12, x14))
        x17 = frozenset({(x14, x14), (x16, x16)})
        x18 = box(x17)
        x13 = fill(x13, x15, x18)
    return x13
