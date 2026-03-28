from synth_rearc.core import *

from .verifier import verify_8fbca751


RECT_HEIGHT_8FBCA751 = FOUR
DOUBLE_WIDTH_CHOICES_8FBCA751 = (
    (FOUR, FOUR),
    (FOUR, FOUR),
    (FOUR, EIGHT),
    (EIGHT, FOUR),
)
SINGLE_HEIGHT_CHOICES_8FBCA751 = (SEVEN, EIGHT, NINE)
SINGLE_WIDTH_CHOICES_8FBCA751 = (FOUR, FOUR, EIGHT)


def _rect_patch_8fbca751(
    top: Integer,
    left: Integer,
    width_value: Integer,
) -> Indices:
    x0 = interval(top, top + RECT_HEIGHT_8FBCA751, ONE)
    x1 = interval(left, left + width_value, ONE)
    return product(x0, x1)


def _touches_all_sides_8fbca751(
    patch: Patch,
    width_value: Integer,
) -> Boolean:
    return (
        uppermost(patch) == ZERO
        and lowermost(patch) == RECT_HEIGHT_8FBCA751 - ONE
        and leftmost(patch) == ZERO
        and rightmost(patch) == width_value - ONE
    )


def _is_connected_8fbca751(
    patch: Patch,
    width_value: Integer,
) -> Boolean:
    x0 = canvas(ZERO, (RECT_HEIGHT_8FBCA751, width_value))
    x1 = fill(x0, EIGHT, patch)
    x2 = objects(x1, T, F, T)
    return size(x2) == ONE


def _has_full_row_or_col_8fbca751(
    patch: Patch,
    width_value: Integer,
) -> Boolean:
    x0 = toindices(patch)
    for i in range(RECT_HEIGHT_8FBCA751):
        if all((i, j) in x0 for j in range(width_value)):
            return True
    for j in range(width_value):
        if all((i, j) in x0 for i in range(RECT_HEIGHT_8FBCA751)):
            return True
    return False


def _augment_patch_8fbca751(
    patch: Patch,
    width_value: Integer,
) -> Indices:
    x0 = set(toindices(patch))
    x1 = list(_rect_patch_8fbca751(ZERO, ZERO, width_value) - x0)
    x2 = tuple(x0)
    x3 = choice((ZERO, ONE, ONE, TWO))
    shuffle(x1)
    for cell in x1:
        if x3 == ZERO:
            break
        if any(cell in dneighbors(loc) for loc in x0):
            continue
        if not any(cell[0] == i or cell[1] == j for i, j in x2):
            continue
        x0.add(cell)
        x3 -= ONE
    return frozenset(x0)


def _normalized_patch_8fbca751(
    diff_lb: float,
    diff_ub: float,
    width_value: Integer,
) -> Indices:
    x0 = _rect_patch_8fbca751(ZERO, ZERO, width_value)
    x1 = size(x0)
    while True:
        if choice((ZERO, ONE)) == ZERO:
            x2 = randint(ZERO, RECT_HEIGHT_8FBCA751 - ONE)
            x3 = {(x2, j) for j in range(width_value)}
            if x2 != ZERO:
                x3.add((ZERO, randint(ZERO, width_value - ONE)))
            if x2 != RECT_HEIGHT_8FBCA751 - ONE:
                x3.add((RECT_HEIGHT_8FBCA751 - ONE, randint(ZERO, width_value - ONE)))
        else:
            x2 = randint(ZERO, width_value - ONE)
            x3 = {(i, x2) for i in range(RECT_HEIGHT_8FBCA751)}
            if x2 != ZERO:
                x3.add((randint(ZERO, RECT_HEIGHT_8FBCA751 - ONE), ZERO))
            if x2 != width_value - ONE:
                x3.add((randint(ZERO, RECT_HEIGHT_8FBCA751 - ONE), width_value - ONE))
        x4 = frozenset(x3)
        x5 = max(size(x4) + ONE, (x1 * 7 + 15) // 16)
        x6 = min(x1 - ONE, (x1 * THREE) // FOUR)
        if x5 > x6:
            x5 = x6
        x7 = unifint(diff_lb, diff_ub, (x5, x6))
        x8 = set(x0)
        for _ in range(EIGHT):
            x9 = list(x8 - set(x4))
            shuffle(x9)
            x10 = False
            for cell in x9:
                if len(x8) <= x7:
                    break
                candidate = frozenset(x8 - {cell})
                if not _touches_all_sides_8fbca751(candidate, width_value):
                    continue
                if not _is_connected_8fbca751(candidate, width_value):
                    continue
                x8 = set(candidate)
                x10 = True
            if len(x8) <= x7 or not x10:
                break
        x11 = frozenset(x8)
        if size(x11) == x1:
            continue
        if x1 - size(x11) < TWO:
            continue
        if not _touches_all_sides_8fbca751(x11, width_value):
            continue
        if not _is_connected_8fbca751(x11, width_value):
            continue
        if not _has_full_row_or_col_8fbca751(x11, width_value):
            continue
        return _augment_patch_8fbca751(x11, width_value)


def _single_layout_8fbca751() -> tuple[IntegerTuple, tuple[tuple[int, int, int], ...]]:
    x0 = choice(SINGLE_WIDTH_CHOICES_8FBCA751)
    x1 = choice(SINGLE_HEIGHT_CHOICES_8FBCA751)
    if x0 == FOUR:
        x2 = choice((SEVEN, EIGHT, NINE))
    else:
        x2 = choice((10, 11, 12))
    x3 = randint(ONE, x1 - RECT_HEIGHT_8FBCA751 - ONE)
    x4 = randint(ONE, x2 - x0 - ONE)
    return (astuple(x1, x2), ((x3, x4, x0),))


def _double_layout_8fbca751() -> tuple[IntegerTuple, tuple[tuple[int, int, int], ...]]:
    x0 = choice(DOUBLE_WIDTH_CHOICES_8FBCA751)
    x1, x2 = x0
    x3 = 12 if x0 != (FOUR, FOUR) else choice((EIGHT, NINE, TEN, 11, 12))
    while True:
        x4 = randint(ZERO, x3 - x1)
        x5 = randint(ZERO, x3 - x2)
        if x4 + x1 <= x5 or x5 + x2 <= x4:
            return (astuple(EIGHT, x3), ((ZERO, x4, x1), (FOUR, x5, x2)))


def generate_8fbca751(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        if choice((ONE, TWO, TWO, TWO)) == ONE:
            x0, x1 = _single_layout_8fbca751()
        else:
            x0, x1 = _double_layout_8fbca751()
        gi = canvas(ZERO, x0)
        go = canvas(ZERO, x0)
        for top, left, width_value in x1:
            x2 = _normalized_patch_8fbca751(diff_lb, diff_ub, width_value)
            x3 = shift(x2, (top, left))
            x4 = _rect_patch_8fbca751(top, left, width_value)
            gi = fill(gi, EIGHT, x3)
            go = fill(go, TWO, x4)
            go = fill(go, EIGHT, x3)
        if gi == go:
            continue
        if verify_8fbca751(gi) != go:
            continue
        return {"input": gi, "output": go}
