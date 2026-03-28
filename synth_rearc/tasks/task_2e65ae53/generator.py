from synth_rearc.core import *


def _frame_dims_2e65ae53(spec: tuple[int, int, int, int, int, int]) -> tuple[int, int]:
    _, _, x0, x1, x2, x3 = spec
    return (x0 + x1 + THREE, x2 + x3 + THREE)


def _frame_outline_2e65ae53(spec: tuple[int, int, int, int, int, int]) -> Indices:
    x0, x1, x2, x3, x4, x5 = spec
    x6, x7 = _frame_dims_2e65ae53(spec)
    x8 = x0 + x6 - ONE
    x9 = x1 + x7 - ONE
    x10 = x0 + x2 + ONE
    x11 = x1 + x4 + ONE
    x12 = box(frozenset({(x0, x1), (x8, x9)}))
    x13 = connect((x10, x1), (x10, x9))
    x14 = connect((x0, x11), (x8, x11))
    return combine(combine(x12, x13), x14)


def _frame_quadrants_2e65ae53(
    spec: tuple[int, int, int, int, int, int],
) -> tuple[Indices, Indices, Indices, Indices]:
    x0, x1, x2, x3, x4, x5 = spec
    x6 = x0 + x2 + ONE
    x7 = x1 + x4 + ONE
    x8 = frozenset((x9, x10) for x9 in range(x0 + ONE, x6) for x10 in range(x1 + ONE, x7))
    x9 = frozenset((x10, x11) for x10 in range(x0 + ONE, x6) for x11 in range(x7 + ONE, x1 + x4 + x5 + THREE - ONE))
    x10 = frozenset((x11, x12) for x11 in range(x6 + ONE, x0 + x2 + x3 + THREE - ONE) for x12 in range(x1 + ONE, x7))
    x11 = frozenset((x12, x13) for x12 in range(x6 + ONE, x0 + x2 + x3 + THREE - ONE) for x13 in range(x7 + ONE, x1 + x4 + x5 + THREE - ONE))
    return (x8, x9, x10, x11)


def _sample_frame_shape_2e65ae53(
    diff_lb: float,
    diff_ub: float,
    frame_count: int,
) -> tuple[int, int, int, int]:
    x0 = SIX if frame_count <= FOUR else FOUR
    x1 = SEVEN if frame_count <= FOUR else FIVE
    x2 = FIVE if frame_count <= FOUR else FOUR
    x3 = SIX if frame_count <= FOUR else FIVE
    x4 = unifint(diff_lb, diff_ub, (ONE, x0))
    x5 = unifint(diff_lb, diff_ub, (ONE, x1))
    x6 = unifint(diff_lb, diff_ub, (ONE, x2))
    x7 = unifint(diff_lb, diff_ub, (ONE, x3))
    return (x4, x5, x6, x7)


def _sample_visibility_2e65ae53(
    diff_lb: float,
    diff_ub: float,
    frame_count: int,
) -> tuple[tuple[int, ...], ...]:
    x0 = tuple(range(FOUR))
    while True:
        x1 = [set() for _ in range(frame_count)]
        x2 = randint(ZERO, frame_count - ONE)
        x3 = choice((TWO, THREE, THREE))
        x4 = set(sample(x0, x3))
        x1[x2] |= x4
        x5 = [x6 for x6 in x0 if x6 not in x4]
        x6 = tuple(x7 for x7 in range(frame_count) if x7 != x2)
        for x7 in x5:
            x8 = [x9 for x9 in x6 if len(x1[x9]) < THREE]
            x9 = choice(x8 if len(x8) > ZERO else x6)
            x1[x9].add(x7)
        x10 = unifint(diff_lb, diff_ub, (ZERO, TWO))
        for _ in range(x10):
            x11 = randint(ZERO, THREE)
            x12 = [x13 for x13 in range(frame_count) if len(x1[x13]) < THREE and x11 not in x1[x13]]
            if len(x12) > ZERO:
                x1[choice(x12)].add(x11)
        if not any(len(x14) == ZERO for x14 in x1):
            continue
        if not any(len(x15) == ONE for x15 in x1):
            continue
        return tuple(tuple(sorted(x16)) for x16 in x1)


def _place_frames_2e65ae53(
    shapes: tuple[tuple[int, int, int, int], ...],
) -> tuple[tuple[int, int, int, int, int, int], ...] | None:
    x0 = list(range(len(shapes)))
    shuffle(x0)
    x1 = len(shapes) // TWO
    x2 = tuple(x0[:x1])
    x3 = tuple(x0[x1:])
    x4 = [None for _ in shapes]

    def x5(x6: tuple[int, ...]) -> tuple[list[tuple[int, int]], int, int]:
        x7 = []
        x8 = ZERO
        x9 = ZERO
        for x10, x11 in enumerate(x6):
            x12, x13 = _frame_dims_2e65ae53((ZERO, ZERO, *shapes[x11]))
            x7.append((x11, x8))
            x8 += x12
            if x10 != len(x6) - ONE:
                x8 += randint(ONE, TWO)
            x9 = max(x9, x13)
        return (x7, x8, x9)

    x6, x7, x8 = x5(x2)
    x9, x10, x11 = x5(x3)
    x12 = randint(ONE, THREE)
    x13 = randint(ZERO, TWO)
    x14 = randint(ZERO, TWO)
    x15 = max(x7 + x13, x10 + x14)
    x16 = x8 + x12 + x11
    if max(x15, x16) > 28:
        return None
    for x17, x18 in x6:
        x19, x20 = _frame_dims_2e65ae53((ZERO, ZERO, *shapes[x17]))
        x21 = randint(ZERO, x8 - x20)
        x22 = shapes[x17]
        x4[x17] = (x18 + x13, x21, x22[ZERO], x22[ONE], x22[TWO], x22[THREE])
    for x23, x24 in x9:
        x25, x26 = _frame_dims_2e65ae53((ZERO, ZERO, *shapes[x23]))
        x27 = x8 + x12 + randint(ZERO, x11 - x26)
        x28 = shapes[x23]
        x4[x23] = (x24 + x14, x27, x28[ZERO], x28[ONE], x28[TWO], x28[THREE])
    return tuple(x4)


def _crop_specs_2e65ae53(
    specs: tuple[tuple[int, int, int, int, int, int], ...],
) -> tuple[int, tuple[tuple[int, int, int, int, int, int], ...]]:
    x0 = [x1[ZERO] for x1 in specs]
    x1 = [x2[ONE] for x2 in specs]
    x2 = [x3[ZERO] + _frame_dims_2e65ae53(x3)[ZERO] - ONE for x3 in specs]
    x3 = [x4[ONE] + _frame_dims_2e65ae53(x4)[ONE] - ONE for x4 in specs]
    x4 = minimum(x0)
    x5 = minimum(x1)
    x6 = maximum(x2)
    x7 = maximum(x3)
    x8 = x6 - x4 + ONE
    x9 = x7 - x5 + ONE
    x10 = 30 - maximum((x8, x9))
    x11 = randint(ZERO, min(TWO, x10))
    x12 = maximum((x8, x9)) + x11
    x13 = randint(ZERO, x12 - x8)
    x14 = randint(ZERO, x12 - x9)
    x15 = tuple(
        (
            x16[ZERO] - x4 + x13,
            x16[ONE] - x5 + x14,
            x16[TWO],
            x16[THREE],
            x16[FOUR],
            x16[FIVE],
        )
        for x16 in specs
    )
    return (x12, x15)


def _draw_grid_2e65ae53(
    side: int,
    specs: tuple[tuple[int, int, int, int, int, int], ...],
    border_color: int,
    quad_colors: tuple[int, int, int, int],
    visible: tuple[tuple[int, ...], ...],
) -> tuple[Grid, Grid]:
    x0 = canvas(ZERO, (side, side))
    x1 = canvas(ZERO, (side, side))
    for x2, x3 in zip(specs, visible):
        x4 = _frame_outline_2e65ae53(x2)
        x0 = fill(x0, border_color, x4)
        x1 = fill(x1, border_color, x4)
        x5 = _frame_quadrants_2e65ae53(x2)
        for x6, x7 in enumerate(x5):
            x1 = fill(x1, quad_colors[x6], x7)
            if x6 in x3:
                x0 = fill(x0, quad_colors[x6], x7)
    return (x0, x1)


def _input_ok_2e65ae53(I: Grid, border_color: int) -> bool:
    x0 = palette(I) - {ZERO}
    if len(x0) != FIVE:
        return F
    x1 = colorcount(I, border_color)
    x2 = colorcount(I, ZERO)
    x3 = tuple(colorcount(I, x4) for x4 in x0 if x4 != border_color)
    return both(x2 > x1, x1 > maximum(x3))


def generate_2e65ae53(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(interval(ONE, TEN, ONE))
    while True:
        x1 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        x2 = tuple(_sample_frame_shape_2e65ae53(diff_lb, diff_ub, x1) for _ in range(x1))
        x3 = _place_frames_2e65ae53(x2)
        if x3 is None:
            continue
        x4, x5 = _crop_specs_2e65ae53(x3)
        x6 = _sample_visibility_2e65ae53(diff_lb, diff_ub, x1)
        x7 = sample(x0, FIVE)
        x8 = x7[ZERO]
        x9 = tuple(x7[ONE:])
        x10, x11 = _draw_grid_2e65ae53(x4, x5, x8, x9, x6)
        if not _input_ok_2e65ae53(x10, x8):
            continue
        return {"input": x10, "output": x11}
