from arc2.core import *

from .verifier import verify_342ae2ed


GRID_SIZE_342AE2ED = 16
BACKGROUND_342AE2ED = SEVEN
COLOR_POOL_342AE2ED = (ZERO, ONE, THREE, FOUR, FIVE, SIX, EIGHT, NINE)
SIZE_CHOICES_342AE2ED = (TWO, TWO, TWO, THREE)


def _square_patch_342ae2ed(
    top: Integer,
    left: Integer,
    side: Integer,
) -> Indices:
    return frozenset(
        (top + di, left + dj)
        for di in range(side)
        for dj in range(side)
    )


def _dilate_patch_342ae2ed(
    patch: Patch,
) -> frozenset[IntegerTuple]:
    return frozenset(
        (i + di, j + dj)
        for i, j in toindices(patch)
        for di in (-ONE, ZERO, ONE)
        for dj in (-ONE, ZERO, ONE)
    )


def _sample_pair_342ae2ed(
    side: Integer,
    gap: Integer,
    diagonal: Integer,
) -> tuple[Indices, Indices, Indices]:
    step = gap + side
    limit = GRID_SIZE_342AE2ED - step - side
    if diagonal == ONE:
        top = randint(ZERO, limit)
        left = randint(ZERO, limit)
        x0 = _square_patch_342ae2ed(top, left, side)
        x1 = _square_patch_342ae2ed(top + step, left + step, side)
        x2 = connect(lrcorner(x0), ulcorner(x1))
        return x0, x1, x2
    top = randint(ZERO, limit)
    left = randint(step, GRID_SIZE_342AE2ED - side)
    x0 = _square_patch_342ae2ed(top, left, side)
    x1 = _square_patch_342ae2ed(top + step, left - step, side)
    x2 = connect(llcorner(x0), urcorner(x1))
    return x0, x1, x2


def generate_342ae2ed(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (3, 5))
        x1 = sample(COLOR_POOL_342AE2ED, x0)
        x2 = [choice(SIZE_CHOICES_342AE2ED) for _ in range(x0)]
        if THREE not in x2:
            x2[randint(ZERO, x0 - ONE)] = THREE
        x3 = list(range(x0))
        shuffle(x3)
        x3.sort(key=lambda k: x2[k], reverse=True)
        x4 = set()
        x5 = set()
        x6 = []
        x7 = True
        for x8 in x3:
            x9 = x1[x8]
            x10 = x2[x8]
            x11 = False
            for _ in range(400):
                x12 = unifint(diff_lb, diff_ub, (2, 6))
                x13 = choice((NEG_ONE, ONE))
                x14, x15, x16 = _sample_pair_342ae2ed(x10, x12, x13)
                x17 = set(x14)
                x18 = set(x15)
                x19 = set(x16)
                if x17 & x4 or x18 & x4:
                    continue
                if (x17 | x18) & x5:
                    continue
                if (x19 - x17 - x18) & x5:
                    continue
                x6.append((x9, x14, x15, x16))
                x4 |= _dilate_patch_342ae2ed(x14)
                x4 |= _dilate_patch_342ae2ed(x15)
                x5 |= x17 | x18 | x19
                x11 = True
                break
            if not x11:
                x7 = False
                break
        if not x7:
            continue
        x20 = canvas(BACKGROUND_342AE2ED, (GRID_SIZE_342AE2ED, GRID_SIZE_342AE2ED))
        x21 = x20
        for x22, x23, x24, x25 in x6:
            x26 = combine(x23, x24)
            x20 = fill(x20, x22, x26)
            x21 = fill(x21, x22, x26)
            x21 = fill(x21, x22, x25)
        if verify_342ae2ed(x20) != x21:
            continue
        return {"input": x20, "output": x21}
