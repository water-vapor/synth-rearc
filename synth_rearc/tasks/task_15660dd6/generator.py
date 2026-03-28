from synth_rearc.core import *


LABELS_15660dd6 = (FIVE, NINE, ZERO)
ODD_COLORS_15660dd6 = (THREE, FOUR, SIX, SEVEN)
TRANSFORMS_15660dd6 = (identity, rot90, rot180, rot270, hmirror, vmirror)


def _neighbors_15660dd6(loc: tuple[int, int], size: int) -> tuple[tuple[int, int], ...]:
    i, j = loc
    cands = []
    for di, dj in ((-ONE, ZERO), (ONE, ZERO), (ZERO, -ONE), (ZERO, ONE)):
        ni = i + di
        nj = j + dj
        if ZERO <= ni < size and ZERO <= nj < size:
            cands.append((ni, nj))
    return tuple(cands)


def _connected_15660dd6(cells: Indices, size: int) -> bool:
    if len(cells) == ZERO:
        return F
    start = next(iter(cells))
    frontier = [start]
    seen = {start}
    while frontier:
        loc = frontier.pop()
        for nxt in _neighbors_15660dd6(loc, size):
            if nxt in cells and nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    return len(seen) == len(cells)


def _carved_mask_15660dd6(size: int, min_cells: int, max_cells: int) -> Indices:
    cells = {(i, j) for i in range(size) for j in range(size)}
    target = randint(min_cells, max_cells)
    while len(cells) > target:
        removed = F
        order = list(cells)
        shuffle(order)
        for loc in order:
            trial = cells - {loc}
            if _connected_15660dd6(trial, size):
                cells = trial
                removed = T
                break
        if not removed:
            break
    return frozenset(cells)


def _plus_mask_15660dd6(size: int) -> Indices:
    midi = randint(ZERO, size - ONE)
    midj = randint(ZERO, size - ONE)
    cells = {(midi, j) for j in range(size)} | {(i, midj) for i in range(size)}
    if size > THREE and choice((T, F)):
        if choice((T, F)):
            extra = max(ZERO, min(size - ONE, midi + choice((-ONE, ONE))))
            cells |= {(extra, j) for j in range(size)}
        else:
            extra = max(ZERO, min(size - ONE, midj + choice((-ONE, ONE))))
            cells |= {(i, extra) for i in range(size)}
    return frozenset(cells)


def _stair_mask_15660dd6(size: int) -> Indices:
    lower = max(ONE, size // TWO)
    widths = [randint(lower, size)]
    for _ in range(size - ONE):
        prev = widths[-ONE]
        cands = [value for value in (prev - ONE, prev, prev + ONE) if ONE <= value <= size]
        widths.append(choice(cands))
    if min(widths) == size:
        widths[randint(ZERO, size - ONE)] = size - ONE
    left_aligned = choice((T, F))
    cells = set()
    for i, width_value in enumerate(widths):
        start = ZERO if left_aligned else size - width_value
        for j in range(start, start + width_value):
            cells.add((i, j))
    return frozenset(cells)


def _solid_mask_15660dd6(size: int) -> Indices:
    return frozenset((i, j) for i in range(size) for j in range(size))


def _transform_mask_15660dd6(mask: Indices, size: int) -> Indices:
    grid = canvas(EIGHT, (size, size))
    grid = fill(grid, TWO, mask)
    grid = choice(TRANSFORMS_15660dd6)(grid)
    return ofcolor(grid, TWO)


def _mask_15660dd6(size: int, odd: bool) -> Indices:
    total = size * size
    while True:
        styles = ["carved", "stair", "plus"]
        if odd:
            styles.append("solid")
        style = choice(styles)
        if style == "solid":
            mask = _solid_mask_15660dd6(size)
        elif style == "plus":
            mask = _plus_mask_15660dd6(size)
        elif style == "stair":
            mask = _stair_mask_15660dd6(size)
        else:
            if odd:
                min_cells = max(size + ONE, (total + ONE) // TWO)
                max_cells = total
            else:
                min_cells = max(size, total // THREE)
                max_cells = total - ONE
            mask = _carved_mask_15660dd6(size, min_cells, max_cells)
        mask = _transform_mask_15660dd6(mask, size)
        if not odd and len(mask) == total:
            continue
        return mask


def _section_grid_15660dd6(size: int, color_value: int, mask: Indices) -> Grid:
    rows = [[ONE for _ in range(size)] for _ in range(size)]
    for i in range(ONE, size - ONE):
        for j in range(ONE, size - ONE):
            rows[i][j] = EIGHT
    for i, j in mask:
        rows[i + ONE][j + ONE] = color_value
    return tuple(tuple(row) for row in rows)


def _panel_grid_15660dd6(label: int, sections: tuple[Grid, ...]) -> Grid:
    size = len(sections[ZERO])
    rows = []
    for i in range(size):
        row = [label]
        for section in sections:
            row.extend(section[i])
            row.append(EIGHT)
        rows.append(tuple(row))
    return tuple(rows)


def _join_sections_15660dd6(sections: tuple[Grid, ...]) -> Grid:
    size = len(sections[ZERO])
    rows = [[] for _ in range(size)]
    for idx, section in enumerate(sections):
        if idx > ZERO:
            for i in range(size):
                rows[i].append(EIGHT)
        for i in range(size):
            rows[i].extend(section[i])
    return tuple(tuple(row) for row in rows)


def generate_15660dd6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        variants = ((FIVE, THREE), (SIX, FOUR), (SEVEN, THREE))
        size, nsections = variants[unifint(diff_lb, diff_ub, (ZERO, TWO))]
        inner = size - TWO
        odd_colors = sample(ODD_COLORS_15660dd6, nsections)
        odd_panels = [randint(ZERO, TWO) for _ in range(nsections)]
        if len(set(odd_panels)) == ONE:
            idx = randint(ZERO, nsections - ONE)
            cands = [value for value in range(THREE) if value != odd_panels[idx]]
            odd_panels[idx] = choice(cands)
        common_seen = set()
        odd_seen = set()
        panel_sections = [[], [], []]
        output_sections = []
        valid = T
        # Each section has one source panel with a distinct colored motif; the other two share a 2-colored motif.
        for idx in range(nsections):
            common_mask = _mask_15660dd6(inner, F)
            for _ in range(20):
                if common_mask not in common_seen:
                    break
                common_mask = _mask_15660dd6(inner, F)
            odd_mask = _mask_15660dd6(inner, T)
            for _ in range(20):
                if odd_mask != common_mask and odd_mask not in odd_seen:
                    break
                odd_mask = _mask_15660dd6(inner, T)
            if common_mask in common_seen or odd_mask == common_mask or odd_mask in odd_seen:
                valid = F
                break
            common_seen.add(common_mask)
            odd_seen.add(odd_mask)
            common_section = _section_grid_15660dd6(size, TWO, common_mask)
            odd_section = _section_grid_15660dd6(size, odd_colors[idx], odd_mask)
            odd_panel = odd_panels[idx]
            for panel_idx in range(THREE):
                section = odd_section if panel_idx == odd_panel else common_section
                panel_sections[panel_idx].append(section)
            output_section = replace(common_section, ONE, LABELS_15660dd6[odd_panel])
            output_section = replace(output_section, TWO, odd_colors[idx])
            output_sections.append(output_section)
        if not valid:
            continue
        panels = tuple(
            _panel_grid_15660dd6(label, tuple(sections))
            for label, sections in zip(LABELS_15660dd6, panel_sections)
        )
        width_value = ONE + nsections * (size + ONE)
        divider = tuple(EIGHT for _ in range(width_value))
        rows = [divider]
        for panel in panels:
            rows.extend(panel)
            rows.append(divider)
        gi = tuple(rows)
        go = _join_sections_15660dd6(tuple(output_sections))
        return {"input": gi, "output": go}
