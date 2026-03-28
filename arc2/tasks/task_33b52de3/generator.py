from arc2.core import *


GRID_SHAPE_33B52DE3 = (23, 23)
LEFT_DIMS_33B52DE3 = ((4, 3), (5, 3), (3, 4), (4, 4), (5, 4))
BELOW_DIMS_33B52DE3 = ((3, 4), (3, 5), (4, 3), (4, 4), (4, 5))
MOTIFS_33B52DE3 = (
    frozenset({(0, 0), (0, 1), (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)}),
)
PALETTE_COLORS_33B52DE3 = tuple(value for value in range(1, 10) if value != FIVE)


def _build_palette_33b52de3(height: int, width: int) -> Grid:
    ncolors = randint(3, min(5, height * width))
    colors = sample(PALETTE_COLORS_33B52DE3, ncolors)
    values = list(colors)
    while len(values) < height * width:
        values.append(choice(colors))
    shuffle(values)
    return tuple(
        tuple(values[width * i:width * (i + 1)])
        for i in range(height)
    )


def _array_shape_33b52de3(height: int, width: int) -> tuple[int, int]:
    return (4 * height - 1, 4 * width - 1)


def _place_layout_33b52de3(layout: str, height: int, width: int) -> tuple[int, int, int, int]:
    array_height, array_width = _array_shape_33b52de3(height, width)
    array_top = 1
    palette_left = 1
    if layout == "left":
        gap = choice((1, 2))
        array_left = palette_left + width + gap
        palette_top = randint(1, min(4, GRID_SHAPE_33B52DE3[0] - height - 1))
        return palette_top, palette_left, array_top, array_left
    array_left = randint(1, min(3, GRID_SHAPE_33B52DE3[1] - array_width - 1))
    palette_top = randint(
        array_top + array_height + 1,
        GRID_SHAPE_33B52DE3[0] - height - 1,
    )
    return palette_top, palette_left, array_top, array_left


def _palette_object_33b52de3(palette_grid: Grid, top: int, left: int) -> Object:
    return frozenset(
        (value, (top + i, left + j))
        for i, row in enumerate(palette_grid)
        for j, value in enumerate(row)
    )


def _motif_array_33b52de3(
    palette_grid: Grid,
    motif: Indices,
    top: int,
    left: int,
    use_palette_colors: bool,
) -> Object:
    obj = set()
    for i, row in enumerate(palette_grid):
        for j, value in enumerate(row):
            anchor = (top + 4 * i, left + 4 * j)
            placed = shift(motif, anchor)
            color = value if use_palette_colors else FIVE
            obj |= set(recolor(color, placed))
    return frozenset(obj)


def generate_33b52de3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    _ = (diff_lb, diff_ub)
    layout = choice(("left", "below"))
    height, width = choice(LEFT_DIMS_33B52DE3 if layout == "left" else BELOW_DIMS_33B52DE3)
    palette_grid = _build_palette_33b52de3(height, width)
    motif = choice(MOTIFS_33B52DE3)
    palette_top, palette_left, array_top, array_left = _place_layout_33b52de3(layout, height, width)
    palette_obj = _palette_object_33b52de3(palette_grid, palette_top, palette_left)
    input_array = _motif_array_33b52de3(palette_grid, motif, array_top, array_left, False)
    output_array = _motif_array_33b52de3(palette_grid, motif, array_top, array_left, True)
    blank = canvas(ZERO, GRID_SHAPE_33B52DE3)
    gi = paint(paint(blank, palette_obj), input_array)
    go = paint(paint(blank, palette_obj), output_array)
    return {"input": gi, "output": go}
