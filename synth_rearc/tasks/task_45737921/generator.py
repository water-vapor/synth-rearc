from synth_rearc.core import *


BLOCK_SHAPE_45737921 = frozenset((i, j) for i in range(THREE) for j in range(THREE))
PATTERN_SEEDS_45737921 = (
    ((ONE, ZERO, ONE), (ONE, ZERO, ONE), (ZERO, ZERO, ZERO)),
    ((ZERO, ZERO, ONE), (ONE, ZERO, ONE), (ZERO, ZERO, ONE)),
    ((ONE, ZERO, ZERO), (ONE, ONE, ZERO), (ONE, ZERO, ZERO)),
    ((ONE, ZERO, ONE), (ONE, ZERO, ONE), (ONE, ONE, ONE)),
    ((ONE, ONE, ONE), (ZERO, ONE, ZERO), (ZERO, ZERO, ZERO)),
    ((ONE, ZERO, ONE), (ZERO, ZERO, ZERO), (ZERO, ONE, ZERO)),
    ((ONE, ZERO, ZERO), (ZERO, ONE, ONE), (ZERO, ONE, ONE)),
    ((ONE, ONE, ZERO), (ONE, ZERO, ZERO), (ZERO, ZERO, ZERO)),
)


def _pattern_library_45737921() -> tuple[Indices, ...]:
    x0 = []
    x1 = set()
    for x2 in PATTERN_SEEDS_45737921:
        x3 = (
            x2,
            rot90(x2),
            rot180(x2),
            rot270(x2),
            hmirror(x2),
            vmirror(x2),
            dmirror(x2),
            cmirror(x2),
        )
        for x4 in x3:
            if x4 in x1:
                continue
            x0.append(ofcolor(x4, ONE))
            x1.add(x4)
    return tuple(x0)


PATTERN_LIBRARY_45737921 = _pattern_library_45737921()


def _sample_layout_45737921(
    height_: int,
    width_: int,
    num_blocks: int,
) -> tuple[Indices, ...] | None:
    x0 = [(i, j) for i in range(ONE, subtract(height_, THREE)) for j in range(ONE, subtract(width_, THREE))]
    shuffle(x0)
    x1 = []
    for x2 in x0:
        x3 = shift(BLOCK_SHAPE_45737921, x2)
        if all(greater(manhattan(x3, x4), ONE) for x4 in x1):
            x1.append(x3)
            if len(x1) == num_blocks:
                return tuple(x1)
    return None


def generate_45737921(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ONE, TEN, ONE)
    x1 = unifint(diff_lb, diff_ub, (ONE, FOUR))
    x2 = double(SEVEN)
    while True:
        x3 = unifint(diff_lb, diff_ub, (SEVEN, x2))
        x4 = unifint(diff_lb, diff_ub, (SEVEN, x2))
        x5 = _sample_layout_45737921(x3, x4, x1)
        if x5 is None:
            continue
        x6 = unifint(diff_lb, diff_ub, (TWO, min(EIGHT, add(x1, TWO))))
        x7 = tuple(sample(x0, x6))
        x8 = canvas(ZERO, (x3, x4))
        x9 = x8
        x10 = list(PATTERN_LIBRARY_45737921)
        shuffle(x10)
        for x11, x12 in enumerate(x5):
            x13 = x10[x11]
            x14, x15 = sample(x7, TWO)
            x16 = shift(x13, ulcorner(x12))
            x8 = fill(x8, x15, x12)
            x8 = fill(x8, x14, x16)
            x9 = fill(x9, x14, x12)
            x9 = fill(x9, x15, x16)
        if palette(x8) == initset(ZERO):
            continue
        return {"input": x8, "output": x9}
