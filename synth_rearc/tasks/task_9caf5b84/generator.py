from synth_rearc.core import *


DIM_BOUNDS_9CAF5B84 = (FOUR, SEVEN)
NCOLOR_OPTIONS_9CAF5B84 = (FOUR, FIVE, FIVE, FIVE, SIX)
INPUT_COLORS_9CAF5B84 = remove(SEVEN, interval(ZERO, TEN, ONE))


def generate_9caf5b84(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, DIM_BOUNDS_9CAF5B84)
        w = unifint(diff_lb, diff_ub, DIM_BOUNDS_9CAF5B84)
        area = h * w
        ncolors = choice(NCOLOR_OPTIONS_9CAF5B84)
        if area < ncolors + SIX:
            continue
        colors = tuple(sample(INPUT_COLORS_9CAF5B84, ncolors))
        dominant1, dominant2 = colors[:TWO]
        minor_colors = colors[TWO:]
        minor_cap = max(ONE, (area - FOUR) // (ncolors + TWO))
        minor_counts = [unifint(diff_lb, diff_ub, (ONE, minor_cap)) for _ in minor_colors]
        minor_total = sum(minor_counts)
        remaining = area - minor_total
        if remaining < SIX:
            continue
        max_minor = max(minor_counts)
        lower = max(max_minor + ONE, remaining // THREE)
        upper = remaining // TWO
        if lower > upper:
            continue
        if (
            choice((ZERO, ONE, TWO, THREE)) == ZERO
            and remaining % TWO == ZERO
            and remaining // TWO > max_minor
        ):
            dominant2_count = remaining // TWO
        else:
            dominant2_count = unifint(diff_lb, diff_ub, (lower, upper))
        dominant1_count = remaining - dominant2_count
        if dominant1_count < dominant2_count or dominant2_count <= max_minor:
            continue
        gi = canvas(dominant1, (h, w))
        cells = sample(totuple(asindices(gi)), area)
        cursor = ZERO
        dominant2_cells = frozenset(cells[cursor:cursor + dominant2_count])
        cursor += dominant2_count
        gi = fill(gi, dominant2, dominant2_cells)
        minor_cells = frozenset()
        for color, count in zip(minor_colors, minor_counts):
            patch = frozenset(cells[cursor:cursor + count])
            cursor += count
            minor_cells = combine(minor_cells, patch)
            gi = fill(gi, color, patch)
        go = fill(gi, SEVEN, minor_cells)
        if numcolors(gi) != ncolors or colorcount(go, SEVEN) != minor_total:
            continue
        if colorcount(gi, dominant1) != dominant1_count:
            continue
        if colorcount(gi, dominant2) != dominant2_count:
            continue
        return {"input": gi, "output": go}
