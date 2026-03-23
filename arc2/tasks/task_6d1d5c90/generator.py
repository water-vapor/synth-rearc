from arc2.core import *


BODY_HEIGHT_6D1D5C90 = SIX
BODY_WIDTH_6D1D5C90 = SIX
BODY_COLORS_6D1D5C90 = (ONE, THREE, FOUR, FIVE, EIGHT, NINE)
ROW_ACTIONS_6D1D5C90 = ("copy", "recolor", "reshape", "both", "recolor", "reshape", "fresh")


def _build_row_6d1d5c90(
    cuts: tuple[int, ...],
    colors: tuple[int, ...],
) -> tuple[int, ...]:
    x0 = []
    x1 = (ZERO,) + cuts
    x2 = cuts + (BODY_WIDTH_6D1D5C90,)
    for x3, x4, x5 in zip(x1, x2, colors):
        x0.extend([x5] * (x4 - x3))
    return tuple(x0)


def _available_colors_6d1d5c90(
    left: int | None = None,
    right: int | None = None,
    current: int | None = None,
) -> tuple[int, ...]:
    x0 = tuple(
        x1
        for x1 in BODY_COLORS_6D1D5C90
        if x1 != left and x1 != right and x1 != current
    )
    if len(x0) > ZERO:
        return x0
    return tuple(x1 for x1 in BODY_COLORS_6D1D5C90 if x1 != left and x1 != right)


def _sample_cuts_6d1d5c90(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, ...]:
    x0 = unifint(diff_lb, diff_ub, (TWO, BODY_WIDTH_6D1D5C90))
    x1 = interval(ONE, BODY_WIDTH_6D1D5C90, ONE)
    return tuple(sorted(sample(x1, x0 - ONE)))


def _sample_colors_6d1d5c90(
    num_runs: int,
) -> tuple[int, ...]:
    x0 = []
    for x1 in range(num_runs):
        x2 = x0[x1 - ONE] if x1 > ZERO else None
        x0.append(choice(_available_colors_6d1d5c90(x2)))
    return tuple(x0)


def _resize_colors_6d1d5c90(
    colors: tuple[int, ...],
    target: int,
) -> tuple[int, ...]:
    x0 = list(colors[:target])
    while len(x0) > target:
        del x0[randint(ZERO, len(x0) - ONE)]
    while len(x0) < target:
        x1 = randint(ZERO, len(x0))
        x2 = x0[x1 - ONE] if x1 > ZERO else None
        x3 = x0[x1] if x1 < len(x0) else None
        x0.insert(x1, choice(_available_colors_6d1d5c90(x2, x3)))
    for x1 in range(len(x0)):
        x2 = x0[x1 - ONE] if x1 > ZERO else None
        x3 = x0[x1 + ONE] if x1 + ONE < len(x0) else None
        if x0[x1] == x2 or x0[x1] == x3:
            x0[x1] = choice(_available_colors_6d1d5c90(x2, x3, x0[x1]))
    return tuple(x0)


def _mutate_cuts_6d1d5c90(
    cuts: tuple[int, ...],
) -> tuple[int, ...]:
    x0 = list(cuts)
    x1 = choice(("shift", "shift", "add", "remove"))
    if x1 == "shift":
        x2 = randint(ZERO, len(x0) - ONE)
        x3 = x0[x2 - ONE] + ONE if x2 > ZERO else ONE
        x4 = x0[x2 + ONE] - ONE if x2 + ONE < len(x0) else BODY_WIDTH_6D1D5C90 - ONE
        x5 = tuple(x6 for x6 in (x0[x2] - ONE, x0[x2] + ONE) if x3 <= x6 <= x4 and x6 != x0[x2])
        if len(x5) > ZERO:
            x0[x2] = choice(x5)
    elif x1 == "add" and len(x0) < BODY_WIDTH_6D1D5C90 - ONE:
        x2 = tuple(x3 for x3 in interval(ONE, BODY_WIDTH_6D1D5C90, ONE) if x3 not in x0)
        x0.append(choice(x2))
        x0.sort()
    elif x1 == "remove" and len(x0) > ONE:
        del x0[randint(ZERO, len(x0) - ONE)]
    return tuple(x0)


def _mutate_colors_6d1d5c90(
    colors: tuple[int, ...],
) -> tuple[int, ...]:
    x0 = list(colors)
    x1 = unifint(ZERO, ONE, (ONE, min(TWO, len(x0))))
    x2 = sample(interval(ZERO, len(x0), ONE), x1)
    for x3 in x2:
        x4 = x0[x3 - ONE] if x3 > ZERO else None
        x5 = x0[x3 + ONE] if x3 + ONE < len(x0) else None
        x0[x3] = choice(_available_colors_6d1d5c90(x4, x5, x0[x3]))
    return tuple(x0)


def _count_runs_6d1d5c90(
    row: tuple[int, ...],
) -> int:
    x0 = ONE
    for x1, x2 in zip(row, row[ONE:]):
        if x1 != x2:
            x0 += ONE
    return x0


def _inject_missing_colors_6d1d5c90(
    rows: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    x0 = [list(x1) for x1 in rows]
    x1 = {x2 for x3 in x0 for x2 in x3}
    x2 = tuple(x3 for x3 in BODY_COLORS_6D1D5C90 if x3 not in x1)
    for x3 in x2:
        x4 = randint(ZERO, BODY_HEIGHT_6D1D5C90 - ONE)
        x5 = randint(ZERO, BODY_WIDTH_6D1D5C90 - ONE)
        x0[x4][x5] = x3
        if x5 < BODY_WIDTH_6D1D5C90 - ONE and choice((T, F, F)):
            x0[x4][x5 + ONE] = x3
    return tuple(tuple(x3) for x3 in x0)


def _build_body_6d1d5c90(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, ...], ...]:
    while True:
        x0 = _sample_cuts_6d1d5c90(diff_lb, diff_ub)
        x1 = _sample_colors_6d1d5c90(len(x0) + ONE)
        x2 = []
        for x3 in range(BODY_HEIGHT_6D1D5C90):
            if x3 > ZERO:
                x4 = choice(ROW_ACTIONS_6D1D5C90)
                if x4 in ("reshape", "both"):
                    x0 = _mutate_cuts_6d1d5c90(x0)
                    x1 = _resize_colors_6d1d5c90(x1, len(x0) + ONE)
                if x4 in ("recolor", "both"):
                    x1 = _mutate_colors_6d1d5c90(x1)
                if x4 == "fresh":
                    x0 = _sample_cuts_6d1d5c90(diff_lb, diff_ub)
                    x1 = _sample_colors_6d1d5c90(len(x0) + ONE)
            x2.append(_build_row_6d1d5c90(x0, x1))
        x5 = _inject_missing_colors_6d1d5c90(tuple(x2))
        x6 = tuple(_count_runs_6d1d5c90(x7) for x7 in x5)
        if len(set(x5)) < THREE:
            continue
        if maximum(x6) < FOUR:
            continue
        return x5


def _rotate_up_6d1d5c90(
    rows: tuple[tuple[int, ...], ...],
    amount: int,
) -> tuple[tuple[int, ...], ...]:
    if amount == ZERO:
        return rows
    return rows[amount:] + rows[:amount]


def _prepend_marker_6d1d5c90(
    rows: tuple[tuple[int, ...], ...],
    marker_row: int,
) -> tuple[tuple[int, ...], ...]:
    return tuple(
        ((TWO if x0 == marker_row else SIX),) + x1
        for x0, x1 in enumerate(rows)
    )


def generate_6d1d5c90(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = _build_body_6d1d5c90(diff_lb, diff_ub)
    x1 = randint(ZERO, BODY_HEIGHT_6D1D5C90 - ONE)
    x2 = _rotate_up_6d1d5c90(x0, x1)
    x3 = _prepend_marker_6d1d5c90(x2, x1)
    return {"input": x3, "output": x0}
