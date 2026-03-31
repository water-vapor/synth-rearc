from synth_rearc.core import *

from .helpers import (
    PALETTE_AF22C60D,
    build_seed_af22c60d,
    carve_input_af22c60d,
    extend_seed_af22c60d,
    make_block_af22c60d,
)


def _palette_triplet_af22c60d(
    colors: tuple[Integer, ...],
) -> tuple[tuple[Integer, Integer, Integer], tuple[Integer, Integer, Integer], tuple[Integer, Integer, Integer]]:
    while True:
        x0 = tuple(sample(colors, THREE))
        x1 = tuple(sample(colors, THREE))
        x2 = tuple(sample(colors, THREE))
        if frozenset(x0) == frozenset(x1):
            continue
        if frozenset(x0) == frozenset(x2):
            continue
        x3 = frozenset(x0) | frozenset(x1) | frozenset(x2)
        if len(x3) != len(colors):
            continue
        return x0, x1, x2


def generate_af22c60d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((FIVE, SIX))
        x1 = tuple(sample(PALETTE_AF22C60D, x0))
        x2, x3, x4 = _palette_triplet_af22c60d(x1)
        x5 = make_block_af22c60d(x2)
        x6 = make_block_af22c60d(x3)
        x7 = make_block_af22c60d(x4)
        if x5 == x6 or x6 == x7 or x5 == x7:
            continue
        x8 = build_seed_af22c60d(x5, x6, x7)
        x9 = extend_seed_af22c60d(x8)
        x10 = carve_input_af22c60d(x9, diff_lb, diff_ub)
        if x10 == x9:
            continue
        return {"input": x10, "output": x9}
