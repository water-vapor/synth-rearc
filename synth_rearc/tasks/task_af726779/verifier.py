from synth_rearc.core import *


def _next_columns_af726779(cols: tuple[int, ...]) -> tuple[int, ...]:
    if size(cols) < TWO:
        return ()
    x0 = fork(remove, last, identity)
    x1 = fork(remove, first, identity)
    x2 = fork(pair, x0, x1)
    x3 = fork(subtract, last, first)
    x4 = matcher(x3, TWO)
    x5 = rbind(sfilter, x4)
    x6 = compose(x5, x2)
    x7 = fork(add, first, last)
    x8 = compose(halve, x7)
    x9 = lbind(apply, x8)
    x10 = compose(x9, x6)
    return x10(cols)


def verify_af726779(I: Grid) -> Grid:
    x0 = ofcolor(I, SEVEN)
    x1 = uppermost(x0)
    x2 = apply(last, x0)
    x3 = order(x2, identity)
    x4 = I
    x5 = x3
    x6 = add(x1, TWO)
    x7 = SIX
    x8 = height(I)
    while both(greater(x8, x6), greater(size(x5), ONE)):
        x5 = _next_columns_af726779(x5)
        if size(x5) == ZERO:
            break
        x9 = product((x6,), x5)
        x4 = fill(x4, x7, x9)
        x6 = add(x6, TWO)
        x7 = branch(equality(x7, SIX), SEVEN, SIX)
    return x4
