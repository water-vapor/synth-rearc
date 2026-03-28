from synth_rearc.core import *

from .verifier import verify_963f59bc


TEMPLATES_963F59BC = (
    frozenset({(0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1)}),
    frozenset({(0, 0), (0, 1), (1, 1), (2, 0), (2, 1), (2, 2), (2, 3)}),
    frozenset({(0, 1), (0, 2), (1, 0), (2, 1), (2, 2), (3, 2)}),
    frozenset({(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 1), (3, 1), (3, 2), (3, 3)}),
    frozenset({(0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 2), (3, 1), (3, 2)}),
    frozenset({(0, 2), (1, 0), (1, 1), (1, 2), (2, 1), (3, 1), (3, 2)}),
    frozenset({(0, 0), (0, 1), (1, 1), (2, 0), (2, 1), (3, 1), (3, 2)}),
)

TRANSFORMS_963F59BC = (
    identity,
    identity,
    hmirror,
    vmirror,
    compose(hmirror, vmirror),
    dmirror,
    cmirror,
)

SEED_COLORS_963F59BC = (TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE)


def _row_counts_963f59bc(patch: Indices) -> dict[int, int]:
    x0 = {}
    for x1, _ in patch:
        x0[x1] = x0.get(x1, ZERO) + ONE
    return x0


def _col_counts_963f59bc(patch: Indices) -> dict[int, int]:
    x0 = {}
    for _, x1 in patch:
        x0[x1] = x0.get(x1, ZERO) + ONE
    return x0


def _singleton_rows_963f59bc(patch: Indices) -> tuple[int, ...]:
    x0 = _row_counts_963f59bc(patch)
    return tuple(sorted(x1 for x1, x2 in x0.items() if x2 == ONE))


def _singleton_cols_963f59bc(patch: Indices) -> tuple[int, ...]:
    x0 = _col_counts_963f59bc(patch)
    return tuple(sorted(x1 for x1, x2 in x0.items() if x2 == ONE))


def _choose_template_963f59bc(
    need_right: bool,
    need_down: bool,
) -> tuple[Indices, tuple[int, ...], tuple[int, ...]]:
    while True:
        x0 = choice(TEMPLATES_963F59BC)
        x1 = normalize(choice(TRANSFORMS_963F59BC)(x0))
        x2 = _singleton_rows_963f59bc(x1)
        x3 = _singleton_cols_963f59bc(x1)
        if need_right and len(x2) == ZERO:
            continue
        if need_down and len(x3) == ZERO:
            continue
        return x1, x2, x3


def _seed_for_right_copy_963f59bc(
    patch: Indices,
    row_value: int,
) -> IntegerTuple:
    return extract(patch, matcher(first, row_value))


def _seed_for_down_copy_963f59bc(
    patch: Indices,
    col_value: int,
) -> IntegerTuple:
    return extract(patch, matcher(last, col_value))


def generate_963f59bc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("right", "down", "both", "both"))
        x1 = x0 != "down"
        x2 = x0 != "right"
        x3, x4, x5 = _choose_template_963f59bc(x1, x2)
        x6 = height(x3)
        x7 = width(x3)
        x8 = unifint(diff_lb, diff_ub, (ZERO, TWO))
        x9 = unifint(diff_lb, diff_ub, (ZERO, TWO))
        x10 = ZERO
        x11 = ZERO
        x12 = ZERO
        x13 = ZERO
        if x1:
            x10 = unifint(diff_lb, diff_ub, (TWO, FOUR))
            x11 = x9 + x7 + x10
        if x2:
            x12 = unifint(diff_lb, diff_ub, (TWO, FOUR))
            x13 = x8 + x6 + x12
        x14 = x8 + x6
        if x2:
            x14 = x13 + x6
        x15 = x9 + x7
        if x1:
            x15 = x11 + x7
        x16 = unifint(diff_lb, diff_ub, (max(11, x14), 16))
        x17 = unifint(diff_lb, diff_ub, (max(11, x15), 16))
        x18 = shift(x3, (x8, x9))
        x19 = canvas(ZERO, (x16, x17))
        x20 = fill(x19, ONE, x18)
        x21 = x20
        x22 = sample(SEED_COLORS_963F59BC, x1 + x2)
        x23 = ZERO
        if x1:
            x24 = choice(x4)
            x25 = shift(vmirror(x3), (x8, x11))
            x26 = _seed_for_right_copy_963f59bc(x25, x8 + x24)
            x20 = fill(x20, x22[x23], initset(x26))
            x21 = fill(x21, x22[x23], x25)
            x23 += ONE
        if x2:
            x27 = choice(x5)
            x28 = shift(hmirror(x3), (x13, x9))
            x29 = _seed_for_down_copy_963f59bc(x28, x9 + x27)
            x20 = fill(x20, x22[x23], initset(x29))
            x21 = fill(x21, x22[x23], x28)
        x30 = {"input": x20, "output": x21}
        if verify_963f59bc(x30["input"]) != x30["output"]:
            continue
        return x30
