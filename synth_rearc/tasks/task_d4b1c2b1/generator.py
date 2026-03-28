from synth_rearc.core import *


NCOLORS_D4B1C2B1 = (ONE, ONE, TWO, TWO, TWO, THREE, THREE, FOUR, FIVE)


def generate_d4b1c2b1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x0 = choice(NCOLORS_D4B1C2B1)
        x1 = sample(cols, x0)
        x2 = list(x1)
        x2.extend(choice(x1) for _ in range(NINE - x0))
        shuffle(x2)
        x3 = tuple(x2)
        gi = (
            x3[:THREE],
            x3[THREE:SIX],
            x3[SIX:NINE],
        )
        if numcolors(gi) != x0:
            continue
        go = upscale(gi, x0)
        return {"input": gi, "output": go}
