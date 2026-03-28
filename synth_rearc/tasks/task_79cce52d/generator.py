from synth_rearc.core import *


INTERIOR_COLORS_79CCE52D = (ONE, THREE, FOUR, FIVE, EIGHT, NINE)
SEED_BLOCKS_79CCE52D = (
    frozenset(product((ZERO, ONE), (ZERO, ONE, TWO))),
    frozenset(product((ZERO, ONE), (THREE, FOUR, FIVE))),
    frozenset(product((TWO, THREE), (ZERO, ONE, TWO))),
    frozenset(product((TWO, THREE), (THREE, FOUR, FIVE))),
    frozenset(product((FOUR, FIVE), (ZERO, ONE, TWO))),
    frozenset(product((FOUR, FIVE), (THREE, FOUR, FIVE))),
)


def _neighbors_79cce52d(cell: IntegerTuple) -> tuple[IntegerTuple, ...]:
    x0, x1 = cell
    x2 = ((x0 - ONE, x1), (x0 + ONE, x1), (x0, x1 - ONE), (x0, x1 + ONE))
    return tuple((a, b) for a, b in x2 if ZERO <= a < SIX and ZERO <= b < SIX)


def _build_targets_79cce52d(diff_lb: float, diff_ub: float) -> list[int]:
    x0 = [FOUR] * SIX
    x1 = branch(greater(unifint(diff_lb, diff_ub, (ZERO, ONE)), ZERO), NINE, EIGHT)
    for _ in range(12):
        x2 = tuple(x3 for x3 in range(SIX) if x0[x3] < x1)
        x3 = choice(x2)
        x0[x3] = add(x0[x3], ONE)
    return x0


def _seed_positions_79cce52d() -> list[IntegerTuple]:
    return [choice(tuple(x0)) for x0 in SEED_BLOCKS_79CCE52D]


def _choose_frontier_79cce52d(
    regions: list[set[IntegerTuple]],
    pending: list[int],
    unassigned: set[IntegerTuple],
) -> tuple[int, IntegerTuple] | None:
    x0 = []
    x1 = minimum(tuple(len(x2) for x2, x3 in zip(regions, pending) if positive(x3)))
    for x2, x3 in enumerate(pending):
        if not positive(x3):
            continue
        if len(regions[x2]) != x1:
            continue
        x4 = tuple(
            x5
            for x6 in regions[x2]
            for x5 in _neighbors_79cce52d(x6)
            if x5 in unassigned
        )
        x5 = dedupe(x4)
        if x5:
            x0.append((x2, x5))
    if len(x0) == ZERO:
        return None
    x2, x3 = choice(x0)
    return (x2, choice(x3))


def _build_interior_79cce52d(diff_lb: float, diff_ub: float) -> Grid:
    while True:
        x0 = _build_targets_79cce52d(diff_lb, diff_ub)
        x1 = _seed_positions_79cce52d()
        if size(frozenset(x1)) != SIX:
            continue
        x2 = [set((x3,)) for x3 in x1]
        x3 = {(a, b) for a in range(SIX) for b in range(SIX)}
        x4 = set(x1)
        x5 = x3.difference(x4)
        x6 = [subtract(x7, ONE) for x7 in x0]
        x7 = False
        while any(positive(x8) for x8 in x6):
            x8 = _choose_frontier_79cce52d(x2, x6, x5)
            if x8 is None:
                x7 = True
                break
            x9, x10 = x8
            x2[x9].add(x10)
            x5.remove(x10)
            x6[x9] = decrement(x6[x9])
        if x7:
            continue
        if len(x5) != ZERO:
            continue
        x8 = canvas(ZERO, (SIX, SIX))
        x9 = sample(INTERIOR_COLORS_79CCE52D, SIX)
        for x10, x11 in zip(x9, x2):
            x8 = fill(x8, x10, frozenset(x11))
        return x8


def _shift_interior_79cce52d(grid: Grid, row_shift: int, col_shift: int) -> Grid:
    x0 = subtract(SIX, row_shift)
    x1 = subtract(SIX, col_shift)
    x2 = crop(grid, (x0, ZERO), (row_shift, SIX))
    x3 = crop(grid, ORIGIN, (x0, SIX))
    x4 = vconcat(x2, x3)
    x5 = crop(x4, (ZERO, x1), (SIX, col_shift))
    x6 = crop(x4, ORIGIN, (SIX, x1))
    return hconcat(x5, x6)


def generate_79cce52d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = _build_interior_79cce52d(diff_lb, diff_ub)
    x1 = unifint(diff_lb, diff_ub, (ONE, SIX))
    x2 = unifint(diff_lb, diff_ub, (ONE, SIX))
    x3 = _shift_interior_79cce52d(x0, subtract(x1, ONE), subtract(x2, ONE))
    x4 = canvas(SIX, (SEVEN, SEVEN))
    x5 = fill(x4, SEVEN, initset(ORIGIN))
    x6 = fill(x5, TWO, frozenset({(x1, ZERO), (ZERO, x2)}))
    x7 = shift(asobject(x0), UNITY)
    x8 = paint(x6, x7)
    return {"input": x8, "output": x3}
