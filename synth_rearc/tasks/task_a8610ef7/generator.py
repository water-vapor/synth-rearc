from synth_rearc.core import *

from .verifier import verify_a8610ef7


GRID_DIMS_A8610EF7 = (SIX, SIX)
MIRROR_ROW_PAIRS_A8610EF7 = (
    (ZERO, FIVE),
    (ONE, FOUR),
    (TWO, THREE),
)
SLOTS_A8610EF7 = tuple(
    sorted(product(interval(ZERO, THREE, ONE), interval(ZERO, SIX, ONE)))
)


def _slot_cells_a8610ef7(
    slot: tuple[Integer, Integer],
) -> tuple[IntegerTuple, IntegerTuple]:
    x0, x1 = slot
    x2, x3 = MIRROR_ROW_PAIRS_A8610EF7[x0]
    x4 = astuple(x2, x1)
    x5 = astuple(x3, x1)
    return x4, x5


def generate_a8610ef7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        x1 = unifint(diff_lb, diff_ub, (NINE, 11))
        if x0 + x1 > len(SLOTS_A8610EF7):
            continue
        x2 = tuple(sample(SLOTS_A8610EF7, x0))
        x3 = tuple(x4 for x4 in SLOTS_A8610EF7 if x4 not in x2)
        x4 = tuple(sample(x3, x1))
        x5 = randint(TWO, x1 - TWO)
        x6 = tuple(sample(x4, x5))
        x7 = tuple(x8 for x8 in x4 if x8 not in x6)
        gi = canvas(ZERO, GRID_DIMS_A8610EF7)
        go = canvas(ZERO, GRID_DIMS_A8610EF7)
        for x8 in x2:
            x9, x10 = _slot_cells_a8610ef7(x8)
            x11 = frozenset({x9, x10})
            gi = fill(gi, EIGHT, x11)
            go = fill(go, TWO, x11)
        for x8 in x6:
            x9, _ = _slot_cells_a8610ef7(x8)
            x10 = initset(x9)
            gi = fill(gi, EIGHT, x10)
            go = fill(go, FIVE, x10)
        for x8 in x7:
            _, x9 = _slot_cells_a8610ef7(x8)
            x10 = initset(x9)
            gi = fill(gi, EIGHT, x10)
            go = fill(go, FIVE, x10)
        x8 = tuple(x9.count(EIGHT) for x9 in gi)
        if minimum(x8) < ONE or maximum(x8) > FIVE:
            continue
        x9 = tuple(x10.count(EIGHT) for x10 in zip(*gi))
        if minimum(x9) < ONE or maximum(x9) > FIVE:
            continue
        x10 = size(ofcolor(go, TWO))
        x11 = size(ofcolor(go, FIVE))
        if x10 < EIGHT or x11 < EIGHT:
            continue
        if verify_a8610ef7(gi) != go:
            continue
        return {"input": gi, "output": go}
