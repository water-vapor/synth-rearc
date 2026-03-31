from synth_rearc.core import *

from .verifier import verify_db695cfb


BG_COLORS_DB695CFB = (TWO, THREE, FOUR, FIVE, SEVEN, EIGHT, NINE)
DIM_BOUNDS_DB695CFB = (8, 28)
SEGMENT_COUNT_CHOICES_DB695CFB = (ONE, ONE, ONE, TWO, TWO, THREE, FOUR)
SINGLETON_COUNT_CHOICES_DB695CFB = (ZERO, ZERO, ZERO, ONE, ONE, TWO)
NOISE6_COUNT_CHOICES_DB695CFB = (ZERO, ZERO, ONE, ONE, TWO)
TRIGGER_COUNT_CHOICES_DB695CFB = (ZERO, ZERO, ONE, ONE, TWO)


def _diagonal_line_db695cfb(
    loc: IntegerTuple,
    orientation: str,
    dims: IntegerTuple,
) -> Indices:
    x0, x1 = dims
    if orientation == "main":
        x2 = combine(shoot(loc, UNITY), shoot(loc, NEG_UNITY))
    else:
        x2 = combine(shoot(loc, UP_RIGHT), shoot(loc, DOWN_LEFT))
    return frozenset((i, j) for i, j in x2 if 0 <= i < x0 and 0 <= j < x1)


def _diagonal_aligned_db695cfb(
    a: IntegerTuple,
    b: IntegerTuple,
) -> Boolean:
    return abs(subtract(a[0], b[0])) == abs(subtract(a[1], b[1]))


def _seed_halo_db695cfb(
    seeds: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple]:
    x0 = set(seeds)
    for x1 in seeds:
        x0 |= set(neighbors(x1))
    return frozenset(x0)


def _sample_segment_db695cfb(
    h: Integer,
    w: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[IntegerTuple, IntegerTuple, Indices, str]:
    x0 = choice(("main", "anti"))
    x1 = unifint(diff_lb, diff_ub, (FOUR, min(h, w)))
    x2 = decrement(x1)
    if x0 == "main":
        x3 = randint(ZERO, subtract(h, x1))
        x4 = randint(ZERO, subtract(w, x1))
        x5 = astuple(x3, x4)
        x6 = astuple(add(x3, x2), add(x4, x2))
    else:
        x3 = randint(ZERO, subtract(h, x1))
        x4 = randint(x2, decrement(w))
        x5 = astuple(x3, x4)
        x6 = astuple(add(x3, x2), subtract(x4, x2))
    x7 = connect(x5, x6)
    return x5, x6, x7, x0


def _valid_segment_db695cfb(
    endpoints: tuple[IntegerTuple, IntegerTuple],
    line: Indices,
    one_seeds: frozenset[IntegerTuple],
    segment_cells: Indices,
) -> Boolean:
    x0, x1 = endpoints
    x2 = _seed_halo_db695cfb(one_seeds)
    if x0 in x2 or x1 in x2:
        return F
    if line & segment_cells:
        return F
    for x3 in endpoints:
        for x4 in one_seeds:
            if _diagonal_aligned_db695cfb(x3, x4):
                return F
    return T


def _pick_triggers_db695cfb(
    interior: tuple[IntegerTuple, ...],
    orientation: str,
    dims: IntegerTuple,
    all_segment_cells: Indices,
    one_seeds: frozenset[IntegerTuple],
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[IntegerTuple, ...], tuple[Indices, ...]] | None:
    x0 = min(choice(TRIGGER_COUNT_CHOICES_DB695CFB), len(interior))
    x1 = list(interior)
    shuffle(x1)
    x2 = []
    x3 = []
    x4 = "anti" if orientation == "main" else "main"
    x5 = frozenset()
    for x6 in x1:
        if x6 in x5:
            continue
        x7 = _diagonal_line_db695cfb(x6, x4, dims)
        if x7 & difference(all_segment_cells, initset(x6)):
            continue
        if x7 & one_seeds:
            continue
        if any(x7 & x8 for x8 in x3):
            continue
        x2.append(x6)
        x3.append(x7)
        x5 = combine(x5, _seed_halo_db695cfb(initset(x6)))
        if len(x2) == x0:
            break
    if len(x2) != x0:
        return None
    return tuple(x2), tuple(x3)


def _sample_non_diagonal_point_db695cfb(
    dims: IntegerTuple,
    blocked: frozenset[IntegerTuple],
    one_seeds: frozenset[IntegerTuple],
) -> IntegerTuple | None:
    x0, x1 = dims
    x2 = [(i, j) for i in range(x0) for j in range(x1)]
    shuffle(x2)
    for x3 in x2:
        if x3 in blocked:
            continue
        if any(_diagonal_aligned_db695cfb(x3, x4) for x4 in one_seeds):
            continue
        return x3
    return None


def _sample_noise_point_db695cfb(
    dims: IntegerTuple,
    blocked: frozenset[IntegerTuple],
) -> IntegerTuple | None:
    x0, x1 = dims
    x2 = [(i, j) for i in range(x0) for j in range(x1) if (i, j) not in blocked]
    if not x2:
        return None
    return choice(x2)


def generate_db695cfb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(BG_COLORS_DB695CFB)
        x1 = unifint(diff_lb, diff_ub, DIM_BOUNDS_DB695CFB)
        x2 = unifint(diff_lb, diff_ub, DIM_BOUNDS_DB695CFB)
        x3 = choice(SEGMENT_COUNT_CHOICES_DB695CFB)
        x4 = []
        x5 = frozenset()
        x6 = frozenset()
        for _ in range(80):
            if len(x4) == x3:
                break
            x8, x9, x10, x11 = _sample_segment_db695cfb(x1, x2, diff_lb, diff_ub)
            x12 = _valid_segment_db695cfb((x8, x9), x10, x5, x6)
            if not x12:
                continue
            x4.append(
                {
                    "endpoints": (x8, x9),
                    "cells": x10,
                    "orientation": x11,
                }
            )
            x5 = combine(x5, frozenset({x8, x9}))
            x6 = combine(x6, x10)
        if len(x4) != x3:
            continue
        x13 = []
        x14 = []
        x15 = frozenset()
        x16 = T
        for x17 in x4:
            x18 = difference(x17["cells"], frozenset(x17["endpoints"]))
            x19 = tuple(sorted(x18))[ONE:NEG_ONE]
            x20 = _pick_triggers_db695cfb(
                x19,
                x17["orientation"],
                astuple(x1, x2),
                x6,
                x5,
                diff_lb,
                diff_ub,
            )
            if x20 is None:
                x16 = F
                break
            x21, x22 = x20
            x17["triggers"] = x21
            x17["trigger_lines"] = x22
            x13.extend(x21)
            x14.extend(x22)
            for x23 in x22:
                x15 = combine(x15, x23)
        if not x16:
            continue
        x24 = list(x13)
        x25 = set(x24)
        x26 = set()
        x27 = x5
        x28 = combine(x6, x15)
        x29 = choice(SINGLETON_COUNT_CHOICES_DB695CFB)
        for _ in range(x29):
            x30 = _sample_non_diagonal_point_db695cfb(
                astuple(x1, x2),
                combine(x28, _seed_halo_db695cfb(combine(x27, frozenset(x25)))),
                x27,
            )
            if x30 is None:
                break
            x26.add(x30)
            x27 = combine(x27, initset(x30))
        x31 = choice(NOISE6_COUNT_CHOICES_DB695CFB)
        x32 = combine(x28, combine(frozenset(x26), frozenset(x25)))
        x33 = set()
        for _ in range(x31):
            x34 = _sample_noise_point_db695cfb(
                astuple(x1, x2),
                combine(
                    x32,
                    combine(
                        frozenset(x33),
                        _seed_halo_db695cfb(combine(combine(x27, frozenset(x25)), frozenset(x33))),
                    ),
                ),
            )
            if x34 is None:
                break
            x33.add(x34)
        x35 = canvas(x0, astuple(x1, x2))
        x36 = canvas(x0, astuple(x1, x2))
        for x37 in x4:
            for x38 in x37["endpoints"]:
                x35 = fill(x35, ONE, initset(x38))
            x36 = fill(x36, ONE, x37["cells"])
        for x39 in x26:
            x35 = fill(x35, ONE, initset(x39))
            x36 = fill(x36, ONE, initset(x39))
        for x40 in x24:
            x35 = fill(x35, SIX, initset(x40))
            x36 = fill(x36, SIX, initset(x40))
        for x41 in x14:
            x36 = fill(x36, SIX, x41)
        for x42 in x33:
            x35 = fill(x35, SIX, initset(x42))
            x36 = fill(x36, SIX, initset(x42))
        if x35 == x36:
            continue
        if verify_db695cfb(x35) != x36:
            continue
        return {"input": x35, "output": x36}
