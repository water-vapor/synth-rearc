from arc2.core import *


SEED_TEMPLATES_0becf7df = (
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ZERO, THREE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO), (TWO, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO)}),
    frozenset({(ZERO, ONE), (ZERO, TWO), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
)

SEED_TRANSFORMS_0becf7df = (
    identity,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
)


def seed_patch_0becf7df() -> Patch:
    x0 = choice(SEED_TEMPLATES_0becf7df)
    x1 = choice(SEED_TRANSFORMS_0becf7df)(x0)
    x2 = normalize(x1)
    return frozenset(x2)


def swap_key_pairs_0becf7df(grid: Grid) -> Grid:
    x0 = index(grid, ORIGIN)
    x1 = index(grid, RIGHT)
    x2 = index(grid, DOWN)
    x3 = index(grid, UNITY)
    x4 = switch(grid, x0, x1)
    x5 = switch(x4, x2, x3)
    x6 = fill(x5, x0, initset(ORIGIN))
    x7 = fill(x6, x1, initset(RIGHT))
    x8 = fill(x7, x2, initset(DOWN))
    x9 = fill(x8, x3, initset(UNITY))
    return x9
