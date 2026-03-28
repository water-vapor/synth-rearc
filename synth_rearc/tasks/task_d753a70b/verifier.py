from synth_rearc.core import *

from .helpers import transformed_component_d753a70b


def verify_d753a70b(I: Grid) -> Grid:
    x0 = shape(I)
    x1 = mostcolor(I)
    x2 = objects(I, T, T, T)
    x3 = canvas(x1, x0)
    for x4 in x2:
        x5 = transformed_component_d753a70b(x4, x0)
        x3 = paint(x3, x5)
    return x3
