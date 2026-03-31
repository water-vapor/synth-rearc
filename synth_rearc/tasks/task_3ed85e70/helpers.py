from __future__ import annotations

from collections import Counter

from synth_rearc.core import *


PALETTE_3ed85e70 = (ONE, TWO, FOUR, SIX, SEVEN, EIGHT)


def bbox_3ed85e70(
    cells: tuple[tuple[int, int], ...] | frozenset[tuple[int, int]],
) -> tuple[int, int, int, int]:
    rows = tuple(i for i, _ in cells)
    cols = tuple(j for _, j in cells)
    return (min(rows), min(cols), max(rows), max(cols))


def dims_3ed85e70(
    obj: Object,
) -> tuple[int, int]:
    x0 = tuple(i for _, (i, _) in obj)
    x1 = tuple(j for _, (_, j) in obj)
    return (max(x0) + ONE, max(x1) + ONE)


def shift_object_3ed85e70(
    obj: Object,
    offset: tuple[int, int],
) -> Object:
    di, dj = offset
    return frozenset((color, (i + di, j + dj)) for color, (i, j) in obj)


def object_to_grid_3ed85e70(
    obj: Object,
) -> Grid:
    h, w = dims_3ed85e70(obj)
    x0 = canvas(ZERO, (h, w))
    return paint(x0, obj)


def object_from_rows_3ed85e70(
    rows: tuple[tuple[int, ...], ...],
) -> Object:
    return frozenset(
        (value, (i, j))
        for i, row in enumerate(rows)
        for j, value in enumerate(row)
        if value != ZERO
    )


def extract_components_3ed85e70(
    grid: Grid,
    allowed_cells: frozenset[tuple[int, int]] | None = None,
    allowed_values: frozenset[int] | None = None,
    by_color: bool = False,
) -> tuple[frozenset[tuple[int, int]], ...]:
    h, w = shape(grid)
    x0 = (
        frozenset((i, j) for i in range(h) for j in range(w))
        if allowed_cells is None
        else allowed_cells
    )
    seen: set[tuple[int, int]] = set()
    out: list[frozenset[tuple[int, int]]] = []
    for start in sorted(x0):
        if start in seen:
            continue
        value = index(grid, start)
        if allowed_values is not None and value not in allowed_values:
            continue
        stack = [start]
        seen.add(start)
        cells: set[tuple[int, int]] = set()
        while stack:
            i, j = stack.pop()
            cells.add((i, j))
            for ni, nj in ((i - ONE, j), (i + ONE, j), (i, j - ONE), (i, j + ONE)):
                loc = (ni, nj)
                if not (ZERO <= ni < h and ZERO <= nj < w):
                    continue
                if loc not in x0 or loc in seen:
                    continue
                nvalue = index(grid, loc)
                if allowed_values is not None and nvalue not in allowed_values:
                    continue
                if by_color and nvalue != value:
                    continue
                seen.add(loc)
                stack.append(loc)
        out.append(frozenset(cells))
    return tuple(out)


def find_panel_bbox_3ed85e70(
    grid: Grid,
) -> tuple[int, int, int, int]:
    x0 = extract_components_3ed85e70(grid, allowed_values=frozenset({THREE}))
    x1 = max(x0, key=len)
    return bbox_3ed85e70(x1)


def panel_box_3ed85e70(
    side: str,
    thickness: int,
) -> tuple[int, int, int, int]:
    if side == "top":
        return (ZERO, ZERO, thickness - ONE, 29)
    if side == "bottom":
        return (30 - thickness, ZERO, 29, 29)
    if side == "left":
        return (ZERO, ZERO, 29, thickness - ONE)
    return (ZERO, 30 - thickness, 29, 29)


def box_overlap_3ed85e70(
    a: tuple[int, int, int, int],
    b: tuple[int, int, int, int],
) -> bool:
    return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])


def expand_box_3ed85e70(
    box: tuple[int, int, int, int],
    margin: int = ONE,
) -> tuple[int, int, int, int]:
    return (
        max(ZERO, box[0] - margin),
        max(ZERO, box[1] - margin),
        min(29, box[2] + margin),
        min(29, box[3] + margin),
    )


def extract_panel_patterns_3ed85e70(
    grid: Grid,
    panel_box: tuple[int, int, int, int],
) -> tuple[Object, ...]:
    a, b, c, d = panel_box
    x0 = frozenset(
        (i, j)
        for i in range(a, c + ONE)
        for j in range(b, d + ONE)
        if index(grid, (i, j)) not in (ZERO, THREE)
    )
    x1 = extract_components_3ed85e70(grid, allowed_cells=x0)
    out: list[Object] = []
    for comp in x1:
        ai, aj, _, _ = bbox_3ed85e70(comp)
        out.append(
            frozenset((index(grid, loc), subtract(loc, (ai, aj))) for loc in comp)
        )
    return tuple(out)


def extract_outside_objects_3ed85e70(
    grid: Grid,
    panel_box: tuple[int, int, int, int],
) -> tuple[frozenset[tuple[int, int]], ...]:
    a, b, c, d = panel_box
    h, w = shape(grid)
    x0 = frozenset(
        (i, j)
        for i in range(h)
        for j in range(w)
        if not (a <= i <= c and b <= j <= d) and index(grid, (i, j)) != ZERO
    )
    return extract_components_3ed85e70(grid, allowed_cells=x0)


def color_partitions_3ed85e70(
    obj: Object,
) -> dict[int, tuple[tuple[int, int], ...]]:
    out: dict[int, list[tuple[int, int]]] = {}
    for color, loc in obj:
        out.setdefault(color, []).append(loc)
    return {color: tuple(sorted(cells)) for color, cells in out.items()}


def color_components_3ed85e70(
    obj: Object,
) -> tuple[tuple[int, tuple[tuple[int, int], ...]], ...]:
    x0 = object_to_grid_3ed85e70(obj)
    x1 = color_partitions_3ed85e70(obj)
    out: list[tuple[int, tuple[tuple[int, int], ...]]] = []
    for color, cells in x1.items():
        x2 = extract_components_3ed85e70(
            x0,
            allowed_cells=frozenset(cells),
            by_color=True,
        )
        out.extend((color, tuple(sorted(comp))) for comp in x2)
    return tuple(out)


def _variant_entry_3ed85e70(
    obj: Object,
) -> tuple[Object, tuple[int, int]]:
    x0 = tuple(i for _, (i, _) in obj)
    x1 = tuple(j for _, (_, j) in obj)
    return (obj, (min(x0), min(x1)))


def fragment_variants_3ed85e70(
    pattern: Object,
) -> tuple[tuple[Object, tuple[int, int]], ...]:
    x0 = object_to_grid_3ed85e70(pattern)
    h, w = shape(x0)
    x1 = Counter(color for color, _ in pattern)
    x2 = max(x1.values())
    x3 = sum(value == x2 for value in x1.values())
    x4 = color_partitions_3ed85e70(pattern)
    seen: set[tuple[tuple[int, tuple[int, int]], ...]] = set()
    out: list[tuple[Object, tuple[int, int]]] = []

    def add(obj: Object) -> None:
        if len(obj) == ZERO:
            return
        key = tuple(sorted(obj))
        if key in seen:
            return
        seen.add(key)
        out.append(_variant_entry_3ed85e70(obj))

    for color, cells in color_components_3ed85e70(pattern):
        if x1[color] < x2:
            add(frozenset((color, loc) for loc in cells))
    for color, cells in x4.items():
        a, b, c, d = bbox_3ed85e70(cells)
        filled = frozenset(
            (color, (i, j))
            for i in range(a, c + ONE)
            for j in range(b, d + ONE)
        )
        comps = extract_components_3ed85e70(
            x0,
            allowed_cells=frozenset(cells),
            by_color=True,
        )
        if (x1[color] == x2 and x3 == ONE) or len(comps) > ONE:
            add(filled)
    for color, cells in x4.items():
        if x1[color] < x2:
            add(frozenset((color, loc) for loc in cells))
    if even(w):
        hw = halve(w)
        for start in (ZERO, hw):
            add(
                frozenset(
                    (index(x0, (i, j)), (i, j))
                    for i in range(h)
                    for j in range(start, start + hw)
                    if index(x0, (i, j)) != ZERO
                )
            )
    if even(h):
        hh = halve(h)
        for start in (ZERO, hh):
            add(
                frozenset(
                    (index(x0, (i, j)), (i, j))
                    for i in range(start, start + hh)
                    for j in range(w)
                    if index(x0, (i, j)) != ZERO
                )
            )
    if even(h) and even(w):
        hh = halve(h)
        hw = halve(w)
        for si in (ZERO, hh):
            for sj in (ZERO, hw):
                add(
                    frozenset(
                        (index(x0, (i, j)), (i, j))
                        for i in range(si, si + hh)
                        for j in range(sj, sj + hw)
                        if index(x0, (i, j)) != ZERO
                    )
                )
    return tuple(out)


def match_variant_3ed85e70(
    grid: Grid,
    cells: frozenset[tuple[int, int]],
    variant: tuple[Object, tuple[int, int]],
) -> bool:
    obj, anchor = variant
    ai, aj, _, _ = bbox_3ed85e70(cells)
    x0 = frozenset((index(grid, loc), subtract(loc, (ai, aj))) for loc in cells)
    x1 = frozenset((color, subtract(loc, anchor)) for color, loc in obj)
    return x0 == x1


def ring_pattern_3ed85e70(
    outer: int,
    inner: int,
) -> Object:
    return object_from_rows_3ed85e70(
        (
            (outer, outer, outer, outer),
            (outer, inner, inner, outer),
            (outer, inner, inner, outer),
            (outer, outer, outer, outer),
        )
    )


def center_pattern_3ed85e70(
    outer: int,
    inner: int,
) -> Object:
    return object_from_rows_3ed85e70(
        (
            (outer, outer, outer),
            (outer, inner, outer),
            (outer, outer, outer),
        )
    )


def antidiag_pattern_3ed85e70(
    outer: int,
    inner: int,
) -> Object:
    return object_from_rows_3ed85e70(
        (
            (outer, outer, inner),
            (outer, inner, outer),
            (inner, outer, outer),
        )
    )


def framed_pattern_3ed85e70(
    border: int,
    center: int,
) -> Object:
    return object_from_rows_3ed85e70(
        (
            (border, border, border, border, border),
            (border, center, center, center, border),
            (border, center, center, center, border),
            (border, center, center, center, border),
            (border, border, border, border, border),
        )
    )


def bars_pattern_3ed85e70(
    border: int,
    center: int,
) -> Object:
    return object_from_rows_3ed85e70(
        (
            (border, border, border, border),
            (ZERO, center, center, ZERO),
            (ZERO, center, center, ZERO),
            (border, border, border, border),
        )
    )


def wings_pattern_3ed85e70(
    edge: int,
    middle: int,
) -> Object:
    return object_from_rows_3ed85e70(
        (
            (edge, middle, middle, edge),
            (edge, middle, middle, edge),
        )
    )


def bent_pattern_3ed85e70(
    edge: int,
    middle: int,
) -> Object:
    return object_from_rows_3ed85e70(
        (
            (edge, edge, ZERO, ZERO),
            (edge, middle, middle, ZERO),
            (ZERO, middle, middle, edge),
            (ZERO, ZERO, edge, edge),
        )
    )


def diagonal_pattern_3ed85e70(
    main: int,
    accent: int,
) -> Object:
    return object_from_rows_3ed85e70(
        (
            (main, accent),
            (accent, main),
        )
    )


def pattern_spec_3ed85e70(
    kind: str,
    colors: tuple[int, int],
) -> dict[str, object]:
    a, b = colors
    if kind == "ring":
        pattern = ring_pattern_3ed85e70(a, b)
        fragments = ((_variant_entry_3ed85e70(frozenset((b, loc) for loc in ((ONE, ONE), (ONE, TWO), (TWO, ONE), (TWO, TWO))))),)
    elif kind == "center":
        pattern = center_pattern_3ed85e70(a, b)
        fragments = (
            _variant_entry_3ed85e70(
                frozenset((a, (i, j)) for i in range(THREE) for j in range(THREE))
            ),
            _variant_entry_3ed85e70(frozenset({(b, (ONE, ONE))})),
        )
    elif kind == "antidiag":
        pattern = antidiag_pattern_3ed85e70(a, b)
        fragments = (
            _variant_entry_3ed85e70(
                frozenset((a, (i, j)) for i in range(THREE) for j in range(THREE))
            ),
        )
    elif kind == "framed":
        pattern = framed_pattern_3ed85e70(a, b)
        fragments = (
            _variant_entry_3ed85e70(
                frozenset((b, (i, j)) for i in range(ONE, FOUR) for j in range(ONE, FOUR))
            ),
        )
    elif kind == "bars":
        pattern = bars_pattern_3ed85e70(a, b)
        fragments = (
            _variant_entry_3ed85e70(
                frozenset((b, (i, j)) for i in range(ONE, THREE) for j in range(ONE, THREE))
            ),
        )
    elif kind == "wings":
        pattern = wings_pattern_3ed85e70(a, b)
        fragments = (
            _variant_entry_3ed85e70(
                frozenset(
                    (index(object_to_grid_3ed85e70(pattern), (i, j)), (i, j))
                    for i in range(TWO)
                    for j in range(TWO)
                    if index(object_to_grid_3ed85e70(pattern), (i, j)) != ZERO
                )
            ),
            _variant_entry_3ed85e70(
                frozenset(
                    (index(object_to_grid_3ed85e70(pattern), (i, j)), (i, j))
                    for i in range(TWO)
                    for j in range(TWO, FOUR)
                    if index(object_to_grid_3ed85e70(pattern), (i, j)) != ZERO
                )
            ),
        )
    elif kind == "bent":
        pattern = bent_pattern_3ed85e70(a, b)
        fragments = (
            _variant_entry_3ed85e70(
                frozenset((b, (i, j)) for i in range(ONE, THREE) for j in range(ONE, THREE))
            ),
            _variant_entry_3ed85e70(
                frozenset(
                    (index(object_to_grid_3ed85e70(pattern), (i, j)), (i, j))
                    for i in range(TWO)
                    for j in range(TWO)
                    if index(object_to_grid_3ed85e70(pattern), (i, j)) != ZERO
                )
            ),
            _variant_entry_3ed85e70(
                frozenset(
                    (index(object_to_grid_3ed85e70(pattern), (i, j)), (i, j))
                    for i in range(TWO, FOUR)
                    for j in range(TWO, FOUR)
                    if index(object_to_grid_3ed85e70(pattern), (i, j)) != ZERO
                )
            ),
        )
    else:
        pattern = diagonal_pattern_3ed85e70(a, b)
        fragments = (
            _variant_entry_3ed85e70(
                frozenset((b, (i, j)) for i in range(TWO) for j in range(TWO))
            ),
        )
    return {"kind": kind, "pattern": pattern, "fragments": fragments}
