from synth_rearc.core import *


def generate_0c786b71(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        x0 = tuple(sample(cols, THREE))
        gi = tuple(tuple(choice(x0) for _ in range(FOUR)) for _ in range(THREE))
        if numcolors(gi) != THREE:
            continue
        x1 = merge(gi)
        x2 = tuple(x1.count(x3) for x3 in x0)
        if min(x2) < TWO:
            continue
        if max(x2) > SIX:
            continue
        if gi == hmirror(gi):
            continue
        if gi == vmirror(gi):
            continue
        if gi == rot180(gi):
            continue
        if len(set(gi)) < THREE:
            continue
        x3 = tuple(zip(*gi))
        if any(len(set(x4)) == ONE for x4 in gi):
            continue
        if any(len(set(x4)) == ONE for x4 in x3):
            continue
        x4 = rot180(gi)
        x5 = hmirror(gi)
        x6 = vmirror(gi)
        x7 = hconcat(x4, x5)
        x8 = hconcat(x6, gi)
        go = vconcat(x7, x8)
        return {"input": gi, "output": go}
