from synth_rearc.core import *


BLOCK_SHAPE_AF24B4CC = astuple(THREE, TWO)
BLOCK_OFFSETS_AF24B4CC = (
    UNITY,
    astuple(ONE, FOUR),
    astuple(ONE, SEVEN),
    astuple(FIVE, ONE),
    astuple(FIVE, FOUR),
    astuple(FIVE, SEVEN),
)
BLOCK_CELLS_AF24B4CC = tuple(product(interval(ZERO, THREE, ONE), interval(ZERO, TWO, ONE)))


def generate_af24b4cc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        ncols = unifint(diff_lb, diff_ub, (THREE, SIX))
        palette0 = tuple(sample(cols, ncols))
        dominants = tuple(choice(palette0) for _ in range(SIX))
        if len(set(dominants)) < THREE:
            continue
        if len(set(dominants[:THREE])) == ONE:
            continue
        if len(set(dominants[THREE:])) == ONE:
            continue
        noise_counts = tuple(choice((ZERO, ONE, TWO, TWO, TWO, TWO)) for _ in range(SIX))
        if noise_counts.count(ZERO) > TWO:
            continue
        if sum(x0 > ZERO for x0 in noise_counts) < FOUR:
            continue
        gi = canvas(ZERO, (NINE, TEN))
        go = canvas(ZERO, (FOUR, FIVE))
        for x0, x1 in enumerate(BLOCK_OFFSETS_AF24B4CC):
            x2 = dominants[x0]
            x3 = noise_counts[x0]
            x4 = remove(x2, palette0)
            if len(x4) == ZERO:
                x4 = remove(x2, cols)
            x5 = choice(x4)
            x6 = frozenset(sample(BLOCK_CELLS_AF24B4CC, x3))
            x7 = canvas(x2, BLOCK_SHAPE_AF24B4CC)
            x8 = fill(x7, x5, x6)
            x9 = shift(asobject(x8), x1)
            gi = paint(gi, x9)
            x10 = astuple(ONE + x0 // THREE, ONE + x0 % THREE)
            go = fill(go, x2, initset(x10))
        return {"input": gi, "output": go}
