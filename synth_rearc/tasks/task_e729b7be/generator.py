from synth_rearc.core import *


PATTERN_COLORS_e729b7be = (ZERO, ONE, TWO, THREE, FIVE, SIX, NINE)


def _make_width_profile_e729b7be(size: Integer, center: Integer) -> tuple[Integer, ...]:
    max_width = center - TWO
    while True:
        top_width = choice((TWO, TWO, THREE))
        bottom_width = choice((TWO, TWO, THREE))
        widths = []
        for width_value in range(top_width, max_width + ONE):
            repeat_ub = TWO if width_value in (top_width, max_width) else THREE
            widths.extend([width_value] * randint(ONE, repeat_ub))
        for width_value in range(max_width - ONE, bottom_width - ONE, -ONE):
            repeat_ub = TWO if width_value in (bottom_width, max_width - ONE) else THREE
            widths.extend([width_value] * randint(ONE, repeat_ub))
        profile = tuple(widths)
        if max_width + THREE <= len(profile) <= size - THREE:
            return profile


def _pick_profile_top_e729b7be(
    size: Integer,
    center: Integer,
    span: Integer,
) -> Integer | None:
    lower = max(ONE, center - span + TWO)
    upper = min(center - ONE, size - span - TWO)
    if lower > upper:
        return None
    return randint(lower, upper)


def _profile_cells_e729b7be(
    center: Integer,
    top: Integer,
    profile: tuple[Integer, ...],
) -> set[tuple[Integer, Integer]]:
    cells = set()
    for offset, width_value in enumerate(profile):
        row = top + offset
        left = center - width_value
        for col in range(left, center):
            cells.add((row, col))
    return cells


def _connected_e729b7be(cells: set[tuple[Integer, Integer]]) -> Boolean:
    start = next(iter(cells))
    stack = [start]
    seen = {start}
    while stack:
        row, col = stack.pop()
        for drow, dcol in ((ONE, ZERO), (-ONE, ZERO), (ZERO, ONE), (ZERO, -ONE)):
            loc = (row + drow, col + dcol)
            if loc in cells and loc not in seen:
                seen.add(loc)
                stack.append(loc)
    return len(seen) == len(cells)


def _add_notches_e729b7be(
    center: Integer,
    top: Integer,
    profile: tuple[Integer, ...],
    cells: set[tuple[Integer, Integer]],
) -> set[tuple[Integer, Integer]]:
    candidates = []
    for offset, width_value in enumerate(profile):
        if width_value < FOUR:
            continue
        row = top + offset
        if abs(row - center) <= ONE:
            continue
        notch_col = center - choice((TWO, THREE if width_value >= FIVE else TWO))
        if (row, notch_col) in cells:
            candidates.append((row, notch_col))
    shuffle(candidates)
    result = set(cells)
    notch_count = choice((ZERO, ZERO, ZERO, ONE, ONE, TWO))
    for row, col in candidates[:notch_count]:
        trial = set(result)
        trial.remove((row, col))
        if _connected_e729b7be(trial):
            result = trial
    return result


def _paint_layer_e729b7be(
    grid: Grid,
    cells: set[tuple[Integer, Integer]],
    center: Integer,
    top: Integer,
    profile: tuple[Integer, ...],
    inset: Integer,
    row_start: Integer,
    row_stop: Integer,
    color_value: Integer,
) -> tuple[Grid, Integer]:
    painted = set()
    for offset, width_value in enumerate(profile):
        if offset < row_start or offset > row_stop:
            continue
        row = top + offset
        left = center - width_value + inset
        for col in range(left, center):
            loc = (row, col)
            if loc in cells:
                painted.add(loc)
    if len(painted) == ZERO:
        return grid, ZERO
    return fill(grid, color_value, painted), len(painted)


def _pick_colors_e729b7be(
    base_count: Integer,
    overlay_count: Integer,
) -> tuple[tuple[Integer, ...], tuple[Integer, ...]]:
    outer = choice((ONE, TWO, THREE, FIVE, SIX))
    need = base_count + overlay_count - ONE
    pool = [color_value for color_value in PATTERN_COLORS_e729b7be if color_value != outer]
    inner = []
    if need > ZERO and NINE in pool and randint(ZERO, FOUR) != ZERO:
        inner.append(NINE)
        pool.remove(NINE)
    inner.extend(sample(pool, need - len(inner)))
    base_colors = (outer,) + tuple(inner[: base_count - ONE])
    overlay_colors = tuple(inner[base_count - ONE :])
    return base_colors, overlay_colors


def generate_e729b7be(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        size = choice((15, 17, 17, 19))
        center = size // TWO
        profile = _make_width_profile_e729b7be(size, center)
        span = len(profile)
        top = _pick_profile_top_e729b7be(size, center, span)
        if top is None:
            continue
        cells = _profile_cells_e729b7be(center, top, profile)
        cells = _add_notches_e729b7be(center, top, profile, cells)
        if len(cells) < 25:
            continue
        base_count = choice((THREE, THREE, FOUR, FOUR, FIVE))
        overlay_cap = min(len(PATTERN_COLORS_e729b7be) - base_count, THREE if size >= 19 else TWO)
        overlay_choices = tuple(
            value
            for value in (ZERO, ZERO, ONE, ONE, TWO, THREE)
            if value <= overlay_cap
        )
        overlay_count = choice(overlay_choices)
        base_colors, overlay_colors = _pick_colors_e729b7be(base_count, overlay_count)
        gi = canvas(SEVEN, (size, size))
        x0 = frozenset((row, center) for row in range(size))
        gi = fill(gi, FOUR, x0)
        x1 = frozenset({(center, ZERO), (center, center), (center, size - ONE)})
        gi = fill(gi, EIGHT, x1)
        gi = fill(gi, base_colors[ZERO], cells)
        inset = ZERO
        top_trim = ZERO
        bottom_trim = ZERO
        failed = F
        for color_value in base_colors[ONE:]:
            inset += choice((ONE, ONE, ONE, TWO if size >= 19 else ONE))
            top_trim += randint(ZERO, TWO)
            bottom_trim += randint(ZERO, TWO)
            if top_trim + bottom_trim >= span - TWO:
                failed = T
                break
            gi, painted_count = _paint_layer_e729b7be(
                gi,
                cells,
                center,
                top,
                profile,
                inset,
                top_trim,
                span - bottom_trim - ONE,
                color_value,
            )
            if painted_count < max(FOUR, inset + TWO):
                failed = T
                break
        if failed:
            continue
        for color_value in overlay_colors:
            band_height = randint(TWO, max(TWO, span // TWO))
            band_start = randint(ZERO, span - band_height)
            band_inset = randint(ONE, max(ONE, center - FOUR))
            gi, painted_count = _paint_layer_e729b7be(
                gi,
                cells,
                center,
                top,
                profile,
                band_inset,
                band_start,
                band_start + band_height - ONE,
                color_value,
            )
            if painted_count < FOUR:
                failed = T
                break
        if failed:
            continue
        palette_size = len(
            {
                value
                for row in gi
                for value in row
                if value not in (FOUR, SEVEN, EIGHT)
            }
        )
        if palette_size < THREE:
            continue
        go = underpaint(gi, asobject(rot180(gi)))
        return {"input": gi, "output": go}
