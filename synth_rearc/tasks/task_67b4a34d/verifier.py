from synth_rearc.core import *


def verify_67b4a34d(
    I: Grid,
) -> Grid:
    x0 = ofcolor(I, THREE)
    x1 = astuple(identity, dmirror)
    x2 = astuple(cmirror, hmirror)
    x3 = astuple(vmirror, rot90)
    x4 = astuple(rot180, rot270)
    x5 = combine(x1, x2)
    x6 = combine(x3, x4)
    x7 = combine(x5, x6)
    x8 = rbind(rapply, I)
    x9 = x8(x7)
    x10 = lbind(subgrid, x0)
    x11 = apply(x10, x9)
    x12 = rbind(colorcount, THREE)
    x13 = matcher(x12, ZERO)
    x14 = extract(x11, x13)
    return x14
