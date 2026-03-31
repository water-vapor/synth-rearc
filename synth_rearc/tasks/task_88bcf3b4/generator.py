from synth_rearc.core import *

from .helpers import sample_local_motif_88bcf3b4, shift_patch_88bcf3b4
from .verifier import verify_88bcf3b4


def _boxes_overlap_88bcf3b4(
    a: tuple[Integer, Integer, Integer, Integer],
    b: tuple[Integer, Integer, Integer, Integer],
    margin: Integer = TWO,
) -> Boolean:
    x0, x1, x2, x3 = a
    x4, x5, x6, x7 = b
    return not (
        x0 + x2 + margin <= x4
        or x4 + x6 + margin <= x0
        or x1 + x3 + margin <= x5
        or x5 + x7 + margin <= x1
    )


def generate_88bcf3b4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (12, 24))
        x1 = unifint(diff_lb, diff_ub, (12, 24))
        x2 = choice(interval(ZERO, TEN, ONE))
        x3 = ONE if min(x0, x1) < 16 else choice((ONE, ONE, TWO))
        x4 = []
        x5 = []
        for _ in range(x3):
            x6 = sample_local_motif_88bcf3b4(diff_lb, diff_ub)
            if x6 is None:
                x4 = []
                break
            x7, x8 = x6["dims"]
            if x7 > x0 or x8 > x1:
                x4 = []
                break
            x9 = False
            for _ in range(160):
                x10 = randint(ZERO, x0 - x7)
                x11 = randint(ZERO, x1 - x8)
                x12 = (x10, x11, x7, x8)
                if any(_boxes_overlap_88bcf3b4(x12, x13) for x13 in x5):
                    continue
                x6["offset"] = (x10, x11)
                x4.append(x6)
                x5.append(x12)
                x9 = True
                break
            if not x9:
                x4 = []
                break
        if len(x4) != x3:
            continue
        x13 = tuple(x14 for x14 in interval(ZERO, TEN, ONE) if x14 != x2)
        x14 = sample(x13, THREE * x3)
        x15 = canvas(x2, (x0, x1))
        x16 = canvas(x2, (x0, x1))
        x17 = ZERO
        for x18 in x4:
            x19 = x14[x17]
            x20 = x14[x17 + ONE]
            x21 = x14[x17 + TWO]
            x17 = x17 + THREE
            x22 = x18["offset"]
            x23 = shift_patch_88bcf3b4(x18["anchor"], x22)
            x24 = shift_patch_88bcf3b4(x18["target"], x22)
            x25 = shift_patch_88bcf3b4(x18["input_path"], x22)
            x26 = shift_patch_88bcf3b4(x18["output_path"], x22)
            x15 = fill(x15, x19, x23)
            x15 = fill(x15, x20, x24)
            x15 = fill(x15, x21, x25)
            x16 = fill(x16, x19, x23)
            x16 = fill(x16, x20, x24)
            x16 = fill(x16, x21, x26)
        if verify_88bcf3b4(x15) != x16:
            continue
        return {"input": x15, "output": x16}
