from arc2.core import *


ORIENTATIONS_54DC2872 = ("ul", "ur", "ll")
SHAPES_54DC2872 = ((THREE, TWO), (TWO, THREE), (THREE, THREE), (THREE, FOUR))


def _make_object_54dc2872(
    main_color: int,
    accent_color: int,
    dims: tuple[int, int],
    orientation: str,
) -> Object:
    x0, x1 = dims
    if orientation == "ul":
        x2 = combine(connect((ZERO, ZERO), (ZERO, x1 - ONE)), connect((ZERO, ZERO), (x0 - ONE, ZERO)))
        x3 = (ONE, ONE)
    elif orientation == "ur":
        x2 = combine(connect((ZERO, ZERO), (ZERO, x1 - ONE)), connect((ZERO, x1 - ONE), (x0 - ONE, x1 - ONE)))
        x3 = (ONE, x1 - TWO)
    else:
        x2 = combine(connect((ZERO, ZERO), (x0 - ONE, ZERO)), connect((x0 - ONE, ZERO), (x0 - ONE, x1 - ONE)))
        x3 = (x0 - TWO, ONE)
    x4 = recolor(main_color, x2)
    x5 = recolor(accent_color, initset(x3))
    return combine(x4, x5)


def _elbow_local_54dc2872(dims: tuple[int, int], orientation: str) -> tuple[int, int]:
    x0, x1 = dims
    if orientation == "ul":
        return ORIGIN
    if orientation == "ur":
        return (ZERO, x1 - ONE)
    return (x0 - ONE, ZERO)


def _buffer_54dc2872(
    top: int,
    left: int,
    height_: int,
    width_: int,
    grid_height: int,
    grid_width: int,
    pad: int = ONE,
) -> frozenset[tuple[int, int]]:
    x0 = max(ZERO, top - pad)
    x1 = max(ZERO, left - pad)
    x2 = min(grid_height - ONE, top + height_ + pad - ONE)
    x3 = min(grid_width - ONE, left + width_ + pad - ONE)
    return frozenset((x4, x5) for x4 in range(x0, x2 + ONE) for x5 in range(x1, x3 + ONE))


def _place_box_54dc2872(
    dims: tuple[int, int],
    grid_height: int,
    grid_width: int,
    occupied: frozenset[tuple[int, int]],
) -> tuple[int, int]:
    x0, x1 = dims
    x2 = []
    for x3 in range(grid_height - x0 + ONE):
        for x4 in range(grid_width - x1 + ONE):
            x5 = _buffer_54dc2872(x3, x4, x0, x1, grid_height, grid_width)
            if x5.isdisjoint(occupied):
                x2.append((x3, x4))
    if len(x2) == ZERO:
        raise ValueError("no box placement available")
    return choice(x2)


def _place_cell_54dc2872(
    grid_height: int,
    grid_width: int,
    occupied: frozenset[tuple[int, int]],
) -> tuple[int, int]:
    x0 = []
    for x1 in range(grid_height):
        for x2 in range(grid_width):
            x3 = _buffer_54dc2872(x1, x2, ONE, ONE, grid_height, grid_width)
            if x3.isdisjoint(occupied):
                x0.append((x1, x2))
    if len(x0) == ZERO:
        raise ValueError("no cell placement available")
    return choice(x0)


def generate_54dc2872(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ONE, TEN, ONE)
    for _ in range(200):
        x1 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x2 = unifint(diff_lb, diff_ub, (ONE, x1 - ONE))
        x3 = choice((ZERO, ZERO, ONE))
        x4 = sample(x0, x1)
        x5 = tuple(x6 for x6 in x0 if x6 not in x4)
        x6 = sample(x5, x1)
        x7 = tuple(x8 for x8 in x5 if x8 not in x6)
        if x3 > len(x7):
            continue
        x8 = sample(x7, x3)
        x9 = sample(tuple(range(x1)), x2)
        x10 = unifint(diff_lb, diff_ub, (12, 18))
        x11 = unifint(diff_lb, diff_ub, (12, 18))
        x12 = []
        x13 = frozenset()
        try:
            for x14, x15 in zip(x4, x6):
                x16 = choice(SHAPES_54DC2872)
                x17 = choice(ORIENTATIONS_54DC2872)
                x18 = _make_object_54dc2872(x14, x15, x16, x17)
                x19 = _place_box_54dc2872(x16, x10, x11, x13)
                x20 = _buffer_54dc2872(x19[ZERO], x19[ONE], x16[ZERO], x16[ONE], x10, x11)
                x13 = combine(x13, x20)
                x21 = _elbow_local_54dc2872(x16, x17)
                x22 = add(x19, x21)
                x12.append(
                    {
                        "object": x18,
                        "dims": x16,
                        "orientation": x17,
                        "target": x19,
                        "marker": x22,
                        "accent": x15,
                    }
                )
            x23 = []
            for x24 in x8:
                x25 = _place_cell_54dc2872(x10, x11, x13)
                x26 = _buffer_54dc2872(x25[ZERO], x25[ONE], ONE, ONE, x10, x11)
                x13 = combine(x13, x26)
                x23.append((x24, x25))
            x27 = x13
            for x29, x30 in enumerate(x12):
                if x29 not in x9:
                    continue
                x31 = _place_box_54dc2872(x30["dims"], x10, x11, x27)
                x32 = _buffer_54dc2872(
                    x31[ZERO],
                    x31[ONE],
                    x30["dims"][ZERO],
                    x30["dims"][ONE],
                    x10,
                    x11,
                )
                x27 = combine(x27, x32)
                x30["source"] = x31
            x33 = canvas(ZERO, (x10, x11))
            x34 = canvas(ZERO, (x10, x11))
            for x35, x36 in enumerate(x12):
                x37 = shift(x36["object"], x36["target"])
                x34 = paint(x34, x37)
                if x35 in x9:
                    x38 = shift(x36["object"], x36["source"])
                    x33 = paint(x33, x38)
                    x33 = fill(x33, x36["accent"], initset(x36["marker"]))
                else:
                    x33 = paint(x33, x37)
            for x39, x40 in x23:
                x41 = initset(x40)
                x33 = fill(x33, x39, x41)
                x34 = fill(x34, x39, x41)
            return {"input": x33, "output": x34}
        except ValueError:
            continue
    raise RuntimeError("failed to generate task_54dc2872 example")
