from synth_rearc.core import *


def verify_29ec7d0e(I: Grid) -> Grid:
    x0 = height(I)
    x1 = width(I)
    x2 = palette(I)
    x3 = None
    x4 = None
    for x5 in x2:
        for x6 in range(ONE, x0 // TWO + ONE):
            for x7 in range(ONE, x1 // TWO + ONE):
                x8 = {}
                x9 = T
                for x10 in range(x0):
                    for x11 in range(x1):
                        x12 = I[x10][x11]
                        if equality(x12, x5):
                            continue
                        x13 = (x10 % x6, x11 % x7)
                        x14 = x8.get(x13)
                        if x14 is None:
                            x8[x13] = x12
                        elif x14 != x12:
                            x9 = F
                            break
                    if flip(x9):
                        break
                if flip(x9):
                    continue
                x15 = (multiply(x6, x7), add(x6, x7), x5)
                if equality(len(x8), multiply(x6, x7)):
                    if x4 is None or x15 < x4:
                        x3 = (x6, x7, x8)
                        x4 = x15
                    continue
                x16 = []
                for x17 in range(x6):
                    x18 = {x8[(x17, x19)] for x19 in range(x7) if (x17, x19) in x8}
                    if equality(len(x18), ONE):
                        x16.append((x17, next(iter(x18))))
                x20 = []
                for x21 in range(x7):
                    x22 = {x8[(x23, x21)] for x23 in range(x6) if (x23, x21) in x8}
                    if equality(len(x22), ONE):
                        x20.append((x21, next(iter(x22))))
                for x24, x25 in x16:
                    for x26, x27 in x20:
                        if x25 != x27:
                            continue
                        x28 = T
                        for x29 in range(x6):
                            for x30 in range(x7):
                                x31 = (x29, x30)
                                if either(equality(x29, x24), equality(x30, x26)):
                                    if x31 in x8 and x8[x31] != x25:
                                        x28 = F
                                        break
                                elif x31 not in x8:
                                    x28 = F
                                    break
                            if flip(x28):
                                break
                        if flip(x28):
                            continue
                        x32 = (multiply(x6, x7), add(x6, x7), x5, x24, x26)
                        if x4 is None or x32 < x4:
                            x33 = {}
                            for x34 in range(x6):
                                for x35 in range(x7):
                                    x36 = (x34, x35)
                                    x33[x36] = x25 if either(equality(x34, x24), equality(x35, x26)) else x8[x36]
                            x3 = (x6, x7, x33)
                            x4 = x32
    if x3 is None:
        raise RuntimeError("no periodic completion found for 29ec7d0e")
    x37, x38, x39 = x3
    return tuple(tuple(x39[(x40 % x37, x41 % x38)] for x41 in range(x1)) for x40 in range(x0))
