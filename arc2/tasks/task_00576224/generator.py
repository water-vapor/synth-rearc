from arc2.core import *


def generate_00576224(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        ncols = unifint(diff_lb, diff_ub, (THREE, FOUR))
        palette0 = sample(cols, ncols)
        vals = tuple(choice(palette0) for _ in range(FOUR))
        gi = (
            (vals[ZERO], vals[ONE]),
            (vals[TWO], vals[THREE]),
        )
        if numcolors(gi) != ncols:
            continue
        if gi[ZERO][ZERO] == gi[ZERO][ONE]:
            continue
        if gi[ONE][ZERO] == gi[ONE][ONE]:
            continue
        x0 = hconcat(gi, gi)
        x1 = hconcat(x0, gi)
        x2 = vmirror(x1)
        go = vconcat(vconcat(x1, x2), x1)
        return {"input": gi, "output": go}
