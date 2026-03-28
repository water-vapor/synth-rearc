from arc2.core import *


LATIN_DIGITS_4CD1B7B2 = interval(ONE, FIVE, ONE)


def _candidates_4cd1b7b2(
    grid: Grid,
    loc: IntegerTuple,
) -> tuple[int, ...]:
    x0, x1 = loc
    x2 = remove(ZERO, frozenset(grid[x0]))
    x3 = remove(ZERO, frozenset(x4[x1] for x4 in grid))
    x4 = difference(LATIN_DIGITS_4CD1B7B2, x2)
    x5 = difference(x4, x3)
    return tuple(x5)


def verify_4cd1b7b2(
    I: Grid,
) -> Grid:
    def _solve(
        x0: Grid,
    ) -> Grid | None:
        x1 = x0
        while True:
            x2 = ofcolor(x1, ZERO)
            if len(x2) == ZERO:
                return x1
            x3 = []
            x4 = F
            for x5 in x2:
                x6 = _candidates_4cd1b7b2(x1, x5)
                x7 = len(x6)
                if x7 == ZERO:
                    return None
                x3.append((x7, x5, x6))
                x4 = either(x4, equality(x7, ONE))
            if flip(x4):
                break
            x3.sort(key=lambda x5: (x5[ZERO], x5[ONE][ZERO], x5[ONE][ONE]))
            for _, x5, x6 in x3:
                if len(x6) != ONE:
                    continue
                x1 = fill(x1, x6[ZERO], initset(x5))
        x8 = min(x3, key=lambda x5: (x5[ZERO], x5[ONE][ZERO], x5[ONE][ONE]))
        _, x9, x10 = x8
        for x11 in x10:
            x12 = fill(x1, x11, initset(x9))
            x13 = _solve(x12)
            if x13 is not None:
                return x13
        return None

    x0 = _solve(I)
    if x0 is None:
        raise ValueError("4cd1b7b2 expected a solvable Latin-square completion")
    return x0
