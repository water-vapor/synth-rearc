from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    block_patch_7b0280bc,
    center_hint_7b0280bc,
    chebyshev_7b0280bc,
    eight_halo_7b0280bc,
    monotone_path_7b0280bc,
    patch_in_bounds_7b0280bc,
    port_candidates_7b0280bc,
)
from .verifier import verify_7b0280bc


CHAIN_OFFSETS_7B0280BC = tuple(
    (di, dj)
    for di in range(-12, 13)
    for dj in range(-12, 13)
    if 4 <= max(abs(di), abs(dj)) <= 12 and (abs(di) >= 2 or abs(dj) >= 2)
)


def _place_chain_blocks_7b0280bc(
    side: Integer,
    square_size: Integer,
    n_bridge_blocks: Integer,
) -> tuple[Indices, ...] | None:
    x0 = []
    x1 = set()
    for x2 in range(n_bridge_blocks + TWO):
        x3 = None
        for _ in range(400):
            if equality(x2, ZERO):
                x4 = randint(ZERO, side - square_size)
                x5 = randint(ZERO, side - square_size)
            else:
                x6 = ulcorner(x0[-ONE])
                x7, x8 = choice(CHAIN_OFFSETS_7B0280BC)
                x4 = x6[ZERO] + x7
                x5 = x6[ONE] + x8
            x9 = block_patch_7b0280bc((x4, x5), square_size)
            if not patch_in_bounds_7b0280bc(x9, side):
                continue
            if positive(size(intersection(eight_halo_7b0280bc(x9), x1))):
                continue
            if positive(x2):
                x10 = ulcorner(x0[-ONE])
                x11 = chebyshev_7b0280bc((x4, x5), x10)
                if x11 < 4 or x11 > 12:
                    continue
            if x2 > ONE:
                x12 = ulcorner(x0[-TWO])
                if chebyshev_7b0280bc((x4, x5), x12) < 5:
                    continue
            x3 = x9
            break
        if x3 is None:
            return None
        x0.append(x3)
        x1 |= set(eight_halo_7b0280bc(x3))
    return tuple(x0)


def _route_chain_7b0280bc(
    blocks: tuple[Indices, ...],
    side: Integer,
) -> tuple[Indices, ...] | None:
    x0 = set().union(*(eight_halo_7b0280bc(x1) for x1 in blocks))
    x1 = set()
    x2 = []
    for x3, x4 in zip(blocks, blocks[ONE:]):
        x5 = set(eight_halo_7b0280bc(x3))
        x6 = set(eight_halo_7b0280bc(x4))
        x7 = x1 | (x0 - x5)
        x8 = x1 | (x0 - x6)
        x9 = x1 | ((x0 - x5) - x6)
        x10 = port_candidates_7b0280bc(x3, center_hint_7b0280bc(x4), side, frozenset(x7))
        x11 = port_candidates_7b0280bc(x4, center_hint_7b0280bc(x3), side, frozenset(x8))
        if len(x10) == ZERO or len(x11) == ZERO:
            return None
        x12 = None
        x13 = x10[: min(len(x10), SIX)]
        x14 = x11[: min(len(x11), SIX)]
        for _ in range(240):
            x15 = choice(x13)
            x16 = choice(x14)
            x17 = monotone_path_7b0280bc(x15, x16)
            if any(x18 in x9 for x18 in x17[ONE:-ONE]):
                continue
            if any(x18 in merge(blocks) for x18 in x17):
                continue
            x12 = frozenset(x17)
            break
        if x12 is None:
            return None
        x2.append(x12)
        x1 |= set(eight_halo_7b0280bc(x12))
    return tuple(x2)


def _free_block_7b0280bc(
    side: Integer,
    square_size: Integer,
    blocked: Indices,
) -> Indices | None:
    for _ in range(300):
        x0 = randint(ZERO, side - square_size)
        x1 = randint(ZERO, side - square_size)
        x2 = block_patch_7b0280bc((x0, x1), square_size)
        if positive(size(intersection(eight_halo_7b0280bc(x2), blocked))):
            continue
        return x2
    return None


def _stub_target_7b0280bc(
    port: IntegerTuple,
    block: Patch,
    side: Integer,
) -> IntegerTuple:
    x0 = center_hint_7b0280bc(block)
    x1 = ZERO if add(port[ZERO], port[ZERO]) == x0[ZERO] else ONE if add(port[ZERO], port[ZERO]) > x0[ZERO] else NEG_ONE
    x2 = ZERO if add(port[ONE], port[ONE]) == x0[ONE] else ONE if add(port[ONE], port[ONE]) > x0[ONE] else NEG_ONE
    if equality(x1, ZERO) and equality(x2, ZERO):
        x1, x2 = choice(((ONE, ZERO), (NEG_ONE, ZERO), (ZERO, ONE), (ZERO, NEG_ONE)))
    x3 = randint(TWO, EIGHT)
    x4 = randint(ZERO, THREE)
    x5 = (-x2, x1)
    x6 = port[ZERO] + x1 * x3 + x5[ZERO] * x4
    x7 = port[ONE] + x2 * x3 + x5[ONE] * x4
    x6 = max(ZERO, min(side - ONE, x6))
    x7 = max(ZERO, min(side - ONE, x7))
    return (x6, x7)


def _stub_from_block_7b0280bc(
    block: Patch,
    side: Integer,
    block_halo: Indices,
    path_halo: Indices,
) -> Indices | None:
    x0 = set(eight_halo_7b0280bc(block))
    x1 = set(path_halo) | (set(block_halo) - x0)
    x2 = port_candidates_7b0280bc(block, center_hint_7b0280bc(block), side, frozenset(x1))
    if len(x2) == ZERO:
        return None
    for _ in range(120):
        x3 = choice(x2)
        x4 = _stub_target_7b0280bc(x3, block, side)
        x5 = monotone_path_7b0280bc(x3, x4)
        if len(x5) < TWO:
            continue
        if any(x6 in x1 for x6 in x5[ONE:]):
            continue
        if any(x6 in merge((block,)) for x6 in x5):
            continue
        return frozenset(x5)
    return None


def _free_path_7b0280bc(
    side: Integer,
    blocked: Indices,
) -> Indices | None:
    x0 = tuple(
        (i, j)
        for i in range(side)
        for j in range(side)
        if (i, j) not in blocked
    )
    if len(x0) == ZERO:
        return None
    for _ in range(120):
        x1 = choice(x0)
        x2 = choice(((ONE, ZERO), (NEG_ONE, ZERO), (ZERO, ONE), (ZERO, NEG_ONE), (ONE, ONE), (ONE, NEG_ONE), (NEG_ONE, ONE), (NEG_ONE, NEG_ONE)))
        x3 = randint(TWO, EIGHT)
        x4 = randint(ZERO, THREE)
        x5 = (-x2[ONE], x2[ZERO])
        x6 = x1[ZERO] + x2[ZERO] * x3 + x5[ZERO] * x4
        x7 = x1[ONE] + x2[ONE] * x3 + x5[ONE] * x4
        x6 = max(ZERO, min(side - ONE, x6))
        x7 = max(ZERO, min(side - ONE, x7))
        if equality((x6, x7), x1):
            continue
        x8 = monotone_path_7b0280bc(x1, (x6, x7))
        if len(x8) < TWO:
            continue
        if any(x9 in blocked for x9 in x8):
            continue
        return frozenset(x8)
    return None


def generate_7b0280bc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = randint(15, 30)
        x1 = [x2 for x2 in range(TEN) if x2 not in (THREE, FIVE)]
        shuffle(x1)
        x2 = x1.pop()
        x3 = x1.pop()
        x4 = x1.pop()
        x5 = x1.pop()
        x6 = choice((TWO, TWO, TWO, THREE))
        x7 = choice((ONE, TWO, TWO, THREE))
        x8 = _place_chain_blocks_7b0280bc(x0, x6, x7)
        if x8 is None:
            continue
        x9 = _route_chain_7b0280bc(x8, x0)
        if x9 is None:
            continue
        x10 = set().union(*(eight_halo_7b0280bc(x11) for x11 in x8))
        x11 = set().union(*(eight_halo_7b0280bc(x12) for x12 in x9))
        x12 = []
        x13 = randint(max(ONE, x7), x7 + 5)
        x14 = False
        for _ in range(x13):
            x15 = _free_block_7b0280bc(x0, x6, frozenset(x10 | x11))
            if x15 is None:
                break
            x12.append(x15)
            x10 |= set(eight_halo_7b0280bc(x15))
            if choice((T, T, F)):
                x16 = _stub_from_block_7b0280bc(x15, x0, frozenset(x10), frozenset(x11))
                if x16 is not None:
                    x11 |= set(eight_halo_7b0280bc(x16))
                    x12.append(x16)
                    x14 = T
        x17 = randint(ZERO, FOUR)
        x18 = []
        for _ in range(x17):
            x19 = _free_path_7b0280bc(x0, frozenset(x10 | x11))
            if x19 is None:
                break
            x18.append(x19)
            x11 |= set(eight_halo_7b0280bc(x19))
        x19 = canvas(x2, (x0, x0))
        x20 = x8[ZERO]
        x21 = x8[-ONE]
        x22 = x8[ONE:-ONE]
        x23 = merge(x9)
        x24 = merge(x12) if len(x12) > ZERO else frozenset()
        x25 = merge(x18) if len(x18) > ZERO else frozenset()
        x26 = merge((x20, x21))
        x27 = merge(x22) if len(x22) > ZERO else frozenset()
        x28 = fill(x19, x3, x26)
        x29 = fill(x28, x4, x27)
        x30 = fill(x29, x5, x23)
        x31 = fill(x30, x4, frozenset(x32 for x32 in x24 if x32 not in x25))
        x32 = fill(x31, x5, x25)
        x33 = fill(x32, THREE, x27)
        x34 = fill(x33, FIVE, x23)
        x35 = colorcount(x30, x4)
        if x35 <= x6 * x6:
            continue
        if not x14 and len(x18) == ZERO:
            continue
        if verify_7b0280bc(x32) != x34:
            continue
        return {
            "input": x32,
            "output": x34,
        }
