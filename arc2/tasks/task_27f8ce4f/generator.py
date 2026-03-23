from arc2.core import *


COUNT_PATTERNS_27F8CE4F = (
    (FOUR, THREE, TWO),
    (FOUR, TWO, TWO, ONE),
    (THREE, TWO, TWO, ONE, ONE),
    (THREE, TWO, TWO, ONE, ONE),
)


def generate_27f8ce4f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    dims = (THREE, THREE)
    inds = totuple(asindices(canvas(ZERO, dims)))
    while True:
        x0 = unifint(diff_lb, diff_ub, (ZERO, len(COUNT_PATTERNS_27F8CE4F) - ONE))
        counts = COUNT_PATTERNS_27F8CE4F[x0]
        palette0 = sample(cols, len(counts))
        domc = palette0[ZERO]
        domn = counts[ZERO]
        while True:
            domlocs = sample(inds, domn)
            if len({i for i, _ in domlocs}) < TWO:
                continue
            if len({j for _, j in domlocs}) < TWO:
                continue
            break
        rem = [ij for ij in inds if ij not in domlocs]
        shuffle(rem)
        obj = {(domc, ij) for ij in domlocs}
        start = ZERO
        for color_value, count_value in zip(palette0[ONE:], counts[ONE:]):
            for ij in rem[start:start + count_value]:
                obj.add((color_value, ij))
            start += count_value
        gi = paint(canvas(ZERO, dims), frozenset(obj))
        x1 = canvas(ZERO, multiply(dims, dims))
        x2 = asobject(gi)
        for loc in domlocs:
            x1 = paint(x1, shift(x2, multiply(loc, dims)))
        return {"input": gi, "output": x1}
