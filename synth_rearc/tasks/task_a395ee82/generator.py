from synth_rearc.core import *


GRID_SHAPE_A395EE82 = (22, 22)
BASE_LAYOUTS_A395EE82 = (
    frozenset({(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0), (2, 0)}),
    frozenset({(-1, -1), (-1, 0), (-1, 1), (0, 0), (1, 0)}),
    frozenset({(-1, 0), (0, -1), (0, 0), (0, 1), (1, -1), (1, 1)}),
)


def _rot90_layout_a395ee82(
    patch,
):
    return frozenset((j, -i) for i, j in patch)


def _vmirror_layout_a395ee82(
    patch,
):
    return frozenset((i, -j) for i, j in patch)


def _layout_variants_a395ee82(
    patch,
):
    x0 = []
    x1 = set()
    x2 = patch
    for _ in range(FOUR):
        for x3 in (x2, _vmirror_layout_a395ee82(x2)):
            if x3 in x1:
                continue
            x1.add(x3)
            x0.append(x3)
        x2 = _rot90_layout_a395ee82(x2)
    return tuple(x0)


LAYOUTS_A395EE82 = tuple(
    x0
    for x1 in BASE_LAYOUTS_A395EE82
    for x0 in _layout_variants_a395ee82(x1)
)


def _sample_proto_patch_a395ee82(
    diff_lb: float,
    diff_ub: float,
):
    for _ in range(400):
        x0 = unifint(diff_lb, diff_ub, (THREE, FOUR))
        x1 = unifint(diff_lb, diff_ub, (THREE, FOUR))
        x2 = max(FIVE, x0 + x1 - ONE)
        x3 = max(x2, x0 * x1 - TWO)
        x4 = unifint(diff_lb, diff_ub, (x2, x3))
        x5 = {(randint(ZERO, x0 - ONE), randint(ZERO, x1 - ONE))}
        while len(x5) < x4:
            x6 = set()
            for x7 in tuple(x5):
                for x8 in dneighbors(x7):
                    if not (ZERO <= x8[ZERO] < x0 and ZERO <= x8[ONE] < x1):
                        continue
                    if x8 in x5:
                        continue
                    x6.add(x8)
            if len(x6) == ZERO:
                break
            x5.add(choice(tuple(x6)))
        if len(x5) != x4:
            continue
        x9 = frozenset(normalize(frozenset(x5)))
        if shape(x9) != (x0, x1):
            continue
        x10 = frozenset(x11[ZERO] for x11 in x9)
        x11 = frozenset(x12[ONE] for x12 in x9)
        if ZERO not in x10 or decrement(x0) not in x10:
            continue
        if ZERO not in x11 or decrement(x1) not in x11:
            continue
        if size(x9) == x0 * x1:
            continue
        return x9
    raise RuntimeError("failed to sample prototype patch for a395ee82")


def _output_shift_a395ee82(
    offset,
    proto_shape,
):
    return multiply(offset, proto_shape)


def _layout_bounds_a395ee82(
    layout,
):
    x0 = tuple(x1[ZERO] for x1 in layout)
    x1 = tuple(x2[ONE] for x2 in layout)
    return minimum(x0), maximum(x0), minimum(x1), maximum(x1)


def _bbox_separated_a395ee82(
    a_top,
    a_left,
    a_bottom,
    a_right,
    b_top,
    b_left,
    b_bottom,
    b_right,
    gap,
):
    return (
        a_bottom + gap < b_top
        or b_bottom + gap < a_top
        or a_right + gap < b_left
        or b_right + gap < a_left
    )


def generate_a395ee82(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = interval(ZERO, TEN, ONE)
    while True:
        x1, x2, x3 = sample(x0, THREE)
        x4 = choice(LAYOUTS_A395EE82)
        x5 = _sample_proto_patch_a395ee82(diff_lb, diff_ub)
        x6 = shape(x5)
        x7 = _layout_bounds_a395ee82(x4)
        x8, x9, x10, x11 = x7
        x12 = -x8 * x6[ZERO]
        x13 = GRID_SHAPE_A395EE82[ZERO] - (x9 + ONE) * x6[ZERO]
        x14 = -x10 * x6[ONE]
        x15 = GRID_SHAPE_A395EE82[ONE] - (x11 + ONE) * x6[ONE]
        if x12 > x13 or x14 > x15:
            continue
        x16 = randint(x12, x13)
        x17 = randint(x14, x15)
        x18 = shift(recolor(x2, x5), (x16, x17))
        x19 = x16 + x8 * x6[ZERO]
        x20 = x17 + x10 * x6[ONE]
        x21 = x16 + (x9 + ONE) * x6[ZERO] - ONE
        x22 = x17 + (x11 + ONE) * x6[ONE] - ONE
        x23 = -double(x8)
        x24 = decrement(GRID_SHAPE_A395EE82[ZERO] - double(x9))
        x25 = -double(x10)
        x26 = decrement(GRID_SHAPE_A395EE82[ONE] - double(x11))
        x27 = None
        for _ in range(400):
            x28 = randint(x23, x24)
            x29 = randint(x25, x26)
            x30 = x28 + double(x8)
            x31 = x29 + double(x10)
            x32 = x28 + double(x9)
            x33 = x29 + double(x11)
            if not _bbox_separated_a395ee82(x19, x20, x21, x22, x30, x31, x32, x33, TWO):
                continue
            x27 = (x28, x29)
            break
        if x27 is None:
            continue
        x34 = canvas(x1, GRID_SHAPE_A395EE82)
        x35 = paint(x34, x18)
        x36 = x27
        x37 = set()
        for x38 in x4:
            x39 = add(x36, double(x38))
            x40 = branch(x38 == ORIGIN, x2, x3)
            x37.add((x40, x39))
        x41 = paint(x35, frozenset(x37))
        x42 = canvas(x1, GRID_SHAPE_A395EE82)
        x43 = x42
        for x44 in x4:
            x45 = _output_shift_a395ee82(x44, x6)
            x46 = shift(recolor(x2, x5), add((x16, x17), x45))
            x43 = paint(x43, x46)
        x44 = shift(recolor(x3, x5), (x16, x17))
        x45 = paint(x43, x44)
        if x41 == x45:
            continue
        return {"input": x41, "output": x45}
