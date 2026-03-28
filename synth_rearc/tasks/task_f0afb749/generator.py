from synth_rearc.core import *


SEED_COLORS_F0AFB749 = (TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _diagonal_cells_f0afb749(
    offset: int,
    size_: int,
) -> Indices:
    return frozenset(
        (i, j)
        for i in range(size_)
        for j in (add(i, offset),)
        if ZERO <= j < size_
    )


def _touching_f0afb749(
    a: IntegerTuple,
    b: IntegerTuple,
) -> Boolean:
    return max(abs(subtract(a[0], b[0])), abs(subtract(a[1], b[1]))) <= ONE


def _trail_cells_f0afb749(
    seeds: Indices,
    size_: int,
) -> Indices:
    x0 = frozenset(subtract(j, i) for i, j in seeds)
    x1 = set()
    for x2 in x0:
        x1 |= _diagonal_cells_f0afb749(x2, size_)
    return frozenset(x1.difference(seeds))


def generate_f0afb749(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, SIX))
        x1 = choice(SEED_COLORS_F0AFB749)
        x2 = min(THREE, divide(add(x0, ONE), TWO))
        x3 = unifint(diff_lb, diff_ub, (ONE, x2))
        x4 = tuple((i, j) for i in range(x0) for j in range(x0))
        x5 = set()
        x6 = set()
        for _ in range(x3):
            x7 = tuple(
                ij
                for ij in x4
                if subtract(ij[1], ij[0]) not in x6
                and all(not _touching_f0afb749(ij, x8) for x8 in x5)
            )
            if len(x7) == ZERO:
                break
            x8 = choice(x7)
            x5.add(x8)
            x6.add(subtract(x8[1], x8[0]))
        if len(x5) != x3:
            continue
        x9 = frozenset(x5)
        x10 = _trail_cells_f0afb749(x9, x0)
        x11 = size(x10)
        if x11 == ZERO:
            continue
        if x11 > add(x0, FOUR):
            continue
        x12 = canvas(ZERO, (x0, x0))
        x13 = fill(x12, x1, x9)
        x14 = upscale(x13, TWO)
        x15 = apply(lbind(multiply, TWO), x10)
        x16 = shift(x15, UNITY)
        x17 = combine(x15, x16)
        x18 = fill(x14, ONE, x17)
        return {"input": x13, "output": x18}
