from synth_rearc.core import *

from .verifier import verify_abbfd121


GRID_HEIGHT_BOUNDS_ABBFD121 = (18, 26)
GRID_WIDTH_BOUNDS_ABBFD121 = (18, 26)
MAIN_RECT_HEIGHT_BOUNDS_ABBFD121 = (6, 12)
MAIN_RECT_WIDTH_BOUNDS_ABBFD121 = (6, 12)


def _rect_patch_abbfd121(
    top: Integer,
    left: Integer,
    height_value: Integer,
    width_value: Integer,
) -> Indices:
    x0 = interval(top, top + height_value, ONE)
    x1 = interval(left, left + width_value, ONE)
    x2 = product(x0, x1)
    return x2


def _tile_abbfd121(
    template_id: Integer,
    colors: Tuple[Integer, ...],
) -> Grid:
    if template_id == ZERO:
        x0, x1, x2 = colors
        return (
            (x0, x0, x0),
            (x1, x2, x2),
            (x2, x1, x1),
        )
    if template_id == ONE:
        x0, x1, x2 = colors
        return (
            (x0, x0, x0),
            (x0, x2, x1),
            (x0, x1, x2),
        )
    if template_id == TWO:
        x0, x1, x2 = colors
        return (
            (x2, x0, x1),
            (x0, x1, x2),
            (x1, x2, x0),
        )
    x0, x1, x2, x3 = colors
    return (
        (x0, x0, x0, x0),
        (x1, x2, x3, x0),
        (x2, x0, x2, x0),
        (x3, x2, x1, x0),
    )


def _render_wallpaper_abbfd121(
    tile: Grid,
    dimensions: IntegerTuple,
) -> Grid:
    x0, x1 = dimensions
    x2 = height(tile)
    x3 = width(tile)
    x4 = tuple(tuple(tile[x5 % x2][x6 % x3] for x6 in range(x1)) for x5 in range(x0))
    return x4


def generate_abbfd121(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = randint(ZERO, THREE)
        x1 = branch(equality(x0, THREE), TWO, choice((TWO, THREE)))
        x2 = unifint(diff_lb, diff_ub, GRID_HEIGHT_BOUNDS_ABBFD121)
        x3 = unifint(diff_lb, diff_ub, GRID_WIDTH_BOUNDS_ABBFD121)
        x4 = list(interval(ZERO, TEN, ONE))
        shuffle(x4)
        x5 = FOUR if x0 == THREE else THREE
        x6 = tuple(x4[:x5])
        x7 = tuple(x4[x5:x5 + x1])
        x8 = _tile_abbfd121(x0, x6)
        x9 = _render_wallpaper_abbfd121(x8, (x2, x3))
        x10 = min(MAIN_RECT_HEIGHT_BOUNDS_ABBFD121[1], x2 - THREE)
        x11 = min(MAIN_RECT_WIDTH_BOUNDS_ABBFD121[1], x3 - THREE)
        x12 = max(MAIN_RECT_HEIGHT_BOUNDS_ABBFD121[0], height(x8) + TWO)
        x13 = max(MAIN_RECT_WIDTH_BOUNDS_ABBFD121[0], width(x8) + TWO)
        if x12 > x10 or x13 > x11:
            continue
        x14 = unifint(diff_lb, diff_ub, (x12, x10))
        x15 = unifint(diff_lb, diff_ub, (x13, x11))
        x16 = randint(ZERO, x2 - x14)
        x17 = randint(ZERO, x3 - x15)
        x18 = _rect_patch_abbfd121(x16, x17, x14, x15)
        x19 = crop(x9, astuple(x16, x17), astuple(x14, x15))
        x20 = [(x18, x7[ZERO], x14, x15)]
        x21 = T
        for x22 in x7[ONE:]:
            x23 = F
            for _ in range(200):
                x24 = randint(THREE, x14)
                x25 = randint(THREE, x15)
                if both(equality(x24, x14), equality(x25, x15)):
                    continue
                x26 = randint(ZERO, x2 - x24)
                x27 = randint(ZERO, x3 - x25)
                x28 = _rect_patch_abbfd121(x26, x27, x24, x25)
                x29 = any(size(intersection(x28, x30[ZERO])) > ZERO for x30 in x20)
                if x29:
                    continue
                x20.append((x28, x22, x24, x25))
                x23 = T
                break
            if not x23:
                x21 = F
                break
        if not x21:
            continue
        x31 = x9
        for x32, x33, _, _ in x20:
            x31 = fill(x31, x33, x32)
        x34 = merge(tuple(x35[ZERO] for x35 in x20))
        x35 = frozenset((x36 % height(x8), x37 % width(x8)) for x36 in range(x2) for x37 in range(x3) if (x36, x37) not in x34)
        x36 = multiply(height(x8), width(x8))
        if size(x35) != x36:
            continue
        x37 = verify_abbfd121(x31)
        if x37 != x19:
            continue
        return {"input": x31, "output": x19}
