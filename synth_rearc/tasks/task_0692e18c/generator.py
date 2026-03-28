from synth_rearc.core import *


def generate_0692e18c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = canvas(ZERO, (THREE, THREE))
    x1 = totuple(asindices(x0))
    x2 = choice((THREE, THREE, FOUR, FOUR, FOUR, FIVE, FIVE, FIVE, SIX, SIX))
    x3 = sample(x1, x2)
    x4 = frozenset(x3)
    x5 = randint(ONE, NINE)
    gi = fill(x0, x5, x4)
    x6 = switch(gi, ZERO, x5)
    x7 = shape(gi)
    x8 = multiply(x7, x7)
    go = canvas(ZERO, x8)
    x9 = asobject(x6)
    x10 = ofcolor(gi, x5)
    x11 = rbind(multiply, x7)
    x12 = apply(x11, x10)
    x13 = lbind(shift, x9)
    x14 = mapply(x13, x12)
    go = paint(go, x14)
    return {"input": gi, "output": go}
