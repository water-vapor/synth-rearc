from collections import defaultdict

from synth_rearc.core import *

from .helpers import (
    canonical_patch_898e7135,
    oriented_variants_898e7135,
    scaled_local_patch_898e7135,
)
from .verifier import verify_898e7135


SCALE_CHOICES_898E7135 = (TWO, TWO, THREE)
HOLE_COUNT_RANGE_898E7135 = (THREE, SIX)
NOISE_COUNT_RANGE_898E7135 = (SIX, 14)


def _orth_halo_898e7135(
    patch: Patch,
) -> frozenset[IntegerTuple]:
    x0 = set(toindices(patch))
    for x1 in tuple(x0):
        x0 |= set(dneighbors(x1))
    return frozenset(x0)


def _random_patch_898e7135(
    max_h: Integer,
    max_w: Integer,
    target_size: Integer,
) -> frozenset[IntegerTuple] | None:
    for _ in range(80):
        x0 = {(randint(ZERO, subtract(max_h, ONE)), randint(ZERO, subtract(max_w, ONE)))}
        while len(x0) < target_size:
            x1 = []
            for x2 in x0:
                for x3 in dneighbors(x2):
                    if x3 in x0:
                        continue
                    x4, x5 = x3
                    if x4 < ZERO or x5 < ZERO or x4 >= max_h or x5 >= max_w:
                        continue
                    x1.append(x3)
            if len(x1) == ZERO:
                break
            x0.add(choice(x1))
        if len(x0) != target_size:
            continue
        x6 = frozenset(normalize(frozenset(x0)))
        if height(x6) <= max_h and width(x6) <= max_w:
            return x6
    return None


def _full_rectangle_898e7135(
    h: Integer,
    w: Integer,
) -> frozenset[IntegerTuple]:
    return frozenset((i, j) for i in range(h) for j in range(w))


def _base_dims_898e7135(
    scale: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Integer]:
    if scale == TWO:
        return (
            unifint(diff_lb, diff_ub, (SIX, 14)),
            unifint(diff_lb, diff_ub, (SIX, 12)),
        )
    return (
        unifint(diff_lb, diff_ub, (SIX, TEN)),
        unifint(diff_lb, diff_ub, (SIX, TEN)),
    )


def _hole_components_898e7135(
    base_h: Integer,
    base_w: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[frozenset[IntegerTuple], ...] | None:
    x0 = unifint(diff_lb, diff_ub, HOLE_COUNT_RANGE_898E7135)
    x1 = []
    x2 = set()
    x3 = ZERO
    for x4 in range(x0):
        x5 = None
        for _ in range(160):
            x6 = min(FOUR, subtract(base_h, TWO))
            x7 = min(FOUR, subtract(base_w, TWO))
            if x6 < ONE or x7 < ONE:
                return None
            x8 = randint(ONE, x6)
            x9 = randint(ONE, x7)
            x10 = min(multiply(x8, x9), choice((ONE, TWO, TWO, THREE, FOUR, FIVE, SIX)))
            if x4 == ZERO:
                x10 = max(TWO, x10)
            x11 = _random_patch_898e7135(x8, x9, x10)
            if x11 is None:
                continue
            x12 = height(x11)
            x13 = width(x11)
            if x12 >= subtract(base_h, ONE) or x13 >= subtract(base_w, ONE):
                continue
            x14 = randint(ONE, subtract(subtract(base_h, ONE), x12))
            x15 = randint(ONE, subtract(subtract(base_w, ONE), x13))
            x16 = shift(x11, (x14, x15))
            if any(x17 in x2 for x17 in _orth_halo_898e7135(x16)):
                continue
            x5 = x16
            break
        if x5 is None:
            return None
        x1.append(x5)
        x2 |= set(_orth_halo_898e7135(x5))
        x3 += size(x5)
    if all(size(x18) == ONE for x18 in x1):
        return None
    if x3 > divide(multiply(base_h, base_w), THREE):
        return None
    return tuple(sorted(x1, key=lambda x19: (uppermost(x19), leftmost(x19), size(x19))))


def _major_offset_choices_898e7135(
    grid_h: Integer,
    grid_w: Integer,
    base_h: Integer,
    base_w: Integer,
) -> tuple[IntegerTuple, ...]:
    x0 = subtract(grid_h, base_h)
    x1 = subtract(grid_w, base_w)
    x2 = (
        (ZERO, ZERO),
        (ZERO, x1),
        (x0, ZERO),
        (x0, x1),
        (halve(x0), ZERO),
        (halve(x0), x1),
        (ZERO, halve(x1)),
        (x0, halve(x1)),
    )
    return dedupe(tuple(x3 for x3 in x2 if x3[ZERO] >= ZERO and x3[ONE] >= ZERO))


def _place_patch_898e7135(
    patch: frozenset[IntegerTuple],
    grid_h: Integer,
    grid_w: Integer,
    blocked: frozenset[IntegerTuple],
) -> frozenset[IntegerTuple] | None:
    x0 = height(patch)
    x1 = width(patch)
    for _ in range(240):
        x2 = randint(ZERO, subtract(grid_h, x0))
        x3 = randint(ZERO, subtract(grid_w, x1))
        x4 = shift(patch, (x2, x3))
        if any(x5 in blocked for x5 in _orth_halo_898e7135(x4)):
            continue
        return x4
    return None


def generate_898e7135(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(SCALE_CHOICES_898E7135)
        x1, x2 = _base_dims_898e7135(x0, diff_lb, diff_ub)
        x3 = _hole_components_898e7135(x1, x2, diff_lb, diff_ub)
        if x3 is None:
            continue
        x4 = _full_rectangle_898e7135(x1, x2)
        x5 = merge(x3)
        x6 = difference(x4, x5)
        x7 = tuple(
            canonical_patch_898e7135(upscale(recolor(ONE, normalize(x8)), x0))
            for x8 in x3
        )
        x8 = tuple(dedupe(x7))
        if len(x8) > SEVEN:
            continue
        x9 = interval(ONE, TEN, ONE)
        x10 = sample(x9, add(len(x8), TWO))
        x11 = x10[ZERO]
        x12 = x10[ONE]
        x13 = {x14: x15 for x14, x15 in zip(x8, x10[TWO:])}
        x14 = tuple(
            {
                "hole": x15,
                "key": x16,
                "color": x13[x16],
                "shape": choice(oriented_variants_898e7135(upscale(recolor(ONE, normalize(x15)), x0))),
            }
            for x15, x16 in zip(x3, x7)
        )
        x15 = max(height(x16["shape"]) for x16 in x14)
        x16 = max(width(x17["shape"]) for x17 in x14)
        x18 = max(add(x1, add(x15, FOUR)), 16)
        x19 = max(add(x2, add(x16, FOUR)), 16)
        x20 = min(30, add(x18, unifint(diff_lb, diff_ub, (ZERO, SIX))))
        x21 = min(30, add(x19, unifint(diff_lb, diff_ub, (ZERO, SIX))))
        x22 = max(x18, x20)
        x23 = max(x19, x21)
        if x22 > 30 or x23 > 30:
            continue
        x24 = canvas(ZERO, (x22, x23))
        x25 = recolor(x11, x6)
        x26 = choice(_major_offset_choices_898e7135(x22, x23, x1, x2))
        x27 = shift(x25, x26)
        x28 = shift(x4, x26)
        x29 = combine(x28, outbox(x28))
        x30 = x24
        x30 = paint(x30, x27)
        x31 = frozenset(x29)
        x32 = []
        x33 = tuple(sorted(x14, key=lambda x34: (-height(x34["shape"]), -width(x34["shape"]), -size(x34["shape"]))))
        x34 = T
        for x35 in x33:
            x36 = _place_patch_898e7135(x35["shape"], x22, x23, x31)
            if x36 is None:
                x34 = F
                break
            x32.append({**x35, "placed": x36})
            x31 = x31 | _orth_halo_898e7135(x36)
            x30 = paint(x30, recolor(x35["color"], x36))
        if not x34:
            continue
        x37 = tuple(
            (i, j)
            for i in range(x22)
            for j in range(x23)
            if x30[i][j] == ZERO
        )
        x38 = unifint(diff_lb, diff_ub, NOISE_COUNT_RANGE_898E7135)
        if len(x37) <= x38:
            continue
        x39 = frozenset(sample(x37, x38))
        x30 = fill(x30, x12, x39)
        if mostcolor(x30) != ZERO:
            continue
        x40 = tuple(objects(x30, T, F, T))
        x41 = max(x40, key=lambda x42: (size(backdrop(x42)), size(x42), -uppermost(x42), -leftmost(x42)))
        if x41 != x27:
            continue
        if any(size(x43) >= size(x27) for x43 in x40 if x43 != x27):
            continue
        if any(size(backdrop(x44)) >= size(backdrop(x27)) for x44 in x40 if x44 != x27):
            continue
        x45 = canvas(x11, multiply((x1, x2), x0))
        for x46 in x3:
            x47 = x13[canonical_patch_898e7135(upscale(recolor(ONE, normalize(x46)), x0))]
            x48 = recolor(x47, scaled_local_patch_898e7135(x46, x0))
            x45 = paint(x45, x48)
        if verify_898e7135(x30) != x45:
            continue
        if x30 == x45:
            continue
        return {"input": x30, "output": x45}
