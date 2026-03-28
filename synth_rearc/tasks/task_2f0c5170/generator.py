from synth_rearc.core import *


ROW_LAYOUTS_2F0C5170 = (
    (ONE, ONE),
    (ONE, TWO),
    (TWO, ONE),
)


def _window_patch_2f0c5170(
    loc: tuple[int, int],
    dims: tuple[int, int],
) -> Indices:
    x0 = asindices(canvas(ZERO, dims))
    x1 = shift(x0, loc)
    return x1


def _pattern_patch_2f0c5170() -> frozenset[tuple[int, int]]:
    while True:
        top_layers, bottom_layers = choice(ROW_LAYOUTS_2F0C5170)
        center_left = randint(ONE, TWO)
        center_right = randint(ONE, TWO)
        rows = {ZERO: (center_left, center_right)}
        prev_left, prev_right = center_left, center_right
        for k in range(ONE, top_layers + ONE):
            left = max(ZERO, prev_left + choice((-ONE, ZERO)))
            right = max(ZERO, prev_right + choice((-ONE, ZERO)))
            if left + right == ZERO:
                if choice((T, F)):
                    left = ONE
                else:
                    right = ONE
            rows[-k] = (left, right)
            prev_left, prev_right = left, right
        prev_left, prev_right = center_left, center_right
        for k in range(ONE, bottom_layers + ONE):
            left = max(ZERO, prev_left + choice((-ONE, ZERO, ONE)))
            right = max(ZERO, prev_right + choice((-ONE, ZERO, ONE)))
            left = min(left, TWO)
            right = min(right, TWO)
            if left + right == ZERO:
                if choice((T, F)):
                    left = ONE
                else:
                    right = ONE
            rows[k] = (left, right)
            prev_left, prev_right = left, right
        split_candidates = tuple(
            row
            for row, (left, right) in rows.items()
            if row != ZERO and left > ZERO and right > ZERO
        )
        split_row = choice(split_candidates) if split_candidates and choice((T, F)) else None
        cells = {(ZERO, ZERO)}
        for row, (left, right) in rows.items():
            if row == split_row:
                for col in range(-left, ZERO):
                    cells.add((row, col))
                for col in range(ONE, right + ONE):
                    cells.add((row, col))
            else:
                for col in range(-left, right + ONE):
                    cells.add((row, col))
        if len(cells) >= SIX:
            patch = frozenset(cells)
            if choice((T, F)):
                patch = frozenset((i, -j) for i, j in patch)
            if choice((T, F)):
                patch = frozenset((-i, j) for i, j in patch)
            return patch


def _colored_pattern_2f0c5170(
    patch: frozenset[tuple[int, int]],
    anchor_color: int,
    anchor: tuple[int, int],
) -> Object:
    ai, aj = anchor
    cells = set()
    for di, dj in patch:
        value = anchor_color if (di, dj) == ORIGIN else FOUR
        cells.add((value, (ai + di, aj + dj)))
    return frozenset(cells)


def generate_2f0c5170(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        anchor_color = choice((ONE, TWO, THREE))
        patch = _pattern_patch_2f0c5170()
        rows = tuple(i for i, _ in patch)
        cols = tuple(j for _, j in patch)
        top_extent = -min(rows)
        bottom_extent = max(rows)
        left_extent = -min(cols)
        right_extent = max(cols)
        pattern_h = top_extent + bottom_extent + ONE
        pattern_w = left_extent + right_extent + ONE

        src_h_lb = max(FOUR, pattern_h)
        src_w_lb = max(FIVE, pattern_w)
        src_h_ub = min(NINE, pattern_h + TWO)
        src_w_ub = min(NINE, pattern_w + TWO)
        tgt_h_lb = max(FIVE, pattern_h)
        tgt_w_lb = max(FIVE, pattern_w)
        tgt_h_ub = NINE
        tgt_w_ub = NINE
        if src_h_lb > src_h_ub or src_w_lb > src_w_ub:
            continue
        source_h = unifint(diff_lb, diff_ub, (src_h_lb, src_h_ub))
        source_w = unifint(diff_lb, diff_ub, (src_w_lb, src_w_ub))
        target_h = unifint(diff_lb, diff_ub, (tgt_h_lb, tgt_h_ub))
        target_w = unifint(diff_lb, diff_ub, (tgt_w_lb, tgt_w_ub))

        source_anchor = (
            randint(top_extent, source_h - ONE - bottom_extent),
            randint(left_extent, source_w - ONE - right_extent),
        )
        target_anchor = (
            randint(top_extent, target_h - ONE - bottom_extent),
            randint(left_extent, target_w - ONE - right_extent),
        )

        gap_rows = unifint(diff_lb, diff_ub, (TWO, FIVE))
        gap_cols = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        top_margin = randint(ZERO, THREE)
        left_margin = randint(ZERO, THREE)
        bottom_margin = randint(ZERO, THREE)
        right_margin = randint(ZERO, THREE)
        grid_h = top_margin + source_h + gap_rows + target_h + bottom_margin
        grid_w = left_margin + source_w + gap_cols + target_w + right_margin
        if grid_h > 30 or grid_w > 30:
            continue

        source_loc = (top_margin, left_margin)
        target_loc = (top_margin + source_h + gap_rows, left_margin + source_w + gap_cols)
        source_box = _window_patch_2f0c5170(source_loc, (source_h, source_w))
        target_box = _window_patch_2f0c5170(target_loc, (target_h, target_w))

        gi = canvas(EIGHT, (grid_h, grid_w))
        gi = fill(gi, ZERO, source_box)
        gi = fill(gi, ZERO, target_box)

        source_obj = _colored_pattern_2f0c5170(patch, anchor_color, source_anchor)
        source_obj = shift(source_obj, source_loc)
        gi = paint(gi, source_obj)

        target_anchor_global = shift(frozenset({target_anchor}), target_loc)
        gi = fill(gi, anchor_color, target_anchor_global)

        go = canvas(ZERO, (target_h, target_w))
        go = paint(go, _colored_pattern_2f0c5170(patch, anchor_color, target_anchor))

        if choice((T, F)):
            gi = hmirror(gi)
            go = hmirror(go)
        if choice((T, F)):
            gi = vmirror(gi)
            go = vmirror(go)

        if mostcolor(gi) != EIGHT:
            continue
        if colorcount(gi, anchor_color) != TWO:
            continue
        return {"input": gi, "output": go}
