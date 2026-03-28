from arc2.core import *


def verify_59341089(I: Grid) -> Grid:
    x0 = vmirror(I)
    x1 = hconcat(x0, I)
    x2 = hconcat(x1, x1)
    return x2
