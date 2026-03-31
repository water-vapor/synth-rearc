from __future__ import annotations

import json
from pathlib import Path

from synth_rearc.core import *


REFERENCE_TASK_PATH_981571DC = "data/official/arc2/evaluation/981571dc.json"
BLOCK_SIZE_981571DC = 5
BLOCK_COUNT_981571DC = 6
GRID_SIZE_981571DC = BLOCK_SIZE_981571DC * BLOCK_COUNT_981571DC


Block981571dc = tuple[tuple[int, ...], ...]
BlockMatrix981571dc = tuple[tuple[Block981571dc, ...], ...]


def _repo_root_981571dc() -> Path:
    return Path(__file__).resolve().parents[3]


def _freeze_grid_981571dc(
    grid: Grid,
) -> Grid:
    return tuple(tuple(int(x0) for x0 in x1) for x1 in grid)


def _dedupe_blocks_981571dc(
    blocks: tuple[Block981571dc, ...] | list[Block981571dc],
) -> tuple[Block981571dc, ...]:
    x0 = []
    for x1 in blocks:
        if x1 not in x0:
            x0.append(x1)
    return tuple(x0)


def _load_reference_examples_981571dc() -> tuple[dict[str, Grid], ...]:
    x0 = _repo_root_981571dc() / REFERENCE_TASK_PATH_981571DC
    with x0.open() as x1:
        x2 = json.load(x1)
    x3 = []
    for x4 in ("train", "test"):
        for x5 in x2[x4]:
            x3.append(
                {
                    "input": _freeze_grid_981571dc(x5["input"]),
                    "output": _freeze_grid_981571dc(x5["output"]),
                }
            )
    return tuple(x3)


def dmirror_block_981571dc(
    block: Block981571dc,
) -> Block981571dc:
    return tuple(tuple(x0) for x0 in zip(*block))


def block_981571dc(
    grid: Grid | list[list[int]],
    block_i: int,
    block_j: int,
) -> Block981571dc:
    x0 = block_i * BLOCK_SIZE_981571DC
    x1 = block_j * BLOCK_SIZE_981571DC
    return tuple(
        tuple(grid[x0 + x2][x1 + x3] for x3 in range(BLOCK_SIZE_981571DC))
        for x2 in range(BLOCK_SIZE_981571DC)
    )


def block_has_zero_981571dc(
    block: Block981571dc,
) -> bool:
    return any(x0 == ZERO for x1 in block for x0 in x1)


def mutable_rows_981571dc(
    grid: Grid,
) -> list[list[int]]:
    return [list(x0) for x0 in grid]


def freeze_rows_981571dc(
    rows: list[list[int]],
) -> Grid:
    return tuple(tuple(x0) for x0 in rows)


def paint_block_981571dc(
    rows: list[list[int]],
    block_i: int,
    block_j: int,
    block: Block981571dc,
) -> None:
    x0 = block_i * BLOCK_SIZE_981571DC
    x1 = block_j * BLOCK_SIZE_981571DC
    for x2 in range(BLOCK_SIZE_981571DC):
        for x3 in range(BLOCK_SIZE_981571DC):
            rows[x0 + x2][x1 + x3] = block[x2][x3]


def transpose_fill_981571dc(
    grid: Grid,
) -> Grid:
    x0 = mutable_rows_981571dc(grid)
    for x1 in range(GRID_SIZE_981571DC):
        for x2 in range(GRID_SIZE_981571DC):
            if x0[x1][x2] == ZERO and x0[x2][x1] != ZERO:
                x0[x1][x2] = x0[x2][x1]
    return freeze_rows_981571dc(x0)


def match_unique_block_981571dc(
    block: Block981571dc,
    candidates: tuple[Block981571dc, ...],
) -> Block981571dc | None:
    x0 = tuple(
        (x1, x2, block[x1][x2])
        for x1 in range(BLOCK_SIZE_981571DC)
        for x2 in range(BLOCK_SIZE_981571DC)
        if block[x1][x2] != ZERO
    )
    x3 = tuple(
        x4
        for x4 in candidates
        if all(x4[x5][x6] == x7 for x5, x6, x7 in x0)
    )
    if len(x3) != ONE:
        return None
    return x3[ZERO]


def sample_block_matrix_981571dc(
    diagonal_bank: tuple[Block981571dc, ...],
    off_bank: tuple[Block981571dc, ...],
) -> BlockMatrix981571dc:
    x0: list[list[Block981571dc | None]] = [
        [None for _ in range(BLOCK_COUNT_981571DC)]
        for _ in range(BLOCK_COUNT_981571DC)
    ]
    for x1 in range(BLOCK_COUNT_981571DC):
        x0[x1][x1] = choice(diagonal_bank)
        for x2 in range(x1 + ONE, BLOCK_COUNT_981571DC):
            x3 = choice(off_bank)
            x0[x1][x2] = x3
            x0[x2][x1] = dmirror_block_981571dc(x3)
    return tuple(tuple(x0[x1][x2] for x2 in range(BLOCK_COUNT_981571DC)) for x1 in range(BLOCK_COUNT_981571DC))


def assemble_block_matrix_981571dc(
    block_matrix: BlockMatrix981571dc,
) -> Grid:
    x0 = []
    for x1 in range(BLOCK_COUNT_981571DC):
        for x2 in range(BLOCK_SIZE_981571DC):
            x3 = []
            for x4 in range(BLOCK_COUNT_981571DC):
                x3.extend(block_matrix[x1][x4][x2])
            x0.append(tuple(x3))
    return tuple(x0)


def sample_reflected_rectangles_981571dc(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int, int, int], ...]:
    x0 = choice((ONE, ONE, TWO, TWO, TWO, THREE))
    x1 = []
    for _ in range(x0):
        x2 = unifint(diff_lb, diff_ub, (TWO, TEN))
        x3 = unifint(diff_lb, diff_ub, (TWO, TEN))
        x4 = randint(ZERO, GRID_SIZE_981571DC - x2)
        x5 = max(ZERO, x4 - THREE)
        x6 = min(GRID_SIZE_981571DC - x3, x4 + SIX)
        if choice((T, T, F)):
            x7 = randint(x5, x6) if x5 <= x6 else randint(ZERO, GRID_SIZE_981571DC - x3)
        else:
            x7 = randint(ZERO, GRID_SIZE_981571DC - x3)
        x1.append((x4, x7, x2, x3))
    return tuple(x1)


def mask_with_reflections_981571dc(
    grid: Grid,
    rectangles: tuple[tuple[int, int, int, int], ...],
) -> Grid:
    x0 = mutable_rows_981571dc(grid)
    for x1, x2, x3, x4 in rectangles:
        for x5 in range(x1, x1 + x3):
            for x6 in range(x2, x2 + x4):
                x0[x5][x6] = ZERO
        if x1 == x2 and x3 == x4:
            continue
        for x5 in range(x2, x2 + x4):
            for x6 in range(x1, x1 + x3):
                x0[x5][x6] = ZERO
    return freeze_rows_981571dc(x0)


def zero_count_981571dc(
    grid: Grid,
) -> int:
    return sum(x0 == ZERO for x1 in grid for x0 in x1)


REFERENCE_EXAMPLES_981571DC = _load_reference_examples_981571dc()
OFFICIAL_OUTPUTS_981571DC = tuple(x0["output"] for x0 in REFERENCE_EXAMPLES_981571DC)

EXAMPLE_BLOCK_BANKS_981571DC = tuple(
    (
        _dedupe_blocks_981571dc(tuple(block_981571dc(x0, x1, x1) for x1 in range(BLOCK_COUNT_981571DC))),
        _dedupe_blocks_981571dc(
            tuple(
                block_981571dc(x0, x1, x2)
                for x1 in range(BLOCK_COUNT_981571DC)
                for x2 in range(x1 + ONE, BLOCK_COUNT_981571DC)
            )
        ),
    )
    for x0 in OFFICIAL_OUTPUTS_981571DC
)

DIAGONAL_BLOCK_BANK_981571DC = _dedupe_blocks_981571dc(
    tuple(x0 for x1, _ in EXAMPLE_BLOCK_BANKS_981571DC for x0 in x1)
)

OFF_DIAGONAL_BLOCK_BANK_981571DC = _dedupe_blocks_981571dc(
    tuple(x0 for _, x1 in EXAMPLE_BLOCK_BANKS_981571DC for x0 in x1)
)
