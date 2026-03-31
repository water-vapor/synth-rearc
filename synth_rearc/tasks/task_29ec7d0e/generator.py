from synth_rearc.core import *


def generate_29ec7d0e(diff_lb: float, diff_ub: float) -> dict:
    x0 = interval(0, 10, 1)
    x1 = unifint(diff_lb, diff_ub, (10, 30))
    x2 = unifint(diff_lb, diff_ub, (10, 30))
    x3 = unifint(diff_lb, diff_ub, (2, subtract(divide(x1, 2), 1)))
    x4 = unifint(diff_lb, diff_ub, (2, subtract(divide(x2, 2), 1)))
    x5 = asindices(canvas(-1, (x3, x4)))
    x6, x7 = sample(x0, TWO)
    x8 = remove(x7, x0)
    x9 = unifint(diff_lb, diff_ub, (2, 9))
    x10 = sample(x8, x9)
    x11 = frozenset({(choice(x10), x12) for x12 in x5})
    x13 = canvas(x6, (x1, x2))
    x14 = set()
    for x15 in range(add(divide(x1, x3), 1)):
        for x16 in range(add(divide(x2, x4), 1)):
            x17 = add(x15, multiply(x3, x15))
            x18 = add(x16, multiply(x4, x16))
            x19 = (x17, x18)
            x14.add(x19)
            x13 = paint(x13, shift(x11, x19))
    x20 = unifint(diff_lb, diff_ub, (1, divide(multiply(x1, x2), 20)))
    x21 = tuple(e for e in x13)
    x22 = apply(lbind(shift, x5), x14)
    x23 = 0
    x24 = 0
    x25 = multiply(5, x20)
    while both(x23 < x20, x24 < x25):
        x24 += 1
        x26 = randint(2, 6)
        x27 = randint(2, 6)
        x28 = randint(0, subtract(x1, x26))
        x29 = randint(0, subtract(x2, x27))
        x30 = backdrop(frozenset({(x28, x29), (add(x28, subtract(x26, 1)), add(x29, subtract(x27, 1)))}))
        x31 = fill(x21, x7, x30)
        x32 = apply(rbind(toobject, x31), x22)
        x33 = apply(normalize, x32)
        x34 = contained(x11, x33)
        x35 = len(sfilter(x31, lambda x36: x7 not in x36)) >= 2
        x37 = len(sfilter(dmirror(x31), lambda x38: x7 not in x38)) >= 2
        if both(x34, both(x35, x37)):
            x23 += 1
            x21 = x31
    x39 = choice((identity, rot90, rot180, rot270))
    x40 = x39(x21)
    x41 = x39(x13)
    return {"input": x40, "output": x41}
