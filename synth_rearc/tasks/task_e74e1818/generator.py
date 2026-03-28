from synth_rearc.core import *


def _band_e74e1818(
    start: Integer,
    stop: Integer,
) -> tuple[int, ...]:
    if start > stop:
        return tuple()
    return tuple(range(start, stop + ONE))


def _parity_band_e74e1818(
    start: Integer,
    stop: Integer,
    parity: Integer,
) -> tuple[int, ...]:
    if start > stop:
        return tuple()
    return tuple(v for v in range(start, stop + ONE) if v % TWO == parity)


def _unique_distances_e74e1818(*values: Integer) -> tuple[int, ...]:
    return tuple(sorted({v for v in values if v is not None and v >= ZERO}))


def _motif_templates_e74e1818(
    half: Integer,
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    full = _band_e74e1818(ZERO, half)
    center = (ZERO,)
    inner = _band_e74e1818(ONE, half - ONE) if half >= TWO else center
    edge = (half,)
    center_edges = _unique_distances_e74e1818(ZERO, half)
    near_full = _band_e74e1818(ZERO, max(ONE, half - ONE))
    upper = _band_e74e1818(ONE, half) if half >= ONE else center
    lower_two = _band_e74e1818(ZERO, min(ONE, half))
    tri_mid = _parity_band_e74e1818(ZERO, half - ONE, ZERO) if half >= TWO else center
    tri_tip = (ONE,) if half >= THREE else center
    mid = (half - ONE,) if half >= TWO else center
    specs = (
        (full,),
        (full, center),
        (full, inner),
        (near_full, center_edges),
        (center_edges, full),
        (upper, full),
        (full, tri_mid if tri_mid else center, tri_tip),
        (center_edges, edge, full),
        (full, edge, full),
        (upper, center, center),
        (upper, center, full),
        (upper, center_edges, full),
        (center, lower_two, mid, full),
        (center, center, upper, full),
        (center, lower_two, center_edges, full),
    )
    out = []
    seen = set()
    for spec in specs:
        spec = tuple(tuple(row) for row in spec)
        if not all(spec) or spec in seen:
            continue
        seen.add(spec)
        out.append(spec)
    return tuple(out)


def _partition_total_e74e1818(
    total: Integer,
    parts: Integer,
) -> tuple[int, ...]:
    out = [ONE] * parts
    remaining = total - parts
    while remaining > ZERO:
        idx = randint(ZERO, parts - ONE)
        if out[idx] < FOUR:
            out[idx] += ONE
            remaining -= ONE
    shuffle(out)
    return tuple(out)


def _object_from_rows_e74e1818(
    top: Integer,
    center: Integer,
    value: Integer,
    rows: tuple[tuple[int, ...], ...],
) -> Object:
    cells = set()
    for di, distances in enumerate(rows):
        i = top + di
        for dj in distances:
            cells.add((value, (i, center - dj)))
            cells.add((value, (i, center + dj)))
    return frozenset(cells)


def _max_halfwidth_e74e1818(side: Integer) -> Integer:
    center = side // TWO
    margin = ONE if side < 11 else TWO
    return max(ONE, center - margin)


def generate_e74e1818(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        side = double(unifint(diff_lb, diff_ub, (THREE, EIGHT))) + ONE
        interior = side - TWO
        possible_counts = tuple(n for n in range(THREE, SIX) if n <= interior <= FOUR * n)
        count = choice(possible_counts)
        heights = _partition_total_e74e1818(interior, count)
        if max(heights) == ONE:
            continue
        colors = sample(cols, count)
        center = side // TWO
        top = ONE
        gi = canvas(ZERO, (side, side))
        go = canvas(ZERO, (side, side))
        changed = False
        for height_value, color_value in zip(heights, colors):
            half = randint(ONE, _max_halfwidth_e74e1818(side))
            templates = tuple(
                tpl for tpl in _motif_templates_e74e1818(half) if len(tpl) == height_value
            )
            rows = choice(templates)
            if rows != rows[::-1] and choice((True, False)):
                rows = rows[::-1]
            obj = _object_from_rows_e74e1818(top, center, color_value, rows)
            gi = paint(gi, obj)
            go = paint(go, hmirror(obj))
            changed = changed or rows != rows[::-1]
            top += height_value
        if changed:
            return {"input": gi, "output": go}
