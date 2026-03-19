from arc2.core import *


def generate_e3fe1151(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(SEVEN, interval(ZERO, TEN, ONE))
    x1 = (
        ORIGIN,
        astuple(ZERO, THREE),
        astuple(THREE, ZERO),
        astuple(THREE, THREE),
    )
    while True:
        x2 = choice((THREE, FOUR, FOUR, FOUR))
        x3 = sample(x0, x2)
        if x2 == FOUR:
            x4 = list(x3)
        else:
            x5 = choice(x3)
            x6 = list(remove(x5, x3))
            x4 = [x5, x5] + x6
        x7 = {x8: x4.count(x8) for x8 in x3}
        x8 = []
        x9 = []
        for x10 in x1:
            x11 = list(x4)
            shuffle(x11)
            x12 = randint(ZERO, THREE)
            x13 = (
                x10,
                add(x10, RIGHT),
                add(x10, DOWN),
                add(x10, UNITY),
            )
            x8.append((x13, x11, x12))
            x9.append(x11[x12])
        if len(set(x9)) == ONE:
            continue
        if any(multiply(x7[x10], FOUR) == x9.count(x10) for x10 in x3):
            continue
        if len({tuple(x10) for _, x10, _ in x8}) == ONE:
            continue
        gi = canvas(SEVEN, (FIVE, FIVE))
        go = canvas(SEVEN, (FIVE, FIVE))
        for x10, x11, x12 in x8:
            for x13, x14 in enumerate(x10):
                go = fill(go, x11[x13], {x14})
                if x13 != x12:
                    gi = fill(gi, x11[x13], {x14})
        if remove(SEVEN, palette(gi)) != frozenset(x3):
            continue
        return {"input": gi, "output": go}
