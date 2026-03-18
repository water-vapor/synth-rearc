from arc2.core import *

from .verifier import verify_f8be4b64


ACTIVE_COLORS_F8BE4B64 = remove(THREE, interval(ONE, TEN, ONE))


def _plus_patch_f8be4b64(
    center: IntegerTuple,
) -> Indices:
    x0, x1 = center
    return frozenset(
        {
            (x0, x1),
            (x0 - ONE, x1),
            (x0 + ONE, x1),
            (x0, x1 - ONE),
            (x0, x1 + ONE),
        }
    )


def _reserved_patch_f8be4b64(
    center: IntegerTuple,
) -> Indices:
    x0, x1 = center
    return frozenset(
        (i, j)
        for i in range(x0 - ONE, x0 + TWO)
        for j in range(x1 - ONE, x1 + TWO)
    )


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


def _has_interaction_f8be4b64(
    centers: tuple[IntegerTuple, ...],
) -> Boolean:
    for x0, x1 in enumerate(centers):
        for x2 in centers[x0 + ONE :]:
            if abs(x1[ZERO] - x2[ZERO]) == ONE or abs(x1[ONE] - x2[ONE]) == ONE:
                return True
    return False


def _sample_centers_f8be4b64(
    side: Integer,
    total: Integer,
) -> tuple[IntegerTuple, ...] | None:
    for _ in range(200):
        x0 = tuple()
        x1 = frozenset()
        x2 = set()
        x3 = set()
        while len(x0) < total:
            x4 = []
            x5 = []
            for x6 in range(ONE, side - ONE):
                if x6 in x2:
                    continue
                for x7 in range(ONE, side - ONE):
                    if x7 in x3:
                        continue
                    x8 = _reserved_patch_f8be4b64((x6, x7))
                    if len(intersection(x8, x1)) > ZERO:
                        continue
                    x4.append((x6, x7))
                    if any(abs(x6 - x9) == ONE or abs(x7 - x10) == ONE for x9, x10 in x0):
                        x5.append((x6, x7))
            if len(x4) == ZERO:
                break
            if len(x5) > ZERO and (len(x0) == ONE or choice((T, F))):
                x6 = choice(x5)
            else:
                x6 = choice(x4)
            x0 = x0 + (x6,)
            x1 = combine(x1, _reserved_patch_f8be4b64(x6))
            x2.add(x6[ZERO])
            x3.add(x6[ONE])
        if len(x0) == total:
            return x0
    return None


def _build_input_f8be4b64(
    side: Integer,
    active_centers: tuple[IntegerTuple, ...],
    plain_centers: tuple[IntegerTuple, ...],
    colors: tuple[Integer, ...],
) -> Grid:
    x0 = canvas(ZERO, (side, side))
    for x1, x2 in active_centers + plain_centers:
        x3 = frozenset(
            {
                (x1 - ONE, x2),
                (x1 + ONE, x2),
                (x1, x2 - ONE),
                (x1, x2 + ONE),
            }
        )
        x0 = fill(x0, THREE, x3)
    for x1, x2 in zip(active_centers, colors):
        x0 = fill(x0, x2, frozenset({x1}))
    return x0


def _build_output_f8be4b64(
    I: Grid,
) -> Grid:
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


def generate_f8be4b64(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TEN, 30))
        x1 = min(FIVE, max(TWO, x0 // SIX + TWO))
        x2 = unifint(diff_lb, diff_ub, (ONE, min(FOUR, x1)))
        if x2 == ONE:
            x3 = ONE
        elif x1 > x2:
            x3 = choice((ZERO, ONE))
        else:
            x3 = ZERO
        x4 = add(x2, x3)
        x5 = _sample_centers_f8be4b64(x0, x4)
        if x5 is None:
            continue
        if x3 == ZERO and not _has_interaction_f8be4b64(x5):
            continue
        x6 = tuple(sample(ACTIVE_COLORS_F8BE4B64, x2))
        x7 = x5[:x2]
        x8 = x5[x2:]
        x9 = _build_input_f8be4b64(x0, x7, x8, x6)
        x10 = _build_output_f8be4b64(x9)
        if x9 == x10:
            continue
        if verify_f8be4b64(x9) != x10:
            continue
        return {"input": x9, "output": x10}
