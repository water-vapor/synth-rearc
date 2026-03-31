from synth_rearc.core import *

from .verifier import verify_45a5af55


NONZERO_COLORS_45A5AF55 = tuple(range(ONE, TEN))
INPUT_HEIGHT_RANGE_45A5AF55 = (TEN, 15)
RUN_COUNT_RANGE_45A5AF55 = (FIVE, SEVEN)
PALETTE_SIZE_RANGE_45A5AF55 = (THREE, FIVE)


def _sample_run_lengths_45a5af55(
    depth: Integer,
    run_count: Integer,
) -> tuple[Integer, ...]:
    x0 = subtract(depth, ONE)
    x1 = subtract(run_count, ONE)
    x2 = [] if x1 == ONE else sorted(sample(range(ONE, x0), x1 - ONE))
    x3 = [ZERO, *x2, x0]
    x4 = [x3[idx + ONE] - x3[idx] for idx in range(len(x3) - ONE)]
    return tuple((*x4, ONE))


def _sample_run_colors_45a5af55(
    run_count: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, ...]:
    x0 = unifint(diff_lb, diff_ub, (THREE, min(FIVE, run_count)))
    while True:
        x1 = tuple(sample(NONZERO_COLORS_45A5AF55, x0))
        x2 = []
        for _ in range(run_count):
            x3 = tuple(x4 for x4 in x1 if len(x2) == ZERO or x4 != x2[-ONE])
            x2.append(choice(x3))
        x4 = tuple(x2)
        if len(set(x4)) < THREE:
            continue
        if len(set(x4)) == run_count:
            continue
        if x4[ZERO] == x4[-ONE]:
            continue
        return x4


def _render_input_45a5af55(
    layers: tuple[Integer, ...],
    width: Integer,
) -> Grid:
    x0 = len(layers)
    x1 = canvas(ZERO, astuple(add(x0, ONE), width))
    x2 = decrement(width)
    for x3, x4 in enumerate(layers):
        x5 = connect((x3, ZERO), (x3, x2))
        x1 = fill(x1, x4, x5)
    x6 = connect((x0, ZERO), (x0, x2))
    x7 = fill(x1, layers[-ONE], x6)
    return x7


def _render_output_45a5af55(
    layers: tuple[Integer, ...],
) -> Grid:
    x0 = len(layers)
    x1 = double(x0)
    x2 = canvas(ZERO, astuple(x1, x1))
    for x3, x4 in enumerate(layers):
        x5 = decrement(subtract(x1, x3))
        x6 = box(frozenset({astuple(x3, x3), astuple(x5, x5)}))
        x2 = fill(x2, x4, x6)
    return x2


def generate_45a5af55(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, INPUT_HEIGHT_RANGE_45A5AF55)
        x1 = subtract(x0, ONE)
        x2 = unifint(diff_lb, diff_ub, (FIVE, min(SEVEN, x1)))
        x3 = _sample_run_lengths_45a5af55(x1, x2)
        x4 = _sample_run_colors_45a5af55(x2, diff_lb, diff_ub)
        x5 = tuple(x6 for x7, x8 in zip(x4, x3) for x6 in repeat(x7, x8))
        x6 = max(EIGHT, subtract(x1, TWO))
        x7 = min(16, add(x1, ONE))
        x8 = unifint(diff_lb, diff_ub, (x6, x7))
        x9 = _render_input_45a5af55(x5, x8)
        x10 = _render_output_45a5af55(x5)
        if verify_45a5af55(x9) != x10:
            continue
        return {"input": x9, "output": x10}
