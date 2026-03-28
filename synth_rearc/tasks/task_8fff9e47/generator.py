from synth_rearc.core import *


def generate_8fff9e47(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ZERO, TEN, ONE)
    while True:
        x1 = double(unifint(diff_lb, diff_ub, (TWO, THREE)))
        x2 = choice((T, F))
        x3 = FOUR if x2 else x1
        x4 = x1 if x2 else FOUR
        x5 = unifint(diff_lb, diff_ub, (SEVEN, TEN))
        x6 = sample(x0, x5)
        x7 = tuple(tuple(choice(x6) for _ in interval(ZERO, x1, ONE)) for _ in interval(ZERO, FOUR, ONE))
        if any(len(set(x8)) < TWO for x8 in x7):
            continue
        x8 = [ZERO, ZERO, ZERO, ZERO]
        x9 = []
        for i in interval(ZERO, x3, ONE):
            x10 = []
            for j in interval(ZERO, x4, ONE):
                x11 = multiply(i % TWO, TWO) + (j % TWO)
                x12 = x8[x11]
                x10.append(x7[x11][x12])
                x8[x11] = increment(x12)
            x9.append(tuple(x10))
        gi = tuple(x9)
        if numcolors(gi) < SIX:
            continue
        x13 = tuple(reversed(x7[ZERO]))
        x14 = tuple(reversed(x7[ONE]))
        x15 = tuple(reversed(x7[TWO]))
        x16 = tuple(reversed(x7[THREE]))
        x17 = decrement(x1)
        x18 = interval(ZERO, x1, ONE)
        x19 = tuple(tuple(x13[min(i, j)] for j in x18) for i in x18)
        x20 = tuple(tuple(x14[min(i, subtract(x17, j))] for j in x18) for i in x18)
        x21 = tuple(tuple(x15[min(subtract(x17, i), j)] for j in x18) for i in x18)
        x22 = tuple(
            tuple(x16[min(subtract(x17, i), subtract(x17, j))] for j in x18)
            for i in x18
        )
        go = vconcat(hconcat(x19, x20), hconcat(x21, x22))
        return {"input": gi, "output": go}
