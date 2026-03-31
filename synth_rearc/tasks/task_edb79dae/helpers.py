from __future__ import annotations

from synth_rearc.core import *


PAIR_LEFT_EDB79DAE = frozenset(
    {
        (ZERO, ZERO),
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ONE),
        (ONE, TWO),
        (TWO, ZERO),
        (TWO, ONE),
    }
)

PAIR_RIGHT_EDB79DAE = frozenset(
    {
        (ZERO, ZERO),
        (ZERO, ONE),
        (ONE, ONE),
        (TWO, ZERO),
        (TWO, ONE),
    }
)


def board_shape_edb79dae(
    motif_size: Integer,
    row_count: Integer,
    col_count: Integer,
) -> IntegerTuple:
    x0 = THREE + row_count * (motif_size + ONE)
    x1 = THREE + col_count * (motif_size + ONE)
    return (x0, x1)


def slot_origin_edb79dae(
    motif_size: Integer,
    row_index: Integer,
    col_index: Integer,
) -> IntegerTuple:
    x0 = TWO + row_index * (motif_size + ONE)
    x1 = TWO + col_index * (motif_size + ONE)
    return (x0, x1)


def solid_square_patch_edb79dae(
    origin: IntegerTuple,
    motif_size: Integer,
) -> Indices:
    x0, x1 = origin
    return frozenset(
        (x2, x3)
        for x2 in range(x0, x0 + motif_size)
        for x3 in range(x1, x1 + motif_size)
    )


def framed_canvas_edb79dae(
    bg_color: Integer,
    border_color: Integer,
    dims: IntegerTuple,
) -> Grid:
    x0, x1 = dims
    x2 = canvas(bg_color, dims)
    x3 = frozenset(
        {
            *((ZERO, x4) for x4 in range(x1)),
            *((x0 - ONE, x5) for x5 in range(x1)),
            *((x6, ZERO) for x6 in range(x0)),
            *((x7, x1 - ONE) for x7 in range(x0)),
        }
    )
    return fill(x2, border_color, x3)


def paint_template_edb79dae(
    grid: Grid,
    target_color: Integer,
    template: Indices,
    origin: IntegerTuple,
) -> Grid:
    x0 = recolor(target_color, template)
    x1 = shift(x0, origin)
    return paint(grid, x1)


def render_boards_edb79dae(
    bg_color: Integer,
    border_color: Integer,
    row_count: Integer,
    col_count: Integer,
    motif_size: Integer,
    placements: tuple[tuple[Integer, Integer, Integer], ...],
    templates: dict[Integer, Indices],
    targets: dict[Integer, Integer],
) -> tuple[Grid, Grid]:
    x0 = board_shape_edb79dae(motif_size, row_count, col_count)
    x1 = framed_canvas_edb79dae(bg_color, border_color, x0)
    x2 = x1
    x3 = x1
    for x4, x5, x6 in placements:
        x7 = slot_origin_edb79dae(motif_size, x5, x6)
        x8 = solid_square_patch_edb79dae(x7, motif_size)
        x2 = fill(x2, x4, x8)
        x3 = paint_template_edb79dae(x3, targets[x4], templates[x4], x7)
    return x2, x3


def pair_objects_edb79dae(
    source_color: Integer,
    target_color: Integer,
    origin: IntegerTuple,
) -> tuple[Object, Object]:
    x0 = shift(recolor(source_color, PAIR_LEFT_EDB79DAE), origin)
    x1 = shift(recolor(target_color, PAIR_RIGHT_EDB79DAE), (origin[0], origin[1] + TWO))
    return (x0, x1)


def embed_grid_edb79dae(
    grid: Grid,
    patch: Grid,
    origin: IntegerTuple,
) -> Grid:
    x0 = [list(x1) for x1 in grid]
    x2, x3 = origin
    for x4, x5 in enumerate(patch):
        for x6, x7 in enumerate(x5):
            x0[x2 + x4][x3 + x6] = x7
    return tuple(tuple(x8) for x8 in x0)
