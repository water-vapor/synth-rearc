from synth_rearc.core import *


_DIRECTION_STEPS_1A244AFD = (
    ((NEG_ONE, ZERO), (ZERO, NEG_ONE)),
    ((ONE, ZERO), (ZERO, ONE)),
    ((NEG_ONE, ZERO), (ZERO, NEG_ONE)),
    ((ONE, ZERO), (ZERO, ONE)),
    ((ZERO, ONE), (NEG_ONE, ZERO)),
    ((ZERO, NEG_ONE), (ONE, ZERO)),
)


def _in_bounds_1a244afd(loc: tuple[int, int], dim: int) -> bool:
    return ZERO <= loc[0] < dim and ZERO <= loc[1] < dim


def _candidate_specs_1a244afd(
    dim: int,
    used_rows: set[int],
    used_cols: set[int],
    reserved: set[tuple[int, int]],
    want_oob: bool,
) -> list[tuple[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    x0 = [i for i in range(dim) if i not in used_rows]
    x1 = [j for j in range(dim) if j not in used_cols]
    x2 = list(_DIRECTION_STEPS_1A244AFD)
    shuffle(x2)
    x3 = list(range(ONE, dim))
    shuffle(x3)
    x4 = []
    for x5, x6 in x2:
        for x7 in x3:
            x8 = multiply(x5, x7)
            x9 = multiply(x6, x7)
            for x10 in x0:
                for x11 in x1:
                    x12 = (x10, x11)
                    x13 = add(x12, x8)
                    x14 = add(x12, x9)
                    if flip(_in_bounds_1a244afd(x13, dim)):
                        continue
                    x15 = _in_bounds_1a244afd(x14, dim)
                    if x15 != (not want_oob):
                        continue
                    if x12 in reserved or x13 in reserved:
                        continue
                    if x15 and x14 in reserved:
                        continue
                    if x13[0] == x12[0]:
                        if x13[1] in used_cols:
                            continue
                    else:
                        if x13[0] in used_rows:
                            continue
                    x4.append((x12, x13, x14))
    return x4


def generate_1a244afd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (EIGHT, 16))
        x1 = min(SEVEN, max(THREE, x0 // TWO - ONE))
        x2 = unifint(diff_lb, diff_ub, (TWO, x1))
        x3 = randint(ZERO, min(TWO, x2 // THREE))
        x4 = [T for _ in range(x3)] + [F for _ in range(x2 - x3)]
        shuffle(x4)
        x5 = set()
        x6 = set()
        x7 = set()
        x8 = []
        x9 = T
        for x10 in x4:
            x11 = _candidate_specs_1a244afd(x0, x5, x6, x7, x10)
            if len(x11) == ZERO:
                x9 = F
                break
            x12, x13, x14 = choice(x11)
            x8.append((x12, x13, x14))
            x5.add(x12[0])
            x6.add(x12[1])
            if x13[0] == x12[0]:
                x6.add(x13[1])
            else:
                x5.add(x13[0])
            x7.add(x12)
            x7.add(x13)
            if _in_bounds_1a244afd(x14, x0):
                x7.add(x14)
        if flip(x9):
            continue
        x15 = frozenset(x16[0] for x16 in x8)
        x17 = frozenset(x16[1] for x16 in x8)
        x18 = frozenset(x16[2] for x16 in x8)
        x19 = canvas(EIGHT, (x0, x0))
        x20 = fill(x19, ONE, x15)
        x21 = fill(x20, SIX, x17)
        x22 = underfill(x20, SEVEN, x18)
        if x21 == x22:
            continue
        return {"input": x21, "output": x22}
