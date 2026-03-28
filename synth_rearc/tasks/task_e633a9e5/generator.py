from synth_rearc.core import *


def generate_e633a9e5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x0 = unifint(diff_lb, diff_ub, (FIVE, SEVEN))
        x1 = sample(cols, x0)
        x2 = list(x1) + [choice(x1) for _ in range(NINE - x0)]
        shuffle(x2)
        x3 = tuple(x2)
        gi = (
            x3[:THREE],
            x3[THREE:SIX],
            x3[SIX:NINE],
        )
        if numcolors(gi) != x0:
            continue
        x4 = tophalf(gi)
        x5 = crop(gi, DOWN, astuple(ONE, THREE))
        x6 = bottomhalf(gi)
        x7 = vconcat(x4, x4)
        x8 = vconcat(x7, x5)
        x9 = vconcat(x8, x6)
        x10 = vconcat(x9, x6)
        x11 = lefthalf(x10)
        x12 = crop(x10, RIGHT, astuple(FIVE, ONE))
        x13 = righthalf(x10)
        x14 = hconcat(x11, x11)
        x15 = hconcat(x14, x12)
        x16 = hconcat(x15, x13)
        go = hconcat(x16, x13)
        return {"input": gi, "output": go}
