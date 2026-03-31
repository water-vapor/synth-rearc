from synth_rearc.core import *

from .helpers import (
    BODY_HOLE_COUNTS_E3721C99,
    GRID_SHAPE_E3721C99,
    LEGEND_COLORS_E3721C99,
    hole_count_e3721c99,
    legend_patch_e3721c99,
    sample_body_patch_e3721c99,
)
from .verifier import verify_e3721c99


LAYOUTS_E3721C99 = ("top", "top", "right", "right", "l")
BODY_HOLE_BAG_E3721C99 = (
    ZERO,
    ZERO,
    ZERO,
    ONE,
    ONE,
    ONE,
    TWO,
    TWO,
    TWO,
    THREE,
    THREE,
    FOUR,
    FIVE,
)


def _sample_legend_counts_e3721c99(
    mode: str,
) -> tuple[Integer, ...]:
    if mode == "top":
        x0 = BODY_HOLE_COUNTS_E3721C99[:FIVE]
        x1 = choice((THREE, FOUR))
    elif mode == "right":
        x0 = BODY_HOLE_COUNTS_E3721C99
        x1 = choice((THREE, FOUR))
    else:
        x0 = BODY_HOLE_COUNTS_E3721C99[:FOUR]
        x1 = choice((TWO, TWO, THREE))
    x2 = tuple(sorted(sample(x0, x1)))
    if maximum(x2) == ZERO:
        return _sample_legend_counts_e3721c99(mode)
    return x2


def _legend_specs_top_e3721c99(
    counts: tuple[Integer, ...],
) -> tuple[tuple[tuple[Integer, Indices], ...], Indices, Indices] | None:
    x0 = tuple(legend_patch_e3721c99(x1, F) for x1 in counts)
    x1 = tuple(width(x2) for x2 in x0)
    x2 = tuple(randint(ONE, TWO) for _ in range(len(x0) - ONE))
    x3 = sum(x1) + sum(x2)
    if x3 > 26:
        return None
    x4 = choice((FIVE, FIVE, SIX, SIX, SEVEN))
    x5 = randint(ONE, 28 - x3)
    x6 = randint(ONE, x4 - FOUR)
    x7 = []
    x8 = x5
    for x9, x10 in zip(counts, x0):
        x11 = shift(x10, (x6, x8))
        x7.append((x9, x11))
        x8 += width(x10)
        if len(x7) < len(x0):
            x8 += x2[len(x7) - ONE]
    x12 = connect((x4, ZERO), (x4, decrement(GRID_SHAPE_E3721C99[ONE])))
    x13 = frozenset(
        (i, j)
        for i in range(x4 + ONE)
        for j in range(GRID_SHAPE_E3721C99[ONE])
    )
    return tuple(x7), x12, x13


def _legend_specs_right_e3721c99(
    counts: tuple[Integer, ...],
) -> tuple[tuple[tuple[Integer, Indices], ...], Indices, Indices] | None:
    x0 = tuple(legend_patch_e3721c99(x1, T) for x1 in counts)
    x1 = tuple(height(x2) for x2 in x0)
    x2 = tuple(randint(ONE, TWO) for _ in range(len(x0) - ONE))
    x3 = sum(x1) + sum(x2)
    if x3 > 26:
        return None
    x4 = choice((22, 23, 24))
    x5 = randint(ONE, 28 - x3)
    x6 = randint(x4 + TWO, GRID_SHAPE_E3721C99[ONE] - FOUR)
    x7 = []
    x8 = x5
    for x9, x10 in zip(counts, x0):
        x11 = shift(x10, (x8, x6))
        x7.append((x9, x11))
        x8 += height(x10)
        if len(x7) < len(x0):
            x8 += x2[len(x7) - ONE]
    x12 = connect((ZERO, x4), (decrement(GRID_SHAPE_E3721C99[ZERO]), x4))
    x13 = frozenset(
        (i, j)
        for i in range(GRID_SHAPE_E3721C99[ZERO])
        for j in range(x4, GRID_SHAPE_E3721C99[ONE])
    )
    return tuple(x7), x12, x13


def _legend_specs_l_e3721c99(
    counts: tuple[Integer, ...],
) -> tuple[tuple[tuple[Integer, Indices], ...], Indices, Indices] | None:
    x0 = tuple(legend_patch_e3721c99(x1, T) for x1 in counts)
    x1 = tuple(height(x2) for x2 in x0)
    x2 = tuple(ONE for _ in range(len(x0) - ONE))
    x3 = sum(x1) + sum(x2)
    x4 = x3 + choice((TWO, THREE))
    if x4 > TEN:
        return None
    x5 = choice((FIVE, SIX, SEVEN, EIGHT))
    x6 = randint(ONE, max(ONE, x4 - x3 - ONE))
    x7 = randint(ONE, max(ONE, x5 - FOUR))
    x8 = []
    x9 = x6
    for x10, x11 in zip(counts, x0):
        x12 = shift(x11, (x9, x7))
        x8.append((x10, x12))
        x9 += height(x11)
        if len(x8) < len(x0):
            x9 += x2[len(x8) - ONE]
    x13 = connect((ZERO, x5), (x4, x5))
    x14 = connect((x4, ZERO), (x4, x5))
    x15 = combine(x13, x14)
    x16 = frozenset(
        (i, j)
        for i in range(x4)
        for j in range(x5)
    )
    x17 = combine(x16, x15)
    return tuple(x8), x15, x17


def _legend_specs_e3721c99(
    mode: str,
    counts: tuple[Integer, ...],
) -> tuple[tuple[tuple[Integer, Indices], ...], Indices, Indices] | None:
    if mode == "top":
        return _legend_specs_top_e3721c99(counts)
    if mode == "right":
        return _legend_specs_right_e3721c99(counts)
    return _legend_specs_l_e3721c99(counts)


def _sample_body_counts_e3721c99(
    counts: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x0 = list(counts)
    x1 = tuple(x2 for x2 in BODY_HOLE_COUNTS_E3721C99 if x2 not in counts)
    if len(x1) > ZERO:
        x0.append(choice(x1))
    x2 = randint(max(FIVE, len(x0) + ONE), SEVEN)
    while len(x0) < x2:
        x3 = choice(BODY_HOLE_BAG_E3721C99)
        if x3 == FIVE and x0.count(FIVE) >= ONE:
            continue
        if x3 == FOUR and x0.count(FOUR) >= TWO:
            continue
        x0.append(x3)
    shuffle(x0)
    return tuple(x0)


def _padded_bbox_e3721c99(
    patch: Patch,
) -> Indices:
    x0 = set(toindices(patch))
    x1 = set(x0)
    for x2 in x0:
        x1 |= neighbors(x2)
    return frozenset(x1)


def _place_patches_e3721c99(
    patches: tuple[Indices, ...],
    blocked: Indices,
) -> tuple[tuple[IntegerTuple, Indices], ...] | None:
    x0 = tuple(
        sorted(
            enumerate(patches),
            key=lambda x1: len(x1[ONE]),
            reverse=T,
        )
    )
    x1 = [None for _ in patches]
    x2 = set(blocked)
    for x3, x4 in x0:
        x5 = []
        x6 = GRID_SHAPE_E3721C99[ZERO] - height(x4)
        x7 = GRID_SHAPE_E3721C99[ONE] - width(x4)
        for x8 in range(x6 + ONE):
            for x9 in range(x7 + ONE):
                x10 = shift(x4, (x8, x9))
                if len(intersection(x10, blocked)) != ZERO:
                    continue
                x11 = _padded_bbox_e3721c99(x10)
                if len(intersection(x11, frozenset(x2))) != ZERO:
                    continue
                x5.append((x8, x9))
        if len(x5) == ZERO:
            return None
        shuffle(x5)
        x8 = choice(tuple(x5[: min(len(x5), 40)]))
        x9 = shift(x4, x8)
        x1[x3] = (x8, x9)
        x2 |= set(_padded_bbox_e3721c99(x9))
    return tuple(x1)


def generate_e3721c99(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(LAYOUTS_E3721C99)
        x1 = _sample_legend_counts_e3721c99(x0)
        x2 = _legend_specs_e3721c99(x0, x1)
        if x2 is None:
            continue
        x3, x4, x5 = x2
        x6 = tuple(sample(LEGEND_COLORS_E3721C99, len(x1)))
        x7 = {x8: x9 for x8, x9 in zip(x1, x6)}
        x8 = _sample_body_counts_e3721c99(x1)
        x9 = tuple(sample_body_patch_e3721c99(x10) for x10 in x8)
        x10 = _place_patches_e3721c99(x9, combine(x5, x4))
        if x10 is None:
            continue
        x11 = canvas(ZERO, GRID_SHAPE_E3721C99)
        x11 = fill(x11, ONE, x4)
        for x12, x13 in x3:
            x11 = fill(x11, x7[x12], x13)
        for (_, x12), x13 in zip(x10, x8):
            if hole_count_e3721c99(x12) != x13:
                break
            x11 = fill(x11, FIVE, x12)
        else:
            x14 = verify_e3721c99(x11)
            if x14 == x11:
                continue
            if verify_e3721c99(x11) != x14:
                continue
            return {"input": x11, "output": x14}
