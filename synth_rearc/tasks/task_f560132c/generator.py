from synth_rearc.core import *

from .helpers import INPUT_QUADRANTS_F560132C
from .helpers import input_canvas_dims_f560132c, input_quadrant_shift_f560132c
from .helpers import sample_partition_f560132c, shape_variants_f560132c
from .verifier import verify_f560132c


def generate_f560132c(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(range(ONE, TEN))
    while True:
        x1, x2, x3, x4 = sample_partition_f560132c(diff_lb, diff_ub)
        x5, x6, x7, x8, x9, x10, x11, x12 = sample(x0, EIGHT)
        x13 = canvas(x5, (x1, x1))
        x13 = fill(x13, x6, x3["tr"])
        x13 = fill(x13, x7, x3["bl"])
        x13 = fill(x13, x8, x3["br"])
        x14 = frozenset(normalize(x2 - x4))
        x15 = {"tr": frozenset(normalize(x3["tr"])), "bl": frozenset(normalize(x3["bl"])), "br": frozenset(normalize(x3["br"]))}
        x16 = [("tr", choice(shape_variants_f560132c(x15["tr"]))), ("bl", choice(shape_variants_f560132c(x15["bl"])))]
        shuffle(x16)
        x17 = {
            "ur": x16[0],
            "bl": ("br", choice(shape_variants_f560132c(x15["br"]))),
            "br": x16[1],
        }
        x21 = input_canvas_dims_f560132c(x14, x17["ur"][1], x17["bl"][1], x17["br"][1], x1)
        x22 = input_quadrant_shift_f560132c(x14, x21, "ul")
        x23 = {x24: input_quadrant_shift_f560132c(x25[1], x21, x24) for x24, x25 in x17.items()}
        x26 = canvas(ZERO, x21)
        x26 = paint(x26, recolor(x9, shift(x14, x22)))
        x27 = shift(x4, x22)
        x28 = tuple(sorted({x29 for x29, _ in x27}))
        x29 = tuple(sorted({x30 for _, x30 in x27}))
        x26 = fill(x26, x5, initset((x28[0], x29[0])))
        x26 = fill(x26, x6, initset((x28[0], x29[1])))
        x26 = fill(x26, x7, initset((x28[1], x29[0])))
        x26 = fill(x26, x8, initset((x28[1], x29[1])))
        x30 = {"ur": x10, "bl": x11, "br": x12}
        for x31 in INPUT_QUADRANTS_F560132C:
            x32 = shift(x17[x31][1], x23[x31])
            x26 = paint(x26, recolor(x30[x31], x32))
        try:
            x33 = verify_f560132c(x26)
        except Exception:
            continue
        if x33 != x13:
            continue
        return {"input": x26, "output": x13}
