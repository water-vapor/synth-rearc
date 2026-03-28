from synth_rearc.core import *


NON_BG_COLORS_58C02A16 = remove(SEVEN, interval(ZERO, TEN, ONE))
SEED_SHAPES_58C02A16 = (
    (TWO, TWO),
    (THREE, TWO),
    (TWO, THREE),
    (THREE, THREE),
    (THREE, THREE),
)


def _render_output_58c02a16(
    seed: Grid,
    primary_color: Integer,
    secondary_color: Integer,
    dims: IntegerTuple,
) -> Grid:
    x0 = ofcolor(seed, primary_color)
    x1 = ofcolor(seed, SEVEN)
    x2 = shape(seed)
    x3 = rbind(multiply, x2)
    x4 = apply(x3, x0)
    x5 = apply(x3, x1)
    x6 = lbind(shift, x0)
    x7 = mapply(x6, x4)
    x8 = mapply(x6, x5)
    x9 = height(seed)
    x10 = width(seed)
    x11 = multiply(x9, x9)
    x12 = multiply(x10, x10)
    x13, x14 = dims
    x15 = divide(add(x13, decrement(x11)), x11)
    x16 = divide(add(x14, decrement(x12)), x12)
    x17 = interval(ZERO, x15, ONE)
    x18 = interval(ZERO, x16, ONE)
    x19 = apply(rbind(multiply, x11), x17)
    x20 = apply(rbind(multiply, x12), x18)
    x21 = product(x19, x20)
    x22 = lbind(shift, x7)
    x23 = lbind(shift, x8)
    x24 = mapply(x22, x21)
    x25 = mapply(x23, x21)
    x26 = canvas(SEVEN, dims)
    x27 = fill(x26, secondary_color, x25)
    x28 = fill(x27, primary_color, x24)
    return x28


def _sample_seed_58c02a16(
    diff_lb: float,
    diff_ub: float,
    seed_shape: IntegerTuple,
    primary_color: Integer,
) -> Grid:
    x0, x1 = seed_shape
    x2 = tuple(product(interval(ZERO, x0, ONE), interval(ZERO, x1, ONE)))
    x3 = remove(ORIGIN, x2)
    x4 = multiply(x0, x1)
    x5 = decrement(decrement(x4))
    while True:
        x6 = unifint(diff_lb, diff_ub, (TWO, x5))
        x7 = frozenset({ORIGIN}) | frozenset(sample(x3, decrement(x6)))
        x8 = frozenset(x9 for x9, _ in x7)
        x9 = frozenset(x10 for _, x10 in x7)
        x10 = greater(size(x8), ONE)
        x11 = greater(size(x9), ONE)
        if both(x10, x11):
            x12 = canvas(SEVEN, seed_shape)
            x13 = fill(x12, primary_color, x7)
            return x13


def _sample_output_dim_58c02a16(
    diff_lb: float,
    diff_ub: float,
    base_dim: Integer,
) -> Integer:
    x0 = unifint(diff_lb, diff_ub, (ZERO, decrement(base_dim)))
    x1 = add(base_dim, x0)
    return x1


def generate_58c02a16(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice(SEED_SHAPES_58C02A16)
    x1, x2 = sample(NON_BG_COLORS_58C02A16, TWO)
    x3 = _sample_seed_58c02a16(diff_lb, diff_ub, x0, x1)
    x4 = height(x3)
    x5 = width(x3)
    x6 = increment(x4)
    x7 = increment(x5)
    x8 = multiply(x4, x4)
    x9 = multiply(x5, x5)
    x10 = _sample_output_dim_58c02a16(diff_lb, diff_ub, x8)
    x11 = _sample_output_dim_58c02a16(diff_lb, diff_ub, x9)
    x12 = canvas(SEVEN, (x10, x11))
    x13 = ofcolor(x3, x1)
    x14 = fill(x12, x1, x13)
    x15 = product(initset(decrement(x6)), interval(ZERO, x7, ONE))
    x16 = product(interval(ZERO, x6, ONE), initset(decrement(x7)))
    x17 = combine(x15, x16)
    x18 = fill(x14, x2, x17)
    x19 = _render_output_58c02a16(x3, x1, x2, (x10, x11))
    return {
        "input": x18,
        "output": x19,
    }
