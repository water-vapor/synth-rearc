from synth_rearc.core import *


COLORS_AC6F9922 = remove(ZERO, interval(ZERO, TEN, ONE))


def _sample_axis_ac6f9922(
    count: Integer,
    size_range: tuple[Integer, Integer],
) -> tuple[tuple[Integer, ...], tuple[Integer, ...]]:
    x0, x1 = size_range
    x2 = tuple(randint(x0, x1) for _ in range(count))
    x3 = tuple(choice((ONE, ONE, TWO)) for _ in range(count + ONE))
    return x2, x3


def _axis_starts_ac6f9922(
    border_value: Integer,
    gaps: tuple[Integer, ...],
    sizes: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    x0 = border_value + gaps[ZERO]
    x1 = []
    for x2, x3 in enumerate(sizes):
        x1.append(x0)
        x0 += x3 + gaps[x2 + ONE]
    return tuple(x1)


def _frame_indices_ac6f9922(
    dims: tuple[Integer, Integer],
    top_value: Integer,
    bottom_value: Integer,
    left_value: Integer,
    right_value: Integer,
) -> Indices:
    x0, x1 = dims
    return frozenset(
        (i, j)
        for i in range(x0)
        for j in range(x1)
        if i < top_value or i >= x0 - bottom_value or j < left_value or j >= x1 - right_value
    )


def _sample_output_ac6f9922(
    diff_lb: float,
    diff_ub: float,
    n_rows: Integer,
    n_cols: Integer,
    wall_value: Integer,
    bg_value: Integer,
) -> Grid:
    x0 = tuple(value for value in COLORS_AC6F9922 if value not in (wall_value, bg_value))
    x1 = multiply(n_rows, n_cols)
    x2 = unifint(diff_lb, diff_ub, (ONE, decrement(x1)))
    x3 = set(sample(tuple(range(x1)), x2))
    x4 = canvas(wall_value, astuple(n_rows, n_cols))
    x5 = x4
    for x6 in range(x1):
        if x6 not in x3:
            continue
        x7 = divide(x6, n_cols)
        x8 = x6 % n_cols
        x9 = choice(x0)
        x10 = fill(x5, x9, initset(astuple(x7, x8)))
        x5 = x10
    return x5


def generate_ac6f9922(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = choice((TWO, TWO, THREE))
    x1 = choice((TWO, TWO, THREE))
    x2 = choice(COLORS_AC6F9922)
    x3 = choice(tuple(value for value in COLORS_AC6F9922 if value != x2))
    x4, x5, x6, x7 = (choice((ONE, ONE, TWO)) for _ in range(FOUR))
    x8, x9 = _sample_axis_ac6f9922(x0, (THREE, SIX))
    x10, x11 = _sample_axis_ac6f9922(x1, (THREE, FOUR))
    x12 = add(add(x4, x5), add(sum(x8), sum(x9)))
    x13 = add(add(x6, x7), add(sum(x10), sum(x11)))
    x14 = astuple(x12, x13)
    x15 = _axis_starts_ac6f9922(x4, x9, x8)
    x16 = _axis_starts_ac6f9922(x6, x11, x10)
    x17 = _sample_output_ac6f9922(diff_lb, diff_ub, x0, x1, x2, x3)
    x18 = canvas(x3, x14)
    x19 = _frame_indices_ac6f9922(x14, x4, x5, x6, x7)
    x20 = fill(x18, x2, x19)
    for x21, x22 in enumerate(x15):
        x23 = x8[x21]
        for x24, x25 in enumerate(x16):
            x26 = x10[x24]
            x27 = frozenset(
                (i, j)
                for i in range(x22, x22 + x23)
                for j in range(x25, x25 + x26)
            )
            x28 = x17[x21][x24]
            if equality(x28, x2):
                x20 = fill(x20, x2, x27)
                continue
            x29 = box(x27)
            x30 = delta(x29)
            x20 = fill(x20, x2, x29)
            x20 = fill(x20, x28, x30)
    return {"input": x20, "output": x17}
