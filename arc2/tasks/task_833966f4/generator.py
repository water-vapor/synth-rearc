from arc2.core import *


COLOR_POOL_833966F4 = interval(ZERO, TEN, ONE)
SWAP_ORDER_833966F4 = (ONE, ZERO, TWO, FOUR, THREE)


def generate_833966f4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    _ = diff_lb, diff_ub
    x0 = tuple(sample(COLOR_POOL_833966F4, FIVE))
    x1 = tuple((value,) for value in x0)
    x2 = tuple(x0[i] for i in SWAP_ORDER_833966F4)
    x3 = tuple((value,) for value in x2)
    return {"input": x1, "output": x3}
