from arc2.core import *


PANEL_SIZE_4E7E0EB9 = NINE
BLOCK_SIZE_4E7E0EB9 = THREE
STEP_4E7E0EB9 = TEN
SEPARATOR_COLOR_BY_LAYOUT_4E7E0EB9 = {
    (TWO, ONE): SEVEN,
    (TWO, TWO): FIVE,
    (TWO, THREE): FIVE,
    (THREE, THREE): NINE,
}
BLOCK_PATCH_4E7E0EB9 = asindices(canvas(ZERO, (THREE, THREE)))
BLOCK_OFFSETS_4E7E0EB9 = (
    (ONE, ONE),
    (ONE, FIVE),
    (FIVE, ONE),
    (FIVE, FIVE),
)
BASE_LAYOUTS_4E7E0EB9 = (
    ("leaf",),
    ("mirror",),
    ("partition", TWO, ONE),
    ("partition", TWO, TWO),
    ("partition", TWO, THREE),
    ("partition", THREE, THREE),
)


def _paint_block_4e7e0eb9(grid: Grid, offset: tuple[int, int], value: int) -> Grid:
    x0 = shift(BLOCK_PATCH_4E7E0EB9, offset)
    x1 = fill(grid, value, x0)
    return x1


def _leaf_panel_4e7e0eb9() -> tuple[Grid, Grid]:
    x0 = choice(tuple(value for value in range(TWO, TEN)))
    x1 = choice((ONE, ONE, TWO, TWO, THREE))
    x2 = set(sample(range(FOUR), x1))
    x3 = canvas(ZERO, (PANEL_SIZE_4E7E0EB9, PANEL_SIZE_4E7E0EB9))
    x4 = canvas(ZERO, (PANEL_SIZE_4E7E0EB9, PANEL_SIZE_4E7E0EB9))
    for x5, x6 in enumerate(BLOCK_OFFSETS_4E7E0EB9):
        x7 = x0 if x5 in x2 else ONE
        x3 = _paint_block_4e7e0eb9(x3, x6, x7)
        x4 = _paint_block_4e7e0eb9(x4, x6, x0)
    return x3, x4


def _mirror_panel_4e7e0eb9() -> tuple[Grid, Grid]:
    x0 = choice(("h", "v"))
    x1 = canvas(ZERO, (PANEL_SIZE_4E7E0EB9, PANEL_SIZE_4E7E0EB9))
    if x0 == "h":
        x1 = fill(x1, FOUR, connect((FOUR, ZERO), (FOUR, EIGHT)))
    else:
        x1 = fill(x1, FOUR, connect((ZERO, FOUR), (EIGHT, FOUR)))
    while True:
        x2 = tuple(choice(tuple(value for value in range(ONE, TEN) if value != FOUR)) for _ in range(FOUR))
        if x0 == "h":
            if x2[ZERO] != x2[TWO] or x2[ONE] != x2[THREE]:
                break
        else:
            if x2[ZERO] != x2[ONE] or x2[TWO] != x2[THREE]:
                break
    x3 = x1
    for x4, x5 in zip(x2, BLOCK_OFFSETS_4E7E0EB9):
        x3 = _paint_block_4e7e0eb9(x3, x5, x4)
    x6 = hmirror(x3) if x0 == "h" else vmirror(x3)
    return x3, x6


def _base_panel_4e7e0eb9(panel_type: str) -> tuple[Grid, Grid]:
    if panel_type == "leaf":
        return _leaf_panel_4e7e0eb9()
    return _mirror_panel_4e7e0eb9()


def _partition_panel_4e7e0eb9(nrows: int, ncols: int) -> tuple[Grid, Grid]:
    x0 = SEPARATOR_COLOR_BY_LAYOUT_4E7E0EB9[(nrows, ncols)]
    x1 = nrows * PANEL_SIZE_4E7E0EB9 + (nrows - ONE)
    x2 = ncols * PANEL_SIZE_4E7E0EB9 + (ncols - ONE)
    x3 = canvas(ZERO, (x1, x2))
    x4 = canvas(ZERO, (x1, x2))
    for x5 in range(ONE, nrows):
        x6 = x5 * STEP_4E7E0EB9 - ONE
        x7 = connect((x6, ZERO), (x6, x2 - ONE))
        x3 = fill(x3, x0, x7)
        x4 = fill(x4, x0, x7)
    for x8 in range(ONE, ncols):
        x9 = x8 * STEP_4E7E0EB9 - ONE
        x10 = connect((ZERO, x9), (x1 - ONE, x9))
        x3 = fill(x3, x0, x10)
        x4 = fill(x4, x0, x10)
    x11 = []
    for _ in range(nrows * ncols):
        x12 = choice(("leaf", "mirror"))
        x11.append(_base_panel_4e7e0eb9(x12))
    for x13, (x14, x15) in enumerate(x11):
        x16 = divide(x13, ncols)
        x17 = x13 % ncols
        x18 = multiply(x16, STEP_4E7E0EB9)
        x19 = multiply(x17, STEP_4E7E0EB9)
        x20 = shift(asobject(x14), (x18, x19))
        x21 = shift(asobject(x15), (x18, x19))
        x3 = paint(x3, x20)
        x4 = paint(x4, x21)
    return x3, x4


def generate_4e7e0eb9(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(BASE_LAYOUTS_4E7E0EB9)
        x1 = x0[ZERO]
        if x1 == "partition":
            x2, x3 = _partition_panel_4e7e0eb9(x0[ONE], x0[TWO])
        else:
            x2, x3 = _base_panel_4e7e0eb9(x1)
        if choice((T, F)):
            x2 = hmirror(x2)
            x3 = hmirror(x3)
        if choice((T, F)):
            x2 = vmirror(x2)
            x3 = vmirror(x3)
        if x2 == x3:
            continue
        return {"input": x2, "output": x3}
