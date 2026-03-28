from arc2.core import *


GRID_SHAPE_4E469F39 = (TEN, TEN)
FRAME_WIDTH_4E469F39 = FOUR
FRAME_HEIGHTS_4E469F39 = (THREE, FOUR, FIVE)
NFRAMES_OPTIONS_4E469F39 = (ONE, ONE, TWO)


def _frame_patch_4e469f39(
    top: Integer,
    left: Integer,
    height_: Integer,
    gap_offset: Integer,
) -> Indices:
    x0 = frozenset({
        (top, left),
        (top + height_ - ONE, left + FRAME_WIDTH_4E469F39 - ONE),
    })
    x1 = box(x0)
    x2 = initset((top, left + gap_offset))
    x3 = difference(x1, x2)
    return x3


def _line_patch_4e469f39(
    top: Integer,
    gap_col: Integer,
    gap_offset: Integer,
) -> Indices:
    x0 = subtract(top, ONE)
    if equality(gap_offset, ONE):
        x1 = frozenset((x0, x2) for x2 in range(gap_col, GRID_SHAPE_4E469F39[ONE]))
    else:
        x1 = frozenset((x0, x2) for x2 in range(gap_col + ONE))
    return x1


def _candidate_specs_4e469f39() -> tuple[tuple[Indices, Indices, Indices, Integer, Integer], ...]:
    x0 = []
    for x1 in FRAME_HEIGHTS_4E469F39:
        for x2 in range(ONE, GRID_SHAPE_4E469F39[ZERO] - x1 + ONE):
            for x3 in range(GRID_SHAPE_4E469F39[ONE] - FRAME_WIDTH_4E469F39 + ONE):
                for x4 in (ONE, TWO):
                    x5 = _frame_patch_4e469f39(x2, x3, x1, x4)
                    x6 = x3 + x4
                    x7 = _line_patch_4e469f39(x2, x6, x4)
                    x8 = combine(delta(x5), x7)
                    x9 = combine(combine(x5, x8), outbox(x5))
                    x10 = subtract(uppermost(x5), ONE)
                    x11 = lowermost(x5)
                    x0.append((x5, x8, x9, x10, x11))
    return tuple(x0)


CANDIDATE_SPECS_4E469F39 = _candidate_specs_4e469f39()


def generate_4e469f39(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(NFRAMES_OPTIONS_4E469F39)
        x1 = list(CANDIDATE_SPECS_4E469F39)
        shuffle(x1)
        x2 = []
        x3 = frozenset()
        for x4 in x1:
            x5, x6, x7, x8, x9 = x4
            x10 = combine(x5, x6)
            if size(intersection(x10, x3)) != ZERO:
                continue
            if any(equality(uppermost(x5), uppermost(x11[ZERO])) for x11 in x2):
                continue
            if any(not (x9 < x11[THREE] or x11[FOUR] < x8) for x11 in x2):
                continue
            x2.append(x4)
            x3 = combine(x3, x7)
            if len(x2) == x0:
                break
        if len(x2) != x0:
            continue
        gi = canvas(ZERO, GRID_SHAPE_4E469F39)
        go = gi
        for x4, x5, _, _, _ in x2:
            gi = fill(gi, FIVE, x4)
            go = fill(go, FIVE, x4)
            go = fill(go, TWO, x5)
        x6 = colorfilter(objects(gi, T, F, T), FIVE)
        if size(x6) != x0:
            continue
        return {"input": gi, "output": go}
