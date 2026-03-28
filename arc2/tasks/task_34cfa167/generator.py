from arc2.core import *

from .helpers import horizontal_cycle_34cfa167, vertical_cycle_34cfa167


def generate_34cfa167(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    backgrounds = (ZERO, FOUR, EIGHT)
    accents = (TWO, THREE, FOUR, SIX, EIGHT)
    while True:
        bg = choice(backgrounds)
        palette0 = remove(bg, accents)
        hlead, vlead, tail = sample(palette0, THREE)
        side = unifint(diff_lb, diff_ub, (ONE, FOUR))
        hrep = unifint(diff_lb, diff_ub, (TWO, FOUR))
        vrep = unifint(diff_lb, diff_ub, (TWO, FOUR))
        gapw = add(multiply(FOUR, hrep), ONE)
        gaph = add(multiply(FOUR, vrep), ONE)
        top = randint(ONE, TWO)
        left = randint(ONE, THREE)
        bottom = randint(ONE, THREE)
        right = randint(ONE, FOUR)
        gh = top + side + gaph + side + ONE + bottom
        gw = left + side + gapw + side + ONE + right
        if greater(gh, 30) or greater(gw, 30):
            continue
        r0 = top
        c0 = left
        r1 = r0 + side + gaph
        c1 = c0 + side + gapw
        gi = canvas(bg, (gh, gw))
        a0 = frozenset((ONE, (r0 + i, c0 + j)) for i in range(side) for j in range(side))
        a1 = frozenset((ONE, (r1 + i, c1 + j)) for i in range(side) for j in range(side))
        gi = paint(gi, a0)
        gi = paint(gi, a1)
        x0 = frozenset((hlead, (r0 + i, c0 + side)) for i in range(side))
        x1 = frozenset((tail, (r0 + i, c0 + side + TWO)) for i in range(side))
        x2 = frozenset((vlead, (r0 + side, c0 + j)) for j in range(side))
        x3 = frozenset((tail, (r0 + side + TWO, c0 + j)) for j in range(side))
        gi = paint(gi, x0)
        gi = paint(gi, x1)
        gi = paint(gi, x2)
        gi = paint(gi, x3)
        go = canvas(bg, (gh, gw))
        go = paint(go, a0)
        go = paint(go, a1)
        a2 = shift(a0, (ZERO, subtract(c1, c0)))
        a3 = shift(a0, (subtract(r1, r0), ZERO))
        go = paint(go, a2)
        go = paint(go, a3)
        x4 = connect((r0 - ONE, c0 + side), (r0 - ONE, c1 - ONE))
        go = fill(go, hlead, x4)
        x5 = connect((r1 + side, c0 + side), (r1 + side, c1 - ONE))
        go = fill(go, hlead, x5)
        x6 = connect((r0 + side, c0 - ONE), (r1 - ONE, c0 - ONE))
        go = fill(go, vlead, x6)
        x7 = connect((r0 + side, c1 + side), (r1 - ONE, c1 + side))
        go = fill(go, vlead, x7)
        hcols = horizontal_cycle_34cfa167(gapw, hlead, tail, bg)
        hobj0 = frozenset(
            (value, (r0 + di, c0 + side + dj))
            for di in range(side)
            for dj, value in enumerate(hcols)
        )
        hobj1 = frozenset(
            (value, (r1 + di, c0 + side + dj))
            for di in range(side)
            for dj, value in enumerate(hcols)
        )
        go = paint(go, hobj0)
        go = paint(go, hobj1)
        vrows = vertical_cycle_34cfa167(gaph, vlead, tail, bg)
        vobj0 = frozenset(
            (value, (r0 + side + di, c0 + dj))
            for di, value in enumerate(vrows)
            for dj in range(side)
        )
        vobj1 = frozenset(
            (value, (r0 + side + di, c1 + dj))
            for di, value in enumerate(vrows)
            for dj in range(side)
        )
        go = paint(go, vobj0)
        go = paint(go, vobj1)
        return {"input": gi, "output": go}
