from arc2.core import *


def _plus_centers_f8be4b64(
    I: Grid,
) -> tuple[tuple[Integer, Integer, Integer], ...]:
    x0, x1 = shape(I)
    return tuple(
        (i, j, I[i][j])
        for i in range(ONE, x0 - ONE)
        for j in range(ONE, x1 - ONE)
        if (
            I[i - ONE][j] == THREE
            and I[i + ONE][j] == THREE
            and I[i][j - ONE] == THREE
            and I[i][j + ONE] == THREE
        )
    )


def _horizontal_patch_f8be4b64(
    I: Grid,
    center: IntegerTuple,
    plain_cols: frozenset[Integer],
) -> Indices:
    x0 = width(I)
    x1, x2 = center
    x3 = {(x1, x2)}
    for x4 in (NEG_ONE, ONE):
        x5 = x2 + x4
        x6 = True
        while ZERO <= x5 < x0:
            x7 = I[x1][x5]
            if x7 == THREE:
                if x6:
                    x6 = False
                    x5 += x4
                    continue
                break
            if x5 not in plain_cols:
                x3.add((x1, x5))
            x6 = False
            x5 += x4
    return frozenset(x3)


def _vertical_patch_f8be4b64(
    I: Grid,
    center: IntegerTuple,
) -> Indices:
    x0 = height(I)
    x1, x2 = center
    x3 = {(x1, x2)}
    for x4 in (NEG_ONE, ONE):
        x5 = x1 + x4
        x6 = True
        while ZERO <= x5 < x0:
            x7 = I[x5][x2]
            if x7 == THREE:
                if x6:
                    x6 = False
                    x5 += x4
                    continue
                break
            x3.add((x5, x2))
            x6 = False
            x5 += x4
    return frozenset(x3)


def verify_f8be4b64(I: Grid) -> Grid:
    x0 = _plus_centers_f8be4b64(I)
    x1 = frozenset(x4 for _, x4, x5 in x0 if x5 in (ZERO, THREE))
    x2 = tuple((x3, x4, x5) for x3, x4, x5 in x0 if x5 not in (ZERO, THREE))
    x3 = I
    for x4, x5, x6 in x2:
        x7 = _horizontal_patch_f8be4b64(I, (x4, x5), x1)
        x3 = fill(x3, x6, x7)
    for x4, x5, x6 in x2:
        x7 = _vertical_patch_f8be4b64(I, (x4, x5))
        x3 = fill(x3, x6, x7)
    return x3
