from synth_rearc.core import *

from .helpers import render_output_4aab4007


def verify_4aab4007(I: Grid) -> Grid:
    x0 = []
    for i, row in enumerate(I):
        for j, value in enumerate(row):
            if value == ZERO or i < THREE or j < THREE:
                continue
            x1 = subtract(i, THREE)
            x2 = subtract(j, THREE)
            x3 = add(x1, x2)
            if greater(x3, TWO):
                x0.append(((x3 - THREE), value))
            elif x1 == ONE and x2 == ONE:
                x0.append((None, value))
    x4 = None
    for x5 in range(ONE, TEN):
        x6 = {}
        x7 = True
        for x8, x9 in x0:
            x10 = x5 - ONE if x8 is None else x8 % x5
            if x10 in x6 and x6[x10] != x9:
                x7 = False
                break
            x6[x10] = x9
        if x7 and len(x6) == x5:
            x4 = tuple(x6[x11] for x11 in range(x5))
            break
    if x4 is None:
        raise ValueError("unable to infer cycle")
    x12 = render_output_4aab4007(x4)
    return x12
