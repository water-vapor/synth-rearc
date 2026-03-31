from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    connected_components_67e490f4,
    free_shape_key_67e490f4,
    free_shape_variants_67e490f4,
    orthopad_67e490f4,
    rectangle_patch_67e490f4,
)


INPUT_SIDE_67E490F4 = 30
PALETTE_67E490F4 = interval(ONE, TEN, ONE)
SHAPE_LIBRARY_67E490F4 = (
    frozenset({(ZERO, ZERO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO), (TWO, ONE), (TWO, TWO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ZERO, THREE), (ZERO, FOUR)}),
)


def _template_spec_67e490f4(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Integer, Integer, Integer]:
    x0 = choice(("block", "block", "block", "banner"))
    if x0 == "banner":
        x1 = unifint(diff_lb, diff_ub, (SEVEN, TEN))
        x2 = unifint(diff_lb, diff_ub, (22, INPUT_SIDE_67E490F4))
        x3 = choice((ZERO, subtract(INPUT_SIDE_67E490F4, x1)))
        x4 = randint(ZERO, subtract(INPUT_SIDE_67E490F4, x2))
        return x3, x4, x1, x2
    x1 = unifint(diff_lb, diff_ub, (NINE, 15))
    x2 = unifint(diff_lb, diff_ub, (NINE, 15))
    x3 = randint(ZERO, subtract(INPUT_SIDE_67E490F4, x1))
    x4 = randint(ZERO, subtract(INPUT_SIDE_67E490F4, x2))
    return x3, x4, x1, x2


def _occurrence_count_67e490f4(
    shape_key: FreeShapeKey67e490f4,
) -> Integer:
    x0 = len(shape_key)
    if x0 <= TWO:
        return choice((TWO, THREE, THREE, FOUR))
    if x0 <= FOUR:
        return choice((TWO, TWO, THREE, THREE, FOUR))
    return choice((ONE, TWO, TWO, THREE))


def _place_patch_67e490f4(
    variants: tuple[Indices, ...],
    forbidden: Indices,
    row_bounds: tuple[Integer, Integer],
    col_bounds: tuple[Integer, Integer],
) -> Indices | None:
    x0, x1 = row_bounds
    x2, x3 = col_bounds
    for _ in range(200):
        x4 = choice(variants)
        x5, x6 = shape(x4)
        if add(x0, x5) > x1 or add(x2, x6) > x3:
            continue
        x7 = randint(x0, subtract(x1, x5))
        x8 = randint(x2, subtract(x3, x6))
        x9 = shift(x4, (x7, x8))
        if len(toindices(x9) & forbidden) > ZERO:
            continue
        return x9
    return None


def generate_67e490f4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = tuple(sample(PALETTE_67E490F4, TWO))
        x1, x2 = x0
        x3, x4, x5, x6 = _template_spec_67e490f4(diff_lb, diff_ub)
        x7 = tuple(
            x8
            for x8 in SHAPE_LIBRARY_67E490F4
            if any(
                both(
                    height(x9) <= subtract(x5, TWO),
                    width(x9) <= subtract(x6, TWO),
                )
                for x9 in free_shape_variants_67e490f4(x8)
            )
        )
        x10 = min(len(x7), unifint(diff_lb, diff_ub, (THREE, FIVE)))
        if x10 < THREE:
            continue
        x11 = tuple(sample(x7, x10))
        x12 = {}
        x13 = set()
        x14 = True
        for x15 in x11:
            x16 = free_shape_key_67e490f4(x15)
            x17 = free_shape_variants_67e490f4(x15)
            x18 = _occurrence_count_67e490f4(x16)
            x19 = []
            for _ in range(x18):
                x20 = _place_patch_67e490f4(
                    x17,
                    frozenset(x13),
                    (ONE, subtract(x5, ONE)),
                    (ONE, subtract(x6, ONE)),
                )
                if x20 is None:
                    x14 = False
                    break
                x19.append(x20)
                x13 |= orthopad_67e490f4(x20)
            if flip(x14):
                break
            x12[x16] = tuple(x19)
        if flip(x14):
            continue
        x21 = merge(merge(tuple(x12.values())))
        x22 = connected_components_67e490f4(x21)
        x23 = sum(len(x24) for x24 in x12.values())
        if len(x22) != x23:
            continue
        x24 = difference(rectangle_patch_67e490f4(ZERO, ZERO, x5, x6), x21)
        x25 = connected_components_67e490f4(x24)
        if len(x25) != ONE:
            continue
        x26 = tuple(
            x27
            for x27 in PALETTE_67E490F4
            if x27 not in (x1, x2)
        )
        if len(x26) < x10:
            continue
        x27 = tuple(sample(x26, x10))
        x28 = {}
        for x29, x30 in zip(x12, x27):
            x31 = choice((ZERO, ONE, ONE, TWO))
            x32 = tuple(
                x33
                for x33 in x26
                if x33 != x30
            )
            x33 = tuple(sample(x32, x31)) if x31 > ZERO else ()
            x28[x29] = (
                x30,
                tuple((x34, ONE) for x34 in x33),
            )
        x34 = rectangle_patch_67e490f4(x3, x4, x5, x6)
        x35 = orthopad_67e490f4(x34)
        x36 = {}
        x37 = True
        for x38 in x11:
            x39 = free_shape_key_67e490f4(x38)
            x40 = free_shape_variants_67e490f4(x38)
            x41 = x28[x39][ZERO]
            x42 = choice((TWO, TWO, THREE, THREE, FOUR))
            x43 = [(x41, x42)]
            x44 = x28[x39][ONE]
            for x45, x46 in x44:
                x43.append((x45, x46))
            x47 = []
            for x48, x49 in x43:
                for _ in range(x49):
                    x50 = _place_patch_67e490f4(
                        x40,
                        frozenset(x35),
                        (ZERO, INPUT_SIDE_67E490F4),
                        (ZERO, INPUT_SIDE_67E490F4),
                    )
                    if x50 is None:
                        x37 = False
                        break
                    x47.append((x48, x50))
                    x35 |= orthopad_67e490f4(x50)
                if flip(x37):
                    break
            if flip(x37):
                break
            x36[x39] = tuple(x47)
        if flip(x37):
            continue
        x51 = canvas(x1, (INPUT_SIDE_67E490F4, INPUT_SIDE_67E490F4))
        x52 = fill(x51, x2, x34)
        x53 = canvas(x2, (x5, x6))
        for x54, x55 in x12.items():
            x56 = x28[x54][ZERO]
            for x57 in x55:
                x58 = shift(x57, (x3, x4))
                x52 = fill(x52, x1, x58)
                x53 = fill(x53, x56, x57)
        for x59 in x36.values():
            for x60, x61 in x59:
                x52 = fill(x52, x60, x61)
        return {"input": x52, "output": x53}
