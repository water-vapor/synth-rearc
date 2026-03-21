from arc2.core import *


SLOT_OFFSETS_A096BF4D = ((ONE, ONE), (ONE, TWO), (TWO, ONE), (TWO, TWO))
ALL_COLORS_A096BF4D = remove(ZERO, interval(ZERO, TEN, ONE))
DIRS_A096BF4D = ("h", "v")


def _make_base_tile_a096bf4d(
    frame_color: Integer,
    inner_color: Integer,
    mode: Integer,
) -> tuple[Grid, tuple[Integer, Integer, Integer, Integer]]:
    x0 = [inner_color, inner_color, inner_color, inner_color]
    if mode != ZERO:
        x0[mode - ONE] = frame_color
    x1 = (
        (frame_color, frame_color, frame_color, frame_color),
        (frame_color, x0[ZERO], x0[ONE], frame_color),
        (frame_color, x0[TWO], x0[THREE], frame_color),
        (frame_color, frame_color, frame_color, frame_color),
    )
    x2 = tuple(x0)
    return x1, x2


def _make_lattice_a096bf4d(
    base_tile: Grid,
    nrows: Integer,
    ncols: Integer,
) -> Grid:
    x0 = astuple(add(multiply(FIVE, nrows), ONE), add(multiply(FIVE, ncols), ONE))
    x1 = canvas(ZERO, x0)
    x2 = asobject(base_tile)
    x3 = x1
    for x4 in range(nrows):
        for x5 in range(ncols):
            x6 = astuple(add(ONE, multiply(FIVE, x4)), add(ONE, multiply(FIVE, x5)))
            x7 = shift(x2, x6)
            x3 = paint(x3, x7)
    return x3


def _slot_index_a096bf4d(
    tile_i: Integer,
    tile_j: Integer,
    slot_k: Integer,
) -> IntegerTuple:
    x0, x1 = SLOT_OFFSETS_A096BF4D[slot_k]
    x2 = add(add(ONE, multiply(FIVE, tile_i)), x0)
    x3 = add(add(ONE, multiply(FIVE, tile_j)), x1)
    x4 = astuple(x2, x3)
    return x4


def _paint_slot_a096bf4d(
    grid: Grid,
    tile_i: Integer,
    tile_j: Integer,
    slot_k: Integer,
    value: Integer,
) -> Grid:
    x0 = _slot_index_a096bf4d(tile_i, tile_j, slot_k)
    x1 = fill(grid, value, {x0})
    return x1


def generate_a096bf4d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x1 = unifint(diff_lb, diff_ub, (THREE, FIVE))
        x2 = choice(ALL_COLORS_A096BF4D)
        x3 = choice(remove(x2, ALL_COLORS_A096BF4D))
        x4 = choice(interval(ZERO, FIVE, ONE))
        x5, x6 = _make_base_tile_a096bf4d(x2, x3, x4)
        gi = _make_lattice_a096bf4d(x5, x0, x1)
        go = gi
        x7 = unifint(diff_lb, diff_ub, (TWO, THREE))
        x8 = sample(range(FOUR), x7)
        x9 = [choice(DIRS_A096BF4D), choice(DIRS_A096BF4D)]
        while len(x9) < x7:
            x9.append(choice(DIRS_A096BF4D))
        if all(x10 == "h" for x10 in x9):
            x9[ZERO] = "v"
        if all(x10 == "v" for x10 in x9):
            x9[ZERO] = "h"
        shuffle(x9)
        x11 = tuple(c for c in ALL_COLORS_A096BF4D if c not in (set(x6) | {x2}))
        x12 = sample(x11, x7)
        x13 = set()
        x14 = True
        for x15, x16, x17 in zip(x8, x9, x12):
            x18 = False
            for _ in range(100):
                if x16 == "h":
                    x19 = randint(ZERO, decrement(x0))
                    x20, x21 = sorted(sample(range(x1), TWO))
                    if subtract(x21, x20) < TWO:
                        continue
                    x22 = [(x19, x23, x15) for x23 in range(x20, increment(x21))]
                    if any(x24 in x13 for x24 in x22):
                        continue
                    gi = _paint_slot_a096bf4d(gi, x19, x20, x15, x17)
                    gi = _paint_slot_a096bf4d(gi, x19, x21, x15, x17)
                    for x25 in range(x20, increment(x21)):
                        go = _paint_slot_a096bf4d(go, x19, x25, x15, x17)
                else:
                    x26 = randint(ZERO, decrement(x1))
                    x27, x28 = sorted(sample(range(x0), TWO))
                    if subtract(x28, x27) < TWO:
                        continue
                    x22 = [(x29, x26, x15) for x29 in range(x27, increment(x28))]
                    if any(x24 in x13 for x24 in x22):
                        continue
                    gi = _paint_slot_a096bf4d(gi, x27, x26, x15, x17)
                    gi = _paint_slot_a096bf4d(gi, x28, x26, x15, x17)
                    for x30 in range(x27, increment(x28)):
                        go = _paint_slot_a096bf4d(go, x30, x26, x15, x17)
                x13.update(x22)
                x18 = True
                break
            if not x18:
                x14 = False
                break
        if not x14:
            continue
        return {"input": gi, "output": go}
