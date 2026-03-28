from synth_rearc.core import *


def verify_ecaa0ec1(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = argmax(x0, size)
    x2 = ulcorner(x1)
    x3 = crop(I, x2, shape(x1))
    x4 = ofcolor(I, FOUR)
    x5 = centerofmass(x1)
    x6 = (ulcorner(x1), urcorner(x1), lrcorner(x1), llcorner(x1))
    x7 = tuple(subtract(x, x5) for x in x6)
    x8 = tuple(bool(ineighbors(x) & x4) for x in x6)
    x9 = x8.index(True)
    x10 = tuple(
        frozenset({
            add(x6[i], toivec(multiply(x7[i][0], TWO))),
            add(x6[i], tojvec(multiply(x7[i][1], TWO))),
            add(x6[i], multiply(x7[i], TWO)),
        })
        for i in range(FOUR)
    )
    x11 = tuple(x10[i] <= x4 for i in range(FOUR))
    x12 = x11.index(True)
    x13 = (x12 - x9) % FOUR
    x14 = branch(
        equality(x13, ZERO),
        x3,
        branch(
            equality(x13, ONE),
            rot90(x3),
            branch(equality(x13, TWO), rot180(x3), rot270(x3)),
        ),
    )
    x15 = add(x6[x12], x7[x12])
    x16 = canvas(ZERO, shape(I))
    x17 = paint(x16, shift(asobject(x14), x2))
    x18 = fill(x17, FOUR, frozenset({x15}))
    return x18
