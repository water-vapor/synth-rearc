from synth_rearc.core import *


def verify_65b59efc(
    I: Grid,
) -> Grid:
    x0 = len(I)
    x1 = len(I[ZERO])
    x2 = tuple(
        j for j in range(x1)
        if FIVE in {I[i][j] for i in range(x0)}
        and {I[i][j] for i in range(x0)} <= {ZERO, FIVE}
    )
    x3 = first(x2)
    x4 = tuple(j for j in x2 if subtract(subtract(x1, j), ONE) >= x3)
    x5 = add(size(x4), ONE)
    x6 = add(x3, ONE)
    x7 = interval(ZERO, x5, ONE)
    x8 = lbind(multiply, x6)
    x9 = apply(x8, x7)
    x10 = tuple(crop(I, (ZERO, j), (x3, x3)) for j in x9)
    x11 = tuple(crop(I, (add(x3, ONE), j), (x3, x3)) for j in x9)
    x12 = add(multiply(TWO, x3), THREE)
    x13 = extract(
        interval(x12, x0, ONE),
        lambda i: any(v not in (ZERO, FIVE) for v in I[i]),
    )
    x14 = tuple(I[x13][j:j + x3] for j in x9)
    x15 = tuple(other(palette(x), ZERO) for x in x10)
    x16 = tuple(other(frozenset(x), ZERO) for x in x14)
    x17 = tuple(extract(x11, lambda g, c=x: contained(c, palette(g))) for x in x15)
    x18 = multiply(x3, x3)
    x19 = canvas(ZERO, (x18, x18))
    for x20, x21, x22, x23 in zip(x10, x17, x15, x16):
        x24 = asobject(replace(x20, x22, x23))
        x25 = ofcolor(x21, x22)
        for x26 in x25:
            x27 = multiply(x26[ZERO], x3)
            x28 = multiply(x26[ONE], x3)
            x29 = shift(x24, (x27, x28))
            x19 = paint(x19, x29)
    return x19
