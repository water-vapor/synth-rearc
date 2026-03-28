from synth_rearc.core import *


COLORS_8618D23E = remove(NINE, interval(ZERO, TEN, ONE))


def _pick_palettes_8618d23e() -> tuple[tuple[Integer, ...], tuple[Integer, ...]]:
    pool = list(COLORS_8618D23E)
    shuffle(pool)
    top_size = choice((ONE, ONE, TWO, TWO, THREE))
    bottom_size = choice((ONE, ONE, TWO, TWO, THREE))
    shared_cap = min(ONE, top_size, bottom_size)
    shared_size = min(shared_cap, choice((ZERO, ZERO, ONE, ONE, ONE)))
    cursor = shared_size
    shared = pool[:shared_size]
    top_palette = shared + pool[cursor : cursor + top_size - shared_size]
    cursor += top_size - shared_size
    bottom_palette = shared + pool[cursor : cursor + bottom_size - shared_size]
    shuffle(top_palette)
    shuffle(bottom_palette)
    return tuple(top_palette), tuple(bottom_palette)


def _make_row_8618d23e(
    width_value: Integer,
    palette_values: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    base_color = choice(palette_values)
    row = [base_color] * width_value
    if len(palette_values) == ONE:
        return tuple(row)
    nsegments = min(width_value, choice((ZERO, ONE, ONE, TWO)))
    for _ in range(nsegments):
        start = randint(ZERO, width_value - ONE)
        end = randint(start, width_value - ONE)
        color_value = choice(palette_values)
        while color_value == base_color:
            color_value = choice(palette_values)
        row[start : end + ONE] = [color_value] * (end - start + ONE)
    return tuple(row)


def _mutate_row_8618d23e(
    row: tuple[Integer, ...],
    palette_values: tuple[Integer, ...],
) -> tuple[Integer, ...]:
    if len(palette_values) == ONE:
        return row
    row_list = list(row)
    start = randint(ZERO, len(row_list) - ONE)
    end = randint(start, len(row_list) - ONE)
    color_value = choice(palette_values)
    while color_value == row_list[start]:
        color_value = choice(palette_values)
    row_list[start : end + ONE] = [color_value] * (end - start + ONE)
    return tuple(row_list)


def _make_half_8618d23e(
    height_value: Integer,
    width_value: Integer,
    palette_values: tuple[Integer, ...],
) -> Grid:
    ntemplates = min(height_value, choice((ONE, ONE, TWO, TWO, THREE)))
    templates = tuple(_make_row_8618d23e(width_value, palette_values) for _ in range(ntemplates))
    rows = []
    for idx in range(height_value):
        row = rows[-ONE] if idx > ZERO and choice((T, T, F)) else choice(templates)
        if choice((F, F, T)):
            row = _mutate_row_8618d23e(row, palette_values)
        rows.append(row)
    return tuple(rows)


def generate_8618d23e(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        half_h = unifint(diff_lb, diff_ub, (ONE, SIX))
        width_value = unifint(diff_lb, diff_ub, (ONE, EIGHT))
        top_palette, bottom_palette = _pick_palettes_8618d23e()
        top_half = _make_half_8618d23e(half_h, width_value, top_palette)
        bottom_half = _make_half_8618d23e(half_h, width_value, bottom_palette)
        gi = vconcat(top_half, bottom_half)
        if numcolors(gi) == ONE:
            continue
        bar = canvas(NINE, (half_h, ONE))
        sep = canvas(NINE, (ONE, increment(width_value)))
        top_out = hconcat(top_half, bar)
        bottom_out = hconcat(bar, bottom_half)
        go = vconcat(vconcat(top_out, sep), bottom_out)
        return {"input": gi, "output": go}
