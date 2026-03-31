from __future__ import annotations

from collections import deque

from synth_rearc.core import *


ORIENTATION_POOL_8698868D = (
    identity,
    rot180,
    hmirror,
    vmirror,
)


FAMILY_SPECS_8698868D = {
    2: {
        "counts": (1, 2),
        "small_side": 4,
        "big_rows": 1,
        "big_cols": 2,
        "height_bounds": (18, 22),
        "width_bounds": (14, 18),
        "zones": ("below", "below", "below", "right"),
    },
    4: {
        "counts": (1, 2, 3, 4),
        "small_side": 6,
        "big_rows": 2,
        "big_cols": 2,
        "height_bounds": (27, 30),
        "width_bounds": (27, 30),
        "zones": ("right", "below", "right", "below"),
    },
    6: {
        "counts": (0, 1, 2, 3, 4, 5),
        "small_side": 5,
        "big_rows": 2,
        "big_cols": 3,
        "height_bounds": (30, 30),
        "width_bounds": (30, 30),
        "zones": ("below", "below", "below", "right"),
    },
}


def mutable_canvas_8698868d(
    value: Integer,
    dimensions: IntegerTuple,
) -> list[list[Integer]]:
    return [[value for _ in range(dimensions[1])] for _ in range(dimensions[0])]


def format_grid_8698868d(
    grid: list[list[Integer]],
) -> Grid:
    return tuple(tuple(row) for row in grid)


def place_block_8698868d(
    grid: list[list[Integer]],
    block: Grid,
    top_left: IntegerTuple,
) -> None:
    x0, x1 = top_left
    for x2, x3 in enumerate(block):
        for x4, x5 in enumerate(x3):
            grid[x0 + x2][x1 + x4] = x5


def background_component_count_8698868d(
    grid: Grid,
    value: Integer,
) -> Integer:
    x0 = len(grid)
    x1 = len(grid[0])
    x2 = set()
    x3 = 0
    for x4 in range(x0):
        for x5 in range(x1):
            if grid[x4][x5] != value or (x4, x5) in x2:
                continue
            x3 += 1
            x6 = deque([(x4, x5)])
            x2.add((x4, x5))
            while len(x6) > 0:
                x7, x8 = x6.popleft()
                for x9, x10 in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x11 = x7 + x9
                    x12 = x8 + x10
                    x13 = (x11, x12)
                    if not (0 <= x11 < x0 and 0 <= x12 < x1):
                        continue
                    if x13 in x2 or grid[x11][x12] != value:
                        continue
                    x2.add(x13)
                    x6.append(x13)
    return x3


def extract_square_panels_8698868d(
    grid: Grid,
) -> tuple[Integer, tuple[dict[str, object], ...], tuple[dict[str, object], ...]]:
    x0 = mostcolor(grid)
    x1 = []
    for x2 in objects(grid, T, F, F):
        x3 = color(x2)
        if x3 == x0:
            continue
        x4 = shape(x2)
        if x4[0] != x4[1] or x4[0] < 4:
            continue
        x5 = ulcorner(x2)
        x6 = crop(grid, x5, x4)
        x1.append(
            {
                "color": x3,
                "grid": x6,
                "top_left": x5,
                "side": x4[0],
            }
        )
    if len(x1) == 0:
        return x0, tuple(), tuple()
    x7 = sorted({x8["side"] for x8 in x1})
    x8 = x7[-1]
    x9 = x7[0]
    x10 = tuple(sorted((x11 for x11 in x1 if x11["side"] == x8), key=lambda x11: x11["top_left"]))
    x11 = tuple(sorted((x12 for x12 in x1 if x12["side"] == x9), key=lambda x12: x12["top_left"]))
    return x0, x10, x11


def compose_block_8698868d(
    frame_color: Integer,
    pattern_grid: Grid,
    bg: Integer,
) -> Grid:
    x0 = len(pattern_grid)
    x1 = mutable_canvas_8698868d(frame_color, (x0 + 2, x0 + 2))
    for x2, x3 in enumerate(pattern_grid):
        for x4, x5 in enumerate(x3):
            if x5 == bg:
                continue
            x1[x2 + 1][x4 + 1] = x5
    return format_grid_8698868d(x1)


def assemble_output_8698868d(
    grid: Grid,
) -> Grid:
    x0, x1, x2 = extract_square_panels_8698868d(grid)
    if len(x1) == 0 or len(x2) == 0:
        return grid
    x3 = {background_component_count_8698868d(x4["grid"], x0): x4 for x4 in x2}
    x4 = {}
    for x5 in x1:
        x6 = x5["top_left"][0]
        x4.setdefault(x6, []).append(x5)
    x7 = []
    for x8 in sorted(x4):
        x9 = sorted(x4[x8], key=lambda x10: x10["top_left"][1])
        x10 = x9[0]["side"]
        x11 = [[] for _ in range(x10)]
        for x12 in x9:
            x13 = background_component_count_8698868d(x12["grid"], x0)
            x14 = x3[x13]
            x15 = compose_block_8698868d(x12["color"], x14["grid"], x0)
            for x16, x17 in enumerate(x15):
                x11[x16].extend(x17)
        x7.extend(tuple(x18) for x18 in x11)
    return tuple(x7)


def available_colors_8698868d(
    bg: Integer,
) -> tuple[Integer, ...]:
    return tuple(x0 for x0 in range(10) if x0 != bg)


def _independent_seed_pool_8698868d(
    side: Integer,
) -> tuple[IntegerTuple, ...]:
    x0 = side - 2
    x1 = tuple((x2, x3) for x2 in range(x0) for x3 in range(x0) if (x2 + x3) % 2 == 0)
    x2 = tuple((x3, x4) for x3 in range(x0) for x4 in range(x0) if (x3 + x4) % 2 == 1)
    return x1 if len(x1) >= len(x2) else x2


def _can_add_cell_8698868d(
    cell: IntegerTuple,
    components: list[set[IntegerTuple]],
    index: Integer,
    inner_side: Integer,
) -> Boolean:
    x0, x1 = cell
    if not (0 <= x0 < inner_side and 0 <= x1 < inner_side):
        return False
    for x2, x3 in enumerate(components):
        if cell in x3:
            return False
        if x2 == index:
            continue
        if any(abs(x0 - x4) + abs(x1 - x5) == 1 for x4, x5 in x3):
            return False
    return True


def sample_hole_cells_8698868d(
    side: Integer,
    component_count: Integer,
    mode: str,
) -> frozenset[IntegerTuple]:
    if component_count == 0:
        return frozenset()
    x0 = side - 2
    x1 = list(_independent_seed_pool_8698868d(side))
    if component_count > len(x1):
        raise ValueError("too many components for panel side")
    x2 = [set([x3]) for x3 in sample(x1, component_count)]
    x3 = 2 if mode == "frame" else min(5, max(2, x0))
    x4 = randint(0, component_count if mode == "frame" else component_count + side)
    for _ in range(x4):
        x5 = list(range(component_count))
        shuffle(x5)
        x6 = False
        for x7 in x5:
            if len(x2[x7]) >= x3:
                continue
            x8 = set()
            for x9, x10 in x2[x7]:
                for x11, x12 in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    x13 = (x9 + x11, x10 + x12)
                    if _can_add_cell_8698868d(x13, x2, x7, x0):
                        x8.add(x13)
            if len(x8) == 0:
                continue
            x2[x7].add(choice(tuple(x8)))
            x6 = True
            break
        if not x6:
            break
    x5 = set()
    for x6 in x2:
        for x7, x8 in x6:
            x5.add((x7 + 1, x8 + 1))
    return frozenset(x5)


def build_panel_8698868d(
    side: Integer,
    color_value: Integer,
    bg: Integer,
    component_count: Integer,
    mode: str,
) -> Grid:
    x0 = mutable_canvas_8698868d(color_value, (side, side))
    x1 = sample_hole_cells_8698868d(side, component_count, mode)
    for x2, x3 in x1:
        x0[x2][x3] = bg
    x4 = format_grid_8698868d(x0)
    if background_component_count_8698868d(x4, bg) != component_count:
        raise ValueError("panel sampling drifted")
    return x4


def _rectangles_overlap_8698868d(
    left: tuple[Integer, Integer, Integer, Integer],
    right: tuple[Integer, Integer, Integer, Integer],
) -> Boolean:
    return not (
        left[2] < right[0]
        or right[2] < left[0]
        or left[3] < right[1]
        or right[3] < left[1]
    )


def _expanded_rect_8698868d(
    rect: tuple[Integer, Integer, Integer, Integer],
    pad: Integer,
) -> tuple[Integer, Integer, Integer, Integer]:
    return (rect[0] - pad, rect[1] - pad, rect[2] + pad, rect[3] + pad)


def sample_scatter_positions_8698868d(
    canvas_shape: IntegerTuple,
    block_side: Integer,
    amount: Integer,
    reserved_rect: tuple[Integer, Integer, Integer, Integer],
    zones: tuple[str, ...],
) -> tuple[IntegerTuple, ...]:
    x0, x1 = canvas_shape
    x2 = []
    x3 = [reserved_rect]
    for _ in range(amount):
        x4 = False
        for _ in range(1200):
            x5 = choice(zones)
            if x5 == "right" and reserved_rect[3] + 2 <= x1 - block_side:
                x6 = randint(0, x0 - block_side)
                x7 = randint(reserved_rect[3] + 2, x1 - block_side)
            elif x5 == "below" and reserved_rect[2] + 2 <= x0 - block_side:
                x6 = randint(reserved_rect[2] + 2, x0 - block_side)
                x7 = randint(0, x1 - block_side)
            else:
                x6 = randint(0, x0 - block_side)
                x7 = randint(0, x1 - block_side)
            x8 = (x6, x7, x6 + block_side - 1, x7 + block_side - 1)
            if any(
                _rectangles_overlap_8698868d(x8, _expanded_rect_8698868d(x9, 1))
                for x9 in x3
            ):
                continue
            x2.append((x6, x7))
            x3.append(x8)
            x4 = True
            break
        if not x4:
            return tuple()
    return tuple(x2)


def build_family_example_8698868d(
    pair_count: Integer,
) -> Grid:
    x0 = FAMILY_SPECS_8698868D[pair_count]
    x1 = x0["small_side"]
    x2 = x1 + 2
    x3 = x0["big_rows"]
    x4 = x0["big_cols"]
    x5 = x0["counts"]
    while True:
        x6 = choice(tuple(range(10)))
        x7 = available_colors_8698868d(x6)
        x8 = sample(x7, pair_count)
        x9 = sample(x7, pair_count)
        x10 = list(x5)
        shuffle(x10)
        x11 = list(x5)
        shuffle(x11)
        x12 = randint(*x0["height_bounds"])
        x13 = randint(*x0["width_bounds"])
        if x12 < x3 * x2 + 2 or x13 < x4 * x2 + 2:
            continue
        x14 = (0, 0, x3 * x2 - 1, x4 * x2 - 1)
        x15 = sample_scatter_positions_8698868d((x12, x13), x1, pair_count, x14, x0["zones"])
        if len(x15) != pair_count:
            continue
        x16 = mutable_canvas_8698868d(x6, (x12, x13))
        x17 = []
        for x18, x19 in enumerate(x8):
            x20 = build_panel_8698868d(x2, x19, x6, x10[x18], "frame")
            x17.append(x20)
        x18 = []
        for x19, x20 in enumerate(x9):
            x21 = build_panel_8698868d(x1, x20, x6, x11[x19], "pattern")
            x18.append(x21)
        x19 = 0
        for x20 in range(x3):
            for x21 in range(x4):
                place_block_8698868d(x16, x17[x19], (x20 * x2, x21 * x2))
                x19 += 1
        x22 = list(range(pair_count))
        shuffle(x22)
        for x23, x24 in zip(x22, x15):
            place_block_8698868d(x16, x18[x23], x24)
        x25 = format_grid_8698868d(x16)
        if mostcolor(x25) != x6:
            continue
        x26, x27, x28 = extract_square_panels_8698868d(x25)
        if x26 != x6 or len(x27) != pair_count or len(x28) != pair_count:
            continue
        return x25
