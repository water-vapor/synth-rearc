from arc2.core import *


def verify_3194b014(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = argmax(x0, size)
    x2 = color(x1)
    x3 = canvas(x2, (THREE, THREE))
    return x3
