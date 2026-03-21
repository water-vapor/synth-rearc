from arc2.core import *


def generate_c48954c1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        ncols = choice((THREE, FOUR, FOUR))
        palette0 = tuple(sample(cols, ncols))
        x0 = choice(palette0)
        x1 = remove(x0, palette0)
        x2 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        vals = [x0] * x2
        vals.extend(x1)
        x3 = NINE - len(vals)
        vals.extend(choice(x1) for _ in range(x3))
        shuffle(vals)
        gi = (
            tuple(vals[:THREE]),
            tuple(vals[THREE:SIX]),
            tuple(vals[SIX:NINE]),
        )
        x4 = tuple(zip(*gi))
        if len(set(gi)) < THREE:
            continue
        if len(set(x4)) < THREE:
            continue
        if any(len(set(x5)) == ONE for x5 in gi):
            continue
        if any(len(set(x5)) == ONE for x5 in x4):
            continue
        x5 = vmirror(gi)
        x6 = hconcat(x5, gi)
        x7 = hconcat(x6, x5)
        x8 = hmirror(x7)
        go = vconcat(vconcat(x8, x7), x8)
        return {"input": gi, "output": go}
