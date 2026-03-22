from arc2.core import *


def grid_area_83eb0a57(
    grid: Grid,
) -> Integer:
    return multiply(height(grid), width(grid))


def extract_fragments_83eb0a57(
    grid: Grid,
) -> tuple[Grid, ...]:
    x0 = objects(grid, F, F, T)
    x1 = tuple(subgrid(x2, grid) for x2 in x0)
    return tuple(sorted(x1, key=grid_area_83eb0a57, reverse=True))


def find_placements_83eb0a57(
    canvas_grid: Grid,
    fragment_grid: Grid,
) -> tuple[IntegerTuple, ...]:
    x0 = height(canvas_grid)
    x1 = width(canvas_grid)
    x2 = height(fragment_grid)
    x3 = width(fragment_grid)
    x4 = intersection(palette(canvas_grid), palette(fragment_grid))
    x5 = tuple()
    for x6 in range(subtract(x0, x2) + ONE):
        for x7 in range(subtract(x1, x3) + ONE):
            x8 = True
            x9 = False
            for x10 in range(x2):
                for x11 in range(x3):
                    x12 = fragment_grid[x10][x11]
                    x13 = canvas_grid[add(x6, x10)][add(x7, x11)]
                    if x12 in x4 or x13 in x4:
                        if x12 != x13:
                            x8 = False
                            break
                        x9 = True
                if not x8:
                    break
            if x8 and x9:
                x5 = x5 + (astuple(x6, x7),)
    return x5


def paint_fragment_83eb0a57(
    canvas_grid: Grid,
    fragment_grid: Grid,
    offset: IntegerTuple,
) -> Grid:
    x0 = shift(asobject(fragment_grid), offset)
    return paint(canvas_grid, x0)


def rect_patch_83eb0a57(
    top: Integer,
    left: Integer,
    patch_height: Integer,
    patch_width: Integer,
) -> Indices:
    x0 = interval(top, add(top, patch_height), ONE)
    x1 = interval(left, add(left, patch_width), ONE)
    return product(x0, x1)


def expand_patch_83eb0a57(
    patch: Patch,
    dims: IntegerTuple,
    margin: Integer = ONE,
) -> Indices:
    x0 = dims[ZERO]
    x1 = dims[ONE]
    x2 = frozenset()
    for x3, x4 in toindices(patch):
        for x5 in range(subtract(x3, margin), add(x3, margin) + ONE):
            for x6 in range(subtract(x4, margin), add(x4, margin) + ONE):
                if 0 <= x5 < x0 and 0 <= x6 < x1:
                    x2 = insert(astuple(x5, x6), x2)
    return x2


def random_anchor_patch_83eb0a57(
    patch_height: Integer,
    patch_width: Integer,
    blocked: Indices,
    num_blocks: Integer,
) -> Indices | None:
    x0 = astuple(patch_height, patch_width)
    x1 = frozenset(blocked)
    x2 = frozenset()
    x3 = ZERO
    x4 = ZERO
    while x3 < num_blocks and x4 < 400:
        x4 = increment(x4)
        x5 = choice((ONE, ONE, TWO))
        x6 = choice((ONE, TWO, TWO, THREE))
        if x5 > patch_height or x6 > patch_width:
            continue
        x7 = randint(ZERO, subtract(patch_height, x5))
        x8 = randint(ZERO, subtract(patch_width, x6))
        x9 = rect_patch_83eb0a57(x7, x8, x5, x6)
        x10 = expand_patch_83eb0a57(x9, x0, ONE)
        if len(intersection(x10, x1)) > ZERO:
            continue
        x1 = combine(x1, x10)
        x2 = combine(x2, x9)
        x3 = increment(x3)
    if x3 != num_blocks:
        return None
    return x2


def scatter_origins_83eb0a57(
    shapes: tuple[IntegerTuple, ...],
    dims: IntegerTuple = (30, 30),
) -> tuple[IntegerTuple, ...] | None:
    x0 = tuple(sorted(shapes, key=lambda x1: multiply(x1[ZERO], x1[ONE]), reverse=True))
    x1 = {}
    x2 = frozenset()
    x3 = tuple()
    for x4 in x0:
        x5 = x4[ZERO]
        x6 = x4[ONE]
        x7 = False
        for _ in range(400):
            x8 = randint(ZERO, subtract(dims[ZERO], x5))
            x9 = randint(ZERO, subtract(dims[ONE], x6))
            x10 = rect_patch_83eb0a57(x8, x9, x5, x6)
            x11 = expand_patch_83eb0a57(x10, dims, ONE)
            if len(intersection(x11, x2)) > ZERO:
                continue
            x2 = combine(x2, x11)
            x1[x4] = x1.get(x4, tuple()) + (astuple(x8, x9),)
            x7 = True
            break
        if not x7:
            return None
    for x12 in shapes:
        x13 = x1[x12]
        x3 = x3 + (x13[ZERO],)
        x1[x12] = x13[ONE:]
    return x3
