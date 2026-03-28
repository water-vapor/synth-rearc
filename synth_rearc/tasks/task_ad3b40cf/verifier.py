from synth_rearc.core import *


def verify_ad3b40cf(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = matcher(color, ONE)
    x2 = extract(x0, x1)
    x3 = remove(x2, x0)
    x4 = argmin(x3, size)
    x5 = color(x4)
    x6 = vline(x2)
    x7 = hline(x2)
    x8 = toindices(x2)
    x9 = contained(ORIGIN, x8)
    x10 = branch(x6, vmirror, branch(x7, hmirror, branch(x9, dmirror, cmirror)))
    x11 = x10(I)
    x12 = ofcolor(x11, x5)
    x13 = underfill(I, x5, x12)
    return x13
