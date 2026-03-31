from synth_rearc.core import *

from .helpers import Block3E6067C3
from .helpers import apply_path_3e6067c3
from .helpers import extract_state_3e6067c3
from .helpers import recover_path_3e6067c3


GRID_SHAPES_3E6067C3 = (
    (TWO, FOUR),
    (THREE, THREE),
    (THREE, FOUR),
    (FOUR, THREE),
    (FOUR, FOUR),
)


def _neighbors_3e6067c3(
    cell: IntegerTuple,
    h: Integer,
    w: Integer,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = cell
    x2 = []
    for x3, x4 in ((-ONE, ZERO), (ONE, ZERO), (ZERO, -ONE), (ZERO, ONE)):
        x5 = x0 + x3
        x6 = x1 + x4
        if ZERO <= x5 < h and ZERO <= x6 < w:
            x2.append((x5, x6))
    return tuple(x2)


def _randomized_3e6067c3(
    values: tuple,
) -> tuple:
    if len(values) <= ONE:
        return values
    return tuple(sample(values, len(values)))


def _path_has_turn_3e6067c3(
    path: tuple[IntegerTuple, ...],
) -> Boolean:
    if len(path) < THREE:
        return F
    for x0, x1, x2 in zip(path, path[ONE:], path[TWO:]):
        x3 = subtract(x1, x0)
        x4 = subtract(x2, x1)
        if x3 != x4:
            return T
    return F


def _path_has_both_axes_3e6067c3(
    path: tuple[IntegerTuple, ...],
) -> Boolean:
    x0 = F
    x1 = F
    for x2, x3 in zip(path, path[ONE:]):
        x4 = subtract(x3, x2)
        if x4[ZERO] != ZERO:
            x0 = T
        if x4[ONE] != ZERO:
            x1 = T
    return both(x0, x1)


def _build_path_3e6067c3(
    cell: IntegerTuple,
    h: Integer,
    w: Integer,
    length: Integer,
    used: frozenset[IntegerTuple],
) -> tuple[IntegerTuple, ...] | None:
    if len(used) == length:
        return (cell,)
    x0 = _randomized_3e6067c3(_neighbors_3e6067c3(cell, h, w))
    for x1 in x0:
        if x1 in used:
            continue
        x2 = _build_path_3e6067c3(x1, h, w, length, used | frozenset({x1}))
        if x2 is not None:
            return (cell,) + x2
    return None


def _sample_lattice_path_3e6067c3(
    gh: Integer,
    gw: Integer,
    length: Integer,
) -> tuple[IntegerTuple, ...]:
    x0 = tuple((x1, x2) for x1 in range(gh) for x2 in range(gw))
    for _ in range(300):
        x3 = choice(x0)
        x4 = _build_path_3e6067c3(x3, gh, gw, length, frozenset({x3}))
        if x4 is None:
            continue
        if not _path_has_turn_3e6067c3(x4):
            continue
        if not _path_has_both_axes_3e6067c3(x4):
            continue
        return x4
    return tuple()


def _sample_sequence_3e6067c3(
    length: Integer,
    background: Integer,
    base: Integer,
) -> tuple[Integer, ...]:
    x0 = tuple(x1 for x1 in interval(ZERO, TEN, ONE) if x1 not in (background, base))
    x2 = tuple()
    x3 = branch(length > len(x0), T, choice((T, F, F)))
    while len(x2) < length:
        x4 = choice(x0)
        if len(x2) > ZERO and x4 == x2[-ONE]:
            continue
        if not x3 and x4 in x2:
            continue
        x2 = x2 + (x4,)
    return x2


def _interval_positions_3e6067c3(
    count: Integer,
    tile: Integer,
    lb: Integer,
    ub: Integer,
) -> tuple[Integer, ...]:
    x0 = [randint(ONE, TWO)]
    for _ in range(count - ONE):
        x1 = randint(lb, ub)
        x0.append(x0[-ONE] + tile + x1)
    return tuple(x0)


def _minimum_extent_3e6067c3(
    count: Integer,
    tile: Integer,
) -> Integer:
    return count * tile + count + TWO


def _center_offset_3e6067c3(
    tile: Integer,
    mark: Integer,
) -> Integer:
    return (tile - mark) // TWO


def _make_block_3e6067c3(
    color: Integer,
    top: Integer,
    left: Integer,
    tile: Integer,
    mark: Integer,
) -> Block3E6067C3:
    x0 = _center_offset_3e6067c3(tile, mark)
    x1 = top + x0
    x2 = left + x0
    return Block3E6067C3(
        color=color,
        outer_top=top,
        outer_left=left,
        outer_bottom=top + tile - ONE,
        outer_right=left + tile - ONE,
        inner_top=x1,
        inner_left=x2,
        inner_bottom=x1 + mark - ONE,
        inner_right=x2 + mark - ONE,
    )


def _paint_block_3e6067c3(
    grid: Grid,
    block: Block3E6067C3,
    base: Integer,
) -> Grid:
    x0 = frozenset(
        (x1, x2)
        for x1 in range(block.outer_top, block.outer_bottom + ONE)
        for x2 in range(block.outer_left, block.outer_right + ONE)
    )
    x1 = frozenset(
        (x2, x3)
        for x2 in range(block.inner_top, block.inner_bottom + ONE)
        for x3 in range(block.inner_left, block.inner_right + ONE)
    )
    x2 = fill(grid, base, x0)
    x3 = fill(x2, block.color, x1)
    return x3


def _legend_row_3e6067c3(
    grid: Grid,
    legend: tuple[Integer, ...],
    row: Integer,
    left: Integer,
) -> Grid:
    x0 = grid
    for x1, x2 in enumerate(legend):
        x3 = left + double(x1)
        x0 = fill(x0, x2, frozenset({(row, x3)}))
    return x0


def _sample_decoys_3e6067c3(
    gh: Integer,
    gw: Integer,
    path: tuple[IntegerTuple, ...],
    colors: tuple[Integer, ...],
    top_positions: tuple[Integer, ...],
    left_positions: tuple[Integer, ...],
    tile: Integer,
    mark: Integer,
) -> tuple[Block3E6067C3, ...]:
    x0 = tuple((x1, x2) for x1 in range(gh) for x2 in range(gw) if (x1, x2) not in path)
    if len(x0) == ZERO or not choice((T, F, F, F)):
        return tuple()
    x3 = randint(ONE, min(TWO, len(x0)))
    x4 = tuple(sample(x0, x3))
    return tuple(
        _make_block_3e6067c3(choice(colors), top_positions[x5[ZERO]], left_positions[x5[ONE]], tile, mark)
        for x5 in x4
    )


def generate_3e6067c3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(GRID_SHAPES_3E6067C3)
        x1, x2 = x0
        x3 = min(x1 * x2, branch(greater(x1 * x2, EIGHT), NINE, EIGHT))
        x4 = unifint(diff_lb, diff_ub, (SIX, x3))
        x5 = _sample_lattice_path_3e6067c3(x1, x2, x4)
        if len(x5) != x4:
            continue
        x6 = choice((THREE, FOUR, FIVE, SIX))
        x7 = branch(even(x6), TWO, ONE)
        if _minimum_extent_3e6067c3(x1, x6) > 30:
            continue
        if _minimum_extent_3e6067c3(x2, x6) > 30:
            continue
        x8 = choice(interval(ZERO, TEN, ONE))
        x9 = choice(remove(x8, interval(ZERO, TEN, ONE)))
        x10 = _sample_sequence_3e6067c3(x4, x8, x9)
        x11 = _interval_positions_3e6067c3(x1, x6, ONE, min(THREE, x6))
        x12 = _interval_positions_3e6067c3(x2, x6, ONE, min(FOUR, increment(x6)))
        x13 = tuple(
            _make_block_3e6067c3(x14, x11[x15[ZERO]], x12[x15[ONE]], x6, x7)
            for x14, x15 in zip(x10, x5)
        )
        x14 = _sample_decoys_3e6067c3(x1, x2, x5, x10, x11, x12, x6, x7)
        x15 = x13 + x14
        x16 = max(x17.outer_bottom for x17 in x15) + randint(ONE, max(TWO, x6))
        x18 = randint(ONE, THREE)
        x19 = ONE
        x20 = x19 + double(x4 - ONE)
        x21 = max(max(x22.outer_right for x22 in x15) + randint(TWO, x6 + TWO), x20 + randint(TWO, FOUR))
        x23 = x16 + x18 + ONE
        if x23 > 30 or x21 + ONE > 30:
            continue
        x24 = canvas(x8, (x23, x21 + ONE))
        x25 = x24
        for x26 in x15:
            x25 = _paint_block_3e6067c3(x25, x26, x9)
        x25 = _legend_row_3e6067c3(x25, x10, x16, x19)
        x27 = apply_path_3e6067c3(x25, x13)
        if x27 == x25:
            continue
        x28 = extract_state_3e6067c3(x25)
        try:
            x29, _ = recover_path_3e6067c3(x25, x28)
        except ValueError:
            continue
        x30 = tuple(x28.blocks[x31].color for x31 in x29)
        if x30 != x10:
            continue
        if x27 != apply_path_3e6067c3(x25, tuple(x28.blocks[x32] for x32 in x29)):
            continue
        return {"input": x25, "output": x27}
