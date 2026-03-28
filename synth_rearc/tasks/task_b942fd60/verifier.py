import heapq

from synth_rearc.core import *


def verify_b942fd60(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = x0[0]
    x2 = first(ofcolor(I, TWO))
    x3 = I
    x4 = [(ZERO, ZERO, x2, RIGHT)]
    x5 = ONE
    x6 = set()
    x7 = {x2: x2}
    while len(x4) > ZERO:
        x8, _, x9, x10 = heapq.heappop(x4)
        x11 = (x9, x10)
        if x11 in x6:
            continue
        x6.add(x11)
        x12 = x9
        x13 = ZERO
        while True:
            x14 = add(x12, x10)
            x15 = index(I, x14)
            if equality(x15, ZERO):
                x3 = fill(x3, TWO, initset(x14))
                x12 = x14
                x13 = increment(x13)
                continue
            x16 = x14 in x7 and equality(x7[x14], x12)
            x17 = both(x16, equality(x13, ZERO))
            if x17:
                x12 = x14
                continue
            break
        x18 = equality(x10, DOWN)
        x19 = equality(x15, SEVEN)
        x20 = equality(x14[0], decrement(x1))
        x21 = both(x18, both(x19, x20))
        if x15 is None or contained(x14, x7) or x21:
            continue
        x22 = add(x8, x13)
        x7[x14] = x12
        if equality(x10[0], ZERO):
            heapq.heappush(x4, (x22, x5, x12, UP))
            x5 = increment(x5)
            heapq.heappush(x4, (x22, x5, x12, DOWN))
            x5 = increment(x5)
        else:
            heapq.heappush(x4, (x22, x5, x12, LEFT))
            x5 = increment(x5)
            heapq.heappush(x4, (x22, x5, x12, RIGHT))
            x5 = increment(x5)
    return x3
