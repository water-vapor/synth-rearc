from arc2.core import *

from .verifier import verify_fe9372f3


def generate_fe9372f3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while T:
        x0 = unifint(diff_lb, diff_ub, (SEVEN, 30))
        x1 = unifint(diff_lb, diff_ub, (SEVEN, 30))
        x2 = randint(THREE, subtract(x0, FOUR))
        x3 = randint(THREE, subtract(x1, FOUR))
        x4 = astuple(x2, x3)
        x5 = add(x4, LEFT)
        x6 = add(x4, RIGHT)
        x7 = add(x4, UP)
        x8 = add(x4, DOWN)
        x9 = connect(x5, x6)
        x10 = connect(x7, x8)
        x11 = combine(x9, x10)
        x12 = canvas(ZERO, (x0, x1))
        gi = fill(x12, TWO, x11)
        x13 = shoot(x4, UNITY)
        x14 = shoot(x4, NEG_UNITY)
        x15 = shoot(x4, UP_RIGHT)
        x16 = shoot(x4, DOWN_LEFT)
        x17 = combine(x13, x14)
        x18 = combine(x15, x16)
        x19 = combine(x17, x18)
        go = underfill(gi, ONE, x19)
        x20 = combine(hfrontier(x4), vfrontier(x4))
        go = underfill(go, EIGHT, x20)
        x21 = interval(FOUR, 30, THREE)
        x22 = (UP, DOWN, LEFT, RIGHT)
        x23 = frozenset(add(x4, multiply(x24, x25)) for x24 in x21 for x25 in x22)
        go = fill(go, FOUR, x23)
        if verify_fe9372f3(gi) != go:
            continue
        return {"input": gi, "output": go}
