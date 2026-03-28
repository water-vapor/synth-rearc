from arc2.core import *


NONZERO_COLORS_66E6C45B = remove(ZERO, interval(ZERO, TEN, ONE))
INPUT_LOCS_66E6C45B = (UNITY, (ONE, TWO), (TWO, ONE), TWO_BY_TWO)
OUTPUT_LOCS_66E6C45B = (ORIGIN, (ZERO, THREE), (THREE, ZERO), THREE_BY_THREE)


def generate_66e6c45b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(sample(NONZERO_COLORS_66E6C45B, FOUR))
    x1 = frozenset((value, index) for value, index in zip(x0, INPUT_LOCS_66E6C45B))
    x2 = frozenset((value, index) for value, index in zip(x0, OUTPUT_LOCS_66E6C45B))
    gi = paint(canvas(ZERO, (FOUR, FOUR)), x1)
    go = paint(canvas(ZERO, (FOUR, FOUR)), x2)
    return {"input": gi, "output": go}
