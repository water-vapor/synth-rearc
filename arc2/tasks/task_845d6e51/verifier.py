from arc2.core import *


def _shape_variants_845d6e51(x0: Patch) -> tuple[Indices, ...]:
    x1 = normalize(toindices(x0))
    x2 = canvas(ZERO, shape(x1))
    x3 = fill(x2, ONE, x1)
    x4 = (
        ofcolor(x3, ONE),
        ofcolor(rot90(x3), ONE),
        ofcolor(rot180(x3), ONE),
        ofcolor(rot270(x3), ONE),
        ofcolor(hmirror(x3), ONE),
        ofcolor(vmirror(x3), ONE),
        ofcolor(dmirror(x3), ONE),
        ofcolor(cmirror(x3), ONE),
    )
    return tuple(dict.fromkeys(x4))


def verify_845d6e51(I: Grid) -> Grid:
    x0 = tuple(row.count(FIVE) for row in I)
    x1 = x0.index(max(x0))
    x2 = max(j for j, x3 in enumerate(I[x1]) if x3 == FIVE)
    x3 = crop(I, ORIGIN, (x1, x2))
    x4 = objects(x3, T, F, T)
    x5 = tuple((color(x6), _shape_variants_845d6e51(x6)) for x6 in x4)
    x6 = objects(I, T, F, T)
    x7 = colorfilter(x6, THREE)
    x8 = I
    for x9 in x7:
        x10 = normalize(toindices(x9))
        x11 = next(x12 for x12, x13 in x5 if x10 in x13)
        x14 = recolor(x11, x9)
        x8 = paint(x8, x14)
    return x8
