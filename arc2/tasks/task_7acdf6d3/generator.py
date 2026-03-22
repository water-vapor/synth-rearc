from arc2.core import *

from .helpers import row_hole_mask_7acdf6d3
from .verifier import verify_7acdf6d3


BACKGROUND_7ACDF6D3 = SEVEN
TASK_COLORS_7ACDF6D3 = (TWO, NINE)


def _outline_from_widths_7acdf6d3(
    widths,
    close_last,
):
    x0 = set()
    x1 = max(widths)
    x2 = len(widths) - 1
    for x3, x4 in enumerate(widths):
        x5 = (x1 - x4) // 2
        if (x3 == x2 and close_last) or x4 <= TWO:
            x6 = range(x5, x5 + x4)
        else:
            x6 = (x5, x5 + x4 - 1)
        for x7 in x6:
            x0.add((x3, x7))
    return frozenset(x0)


def _recipient_patch_7acdf6d3(
    diff_lb,
    diff_ub,
    banned_counts,
):
    while True:
        x0 = choice(("triangle", "triangle", "cup"))
        if x0 == "triangle":
            x1 = unifint(diff_lb, diff_ub, (THREE, SIX))
            x2 = tuple(range(x1, ZERO, -TWO))
            x3 = F
        else:
            x1 = unifint(diff_lb, diff_ub, (THREE, FIVE))
            x2 = repeat(x1, unifint(diff_lb, diff_ub, (TWO, THREE)))
            x3 = T
        x4 = _outline_from_widths_7acdf6d3(x2, x3)
        x5 = size(row_hole_mask_7acdf6d3(x4))
        if x5 == ZERO:
            continue
        if x5 in banned_counts:
            continue
        return x4, x5


def _donor_patch_7acdf6d3(count):
    if count == ONE:
        return frozenset({ORIGIN})
    x0 = choice(("scatter", "line", "line"))
    if x0 == "line":
        if choice((T, F)):
            return frozenset((x1, ZERO) for x1 in range(count))
        return frozenset((ZERO, x1) for x1 in range(count))
    while True:
        x1 = randint(ONE, min(FOUR, count + ONE))
        x2 = randint(TWO, min(SIX, count + TWO))
        x3 = tuple((x4 * TWO, x5 * TWO) for x4 in range(x1) for x5 in range(x2))
        if len(x3) < count:
            continue
        return frozenset(sample(x3, count))


def _expand8_7acdf6d3(patch):
    x0 = set()
    for x1, x2 in patch:
        for x3 in (-1, ZERO, ONE):
            for x4 in (-1, ZERO, ONE):
                x0.add((x1 + x3, x2 + x4))
    return frozenset(x0)


def _place_patch_7acdf6d3(
    side,
    patch,
    blocked,
):
    x0 = normalize(patch)
    x1 = side - height(x0)
    x2 = side - width(x0)
    x3 = [(x4, x5) for x4 in range(x1 + 1) for x5 in range(x2 + 1)]
    shuffle(x3)
    for x4 in x3:
        x5 = shift(x0, x4)
        if len(intersection(x5, blocked)) == ZERO:
            return x5
    return None


def generate_7acdf6d3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(TASK_COLORS_7ACDF6D3)
        x1 = other(TASK_COLORS_7ACDF6D3, x0)
        x2, x3 = _recipient_patch_7acdf6d3(diff_lb, diff_ub, frozenset())
        x4, x5 = _recipient_patch_7acdf6d3(diff_lb, diff_ub, frozenset({x3}))
        x6 = _donor_patch_7acdf6d3(x3)
        x7 = max(12, add(add(width(x2), width(x4)), add(width(x6), FIVE)))
        x8 = max(12, add(add(height(x2), height(x4)), add(height(x6), FIVE)))
        x9 = max(x7, x8)
        x10 = unifint(diff_lb, diff_ub, (x9, min(18, add(x9, FOUR))))
        x11 = (
            ("target", x2),
            ("distractor", x4),
            ("donor", x6),
        )
        x12 = order(x11, lambda x: -size(last(x)))
        x13 = {}
        x14 = frozenset()
        x15 = T
        for x16, x17 in x12:
            x18 = _place_patch_7acdf6d3(x10, x17, x14)
            if x18 is None:
                x15 = F
                break
            x13[x16] = x18
            x14 = combine(x14, _expand8_7acdf6d3(x18))
        if not x15:
            continue
        x19 = canvas(BACKGROUND_7ACDF6D3, (x10, x10))
        x20 = fill(x19, x0, x13["target"])
        x21 = fill(x20, x0, x13["distractor"])
        x22 = fill(x21, x1, x13["donor"])
        x23 = fill(x21, BACKGROUND_7ACDF6D3, x13["donor"])
        x24 = row_hole_mask_7acdf6d3(x13["target"])
        x25 = fill(x23, x1, x24)
        if verify_7acdf6d3(x22) != x25:
            continue
        return {"input": x22, "output": x25}
