from synth_rearc.core import *

from .helpers import build_input_136b0064
from .helpers import render_trace_136b0064
from .verifier import verify_136b0064


SYMBOL_CHOICES_136b0064 = (SIX, SIX, SIX, ONE, ONE, TWO, TWO, THREE)


def _valid_symbols_136b0064(
    cursor_col: Integer,
    height_used: Integer,
    length: Integer,
    index_value: Integer,
) -> tuple[int, ...]:
    x0 = subtract(subtract(length, index_value), ONE)
    x1 = []
    for x2 in dedupe(SYMBOL_CHOICES_136b0064):
        if x2 == ONE and greater(add(cursor_col, TWO), SIX):
            continue
        if x2 == TWO and greater(ONE, cursor_col):
            continue
        if x2 == THREE and greater(THREE, cursor_col):
            continue
        x3 = branch(equality(x2, SIX), TWO, ONE)
        x4 = add(height_used, x3)
        if greater(add(x4, x0), subtract(multiply(TWO, length), TWO)):
            continue
        x1.append(x2)
    return tuple(x1)


def _sample_sequence_136b0064(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, tuple[int, ...]]:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, FIVE))
        x1 = multiply(TWO, x0)
        x2 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x3 = x2
        x4 = ZERO
        x5 = []
        for x6 in range(x1):
            x7 = _valid_symbols_136b0064(x3, x4, x1, x6)
            if len(x7) == ZERO:
                break
            x8 = tuple(x9 for x9 in SYMBOL_CHOICES_136b0064 if contained(x9, x7))
            if len(x5) >= TWO and x5[-1] == SIX and x5[-2] == SIX:
                x8 = tuple(x9 for x9 in x8 if x9 != SIX)
            if len(x8) == ZERO:
                break
            x10 = choice(x8)
            x5.append(x10)
            x4 = add(x4, branch(equality(x10, SIX), TWO, ONE))
            if x10 == ONE:
                x3 = add(x3, TWO)
            elif x10 == TWO:
                x3 = subtract(x3, ONE)
            elif x10 == THREE:
                x3 = subtract(x3, THREE)
        if len(x5) != x1:
            continue
        x11 = tuple(x5)
        if not contained(SIX, x11):
            continue
        if x11.count(SIX) > x0:
            continue
        if not contained(ONE, x11):
            continue
        if not any(x12 in (TWO, THREE) for x12 in x11):
            continue
        if equality(len(set(x11)), ONE):
            continue
        return x2, x11


def generate_136b0064(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0, x1 = _sample_sequence_136b0064(diff_lb, diff_ub)
        x2 = build_input_136b0064(x1, x0)
        x3 = canvas(ZERO, (subtract(multiply(FOUR, halve(len(x1))), ONE), 7))
        x4 = fill(x3, FIVE, {(ZERO, x0)})
        x5 = render_trace_136b0064(x4, (ZERO, x0), x1)
        if verify_136b0064(x2) != x5:
            continue
        return {"input": x2, "output": x5}
