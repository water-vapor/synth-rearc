from synth_rearc.core import *


def generate_62b74c02(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        h = unifint(diff_lb, diff_ub, (THREE, FOUR))
        w = unifint(diff_lb, diff_ub, (THREE, FOUR))
        gap = double(unifint(diff_lb, diff_ub, (TWO, THREE)))
        ncols = unifint(diff_lb, diff_ub, (THREE, FOUR))
        palette0 = sample(cols, ncols)
        rows = []
        for _ in range(h):
            edge = choice(palette0)
            middle = [choice(palette0) for _ in range(w - TWO)]
            if all(value == edge for value in middle):
                idx = randint(ZERO, len(middle) - ONE)
                middle[idx] = choice(remove(edge, palette0))
            row = (edge,) + tuple(middle) + (edge,)
            rows.append(row)
        block = tuple(rows)
        if numcolors(block) != ncols:
            continue
        if len(set(block)) == ONE:
            continue
        x0 = crop(block, ORIGIN, (h, ONE))
        x1 = hupscale(x0, gap)
        gi = hconcat(block, canvas(ZERO, (h, add(gap, w))))
        go = hconcat(hconcat(block, x1), block)
        return {"input": gi, "output": go}
