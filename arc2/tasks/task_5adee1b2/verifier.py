from arc2.core import *


def verify_5adee1b2(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = matcher(leftmost, ZERO)
    x2 = sfilter(x0, x1)
    x3 = matcher(height, TWO)
    x4 = sfilter(x2, x3)
    x5 = matcher(width, ONE)
    x6 = sfilter(x4, x5)
    x7 = order(x6, uppermost)
    x8 = rbind(shift, RIGHT)
    x9 = apply(x8, x7)
    x10 = rbind(toobject, I)
    x11 = apply(x10, x9)
    x12 = {color(x): color(y) for x, y in zip(x7, x11)}
    x13 = combine(x6, x11)
    x14 = difference(x0, x13)
    x15 = tuple(obj for obj in x14 if color(obj) in x12)
    x16 = []
    for obj in x15:
        x17 = canvas(ZERO, shape(obj))
        x18 = fill(x17, ONE, normalize(obj))
        x19 = objects(x18, T, F, F)
        x20 = colorfilter(x19, ZERO)
        x21 = rbind(bordering, x18)
        x22 = sfilter(x20, x21)
        x23 = shift(toindices(merge(x22)), ulcorner(obj))
        x24 = combine(x23, outbox(obj))
        x25 = recolor(x12[color(obj)], x24)
        x16.append(x25)
    x26 = merge(frozenset(x16)) if len(x16) > ZERO else frozenset({})
    x27 = underpaint(I, x26)
    return x27
