from synth_rearc.core import *

from .helpers import TARGET_SIZE_269E22FB, candidate_outputs_269e22fb


def verify_269e22fb(I: Grid) -> Grid:
    x0 = order(palette(I), identity)
    x1 = first(x0)
    x2 = last(x0)
    x3 = candidate_outputs_269e22fb(x1, x2)
    x4 = shape(I)
    x5 = subtract(TARGET_SIZE_269E22FB, x4[0])
    x6 = subtract(TARGET_SIZE_269E22FB, x4[1])
    for x7 in x3:
        for x8 in interval(ZERO, add(x5, ONE), ONE):
            for x9 in interval(ZERO, add(x6, ONE), ONE):
                x10 = crop(x7, (x8, x9), x4)
                if equality(x10, I):
                    return x7
    return I
