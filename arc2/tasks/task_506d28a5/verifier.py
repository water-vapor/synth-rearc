from arc2.core import *


def verify_506d28a5(
    I: Grid,
) -> Grid:
    x0 = tophalf(I)
    x1 = bottomhalf(I)
    x2 = replace(x0, TWO, THREE)
    x3 = replace(x1, ONE, THREE)
    x4 = cellwise(x2, x3, THREE)
    return x4
