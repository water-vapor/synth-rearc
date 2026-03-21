from arc2.core import *

from .verifier import verify_a834deea


STENCIL_CELLS_A834DEEA = (
    (ONE, UNITY),
    (SEVEN, (ONE, TWO)),
    (SIX, (ONE, THREE)),
    (FOUR, (TWO, ONE)),
    (FIVE, (TWO, THREE)),
    (TWO, (THREE, ONE)),
    (NINE, (THREE, TWO)),
    (THREE, (THREE, THREE)),
)
INTERIOR_CELLS_A834DEEA = frozenset(
    (i, j)
    for i in range(ONE, FOUR)
    for j in range(ONE, FOUR)
)
INTERIOR_CENTER_A834DEEA = TWO_BY_TWO


def _sample_interior_a834deea(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    x0 = tuple(INTERIOR_CELLS_A834DEEA)
    x1 = (THREE, THREE, FOUR, FOUR, FIVE, FIVE, FIVE, SIX, SEVEN, EIGHT)
    for _ in range(200):
        x2 = choice(x1)
        x3 = unifint(diff_lb, diff_ub, (ZERO, subtract(x2, THREE)))
        x4 = add(THREE, x3)
        x5 = frozenset(sample(x0, x4))
        if x5 == INTERIOR_CELLS_A834DEEA:
            continue
        if size(difference(x5, initset(INTERIOR_CENTER_A834DEEA))) == ZERO:
            continue
        return x5
    raise RuntimeError("failed to sample interior mask")


def _reserve_patch_a834deea(
    loc: IntegerTuple,
) -> Indices:
    x0, x1 = loc
    return frozenset(
        (i, j)
        for i in range(subtract(x0, ONE), add(x0, SIX))
        for j in range(subtract(x1, ONE), add(x1, SIX))
    )


def _sample_locations_a834deea(
    side: Integer,
    total: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0 = tuple()
    x1 = frozenset()
    for _ in range(400):
        if len(x0) == total:
            return x0
        x2 = tuple(
            (i, j)
            for i in range(subtract(side, FOUR))
            for j in range(subtract(side, FOUR))
            if size(intersection(_reserve_patch_a834deea((i, j)), x1)) == ZERO
        )
        if len(x2) == ZERO:
            return None
        x3 = choice(x2)
        x0 = x0 + (x3,)
        x1 = combine(x1, _reserve_patch_a834deea(x3))
    return None


def _paint_box_a834deea(
    grid: Grid,
    loc: IntegerTuple,
    interior_zeroes: Indices,
) -> Grid:
    x0 = frozenset({loc, add(loc, (FOUR, FOUR))})
    x1 = backdrop(x0)
    x2 = fill(grid, ZERO, x1)
    x3 = difference(INTERIOR_CELLS_A834DEEA, interior_zeroes)
    x4 = shift(x3, loc)
    x5 = fill(x2, EIGHT, x4)
    return x5


def _paint_labels_a834deea(
    grid: Grid,
    loc: IntegerTuple,
    interior_zeroes: Indices,
) -> Grid:
    x0 = frozenset()
    for x1, x2 in STENCIL_CELLS_A834DEEA:
        if contained(x2, interior_zeroes):
            x3 = add(loc, x2)
            x0 = insert((x1, x3), x0)
    x4 = paint(grid, x0)
    return x4


def generate_a834deea(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (NINE, 18))
        x1 = min(FOUR, add(ONE, divide(subtract(x0, NINE), TWO)))
        x2 = _sample_locations_a834deea(x0, x1)
        if x2 is None:
            continue
        x3 = tuple(_sample_interior_a834deea(diff_lb, diff_ub) for _ in range(x1))
        x4 = canvas(EIGHT, (x0, x0))
        for x5, x6 in zip(x2, x3):
            x4 = _paint_box_a834deea(x4, x5, x6)
        x7 = x4
        for x8, x9 in zip(x2, x3):
            x7 = _paint_labels_a834deea(x7, x8, x9)
        if x4 == x7:
            continue
        if verify_a834deea(x4) != x7:
            continue
        return {"input": x4, "output": x7}
