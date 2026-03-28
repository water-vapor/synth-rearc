from synth_rearc.core import *


PALETTE_SIZES_BC4146BD = (TWO, THREE, THREE)


def generate_bc4146bd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x1 = choice(PALETTE_SIZES_BC4146BD)
        x2 = tuple(sample(x0, x1))
        gi = tuple(tuple(choice(x2) for _ in range(FOUR)) for _ in range(FOUR))
        x3 = merge(gi)
        x4 = tuple(x3.count(x5) for x5 in x2)
        if min(x4) < TWO:
            continue
        if len(set(gi)) < THREE:
            continue
        if gi == vmirror(gi):
            continue
        x6 = vmirror(gi)
        x7 = hconcat(gi, x6)
        x8 = hconcat(x7, gi)
        x9 = hconcat(x8, x6)
        go = hconcat(x9, gi)
        return {"input": gi, "output": go}
