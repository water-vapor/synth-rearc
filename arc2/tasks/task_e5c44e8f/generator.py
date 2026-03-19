from arc2.core import *

from .helpers import spiral_path_e5c44e8f


ANCHOR_ROWS_E5C44E8F = (FOUR, FOUR, FIVE, FIVE, FIVE, SIX)
ANCHOR_COLS_E5C44E8F = (FOUR, FIVE, FIVE, SIX, SIX)


def _separated_reds_e5c44e8f(
    candidates: tuple[IntegerTuple, ...],
    fixed: tuple[IntegerTuple, ...],
    target: Integer,
) -> tuple[IntegerTuple, ...]:
    chosen = list(fixed)
    shuffled = list(candidates)
    shuffle(shuffled)
    for cell in shuffled:
        if len(chosen) >= target:
            break
        if any(max(abs(cell[0] - i), abs(cell[1] - j)) <= ONE for i, j in chosen):
            continue
        chosen.append(cell)
    return tuple(chosen)


def generate_e5c44e8f(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = (11, 11)
        x1 = astuple(choice(ANCHOR_ROWS_E5C44E8F), choice(ANCHOR_COLS_E5C44E8F))
        x2 = spiral_path_e5c44e8f(x1, x0)
        x3 = choice((T, T, T, F))
        x4 = tuple()
        x5 = frozenset({x1})
        if x3:
            x6 = len(x2)
            x7 = min(FIVE, x6 - ONE)
            x8 = unifint(diff_lb, diff_ub, (x7, x6 - ONE))
            x9 = x2[x8]
            x4 = (x9,)
            x5 = frozenset((x1,)) | frozenset(x2[:x8])
            x10 = unifint(diff_lb, diff_ub, (THREE, EIGHT))
        else:
            x10 = unifint(diff_lb, diff_ub, (ZERO, THREE))
        x11 = tuple(
            (i, j)
            for i in range(11)
            for j in range(11)
            if (i, j) not in x5 and (i, j) not in x4 and not contained((i, j), x2)
        )
        x12 = add(len(x4), x10)
        x13 = _separated_reds_e5c44e8f(x11, x4, x12)
        if len(x13) != x12:
            continue
        x14 = canvas(ZERO, x0)
        x15 = fill(x14, THREE, initset(x1))
        x16 = fill(x15, TWO, x13)
        x17 = x16
        x18 = frozenset(x13)
        for x19 in x2:
            if contained(x19, x18):
                break
            x17 = fill(x17, THREE, initset(x19))
        if colorcount(x16, TWO) == ZERO and colorcount(x17, THREE) < 30:
            continue
        if colorcount(x16, TWO) > ZERO and colorcount(x17, THREE) < SIX:
            continue
        return {"input": x16, "output": x17}
