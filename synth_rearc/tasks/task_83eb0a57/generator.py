from synth_rearc.core import *

from .helpers import (
    extract_fragments_83eb0a57,
    find_placements_83eb0a57,
    grid_area_83eb0a57,
    paint_fragment_83eb0a57,
    random_anchor_patch_83eb0a57,
    rect_patch_83eb0a57,
    scatter_origins_83eb0a57,
)
from .verifier import verify_83eb0a57


def generate_83eb0a57(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((T, F))
        x1 = branch(x0, THREE, TWO)
        x2 = sample(interval(ZERO, TEN, ONE), add(x1, TWO))
        x3 = x2[ZERO]
        x4 = x2[ONE]
        x5 = x2[TWO:]
        x6 = unifint(diff_lb, diff_ub, branch(x0, (EIGHT, 16), (FIVE, 18)))
        x7 = unifint(diff_lb, diff_ub, branch(x0, (EIGHT, 16), (FIVE, 18)))
        x8 = unifint(diff_lb, diff_ub, (FOUR, subtract(x6, ONE)))
        x9 = unifint(diff_lb, diff_ub, (FOUR, subtract(x7, ONE)))
        x10 = randint(ZERO, subtract(x6, x8))
        x11 = randint(ZERO, subtract(x7, x9))
        x12 = canvas(x5[ZERO], astuple(x6, x7))
        if x0:
            x13 = unifint(diff_lb, diff_ub, (THREE, subtract(x8, ONE)))
            x14 = unifint(diff_lb, diff_ub, (THREE, subtract(x9, ONE)))
            x15 = randint(ZERO, subtract(x8, x13))
            x16 = randint(ZERO, subtract(x9, x14))
            x17 = randint(ONE, subtract(x13, TWO))
            x18 = randint(ONE, subtract(x14, TWO))
            x19 = initset(astuple(add(x15, x17), add(x16, x18)))
            x20 = rect_patch_83eb0a57(x15, x16, x13, x14)
            x25 = random_anchor_patch_83eb0a57(
                x8,
                x9,
                x20,
                unifint(diff_lb, diff_ub, (ONE, TWO)),
            )
            if x25 is None:
                continue
            x26 = combine(x19, x25)
            x27 = canvas(x5[ONE], astuple(x8, x9))
            x28 = fill(x27, x4, x26)
            x29 = canvas(x5[TWO], astuple(x13, x14))
            x30 = fill(x29, x4, initset(astuple(x17, x18)))
            x31 = fill(x12, x4, shift(x26, astuple(x10, x11)))
            x32 = find_placements_83eb0a57(x31, x28)
            if x32 != (astuple(x10, x11),):
                continue
            x33 = paint_fragment_83eb0a57(x31, x28, astuple(x10, x11))
            x34 = add(astuple(x10, x11), astuple(x15, x16))
            x35 = find_placements_83eb0a57(x33, x30)
            if x35 != (x34,):
                continue
            x36 = paint_fragment_83eb0a57(x33, x30, x34)
            x37 = (x31, x28, x30)
        else:
            x13 = random_anchor_patch_83eb0a57(
                x8,
                x9,
                frozenset(),
                unifint(diff_lb, diff_ub, (ONE, THREE)),
            )
            if x13 is None:
                continue
            x14 = canvas(x5[ONE], astuple(x8, x9))
            x15 = fill(x14, x4, x13)
            x16 = fill(x12, x4, shift(x13, astuple(x10, x11)))
            x17 = find_placements_83eb0a57(x16, x15)
            if x17 != (astuple(x10, x11),):
                continue
            x36 = paint_fragment_83eb0a57(x16, x15, astuple(x10, x11))
            x37 = (x16, x15)
        x38 = tuple(astuple(height(x39), width(x39)) for x39 in x37)
        x39 = tuple(grid_area_83eb0a57(x40) for x40 in x37)
        if len(x39) != len(set(x39)):
            continue
        x40 = scatter_origins_83eb0a57(x38)
        if x40 is None:
            continue
        x41 = canvas(x3, (30, 30))
        for x42, x43 in zip(x37, x40):
            x41 = paint_fragment_83eb0a57(x41, x42, x43)
        x44 = extract_fragments_83eb0a57(x41)
        if len(x44) != x1:
            continue
        if verify_83eb0a57(x41) != x36:
            continue
        return {"input": x41, "output": x36}
