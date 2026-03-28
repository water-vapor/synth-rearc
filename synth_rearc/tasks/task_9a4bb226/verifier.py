from synth_rearc.core import *


def verify_9a4bb226(I: Grid) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = argmax(x0, numcolors)
    x2 = subgrid(x1, I)
    return x2
