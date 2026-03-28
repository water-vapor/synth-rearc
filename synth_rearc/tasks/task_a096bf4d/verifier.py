from synth_rearc.core import *


SLOT_OFFSETS_A096BF4D = ((ONE, ONE), (ONE, TWO), (TWO, ONE), (TWO, TWO))


def verify_a096bf4d(I: Grid) -> Grid:
    x0 = len(I)
    x1 = len(I[ZERO])
    x2 = tuple(i for i in range(x0) if set(I[i]) == {ZERO})
    x3 = tuple(j for j in range(x1) if all(I[i][j] == ZERO for i in range(x0)))
    x4 = tuple(i for i in range(x0) if i not in x2)
    x5 = tuple(j for j in range(x1) if j not in x3)
    x6 = x4[::FOUR]
    x7 = x5[::FOUR]
    x8 = list(list(r) for r in I)
    x9 = tuple(
        mostcommon(tuple(I[add(r, di)][add(c, dj)] for r in x6 for c in x7))
        for di, dj in SLOT_OFFSETS_A096BF4D
    )
    for x10, (x11, x12) in enumerate(SLOT_OFFSETS_A096BF4D):
        x13 = x9[x10]
        for x14, x15 in enumerate(x6):
            x16 = {}
            for x17, x18 in enumerate(x7):
                x19 = I[add(x15, x11)][add(x18, x12)]
                if x19 != x13:
                    x16.setdefault(x19, []).append(x17)
            for x20, x21 in x16.items():
                if len(x21) < TWO:
                    continue
                x22 = minimum(tuple(x21))
                x23 = maximum(tuple(x21))
                for x24 in range(increment(x22), x23):
                    x25 = x7[x24]
                    if x8[add(x15, x11)][add(x25, x12)] == x13:
                        x8[add(x15, x11)][add(x25, x12)] = x20
        for x26, x27 in enumerate(x7):
            x28 = {}
            for x29, x30 in enumerate(x6):
                x31 = I[add(x30, x11)][add(x27, x12)]
                if x31 != x13:
                    x28.setdefault(x31, []).append(x29)
            for x32, x33 in x28.items():
                if len(x33) < TWO:
                    continue
                x34 = minimum(tuple(x33))
                x35 = maximum(tuple(x33))
                for x36 in range(increment(x34), x35):
                    x37 = x6[x36]
                    if x8[add(x37, x11)][add(x27, x12)] == x13:
                        x8[add(x37, x11)][add(x27, x12)] = x32
    x38 = tuple(tuple(r) for r in x8)
    return x38
