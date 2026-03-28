from synth_rearc.core import *


NREPEATS_A59B95C0 = (TWO, TWO, THREE, THREE, FOUR)
FG_COLORS_A59B95C0 = remove(ZERO, interval(ZERO, TEN, ONE))


def _tile_grid_a59b95c0(grid: Grid, factor: Integer) -> Grid:
    x0 = rbind(repeat, factor)
    x1 = compose(merge, x0)
    x2 = apply(x1, grid)
    x3 = repeat(x2, factor)
    x4 = merge(x3)
    return x4


def generate_a59b95c0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(NREPEATS_A59B95C0)
        x1 = sample(FG_COLORS_A59B95C0, x0)
        x2 = list(x1)
        x2.extend(choice(x1) for _ in range(subtract(NINE, x0)))
        shuffle(x2)
        x3 = tuple(x2)
        gi = (
            x3[:THREE],
            x3[THREE:SIX],
            x3[SIX:NINE],
        )
        if numcolors(gi) != x0:
            continue
        go = _tile_grid_a59b95c0(gi, x0)
        return {"input": gi, "output": go}
