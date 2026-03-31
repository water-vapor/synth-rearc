from __future__ import annotations

from synth_rearc.core import *

from .helpers import SignatureC7F57C3E, build_object_c7f57c3e, footprint_bounds_c7f57c3e
from .verifier import verify_c7f57c3e


SCAFFOLD_A_C7F57C3E = ((ZERO, ONE), (ONE, ZERO), (ONE, TWO))
SCAFFOLD_B_C7F57C3E = ((ZERO, ZERO), (ZERO, TWO), (TWO, ZERO), (TWO, TWO))
SCAFFOLD_C_C7F57C3E = (
    (ZERO, ONE),
    (ZERO, TWO),
    (ONE, ZERO),
    (ONE, THREE),
    (TWO, ONE),
    (TWO, TWO),
)


def _family_a_signatures_c7f57c3e(
    colors: tuple[Integer, Integer, Integer],
) -> tuple[tuple[SignatureC7F57C3E, SignatureC7F57C3E], tuple[Integer, ...]]:
    x0, x1, x2 = colors
    x3 = (
        (x0, (ONE, ONE)),
        (x0, (TWO, ONE)),
        (x1, (THREE, ZERO)),
        (x1, (THREE, ONE)),
        (x1, (THREE, TWO)),
    )
    x4 = (
        (x0, (ONE, ONE)),
        (x2, (TWO, ONE)),
        (x2, (THREE, ZERO)),
        (x2, (THREE, ONE)),
        (x2, (THREE, TWO)),
    )
    return (x3, x4), (ONE, x0, x1, x2)


def _family_b_signatures_c7f57c3e(
    colors: tuple[Integer, Integer, Integer],
) -> tuple[tuple[SignatureC7F57C3E, SignatureC7F57C3E], tuple[Integer, ...]]:
    x0, x1, x2 = colors
    x3 = (
        (x0, (ONE, ONE)),
        (x1, (THREE, ONE)),
    )
    x4 = (
        (x2, (-ONE, ONE)),
        (x0, (ONE, ONE)),
    )
    return (x3, x4), (ONE, x0, x1, x2)


def _family_c_signatures_c7f57c3e(
    colors: tuple[Integer, Integer, Integer, Integer],
) -> tuple[tuple[SignatureC7F57C3E, SignatureC7F57C3E], tuple[Integer, ...]]:
    x0, x1, x2, x3 = colors
    x4 = (
        (x0, (-ONE, ONE)),
        (x0, (-ONE, TWO)),
        (x1, (ONE, ONE)),
        (x1, (ONE, TWO)),
    )
    x5 = (
        (x2, (ONE, ONE)),
        (x2, (ONE, TWO)),
        (x3, (THREE, ONE)),
        (x3, (THREE, TWO)),
    )
    return (x4, x5), (ONE, x0, x1, x2, x3)


FAMILY_SPECS_C7F57C3E = (
    {
        "scaffold": SCAFFOLD_A_C7F57C3E,
        "signatures": _family_a_signatures_c7f57c3e,
        "n_colors": THREE,
        "scales": (ONE, ONE, TWO),
        "labels": ("minority", "majority", "majority"),
        "side_range": (16, 24),
    },
    {
        "scaffold": SCAFFOLD_B_C7F57C3E,
        "signatures": _family_b_signatures_c7f57c3e,
        "n_colors": THREE,
        "scales": (ONE, ONE, TWO),
        "labels": ("minority", "majority", "majority"),
        "side_range": (16, 24),
    },
    {
        "scaffold": SCAFFOLD_C_C7F57C3E,
        "signatures": _family_c_signatures_c7f57c3e,
        "n_colors": FOUR,
        "scales": (ONE, ONE, ONE, THREE),
        "labels": ("minority", "majority", "majority", "majority"),
        "side_range": (24, 30),
    },
)


def _pick_colors_c7f57c3e(
    count: Integer,
) -> tuple[Integer, ...]:
    x0 = list(range(TEN))
    x0.remove(ONE)
    shuffle(x0)
    return tuple(x0[:count])


def _background_color_c7f57c3e(
    used_colors: tuple[Integer, ...],
) -> Integer:
    x0 = [x1 for x1 in range(TEN) if x1 not in used_colors]
    shuffle(x0)
    return x0[ZERO]


def _rect_from_anchor_c7f57c3e(
    bounds: tuple[Integer, Integer, Integer, Integer],
    scale: Integer,
    anchor: IntegerTuple,
) -> tuple[Integer, Integer, Integer, Integer]:
    x0, x1, x2, x3 = bounds
    x4, x5 = anchor
    x6 = add(x4, multiply(x0, scale))
    x7 = add(x5, multiply(x1, scale))
    x8 = subtract(add(x4, multiply(increment(x2), scale)), ONE)
    x9 = subtract(add(x5, multiply(increment(x3), scale)), ONE)
    return (x6, x7, x8, x9)


def _rects_separate_c7f57c3e(
    rect: tuple[Integer, Integer, Integer, Integer],
    others: tuple[tuple[Integer, Integer, Integer, Integer], ...],
    gap: Integer,
) -> Boolean:
    x0, x1, x2, x3 = rect
    for x4, x5, x6, x7 in others:
        if x2 + gap < x4 or x6 + gap < x0 or x3 + gap < x5 or x7 + gap < x1:
            continue
        return False
    return True


def _place_anchors_c7f57c3e(
    side: Integer,
    bounds: tuple[Integer, Integer, Integer, Integer],
    scales: tuple[Integer, ...],
) -> tuple[IntegerTuple, ...] | None:
    x0 = []
    x1 = []
    x2 = tuple(sorted(scales, reverse=True))
    for x3 in x2:
        x4, x5, x6, x7 = bounds
        x8 = multiply(-x4, x3)
        x9 = subtract(side, multiply(increment(x6), x3))
        x10 = multiply(-x5, x3)
        x11 = subtract(side, multiply(increment(x7), x3))
        if x9 < x8 or x11 < x10:
            return None
        x12 = False
        for _ in range(120):
            x13 = randint(x8, x9)
            x14 = randint(x10, x11)
            x15 = (x13, x14)
            x16 = _rect_from_anchor_c7f57c3e(bounds, x3, x15)
            if not _rects_separate_c7f57c3e(x16, tuple(x1), TWO):
                continue
            x0.append((x3, x15))
            x1.append(x16)
            x12 = True
            break
        if not x12:
            return None
    x17 = {x18: [] for x18 in scales}
    for x19, x20 in x0:
        x17[x19].append(x20)
    x21 = []
    for x22 in scales:
        x21.append(x17[x22].pop())
    return tuple(x21)


def generate_c7f57c3e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(FAMILY_SPECS_C7F57C3E)
        x1 = x0["scaffold"]
        x2 = x0["signatures"]
        x3 = x0["n_colors"]
        x4 = x2(_pick_colors_c7f57c3e(x3))
        x5, x6 = x4
        x7, x8 = x5
        x9 = x0["scales"]
        x10 = x0["labels"]
        x11 = footprint_bounds_c7f57c3e(x1, x5)
        x12, x13 = x0["side_range"]
        x14 = unifint(diff_lb, diff_ub, (x12, x13))
        x15 = _place_anchors_c7f57c3e(x14, x11, x9)
        if x15 is None:
            continue
        x16 = _background_color_c7f57c3e(x6)
        x17 = canvas(x16, (x14, x14))
        for x18, x19, x20 in zip(x10, x9, x15):
            x21 = x8 if x18 == "minority" else x7
            x22 = build_object_c7f57c3e(x1, x21, x19, x20)
            x17 = paint(x17, x22)
        x23 = verify_c7f57c3e(x17)
        if x23 == x17:
            continue
        if size(objects(x17, F, T, T)) != len(x10):
            continue
        if size(objects(x23, F, T, T)) != len(x10):
            continue
        return {"input": x17, "output": x23}
