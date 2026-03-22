from arc2.core import *


def verify_94133066(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = colorfilter(x0, ONE)
    x2 = argmax(x1, size)
    x3 = subgrid(x2, I)
    x4 = backdrop(x2)
    x5 = sizefilter(x0, ONE)
    x6 = compose(rbind(contained, x4), ulcorner)
    x7 = sfilter(x5, compose(flip, x6))
    x8 = apply(color, x7)
    x9 = compose(rbind(contained, x8), color)
    x10 = normalize(merge(x7))
    x11 = astuple(identity, rot90)
    x12 = astuple(rot180, rot270)
    x13 = combine(x11, x12)
    x14 = astuple(dmirror, cmirror)
    x15 = astuple(hmirror, vmirror)
    x16 = combine(x14, x15)
    x17 = combine(x13, x16)
    x18 = lambda x19: normalize(
        merge(sfilter(sizefilter(objects(x19(x3), T, F, T), ONE), x9))
    )
    x19 = matcher(x18, x10)
    x20 = extract(x17, x19)
    x21 = x20(x3)
    return x21
