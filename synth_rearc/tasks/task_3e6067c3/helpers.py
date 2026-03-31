from dataclasses import dataclass

from synth_rearc.core import *


@dataclass(frozen=True)
class Block3E6067C3:
    color: Integer
    outer_top: Integer
    outer_left: Integer
    outer_bottom: Integer
    outer_right: Integer
    inner_top: Integer
    inner_left: Integer
    inner_bottom: Integer
    inner_right: Integer


@dataclass(frozen=True)
class TaskState3E6067C3:
    background: Integer
    base: Integer
    legend_row: Integer
    legend: tuple[Integer, ...]
    blocks: tuple[Block3E6067C3, ...]


def _base_color_3e6067c3(
    grid: Grid,
    background: Integer,
) -> Integer:
    x0 = {}
    for x1 in grid:
        for x2 in x1:
            if x2 == background:
                continue
            x0[x2] = x0.get(x2, ZERO) + ONE
    return max(x0, key=x0.get)


def _legend_row_3e6067c3(
    grid: Grid,
    background: Integer,
    base: Integer,
) -> Integer:
    x0 = tuple(
        x1
        for x1, x2 in enumerate(grid)
        if base not in x2 and any(x3 != background for x3 in x2)
    )
    if len(x0) == ZERO:
        raise ValueError("missing legend row")
    return max(x0, key=lambda x4: sum(x5 != background for x5 in grid[x4]))


def _legend_sequence_3e6067c3(
    row: tuple[Integer, ...],
    background: Integer,
) -> tuple[Integer, ...]:
    return tuple(x0 for x0 in row if x0 != background)


def extract_state_3e6067c3(
    grid: Grid,
) -> TaskState3E6067C3:
    x0 = mostcolor(grid)
    x1 = _base_color_3e6067c3(grid, x0)
    x2 = _legend_row_3e6067c3(grid, x0, x1)
    x3 = _legend_sequence_3e6067c3(grid[x2], x0)
    x4 = objects(grid, F, F, T)
    x5 = []
    for x6 in x4:
        x7 = palette(x6)
        if x1 not in x7 or len(x7) != TWO:
            continue
        x8 = next(x9 for x9 in x7 if x9 != x1)
        x10 = frozenset(x11 for x12, x11 in x6 if x12 == x8)
        x13 = Block3E6067C3(
            color=x8,
            outer_top=uppermost(x6),
            outer_left=leftmost(x6),
            outer_bottom=lowermost(x6),
            outer_right=rightmost(x6),
            inner_top=uppermost(x10),
            inner_left=leftmost(x10),
            inner_bottom=lowermost(x10),
            inner_right=rightmost(x10),
        )
        x5.append(x13)
    x14 = tuple(sorted(x5, key=lambda x15: (x15.outer_top, x15.outer_left)))
    return TaskState3E6067C3(
        background=x0,
        base=x1,
        legend_row=x2,
        legend=x3,
        blocks=x14,
    )


def corridor_3e6067c3(
    left: Block3E6067C3,
    right: Block3E6067C3,
) -> Indices:
    x0 = max(left.inner_top, right.inner_top)
    x1 = min(left.inner_bottom, right.inner_bottom)
    x2 = left.outer_right + ONE
    x3 = right.outer_left - ONE
    if x0 > x1 or x2 > x3:
        return frozenset()
    return frozenset((x4, x5) for x4 in range(x0, x1 + ONE) for x5 in range(x2, x3 + ONE))


def vertical_corridor_3e6067c3(
    upper: Block3E6067C3,
    lower: Block3E6067C3,
) -> Indices:
    x0 = max(upper.inner_left, lower.inner_left)
    x1 = min(upper.inner_right, lower.inner_right)
    x2 = upper.outer_bottom + ONE
    x3 = lower.outer_top - ONE
    if x0 > x1 or x2 > x3:
        return frozenset()
    return frozenset((x4, x5) for x4 in range(x2, x3 + ONE) for x5 in range(x0, x1 + ONE))


def segment_between_3e6067c3(
    first: Block3E6067C3,
    second: Block3E6067C3,
) -> Indices:
    if first.outer_right < second.outer_left:
        x0 = corridor_3e6067c3(first, second)
        if len(x0) > ZERO:
            return x0
    if second.outer_right < first.outer_left:
        x1 = corridor_3e6067c3(second, first)
        if len(x1) > ZERO:
            return x1
    if first.outer_bottom < second.outer_top:
        x2 = vertical_corridor_3e6067c3(first, second)
        if len(x2) > ZERO:
            return x2
    if second.outer_bottom < first.outer_top:
        x3 = vertical_corridor_3e6067c3(second, first)
        if len(x3) > ZERO:
            return x3
    return frozenset()


def _background_segment_3e6067c3(
    grid: Grid,
    background: Integer,
    first: Block3E6067C3,
    second: Block3E6067C3,
) -> Indices:
    x0 = segment_between_3e6067c3(first, second)
    if len(x0) == ZERO:
        return frozenset()
    if all(index(grid, x1) == background for x1 in x0):
        return x0
    return frozenset()


def recover_path_3e6067c3(
    grid: Grid,
    state: TaskState3E6067C3 | None = None,
) -> tuple[tuple[Integer, ...], tuple[Indices, ...]]:
    x0 = extract_state_3e6067c3(grid) if state is None else state
    x1 = x0.blocks
    x2 = x0.legend
    if len(x1) < len(x2):
        raise ValueError("legend is longer than the available block set")
    x3 = {}
    for x4, x5 in enumerate(x1):
        x3.setdefault(x5.color, []).append(x4)
    x6 = {}
    for x7 in range(len(x1)):
        for x8 in range(len(x1)):
            if x7 == x8:
                continue
            x9 = _background_segment_3e6067c3(grid, x0.background, x1[x7], x1[x8])
            if len(x9) > ZERO:
                x6[(x7, x8)] = x9
    x10 = []

    def x11(
        x12: Integer,
        x13: Integer,
        x14: tuple[Integer, ...],
        x15: frozenset[Integer],
    ) -> None:
        if len(x10) > ONE:
            return
        if x12 == len(x2) - ONE:
            x10.append(x14)
            return
        x16 = x2[x12 + ONE]
        x17 = tuple(
            x18
            for x18 in x3.get(x16, [])
            if x18 not in x15 and (x13, x18) in x6
        )
        x19 = tuple(
            sorted(
                x17,
                key=lambda x20: (
                    len(x6[(x13, x20)]),
                    x1[x20].outer_top,
                    x1[x20].outer_left,
                ),
            )
        )
        for x21 in x19:
            x11(x12 + ONE, x21, x14 + (x21,), x15 | frozenset({x21}))

    for x22 in tuple(sorted(x3.get(x2[ZERO], []), key=lambda x23: (x1[x23].outer_top, x1[x23].outer_left))):
        x11(ZERO, x22, (x22,), frozenset({x22}))
    if len(x10) != ONE:
        raise ValueError("ambiguous or missing block path")
    x24 = x10[ZERO]
    x25 = tuple(x6[(x26, x27)] for x26, x27 in zip(x24, x24[ONE:]))
    return x24, x25


def apply_path_3e6067c3(
    grid: Grid,
    path: tuple[Block3E6067C3, ...],
) -> Grid:
    x0 = grid
    for x1, x2 in zip(path, path[ONE:]):
        x3 = segment_between_3e6067c3(x1, x2)
        x0 = fill(x0, x1.color, x3)
    return x0
