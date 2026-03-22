from arc2.core import *


def verify_7bb29440(
    I: Grid,
) -> Grid:
    x0 = objects(I, F, F, T)
    x1 = argmin(
        x0,
        lambda x2: (
            add(colorcount(x2, FOUR), colorcount(x2, SIX)),
            uppermost(x2),
            leftmost(x2),
            height(x2),
            width(x2),
        ),
    )
    x2 = subgrid(x1, I)
    return x2
