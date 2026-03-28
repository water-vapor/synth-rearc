from synth_rearc.core import *


GRID_SHAPE_DE493100 = (30, 30)
SEED_SHAPE_DE493100 = (16, 14)
MASK_COLOR_DE493100 = SEVEN
AVAILABLE_COLORS_DE493100 = tuple(color for color in range(TEN) if color != SEVEN)
MASK_MODES_DE493100 = ("top_right", "bottom_left", "bottom_right", "left_mid")


def rect_patch_de493100(
    top: Integer,
    left: Integer,
    height: Integer,
    width: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(top, top + height) for j in range(left, left + width))


def _diag_patch_de493100(
    start: IntegerTuple,
    length: Integer,
    descending: Boolean,
) -> Indices:
    if descending:
        end = (start[0] + length - ONE, start[1] + length - ONE)
    else:
        end = (start[0] + length - ONE, start[1] - length + ONE)
    return connect(start, end)


def _cross_patch_de493100(
    row: Integer,
    col: Integer,
    vspan: Integer,
    hspan: Integer,
) -> Indices:
    top = max(ZERO, row - vspan)
    bottom = min(SEED_SHAPE_DE493100[ZERO] - ONE, row + vspan)
    left = max(ZERO, col - hspan)
    right = min(SEED_SHAPE_DE493100[ONE] - ONE, col + hspan)
    vertical = connect((top, col), (bottom, col))
    horizontal = connect((row, left), (row, right))
    return combine(vertical, horizontal)


def make_seed_de493100(
    diff_lb: float,
    diff_ub: float,
    palette_values: tuple[Integer, ...],
    bg: Integer,
) -> Grid:
    gi = canvas(bg, SEED_SHAPE_DE493100)
    accents = tuple(color for color in palette_values if color != bg)
    if len(accents) == ZERO:
        accents = palette_values

    for _ in range(unifint(diff_lb, diff_ub, (3, 5))):
        color = choice(accents)
        top = randint(ZERO, EIGHT)
        left = randint(ZERO, SIX)
        height = randint(3, 7)
        width = randint(3, 7)
        patch = rect_patch_de493100(top, left, height, width)
        mode = choice(("solid", "box", "ring"))
        if mode == "solid":
            gi = fill(gi, color, patch)
        elif mode == "box":
            gi = fill(gi, color, box(patch))
        else:
            gi = fill(gi, color, box(patch))
            if height > THREE and width > THREE:
                inner = rect_patch_de493100(top + ONE, left + ONE, height - TWO, width - TWO)
                gi = fill(gi, choice(palette_values), inner)

    for _ in range(unifint(diff_lb, diff_ub, (12, 22))):
        color = choice(accents)
        mode = choice(("solid", "box", "cross", "diag", "dot"))
        if mode == "solid":
            top = randint(ZERO, SEED_SHAPE_DE493100[ZERO] - TWO)
            left = randint(ZERO, SEED_SHAPE_DE493100[ONE] - TWO)
            height = randint(ONE, FOUR)
            width = randint(ONE, FOUR)
            patch = rect_patch_de493100(top, left, height, width)
            gi = fill(gi, color, patch)
        elif mode == "box":
            top = randint(ZERO, SEED_SHAPE_DE493100[ZERO] - THREE)
            left = randint(ZERO, SEED_SHAPE_DE493100[ONE] - THREE)
            height = randint(TWO, FIVE)
            width = randint(TWO, FIVE)
            patch = rect_patch_de493100(top, left, height, width)
            gi = fill(gi, color, box(patch))
        elif mode == "cross":
            row = randint(ZERO, SEED_SHAPE_DE493100[ZERO] - ONE)
            col = randint(ZERO, SEED_SHAPE_DE493100[ONE] - ONE)
            patch = _cross_patch_de493100(row, col, randint(ONE, THREE), randint(ONE, THREE))
            gi = fill(gi, color, patch)
        elif mode == "diag":
            length = randint(TWO, FIVE)
            descending = choice((T, F))
            top = randint(ZERO, SEED_SHAPE_DE493100[ZERO] - length)
            if descending:
                left = randint(ZERO, SEED_SHAPE_DE493100[ONE] - length)
            else:
                left = randint(length - ONE, SEED_SHAPE_DE493100[ONE] - ONE)
            patch = _diag_patch_de493100((top, left), length, descending)
            gi = fill(gi, color, patch)
        else:
            patch = frozenset({(randint(ZERO, SEED_SHAPE_DE493100[ZERO] - ONE), randint(ZERO, SEED_SHAPE_DE493100[ONE] - ONE))})
            gi = fill(gi, color, patch)

    for _ in range(unifint(diff_lb, diff_ub, (10, 18))):
        color = choice(accents)
        top = randint(ZERO, SEED_SHAPE_DE493100[ZERO] - TWO)
        left = randint(ZERO, THREE)
        patch = rect_patch_de493100(top, left, randint(ONE, THREE), randint(ONE, THREE))
        gi = fill(gi, color, patch)

    return gi


def build_complete_grid_de493100(
    seed: Grid,
    corner: Grid,
) -> Grid:
    grid = [[None for _ in range(GRID_SHAPE_DE493100[ONE])] for _ in range(GRID_SHAPE_DE493100[ZERO])]

    for i, row in enumerate(seed):
        for j, value in enumerate(row):
            grid[i][j + 16] = value

    for i, row in enumerate(corner):
        for j, value in enumerate(row):
            grid[i][j] = value

    for i in range(16):
        for j in range(TWO, 16):
            grid[i][j] = grid[i][31 - j]

    for i in range(TWO, 16):
        for j in range(TWO):
            grid[i][j] = grid[j][i]

    for i in range(16, 30):
        src = 31 - i
        for j in range(30):
            grid[i][j] = grid[src][j]

    return tuple(tuple(value for value in row) for row in grid)


def choose_mask_box_de493100(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Integer, Integer, Integer]:
    mode = choice(MASK_MODES_DE493100)
    if mode == "top_right":
        height = unifint(diff_lb, diff_ub, (4, 8))
        width = unifint(diff_lb, diff_ub, (3, 8))
        top = randint(ZERO, EIGHT)
        left = randint(max(18, 30 - width - 6), 30 - width)
    elif mode == "bottom_left":
        height = unifint(diff_lb, diff_ub, (4, 9))
        width = unifint(diff_lb, diff_ub, (4, 10))
        top = randint(16, 30 - height)
        left = randint(ZERO, max(ZERO, 10 - width))
    elif mode == "bottom_right":
        height = unifint(diff_lb, diff_ub, (4, 9))
        width = unifint(diff_lb, diff_ub, (4, 10))
        top = randint(16, 30 - height)
        left = randint(max(18, 30 - width - 8), 30 - width)
    else:
        height = unifint(diff_lb, diff_ub, (6, 10))
        width = unifint(diff_lb, diff_ub, (4, 10))
        top = randint(10, 23 - height)
        left = randint(ZERO, max(ZERO, 10 - width))
    return top, left, height, width
