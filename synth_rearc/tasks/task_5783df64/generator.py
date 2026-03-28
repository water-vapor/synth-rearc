from synth_rearc.core import *


COLORS = interval(ONE, TEN, ONE)


def generate_5783df64(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    block_size = unifint(diff_lb, diff_ub, (TWO, THREE))
    colors = sample(COLORS, NINE)
    go = tuple(tuple(colors[THREE * i:THREE * (i + ONE)]) for i in range(THREE))
    side = multiply(THREE, block_size)
    gi = canvas(ZERO, (side, side))
    offsets = interval(ZERO, block_size, ONE)
    for i in range(THREE):
        for j in range(THREE):
            di = choice(offsets)
            dj = choice(offsets)
            loc = (i * block_size + di, j * block_size + dj)
            gi = fill(gi, go[i][j], initset(loc))
    return {"input": gi, "output": go}
