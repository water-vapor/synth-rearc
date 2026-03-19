from arc2.core import *

from .verifier import verify_ea959feb


HEIGHT_EA959FEB = 22
WIDTH_EA959FEB = 25

FAMILIES_EA959FEB = (
    (SIX, (ZERO, ONE, ZERO, TWO, THREE, TWO)),
    (SEVEN, (ZERO, ONE, ONE, ZERO, TWO, THREE, TWO)),
    (EIGHT, (ZERO, ONE, TWO, ONE)),
    (NINE, (ZERO, ONE, TWO, TWO, ONE, ZERO, THREE, ONE, THREE)),
)


def _normalize_color_ea959feb(
    value: Integer,
    row_index: Integer,
    period: Integer,
) -> Integer:
    return ((value - row_index - ONE) % period) + ONE


def _horizontal_period_ea959feb(
    sequence: tuple[Integer, ...],
) -> Integer:
    x0 = len(sequence)
    for x1 in range(ONE, x0 + ONE):
        if all(sequence[x2] == sequence[x2 % x1] for x2 in range(x0)):
            return x1
    return x0


def _shift_color_ea959feb(
    value: Integer,
    delta: Integer,
    period: Integer,
) -> Integer:
    return ((value - delta - ONE) % period) + ONE


def _make_motif_ea959feb(
    period: Integer,
    template: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    while True:
        x0 = randint(ONE, period)
        if period == EIGHT:
            x1 = tuple(sorted(sample(interval(ONE, period, ONE), TWO)))
            x2 = (ZERO, x1[ZERO], x1[ONE])
        elif period == NINE:
            x1 = tuple(sorted(sample(interval(ONE, period, ONE), THREE)))
            x2 = (ZERO, x1[ONE], x1[TWO], x1[ZERO])
        else:
            x1 = tuple(sorted(sample(interval(ONE, period, ONE), THREE)))
            x2 = (ZERO, x1[ZERO], x1[ONE], x1[TWO])
        x3 = tuple(_shift_color_ea959feb(x0, x4, period) for x4 in x2)
        x4 = tuple(x3[x5] for x5 in template)
        if _horizontal_period_ea959feb(x4) == len(template):
            return x4


def _build_output_ea959feb(
    period: Integer,
    motif: tuple[Integer, ...],
) -> Grid:
    x0 = len(motif)
    return tuple(
        tuple((((motif[x1 % x0] + x2 - ONE) % period) + ONE) for x1 in range(WIDTH_EA959FEB))
        for x2 in range(HEIGHT_EA959FEB)
    )


def _rect_patch_ea959feb(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> frozenset[IntegerTuple]:
    return frozenset(
        (i, j)
        for i in range(top, top + height_value)
        for j in range(left, left + width_value)
    )


def _halo_patch_ea959feb(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> frozenset[IntegerTuple]:
    return frozenset(
        (i, j)
        for i in range(max(ZERO, top - ONE), min(HEIGHT_EA959FEB, top + height_value + ONE))
        for j in range(max(ZERO, left - ONE), min(WIDTH_EA959FEB, left + width_value + ONE))
    )


def _apply_corruption_ea959feb(
    output: Grid,
    diff_lb: float,
    diff_ub: float,
) -> Grid | None:
    x0 = unifint(diff_lb, diff_ub, (THREE, FIVE))
    x1: list[frozenset[IntegerTuple]] = []
    x2: set[IntegerTuple] = set()
    x3: set[IntegerTuple] = set()
    x4 = [ZERO for _ in range(WIDTH_EA959FEB)]
    x5 = 0
    while len(x1) < x0 and x5 < 400:
        x5 += ONE
        if choice((T, F)):
            x6 = randint(TWO, FOUR)
            x7 = randint(THREE, FIVE)
        else:
            x6 = randint(THREE, SEVEN)
            x7 = randint(TWO, THREE)
        x8 = randint(ZERO, HEIGHT_EA959FEB - x6)
        x9 = randint(ZERO, WIDTH_EA959FEB - x7)
        x10 = _rect_patch_ea959feb(x8, x9, x6, x7)
        x11 = _halo_patch_ea959feb(x8, x9, x6, x7)
        if x10 & x2:
            continue
        if x11 & x3:
            continue
        if any(x4[x12] + x6 > TEN for x12 in range(x9, x9 + x7)):
            continue
        x1.append(x10)
        x2 |= x10
        x3 |= x11
        for x12 in range(x9, x9 + x7):
            x4[x12] += x6
    if len(x1) != x0:
        return None
    x6 = output
    for x7 in x1:
        x6 = fill(x6, ONE, x7)
    x7 = sum(
        ONE
        for i in range(HEIGHT_EA959FEB)
        for j in range(WIDTH_EA959FEB)
        if x6[i][j] != output[i][j]
    )
    if x7 < 24:
        return None
    x8 = max(max(row) for row in x6)
    x8 = tuple(
        tuple(_normalize_color_ea959feb(x6[i][j], i, x8) for i in range(HEIGHT_EA959FEB))
        for j in range(WIDTH_EA959FEB)
    )
    if any(TWO * x9.count(mostcommon(x9)) <= len(x9) for x9 in x8):
        return None
    return x6


def generate_ea959feb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(FAMILIES_EA959FEB)
        x1 = x0[ZERO]
        x2 = x0[ONE]
        x3 = _make_motif_ea959feb(x1, x2)
        x4 = _build_output_ea959feb(x1, x3)
        x5 = _apply_corruption_ea959feb(x4, diff_lb, diff_ub)
        if x5 is None:
            continue
        if verify_ea959feb(x5) != x4:
            continue
        return {"input": x5, "output": x4}
