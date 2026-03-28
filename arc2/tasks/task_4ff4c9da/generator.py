from collections import defaultdict

from arc2.core import *

from .helpers import (
    _assemble_tiles_4ff4c9da,
    _col_bands_4ff4c9da,
    _render_template_4ff4c9da,
    _row_bands_4ff4c9da,
    _tile_signature_4ff4c9da,
)


INPUT_TEMPLATES_4FF4C9DA = {
    (ONE, ONE): (
        ("0",),
        ("a",),
    ),
    (ONE, THREE): (
        ("000",),
        ("00a",),
        ("00s",),
        ("a00",),
        ("aa0",),
        ("aaa",),
        ("sa0",),
    ),
    (THREE, ONE): (
        ("0", "0", "0"),
        ("0", "0", "a"),
        ("0", "0", "s"),
        ("a", "0", "0"),
        ("a", "a", "0"),
        ("a", "a", "a"),
        ("s", "a", "0"),
    ),
    (TWO, TWO): (
        ("00", "00"),
        ("00", "aa"),
        ("00", "ss"),
        ("0a", "0a"),
        ("0a", "aa"),
        ("0a", "sa"),
        ("0s", "0s"),
        ("0s", "aa"),
        ("0s", "ss"),
        ("a0", "a0"),
        ("a0", "aa"),
        ("a0", "as"),
        ("aa", "00"),
        ("aa", "0a"),
        ("aa", "0s"),
        ("aa", "a0"),
        ("aa", "s0"),
        ("aa", "sa"),
        ("as", "a0"),
        ("as", "aa"),
        ("s0", "aa"),
        ("s0", "s0"),
        ("s0", "ss"),
        ("sa", "0a"),
        ("sa", "aa"),
        ("sa", "sa"),
        ("ss", "00"),
        ("ss", "0s"),
        ("ss", "aa"),
        ("ss", "s0"),
    ),
    (THREE, THREE): (
        ("000", "000", "000"),
        ("00a", "00a", "aaa"),
        ("00a", "00a", "ssa"),
        ("00a", "aaa", "00a"),
        ("00s", "00s", "aaa"),
        ("00s", "00s", "sss"),
        ("0a0", "0a0", "aaa"),
        ("0a0", "aaa", "0a0"),
        ("a00", "a00", "aaa"),
        ("a00", "aaa", "a00"),
        ("aa0", "aa0", "aaa"),
        ("aa0", "aa0", "aas"),
        ("aaa", "00a", "00a"),
        ("aaa", "0a0", "0a0"),
        ("aaa", "a00", "a00"),
        ("aaa", "aa0", "aa0"),
        ("aaa", "aaa", "00a"),
        ("aaa", "aaa", "00s"),
        ("aaa", "aaa", "a00"),
        ("aaa", "aaa", "aa0"),
        ("sa0", "sa0", "aaa"),
        ("sa0", "sa0", "sas"),
        ("sas", "asa", "sa0"),
        ("ssa", "aaa", "00a"),
    ),
}

SEED_TEMPLATES_4FF4C9DA = {
    (ONE, THREE): (
        ("880",),
    ),
    (THREE, ONE): (
        ("8", "8", "0"),
    ),
    (TWO, TWO): (
        ("88", "80"),
        ("s8", "88"),
    ),
    (THREE, THREE): (
        ("080", "888", "080"),
        ("s8s", "8s8", "s80"),
        ("sss", "888", "00s"),
    ),
}

LAYOUTS_4FF4C9DA = (
    ("simple3", (THREE, THREE, THREE, THREE, ONE), F),
    ("simple3", (THREE, ONE, ONE, THREE, THREE, ONE, ONE, THREE), F),
    ("simple3", (THREE, THREE, THREE, THREE, THREE, ONE), F),
    ("mixed3", (THREE, THREE, THREE, THREE, ONE), F),
    ("mixed3", (THREE, ONE, ONE, THREE, THREE, ONE, ONE, THREE), F),
    ("mixed3", (THREE, THREE, THREE, THREE, THREE, ONE), F),
    ("mini2", (TWO, TWO, TWO, TWO, TWO, TWO, TWO, TWO, TWO), T),
)


def _normalize_cells_4ff4c9da(
    cells: frozenset[tuple[int, int]],
) -> frozenset[tuple[int, int]]:
    if len(cells) == ZERO:
        return frozenset()
    x0 = min(i for i, _ in cells)
    x1 = min(j for _, j in cells)
    return frozenset((i - x0, j - x1) for i, j in cells)


def _template_patch_4ff4c9da(
    template: tuple[str, ...],
    token: str,
) -> frozenset[tuple[int, int]]:
    return frozenset(
        (i, j)
        for i, row in enumerate(template)
        for j, cell in enumerate(row)
        if cell == token
    )


def _target_shape_4ff4c9da(
    template: tuple[str, ...],
) -> frozenset[tuple[int, int]]:
    return _normalize_cells_4ff4c9da(_template_patch_4ff4c9da(template, "a"))


def _seed_shape_4ff4c9da(
    template: tuple[str, ...],
) -> frozenset[tuple[int, int]]:
    return _normalize_cells_4ff4c9da(_template_patch_4ff4c9da(template, "8"))


def _uses_separator_4ff4c9da(
    template: tuple[str, ...],
) -> bool:
    return any("s" in row for row in template)


def _theme_dims_4ff4c9da(
    theme: str,
) -> tuple[tuple[int, int], ...]:
    if theme == "mini2":
        return ((TWO, TWO),)
    return (
        (ONE, ONE),
        (ONE, THREE),
        (THREE, ONE),
        (THREE, THREE),
    )


def _theme_allows_4ff4c9da(
    theme: str,
    template: tuple[str, ...],
) -> bool:
    if theme == "mini2":
        return T
    if theme == "simple3":
        return not _uses_separator_4ff4c9da(template)
    return T


def _theme_target_pools_4ff4c9da(
    theme: str,
) -> tuple[
    dict[tuple[int, int], tuple[tuple[str, ...], ...]],
    dict[tuple[int, int], tuple[tuple[str, ...], ...]],
    dict[tuple[tuple[int, int], frozenset[tuple[int, int]]], tuple[tuple[str, ...], ...]],
]:
    x0 = {}
    x1 = defaultdict(list)
    x2 = defaultdict(list)
    for dims in _theme_dims_4ff4c9da(theme):
        x3 = tuple(
            template
            for template in INPUT_TEMPLATES_4FF4C9DA[dims]
            if _theme_allows_4ff4c9da(theme, template)
        )
        if len(x3) == ZERO:
            continue
        x0[dims] = x3
        for template in x3:
            x4 = _target_shape_4ff4c9da(template)
            if len(x4) == ZERO:
                x1[dims].append(template)
            else:
                x2[(dims, x4)].append(template)
    x5 = {dims: tuple(values) for dims, values in x1.items()}
    x6 = {key: tuple(values) for key, values in x2.items()}
    return x0, x5, x6


def _theme_seed_pools_4ff4c9da(
    theme: str,
) -> dict[tuple[tuple[int, int], frozenset[tuple[int, int]]], tuple[tuple[str, ...], ...]]:
    x0 = defaultdict(list)
    for dims in _theme_dims_4ff4c9da(theme):
        for template in SEED_TEMPLATES_4FF4C9DA.get(dims, ()):
            if not _theme_allows_4ff4c9da(theme, template):
                continue
            x1 = _seed_shape_4ff4c9da(template)
            x0[(dims, x1)].append(template)
    return {key: tuple(values) for key, values in x0.items()}


def _positions_by_dims_4ff4c9da(
    sizes: tuple[int, ...],
) -> dict[tuple[int, int], tuple[tuple[int, int], ...]]:
    x0 = defaultdict(list)
    for i, rh in enumerate(sizes):
        for j, cw in enumerate(sizes):
            x0[(rh, cw)].append((i, j))
    return {dims: tuple(values) for dims, values in x0.items()}


def _instantiate_template_4ff4c9da(
    template: tuple[str, ...],
    separator: Integer,
    accent: Integer,
) -> Grid:
    return _render_template_4ff4c9da(template, separator, accent)


def _output_template_4ff4c9da(
    template: tuple[str, ...],
    dims: tuple[int, int],
    active_shapes: frozenset[tuple[tuple[int, int], frozenset[tuple[int, int]]]],
) -> tuple[str, ...]:
    if any("8" in row for row in template):
        return template
    x0 = _target_shape_4ff4c9da(template)
    if len(x0) == ZERO:
        return template
    if (dims, x0) not in active_shapes:
        return template
    return tuple(row.replace("a", "8") for row in template)


def _append_trailing_separator_4ff4c9da(
    grid: Grid,
    separator: Integer,
) -> Grid:
    x0 = canvas(separator, (height(grid), ONE))
    x1 = hconcat(grid, x0)
    x2 = canvas(separator, (ONE, width(x1)))
    return vconcat(x1, x2)


def _apply_rule_4ff4c9da(
    grid: Grid,
) -> Grid:
    x0 = mostcolor(grid)
    x1 = _row_bands_4ff4c9da(grid)
    x2 = _col_bands_4ff4c9da(grid)
    x3 = frozenset()
    x4 = []
    for x5, x6 in x1:
        for x7, x8 in x2:
            x9 = crop(grid, (x5, x7), (x6 - x5, x8 - x7))
            x10, x11, x12 = _tile_signature_4ff4c9da(x9, x0)
            if len(x10) > ZERO:
                x3 = combine(x3, initset(x10))
            x4.append(((x5, x7), x11, x12))
    x13 = grid
    for x14, x15, x16 in x4:
        if len(x15) == ZERO:
            continue
        if x16 not in x3:
            continue
        x17 = shift(x15, x14)
        x13 = fill(x13, EIGHT, x17)
    return x13


def generate_4ff4c9da(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = LAYOUTS_4FF4C9DA[unifint(diff_lb, diff_ub, (ZERO, len(LAYOUTS_4FF4C9DA) - ONE))]
        x1, x2, x3 = x0
        x4 = choice((ONE, TWO))
        x5 = TWO if x4 == ONE else ONE
        x6, x7, x8 = _theme_target_pools_4ff4c9da(x1)
        x9 = _theme_seed_pools_4ff4c9da(x1)
        x10 = _positions_by_dims_4ff4c9da(x2)
        x11 = []
        for x12, x13 in x9.items():
            if x12 not in x8:
                continue
            x14 = x10.get(x12[ZERO], ())
            if len(x14) < THREE:
                continue
            x11.append((x12, x14))
        if len(x11) == ZERO:
            continue
        shuffle(x11)
        x15 = ONE if x1 == "mini2" else unifint(diff_lb, diff_ub, (ONE, TWO))
        x16 = []
        x17 = set()
        for x18, x19 in x11:
            x20 = [pos for pos in x19 if pos not in x17]
            if len(x20) < THREE:
                continue
            shuffle(x20)
            x21 = min(len(x20), choice((THREE, THREE, FOUR, FIVE)))
            if x21 < THREE:
                continue
            x22 = tuple(x20[:x21])
            x16.append((x18, x22))
            x17.update(x22)
            if len(x16) >= x15:
                break
        if len(x16) == ZERO:
            continue
        x23 = frozenset(key for key, _ in x16)
        x24 = {}
        for x25, x26 in x16:
            x27 = list(x26)
            shuffle(x27)
            x28 = x27[ZERO]
            x24[x28] = choice(x9[x25])
            for pos in x27[ONE:]:
                x24[pos] = choice(x8[x25])
        x29 = {}
        for dims, values in x10.items():
            x30 = [key[ONE] for key in x8 if key[ZERO] == dims and key not in x23]
            shuffle(x30)
            if len(x30) == ZERO:
                x29[dims] = tuple()
                continue
            x31 = min(len(x30), max(ONE, unifint(diff_lb, diff_ub, (ONE, THREE))))
            x29[dims] = tuple(x30[:x31])
        for i in range(len(x2)):
            for j in range(len(x2)):
                pos = (i, j)
                if pos in x24:
                    continue
                dims = (x2[i], x2[j])
                x32 = list(x7.get(dims, ()))
                x33 = []
                for shape in x29.get(dims, ()):
                    x33.extend(x8[(dims, shape)])
                if len(x33) > ZERO and (len(x32) == ZERO or randint(ZERO, THREE) > ZERO):
                    x24[pos] = choice(tuple(x33))
                    continue
                if len(x32) > ZERO:
                    x24[pos] = choice(tuple(x32))
                    continue
                x24[pos] = choice(x6[dims])
        x34 = []
        x35 = []
        for i in range(len(x2)):
            x36 = []
            x37 = []
            for j in range(len(x2)):
                dims = (x2[i], x2[j])
                x38 = x24[(i, j)]
                x39 = _output_template_4ff4c9da(x38, dims, x23)
                x36.append(_instantiate_template_4ff4c9da(x38, x4, x5))
                x37.append(_instantiate_template_4ff4c9da(x39, x4, x5))
            x34.append(tuple(x36))
            x35.append(tuple(x37))
        x40 = _assemble_tiles_4ff4c9da(tuple(x34), x4)
        x41 = _assemble_tiles_4ff4c9da(tuple(x35), x4)
        if x3:
            x40 = _append_trailing_separator_4ff4c9da(x40, x4)
            x41 = _append_trailing_separator_4ff4c9da(x41, x4)
        if height(x40) != width(x40):
            continue
        if mostcolor(x40) != x4:
            continue
        if tuple(b - a for a, b in _row_bands_4ff4c9da(x40)) != x2:
            continue
        if tuple(b - a for a, b in _col_bands_4ff4c9da(x40)) != x2:
            continue
        if x40 == x41:
            continue
        if _apply_rule_4ff4c9da(x40) != x41:
            continue
        return {"input": x40, "output": x41}
