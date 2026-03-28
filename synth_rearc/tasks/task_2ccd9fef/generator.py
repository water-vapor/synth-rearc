from synth_rearc.core import *

from .helpers import compose_blocks_2ccd9fef, solve_2ccd9fef


TRAIN1_MASK_2CCD9FEF = (
    "01000000010",
    "11000000011",
    "00000000000",
    "00000000000",
    "00000000000",
    "00000000000",
    "11000000011",
    "01000000010",
)

TRAIN2_MASK_2CCD9FEF = (
    "10000000001",
    "01101110110",
    "00000000000",
    "00000000000",
    "00000000000",
    "01101110110",
    "10000000001",
)

TEST1_MASK_2CCD9FEF = (
    "11011",
    "10001",
    "00000",
    "00000",
    "10001",
    "10001",
    "10001",
    "00000",
    "00000",
    "10001",
    "11011",
)

TEST2_MASK_2CCD9FEF = (
    "100010001",
    "010111010",
    "000000000",
    "010000010",
    "000000000",
    "110000011",
    "000000000",
    "010000010",
    "000000000",
    "010111010",
    "100010001",
)


def _template_2ccd9fef(mask: tuple[str, ...], base: Integer, accent: Integer) -> Grid:
    h = len(mask)
    w = len(first(mask))
    grid = canvas(base, (h, w))
    cells = frozenset(
        (i, j)
        for i, row in enumerate(mask)
        for j, value in enumerate(row)
        if value == "1"
    )
    return fill(grid, accent, cells)


def _train1_block_2ccd9fef(blank: Grid, stage: int, rect_color: Integer, bracket_color: Integer) -> Grid:
    rect_patch = frozenset((row, col) for row in (3, 4) for col in range(2, 3 + stage))
    left = 7 - stage
    bracket_patch = frozenset(
        (
            {(2, col) for col in range(left, 9)}
            | {(5, col) for col in range(left, 9)}
            | {(3, 8), (4, 8)}
        )
    )
    grid = fill(blank, rect_color, rect_patch)
    return fill(grid, bracket_color, bracket_patch)


def _train2_block_2ccd9fef(blank: Grid, bar_color: Integer, hook_color: Integer, stage: int) -> Grid:
    bar_patch = frozenset(
        {(2, col) for col in range(2, 4 + stage)} | {(4, col) for col in range(2, 4 + stage)}
    )
    hook_patch = frozenset(
        {(3, col) for col in range(2, 5 + stage)} | {(2, 4 + stage), (4, 4 + stage)}
    )
    grid = fill(blank, bar_color, bar_patch)
    return fill(grid, hook_color, hook_patch)


def _test2_block_2ccd9fef(blank: Grid, stem_color: Integer, rail_color: Integer, stage: int) -> Grid:
    bar_row = 3 + stage
    stem_patch = frozenset(
        {(bar_row, col) for col in range(2, 7)}
        | {(bar_row + delta, 4) for delta in range(1, stage + 2)}
    )
    rail_patch = frozenset(
        (row, col)
        for row in range(8 - stage, 9)
        for col in (2, 3, 5, 6)
    )
    grid = fill(blank, stem_color, stem_patch)
    return fill(grid, rail_color, rail_patch)


def _alternating_block_2ccd9fef(
    blank: Grid,
    primary_color: Integer,
    accent_color: Integer,
    stage: int,
    top: int,
) -> Grid:
    primary_patch = set()
    accent_patch = set()
    for delta in range(2 * stage + 1):
        row = top + delta
        if delta % 2 == 0:
            primary_patch |= {(row, 1), (row, 3)}
            accent_patch.add((row, 2))
        else:
            primary_patch |= {(row, 1), (row, 2), (row, 3)}
    grid = fill(blank, primary_color, frozenset(primary_patch))
    return fill(grid, accent_color, frozenset(accent_patch))


def _maybe_reflect_2ccd9fef(blocks: tuple[Grid, ...], output: Grid) -> tuple[tuple[Grid, ...], Grid]:
    do_h = bool(randint(0, 1))
    do_v = bool(randint(0, 1))
    transformed_blocks = blocks
    transformed_output = output
    if do_h:
        transformed_blocks = tuple(hmirror(block) for block in transformed_blocks)
        transformed_output = hmirror(transformed_output)
    if do_v:
        transformed_blocks = tuple(vmirror(block) for block in transformed_blocks)
        transformed_output = vmirror(transformed_output)
    return transformed_blocks, transformed_output


def _generate_train1_family_2ccd9fef(colors: tuple[int, ...]) -> dict:
    bg_base, bg_accent, rect_color, bracket_color = colors[:4]
    blank = _template_2ccd9fef(TRAIN1_MASK_2CCD9FEF, bg_base, bg_accent)
    block0 = _train1_block_2ccd9fef(blank, 0, rect_color, bracket_color)
    block1 = _train1_block_2ccd9fef(blank, 1, rect_color, bracket_color)
    output = _train1_block_2ccd9fef(blank, 2, rect_color, bracket_color)
    blocks, output = _maybe_reflect_2ccd9fef((block0, block1, blank), output)
    return {"input": compose_blocks_2ccd9fef(blocks, "vertical"), "output": output}


def _generate_train2_family_2ccd9fef(colors: tuple[int, ...]) -> dict:
    bg_base, bg_accent, bar_color, hook_color = colors[:4]
    blank = _template_2ccd9fef(TRAIN2_MASK_2CCD9FEF, bg_base, bg_accent)
    block0 = _train2_block_2ccd9fef(blank, bar_color, hook_color, 0)
    block1 = _train2_block_2ccd9fef(blank, bar_color, hook_color, 1)
    output = _train2_block_2ccd9fef(blank, bar_color, hook_color, 2)
    blocks, output = _maybe_reflect_2ccd9fef((block0, block1, blank), output)
    return {"input": compose_blocks_2ccd9fef(blocks, "vertical"), "output": output}


def _generate_test2_family_2ccd9fef(colors: tuple[int, ...]) -> dict:
    bg_base, bg_accent, stem_color, rail_color = colors[:4]
    blank = _template_2ccd9fef(TEST2_MASK_2CCD9FEF, bg_base, bg_accent)
    block0 = _test2_block_2ccd9fef(blank, stem_color, rail_color, 0)
    block1 = _test2_block_2ccd9fef(blank, stem_color, rail_color, 1)
    output = _test2_block_2ccd9fef(blank, stem_color, rail_color, 2)
    blocks, output = _maybe_reflect_2ccd9fef((block0, block1, blank), output)
    return {"input": compose_blocks_2ccd9fef(blocks, "horizontal"), "output": output}


def _generate_test1_family_2ccd9fef(colors: tuple[int, ...], top: int) -> dict:
    bg_base, bg_accent, primary_a, primary_b, accent_color = colors[:5]
    blank = _template_2ccd9fef(TEST1_MASK_2CCD9FEF, bg_base, bg_accent)
    stages = []
    primary_colors = (primary_a, primary_b, primary_a, primary_b)
    for stage, primary_color in enumerate(primary_colors):
        stages.append(_alternating_block_2ccd9fef(blank, primary_color, accent_color, stage, top))
    output = _alternating_block_2ccd9fef(blank, primary_a, accent_color, 4, top)
    blocks, output = _maybe_reflect_2ccd9fef(tuple(stages) + (blank,), output)
    return {"input": compose_blocks_2ccd9fef(blocks, "horizontal"), "output": output}


def generate_2ccd9fef(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = tuple(remove(ZERO, interval(ZERO, TEN, ONE)))
    families = (
        _generate_train1_family_2ccd9fef,
        _generate_train2_family_2ccd9fef,
        _generate_test2_family_2ccd9fef,
        _generate_test1_family_2ccd9fef,
    )
    while True:
        family = choice(families)
        if family is _generate_test1_family_2ccd9fef:
            colors = tuple(sample(cols, FIVE))
            top = unifint(diff_lb, diff_ub, (0, 2))
            example = family(colors, top)
        else:
            colors = tuple(sample(cols, FOUR))
            example = family(colors)
        if solve_2ccd9fef(example["input"]) != example["output"]:
            continue
        return example
