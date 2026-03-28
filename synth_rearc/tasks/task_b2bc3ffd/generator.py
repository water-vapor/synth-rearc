from synth_rearc.core import *


SHAPES_B2BC3FFD = (
    frozenset({(ZERO, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ZERO, THREE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE), (ONE, TWO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ZERO, THREE), (ZERO, FOUR)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ZERO, THREE), (ZERO, FOUR), (ZERO, FIVE)}),
)

SHAPE_POOL_B2BC3FFD = (
    SHAPES_B2BC3FFD[ZERO],
    SHAPES_B2BC3FFD[ONE],
    SHAPES_B2BC3FFD[ONE],
    SHAPES_B2BC3FFD[TWO],
    SHAPES_B2BC3FFD[TWO],
    SHAPES_B2BC3FFD[THREE],
    SHAPES_B2BC3FFD[THREE],
    SHAPES_B2BC3FFD[FOUR],
    SHAPES_B2BC3FFD[FIVE],
    SHAPES_B2BC3FFD[FIVE],
    SHAPES_B2BC3FFD[SIX],
    SHAPES_B2BC3FFD[SEVEN],
    SHAPES_B2BC3FFD[EIGHT],
    SHAPES_B2BC3FFD[NINE],
    SHAPES_B2BC3FFD[TEN],
    SHAPES_B2BC3FFD[11],
    SHAPES_B2BC3FFD[12],
    SHAPES_B2BC3FFD[13],
)

COLORS_B2BC3FFD = tuple(c for c in interval(ONE, TEN, ONE) if c not in (SEVEN, EIGHT))


def _base_grid_b2bc3ffd() -> Grid:
    x0 = canvas(SEVEN, (EIGHT, EIGHT))
    x1 = frozenset((SEVEN, x2) for x2 in range(EIGHT))
    return fill(x0, EIGHT, x1)


def _shape_ok_b2bc3ffd(shape_: Indices) -> bool:
    x0 = size(shape_)
    x1 = height(shape_)
    return x0 <= subtract(SEVEN, x1)


def _sample_shape_b2bc3ffd() -> Indices:
    while True:
        x0 = choice(SHAPE_POOL_B2BC3FFD)
        x1 = branch(choice((T, F)), x0, vmirror(x0))
        if _shape_ok_b2bc3ffd(x1):
            return x1


def _sample_shapes_b2bc3ffd(diff_lb: float, diff_ub: float) -> tuple[Indices, ...]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x1 = tuple(_sample_shape_b2bc3ffd() for _ in range(x0))
        x2 = tuple(width(x3) for x3 in x1)
        if sum(x2) + x0 - ONE > EIGHT:
            continue
        x3 = tuple(size(x4) for x4 in x1)
        if sum(x3) < FIVE:
            continue
        if max(x3) < THREE:
            continue
        return x1


def _column_starts_b2bc3ffd(widths: tuple[int, ...]) -> tuple[int, ...]:
    x0 = len(widths)
    x1 = EIGHT - sum(widths) - (x0 - ONE)
    x2 = [ZERO for _ in range(x0 + ONE)]
    for _ in range(x1):
        x3 = randint(ZERO, x0)
        x2[x3] += ONE
    x4 = [x2[ZERO]]
    x5 = x4[ZERO]
    for x6, x7 in enumerate(widths[:-ONE]):
        x5 += x7 + ONE + x2[x6 + ONE]
        x4.append(x5)
    return tuple(x4)


def _input_patch_b2bc3ffd(shape_: Indices, left: int) -> Indices:
    x0 = subtract(SEVEN, height(shape_))
    return shift(shape_, (x0, left))


def generate_b2bc3ffd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_shapes_b2bc3ffd(diff_lb, diff_ub)
        x1 = tuple(width(x2) for x2 in x0)
        x2 = _column_starts_b2bc3ffd(x1)
        x3 = sample(COLORS_B2BC3FFD, len(x0))
        x4 = _base_grid_b2bc3ffd()
        x5 = _base_grid_b2bc3ffd()
        x6 = []
        for x7, x8, x9 in zip(x0, x2, x3):
            x10 = _input_patch_b2bc3ffd(x7, x8)
            x11 = recolor(x9, x10)
            x12 = astuple(invert(size(x10)), ZERO)
            x13 = shift(x11, x12)
            x4 = paint(x4, x11)
            x5 = paint(x5, x13)
            x6.append((x10, x13))
        x14 = frozenset()
        x15 = frozenset()
        x16 = T
        for x17, x18 in x6:
            if len(intersection(x14, x17)) > ZERO:
                x16 = F
                break
            if len(intersection(x15, toindices(x18))) > ZERO:
                x16 = F
                break
            x14 = combine(x14, x17)
            x15 = combine(x15, toindices(x18))
        if x16:
            return {"input": x4, "output": x5}
