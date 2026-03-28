from synth_rearc.core import *


def _render_output_332202d5(
    column: int,
    marker_rows: Tuple[int, ...],
    marker_colors: Tuple[int, ...],
) -> Grid:
    x0 = {x1: x2 for x1, x2 in zip(marker_rows, marker_colors)}
    x1 = [[ONE for _ in range(16)] for _ in range(16)]
    for x2 in range(16):
        if x2 in x0:
            x1[x2][column] = EIGHT
            continue
        x3 = tuple(abs(x2 - x4) for x4 in marker_rows)
        x4 = min(x3)
        x5 = {x0[x6] for x6, x7 in zip(marker_rows, x3) if x7 == x4}
        if len(x5) == ONE:
            x6 = next(iter(x5))
            x1[x2] = [x6 for _ in range(16)]
            x1[x2][column] = ONE
    x7 = tuple(tuple(row) for row in x1)
    return x7


def generate_332202d5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = remove(EIGHT, remove(SEVEN, remove(ONE, interval(ZERO, TEN, ONE))))
    x1 = interval(TWO, 15, ONE)
    while True:
        x2 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x3 = tuple(sorted(sample(x1, x2)))
        x4 = tuple(b - a for a, b in zip(x3, x3[ONE:]))
        if any(x5 < THREE for x5 in x4):
            continue
        if x2 == TWO:
            x5 = TWO
        elif x2 == THREE:
            x5 = choice((TWO, THREE))
        else:
            x5 = THREE
        x6 = sample(x0, x5)
        x7 = list(x6)
        while len(x7) < x2:
            x7.append(choice(x6))
        shuffle(x7)
        x8 = tuple(x7)
        if len(set(x8)) != x5:
            continue
        x9 = unifint(diff_lb, diff_ub, (TWO, 13))
        x10 = canvas(SEVEN, (16, 16))
        x11 = frozenset((x12, x9) for x12 in range(16))
        x12 = fill(x10, EIGHT, x11)
        for x13, x14 in zip(x3, x8):
            x15 = frozenset((x13, x16) for x16 in range(16))
            x12 = fill(x12, x14, x15)
            x12 = fill(x12, ONE, frozenset({(x13, x9)}))
        x13 = _render_output_332202d5(x9, x3, x8)
        if x12 == x13:
            continue
        return {"input": x12, "output": x13}
