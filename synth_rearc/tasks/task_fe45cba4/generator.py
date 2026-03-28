from synth_rearc.core import *

from .verifier import verify_fe45cba4


BG_FE45CBA4 = SEVEN


def _rectangle_fe45cba4(
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(h) for j in range(w))


def _mask_from_widths_fe45cba4(
    widths: tuple[Integer, ...],
    extras: Indices = frozenset(),
) -> Indices:
    cells = {(i, j) for i, width_value in enumerate(widths) for j in range(width_value)}
    return frozenset(cells | set(extras))


def _connected_fe45cba4(
    patch: Indices,
) -> Boolean:
    if len(patch) == ZERO:
        return F
    start = next(iter(patch))
    seen = {start}
    frontier = [start]
    while len(frontier) > ZERO:
        i, j = frontier.pop()
        for di, dj in ((-ONE, ZERO), (ONE, ZERO), (ZERO, -ONE), (ZERO, ONE)):
            loc = (i + di, j + dj)
            if loc not in patch or loc in seen:
                continue
            seen.add(loc)
            frontier.append(loc)
    return len(seen) == len(patch)


def _sample_mask_fe45cba4(
    h: Integer,
    w: Integer,
    edge_width: Integer,
    allow_extras: Boolean,
) -> Indices:
    rect = _rectangle_fe45cba4(h, w)
    while True:
        peak_start = randint(ONE, h - TWO)
        peak_end = randint(peak_start, h - TWO)
        peak = randint(edge_width + ONE, w - ONE)
        widths = [edge_width for _ in range(h)]
        for row in range(peak_start, peak_end + ONE):
            widths[row] = peak
        if peak > edge_width + ONE and peak_start > ONE and choice((T, F)):
            widths[peak_start - ONE] = randint(edge_width + ONE, peak - ONE)
        if peak > edge_width + ONE and peak_end < h - TWO and choice((T, F)):
            widths[peak_end + ONE] = randint(edge_width + ONE, peak - ONE)
        extras = set()
        upper = peak_start - ONE
        lower = peak_end + ONE
        can_pair = (
            allow_extras
            and peak >= FOUR
            and upper >= ONE
            and lower <= h - TWO
            and widths[upper] > edge_width
            and widths[lower] > edge_width
            and peak > max(widths[upper], widths[lower]) + ONE
        )
        if can_pair and choice((T, F)):
            extra_col = randint(max(widths[upper], widths[lower]) + ONE, peak - ONE)
            extras = {(upper, extra_col), (lower, extra_col)}
        mask = _mask_from_widths_fe45cba4(tuple(widths), frozenset(extras))
        part = difference(rect, mask)
        if len(mask) == ZERO or len(part) == ZERO:
            continue
        if not _connected_fe45cba4(mask):
            continue
        if not _connected_fe45cba4(part):
            continue
        return mask


def generate_fe45cba4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(BG_FE45CBA4, interval(ZERO, TEN, ONE))
    while True:
        target_h = unifint(diff_lb, diff_ub, (THREE, SIX))
        target_w = unifint(diff_lb, diff_ub, (FOUR, EIGHT))
        distract_h = unifint(diff_lb, diff_ub, (THREE, SIX))
        distract_w = unifint(diff_lb, diff_ub, (THREE, SEVEN))
        target_mask = _sample_mask_fe45cba4(target_h, target_w, ONE, T)
        distract_mask = _sample_mask_fe45cba4(distract_h, distract_w, ZERO, T)
        target_rect = _rectangle_fe45cba4(target_h, target_w)
        distract_rect = _rectangle_fe45cba4(distract_h, distract_w)
        target_main = difference(target_rect, target_mask)
        distract_part = difference(distract_rect, distract_mask)
        frag_w = width(target_mask)
        min_side = max(
            EIGHT,
            target_h + distract_h + ONE,
            max(target_w, distract_w) + frag_w + ONE,
        )
        if min_side > 30:
            continue
        max_side = min(30, min_side + EIGHT)
        side = unifint(diff_lb, diff_ub, (min_side, max_side))
        order = choice((T, F))
        if order:
            target_top = randint(ZERO, side - target_h - distract_h - ONE)
            distract_top = randint(target_top + target_h + ONE, side - distract_h)
        else:
            distract_top = randint(ZERO, side - target_h - distract_h - ONE)
            target_top = randint(distract_top + distract_h + ONE, side - target_h)
        target_left = side - target_w
        target_main_left = target_left + ONE
        distract_left = side - distract_w
        right_left = min(target_main_left, distract_left)
        frag_col_max = right_left - frag_w - ONE
        if frag_col_max < ZERO:
            continue
        frag_top_lb = max(ZERO, target_top - TWO)
        frag_top_ub = min(side - target_h, target_top + TWO)
        frag_top = randint(frag_top_lb, frag_top_ub)
        frag_left = randint(ZERO, frag_col_max)
        target_color, distractor_color = sample(cols, TWO)
        gi = canvas(BG_FE45CBA4, (side, side))
        go = canvas(BG_FE45CBA4, (side, side))
        target_main_patch = shift(target_main, (target_top, target_left))
        target_fragment_patch = shift(target_mask, (frag_top, frag_left))
        distract_patch = shift(distract_part, (distract_top, distract_left))
        target_output_patch = shift(target_rect, (target_top, target_left))
        gi = fill(gi, target_color, target_main_patch)
        gi = fill(gi, target_color, target_fragment_patch)
        gi = fill(gi, distractor_color, distract_patch)
        go = fill(go, target_color, target_output_patch)
        go = fill(go, distractor_color, distract_patch)
        if gi == go:
            continue
        if verify_fe45cba4(gi) != go:
            continue
        return {"input": gi, "output": go}
