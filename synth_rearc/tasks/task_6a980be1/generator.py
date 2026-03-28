from synth_rearc.core import *

from .verifier import verify_6a980be1


FRAME_COLORS_6A980BE1 = remove(TWO, remove(THREE, interval(ONE, TEN, ONE)))


def _stripe_starts_6a980be1(
    length_value: Integer,
    span: Integer,
    gap: Integer,
    offset: Integer,
) -> tuple[int, ...]:
    x0 = []
    x1 = offset
    x2 = add(span, gap)
    while x1 < length_value:
        x0.append(x1)
        x1 = add(x1, x2)
    return tuple(x0)


def _stripe_patch_6a980be1(
    vertical: Boolean,
    starts: tuple[int, ...],
    span: Integer,
    dims: IntegerTuple,
) -> Indices:
    x0 = frozenset()
    x1 = branch(vertical, compose(hfrontier, toivec), compose(vfrontier, tojvec))
    x2 = decrement(branch(vertical, dims[0], dims[1]))
    for x3 in starts:
        x4 = ZERO
        while True:
            if greater(x4, decrement(span)):
                break
            x5 = add(x3, x4)
            if greater(x5, x2):
                break
            x0 = combine(x0, x1(x5))
            x4 = increment(x4)
    return x0


def _separator_patch_6a980be1(
    vertical: Boolean,
    sep_a: Integer,
    sep_b: Integer,
    dims: IntegerTuple,
    full: Boolean,
) -> Indices:
    if vertical:
        x0 = branch(full, interval(ZERO, dims[0], ONE), interval(ONE, decrement(dims[0]), ONE))
        x1 = (sep_a, sep_b)
        return product(x0, x1)
    x0 = (sep_a, sep_b)
    x1 = branch(full, interval(ZERO, dims[1], ONE), interval(ONE, decrement(dims[1]), ONE))
    return product(x0, x1)


def _band_patch_6a980be1(
    vertical: Boolean,
    sep_a: Integer,
    sep_b: Integer,
    dims: IntegerTuple,
    inner_only: Boolean,
) -> Indices:
    if vertical:
        x0 = branch(inner_only, interval(ONE, decrement(dims[0]), ONE), interval(ZERO, dims[0], ONE))
        x1 = interval(increment(sep_a), sep_b, ONE)
        return product(x0, x1)
    x0 = interval(increment(sep_a), sep_b, ONE)
    x1 = branch(inner_only, interval(ONE, decrement(dims[1]), ONE), interval(ZERO, dims[1], ONE))
    return product(x0, x1)


def generate_6a980be1(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((T, F))
        x1 = unifint(diff_lb, diff_ub, (14, 29))
        x2 = unifint(diff_lb, diff_ub, (14, 29))
        x3 = (x1, x2)
        x4 = choice(FRAME_COLORS_6A980BE1)
        x5 = branch(x0, subtract(x2, SIX), subtract(x1, SIX))
        if x5 < ONE:
            continue
        x6 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, x5)))
        x7 = branch(x0, subtract(subtract(x2, x6), FOUR), subtract(subtract(x1, x6), FOUR))
        if x7 < TWO:
            continue
        x8 = unifint(diff_lb, diff_ub, (ONE, subtract(x7, ONE)))
        x9 = add(ONE, x8)
        x10 = add(x9, add(x6, ONE))
        x11 = branch(x0, x1, x2)
        x12 = max(ONE, subtract(x11, FOUR))
        x13 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, x12)))
        x14 = max(ONE, subtract(subtract(x11, x13), TWO))
        x15 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, x14)))
        x16 = unifint(diff_lb, diff_ub, (ONE, x15))
        x17 = _stripe_starts_6a980be1(x11, x13, x15, x16)
        x18 = tuple(x for x in x17 if x >= ONE and x + x13 <= x11 - ONE)
        if len(x18) < TWO:
            continue
        x19 = _stripe_patch_6a980be1(x0, x17, x13, x3)
        x20 = canvas(ZERO, x3)
        x21 = box(asindices(x20))
        x22 = _separator_patch_6a980be1(x0, x9, x10, x3, F)
        x23 = _separator_patch_6a980be1(x0, x9, x10, x3, T)
        x24 = _band_patch_6a980be1(x0, x9, x10, x3, T)
        x25 = _band_patch_6a980be1(x0, x9, x10, x3, F)
        x26 = intersection(x19, x24)
        x27 = intersection(x19, x25)
        gi = fill(x20, x4, x21)
        gi = fill(gi, THREE, x22)
        gi = fill(gi, TWO, x26)
        go = fill(x20, x4, x19)
        go = fill(go, THREE, x23)
        go = fill(go, TWO, x27)
        x28 = objects(gi, T, F, F)
        x29 = colorfilter(x28, TWO)
        if size(x29) < TWO:
            continue
        if gi == go:
            continue
        if verify_6a980be1(gi) != go:
            continue
        return {"input": gi, "output": go}
