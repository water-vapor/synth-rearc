from synth_rearc.core import *

from .helpers import (
    LABEL_OFFSET_DFADAB01,
    MARKER_SPECS_DFADAB01,
    assemble_output_dfadab01,
    visible_markers_dfadab01,
)


MARKER_COLORS_DFADAB01 = tuple(x0 for x0, _, _ in MARKER_SPECS_DFADAB01)
OUTPUT_COLORS_DFADAB01 = {x0: x1 for x0, x1, _ in MARKER_SPECS_DFADAB01}
PATTERNS_DFADAB01 = {x0: x1 for x0, _, x1 in MARKER_SPECS_DFADAB01}


def _fullfit_anchors_dfadab01(
    anchors: tuple[IntegerTuple, ...],
    height_: Integer,
    width_: Integer,
) -> tuple[IntegerTuple, ...]:
    return tuple(
        x0 for x0 in anchors
        if x0[ZERO] <= height_ - FOUR and x0[ONE] <= width_ - FOUR
    )


def _visible_pattern_dfadab01(
    marker_color: Integer,
    anchor: IntegerTuple,
    height_: Integer,
    width_: Integer,
) -> Indices:
    x0 = PATTERNS_DFADAB01[marker_color]
    x1 = shift(x0, anchor)
    x2 = frozenset(
        (i, j) for i, j in x1 if 0 <= i < height_ and 0 <= j < width_
    )
    return x2


def _visible_candidates_dfadab01(
    marker_color: Integer,
    anchors: tuple[IntegerTuple, ...],
    height_: Integer,
    width_: Integer,
) -> tuple[IntegerTuple, ...]:
    return tuple(
        x0 for x0 in anchors
        if greater(len(_visible_pattern_dfadab01(marker_color, x0, height_, width_)), ZERO)
    )


def _invisible_candidates_dfadab01(
    marker_color: Integer,
    anchors: tuple[IntegerTuple, ...],
    height_: Integer,
    width_: Integer,
) -> tuple[IntegerTuple, ...]:
    return tuple(
        x0 for x0 in anchors
        if equality(len(_visible_pattern_dfadab01(marker_color, x0, height_, width_)), ZERO)
    )


def generate_dfadab01(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = (TEN, 20)
    x1 = (FOUR, FIVE, SIX)
    while True:
        x2 = choice(x0)
        x3 = x2
        x4 = choice(x1)
        x5 = randint(ZERO, x4 - ONE)
        x6 = randint(ZERO, x4 - ONE)
        x7 = tuple(interval(x5, x2, x4))
        x8 = tuple(interval(x6, x3, x4))
        x9 = tuple(product(x7, x8))
        if len(x9) < ONE:
            continue
        x10 = unifint(diff_lb, diff_ub, (ONE, FOUR))
        x11 = tuple(sample(MARKER_COLORS_DFADAB01, x10))
        x12 = {x13: _visible_candidates_dfadab01(x13, x9, x2, x3) for x13 in x11}
        if any(equality(len(x12[x13]), ZERO) for x13 in x11):
            continue
        x14 = min(len(x9), branch(equality(x2, TEN), EIGHT, 25))
        if x14 < x10:
            continue
        x15 = unifint(diff_lb, diff_ub, (x10, x14))
        x16 = {x17: set() for x17 in x11}
        x18 = set()
        x19 = True
        for x20 in x11:
            x21 = tuple(x22 for x22 in x12[x20] if x22 not in x18)
            if len(x21) == ZERO:
                x19 = False
                break
            x23 = choice(x21)
            x16[x20].add(x23)
            x18.add(x23)
        if not x19:
            continue
        for _ in range(x15 - x10):
            x20 = tuple(
                x21 for x21 in x11
                if greater(len(tuple(x22 for x22 in x12[x21] if x22 not in x18)), ZERO)
            )
            if len(x20) == ZERO:
                x19 = False
                break
            x21 = choice(x20)
            x22 = tuple(x23 for x23 in x12[x21] if x23 not in x18)
            x23 = choice(x22)
            x16[x21].add(x23)
            x18.add(x23)
        if not x19:
            continue
        x24 = randint(ZERO, min(TWO, len(x9) - len(x18)))
        for _ in range(x24):
            x20 = tuple(
                x21 for x21 in x11
                if greater(
                    len(
                        tuple(
                            x22 for x22 in _invisible_candidates_dfadab01(x21, x9, x2, x3)
                            if x22 not in x18
                        )
                    ),
                    ZERO,
                )
            )
            if len(x20) == ZERO:
                break
            x21 = choice(x20)
            x22 = tuple(
                x23 for x23 in _invisible_candidates_dfadab01(x21, x9, x2, x3)
                if x23 not in x18
            )
            x23 = choice(x22)
            x16[x21].add(x23)
            x18.add(x23)
        x25 = tuple(_fullfit_anchors_dfadab01(x9, x2, x3))
        x26 = tuple((x27, frozenset(x16[x27])) for x27 in x11)
        x27 = merge(tuple(x28 for _, x28 in x26))
        x28 = None
        x29 = None
        x30 = branch(equality(x10, FOUR), ONE, THREE)
        x31 = greater(x30, randint(ZERO, THREE))
        if both(x31, greater(len(x25), ZERO)):
            x32 = choice(x11)
            x33 = tuple(
                x34 for x34 in x25
                if add(x34, LABEL_OFFSET_DFADAB01) not in x27
                and (
                    x34 not in x27
                    or (
                        x32 == THREE
                        and THREE in x16
                        and x34 in x16[THREE]
                    )
                )
            )
            if greater(len(x33), ZERO):
                x28 = x32
                x29 = choice(x33)
        x34 = canvas(ZERO, (x2, x3))
        if both(x28 is not None, x29 is not None):
            x35 = PATTERNS_DFADAB01[x28]
            x36 = OUTPUT_COLORS_DFADAB01[x28]
            x37 = recolor(x36, shift(x35, x29))
            x34 = paint(x34, x37)
            x38 = add(x29, LABEL_OFFSET_DFADAB01)
            x34 = fill(x34, x28, frozenset({x38}))
        for x35 in x11:
            x34 = fill(x34, x35, frozenset(x16[x35]))
        x39 = assemble_output_dfadab01(x34)
        if x39 == x34:
            continue
        if x28 is not None:
            x40 = visible_markers_dfadab01(x34, x28, OUTPUT_COLORS_DFADAB01[x28], PATTERNS_DFADAB01[x28])
            x41 = add(x29, LABEL_OFFSET_DFADAB01)
            if contained(x41, x40):
                continue
        x42 = palette(x39)
        if not all(OUTPUT_COLORS_DFADAB01[x43] in x42 for x43 in x11):
            continue
        return {"input": x34, "output": x39}
