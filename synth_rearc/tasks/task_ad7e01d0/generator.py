from synth_rearc.core import *

from .verifier import verify_ad7e01d0


ACCENT_COLORS_AD7E01D0 = (ONE, TWO, THREE)


def _expand_ad7e01d0(gi: Grid) -> Grid:
    x0 = shape(gi)
    x1 = multiply(x0, x0)
    x2 = canvas(ZERO, x1)
    x3 = ofcolor(gi, FIVE)
    x4 = asobject(gi)
    x5 = rbind(multiply, x0)
    x6 = apply(x5, x3)
    x7 = lbind(shift, x4)
    x8 = apply(x7, x6)
    x9 = merge(x8)
    x10 = paint(x2, x9)
    return x10


def _random_mask_ad7e01d0(n: Integer) -> frozenset[IntegerTuple]:
    x0 = tuple((i, j) for i in range(n) for j in range(n))
    x1 = max(TWO, n)
    x2 = n * n - ONE
    x3 = randint(x1, x2)
    return frozenset(sample(x0, x3))


def _line_mask_ad7e01d0(n: Integer) -> frozenset[IntegerTuple]:
    x0 = choice(("row", "col"))
    x1 = randint(ZERO, n - ONE)
    x2 = randint(ZERO, n - ONE)
    x3 = product(initset(x1), interval(ZERO, n, ONE))
    x4 = product(interval(ZERO, n, ONE), initset(x2))
    x5 = branch(x0 == "row", x3, x4)
    if randint(ZERO, ONE) == ONE:
        x6 = randint(ZERO, n - ONE)
        x7 = branch(
            x0 == "row",
            product(interval(ZERO, n, ONE), initset(x6)),
            product(initset(x6), interval(ZERO, n, ONE)),
        )
        x5 = combine(x5, x7)
    if size(x5) == n * n:
        x8 = choice(totuple(x5))
        x5 = remove(x8, x5)
    return x5


def _frame_mask_ad7e01d0(n: Integer) -> frozenset[IntegerTuple]:
    x0 = product(initset(ZERO), interval(ZERO, n, ONE))
    x1 = product(initset(n - ONE), interval(ZERO, n, ONE))
    x2 = product(interval(ZERO, n, ONE), initset(ZERO))
    x3 = product(interval(ZERO, n, ONE), initset(n - ONE))
    return combine(combine(x0, x1), combine(x2, x3))


def _cross_mask_ad7e01d0(n: Integer) -> frozenset[IntegerTuple]:
    x0 = n // TWO
    x1 = product(initset(x0), interval(ZERO, n, ONE))
    x2 = product(interval(ZERO, n, ONE), initset(x0))
    return combine(x1, x2)


def _sample_mask_ad7e01d0(n: Integer) -> frozenset[IntegerTuple]:
    x0 = [_random_mask_ad7e01d0, _line_mask_ad7e01d0]
    if n >= FOUR:
        x0.append(_frame_mask_ad7e01d0)
    if not even(n):
        x0.append(_cross_mask_ad7e01d0)
    return choice(tuple(x0))(n)


def _sample_nonmask_values_ad7e01d0(k: Integer) -> tuple[Integer, ...]:
    x0 = sample(ACCENT_COLORS_AD7E01D0, randint(ONE, min(THREE, k)))
    x1 = branch(randint(ZERO, ONE) == ONE, (ZERO,) + tuple(x0), tuple(x0))
    x2 = list(x0[:min(len(x0), k)])
    while len(x2) < k:
        x2.append(choice(x1))
    shuffle(x2)
    return tuple(x2)


def _render_input_ad7e01d0(mask: frozenset[IntegerTuple], n: Integer) -> Grid:
    x0 = tuple((i, j) for i in range(n) for j in range(n))
    x1 = tuple(loc for loc in x0 if loc not in mask)
    x2 = canvas(ZERO, (n, n))
    x3 = fill(x2, FIVE, mask)
    x4 = _sample_nonmask_values_ad7e01d0(len(x1))
    x5 = x3
    for x6, x7 in zip(x1, x4):
        x5 = fill(x5, x7, frozenset({x6}))
    return x5


def generate_ad7e01d0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x1 = _sample_mask_ad7e01d0(x0)
        if size(x1) == ZERO or size(x1) == x0 * x0:
            continue
        x2 = _render_input_ad7e01d0(x1, x0)
        x3 = palette(x2)
        if size(x3) < TWO:
            continue
        if FIVE not in x3:
            continue
        if size(difference(x3, initset(FIVE))) == ZERO:
            continue
        x4 = _expand_ad7e01d0(x2)
        if verify_ad7e01d0(x2) != x4:
            continue
        return {"input": x2, "output": x4}
