from synth_rearc.core import *


def verify_6a980be1(I: Grid) -> Grid:
    x0 = index(I, ORIGIN)
    x1 = objects(I, T, F, F)
    x2 = colorfilter(x1, THREE)
    x3 = colorfilter(x1, TWO)
    x4 = first(x2)
    x5 = vline(x4)
    x6 = branch(x5, uppermost, leftmost)
    x7 = order(x3, x6)
    x8 = first(x7)
    x9 = apply(x6, x7)
    x10 = first(x9)
    x11 = x9[ONE]
    x12 = subtract(x11, x10)
    x13 = branch(x5, height, width)(x8)
    x14 = branch(x5, height(I), width(I))
    x15 = decrement(x14)
    x16 = branch(x5, compose(hfrontier, toivec), compose(vfrontier, tojvec))
    x17 = canvas(ZERO, shape(I))
    x18 = x10
    while True:
        if greater(x18, x15):
            break
        x19 = ZERO
        while True:
            if greater(x19, decrement(x13)):
                break
            x20 = add(x18, x19)
            if greater(x20, x15):
                break
            x21 = x16(x20)
            x17 = fill(x17, x0, x21)
            x19 = increment(x19)
        x18 = add(x18, x12)
    x22 = ofcolor(I, THREE)
    x23 = apply(last, x22)
    x24 = apply(first, x22)
    x25 = branch(x5, x23, x24)
    x26 = branch(x5, compose(vfrontier, tojvec), compose(hfrontier, toivec))
    x27 = mapply(x26, x25)
    x28 = fill(x17, THREE, x27)
    x29 = minimum(x23)
    x30 = maximum(x23)
    x31 = minimum(x24)
    x32 = maximum(x24)
    x33 = interval(ZERO, height(I), ONE)
    x34 = interval(ZERO, width(I), ONE)
    x35 = product(x33, interval(increment(x29), x30, ONE))
    x36 = product(interval(increment(x31), x32, ONE), x34)
    x37 = branch(x5, x35, x36)
    x38 = intersection(x37, ofcolor(x17, x0))
    x39 = fill(x28, TWO, x38)
    return x39
