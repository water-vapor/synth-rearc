from synth_rearc.core import *


BLOCKER_COLORS_9DEF23FE = (ONE, THREE, FOUR, EIGHT)


def _side_count_patterns_9def23fe() -> tuple[tuple[int, int, int, int], ...]:
    patterns = []
    for left_count in range(5):
        for right_count in range(5):
            for up_count in range(5):
                for down_count in range(5):
                    row_total = left_count + right_count
                    col_total = up_count + down_count
                    if left_count + right_count + up_count + down_count != 8:
                        continue
                    if not 2 <= row_total <= 6:
                        continue
                    if not 2 <= col_total <= 6:
                        continue
                    patterns.append((left_count, right_count, up_count, down_count))
    return tuple(patterns)


SIDE_PATTERNS_9DEF23FE = _side_count_patterns_9def23fe()


def _extension_patch_9def23fe(
    rows: tuple[int, ...],
    cols: tuple[int, ...],
) -> frozenset[tuple[int, int]]:
    return frozenset((i, j) for i in rows for j in cols)


def _build_output_9def23fe(
    gi: Grid,
    top: int,
    left: int,
    side: int,
    blocked_left_rows: frozenset[int],
    blocked_right_rows: frozenset[int],
    blocked_up_cols: frozenset[int],
    blocked_down_cols: frozenset[int],
) -> Grid:
    rect_rows = tuple(range(top, top + side))
    rect_cols = tuple(range(left, left + side))
    left_cols = tuple(range(left))
    right_cols = tuple(range(left + side, width(gi)))
    up_rows = tuple(range(top))
    down_rows = tuple(range(top + side, height(gi)))
    clear_left_rows = tuple(r for r in rect_rows if r not in blocked_left_rows)
    clear_right_rows = tuple(r for r in rect_rows if r not in blocked_right_rows)
    clear_up_cols = tuple(c for c in rect_cols if c not in blocked_up_cols)
    clear_down_cols = tuple(c for c in rect_cols if c not in blocked_down_cols)
    x0 = _extension_patch_9def23fe(clear_left_rows, left_cols)
    x1 = _extension_patch_9def23fe(clear_right_rows, right_cols)
    x2 = _extension_patch_9def23fe(up_rows, clear_up_cols)
    x3 = _extension_patch_9def23fe(down_rows, clear_down_cols)
    x4 = combine(x0, x1)
    x5 = combine(x2, x3)
    x6 = combine(x4, x5)
    return fill(gi, TWO, x6)


def generate_9def23fe(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (18, 24))
        w = unifint(diff_lb, diff_ub, (15, 26))
        side = unifint(diff_lb, diff_ub, (FIVE, EIGHT))
        if h <= side + TWO or w <= side + TWO:
            continue
        top = randint(ONE, h - side - ONE)
        left = randint(ONE, w - side - ONE)
        left_count, right_count, up_count, down_count = choice(SIDE_PATTERNS_9DEF23FE)
        blocker_color = choice(BLOCKER_COLORS_9DEF23FE)
        rect_rows = tuple(range(top, top + side))
        rect_cols = tuple(range(left, left + side))
        blocked_left_rows = frozenset(sample(rect_rows, left_count))
        blocked_right_rows = frozenset(sample(rect_rows, right_count))
        blocked_up_cols = frozenset(sample(rect_cols, up_count))
        blocked_down_cols = frozenset(sample(rect_cols, down_count))
        rectangle = frozenset((i, j) for i in rect_rows for j in rect_cols)
        blockers = set()
        for i in blocked_left_rows:
            blockers.add((i, randint(ZERO, left - ONE)))
        for i in blocked_right_rows:
            blockers.add((i, randint(left + side, w - ONE)))
        for j in blocked_up_cols:
            blockers.add((randint(ZERO, top - ONE), j))
        for j in blocked_down_cols:
            blockers.add((randint(top + side, h - ONE), j))
        if len(blockers) != 8:
            continue
        gi = canvas(ZERO, (h, w))
        gi = fill(gi, TWO, rectangle)
        gi = fill(gi, blocker_color, blockers)
        go = _build_output_9def23fe(
            gi,
            top,
            left,
            side,
            blocked_left_rows,
            blocked_right_rows,
            blocked_up_cols,
            blocked_down_cols,
        )
        return {"input": gi, "output": go}
