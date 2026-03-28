from arc2.core import *


GRID_SIDE_522FDD07 = 16
BACKGROUND_522FDD07 = SEVEN
COLORS_522FDD07 = tuple(x0 for x0 in interval(ZERO, TEN, ONE) if x0 != SEVEN)
SIZES_522FDD07 = (THREE, THREE, FIVE, FIVE, FIVE, SEVEN, SEVEN, NINE)


def _square_patch_522fdd07(
    top: Integer,
    left: Integer,
    size_: Integer,
) -> Indices:
    x0 = interval(top, top + size_, ONE)
    x1 = interval(left, left + size_, ONE)
    return product(x0, x1)


def _output_patch_522fdd07(
    top: Integer,
    left: Integer,
    size_: Integer,
) -> Indices:
    if equality(size_, ONE):
        x0 = max(ZERO, top - FOUR)
        x1 = min(GRID_SIDE_522FDD07, top + FIVE)
        x2 = max(ZERO, left - FOUR)
        x3 = min(GRID_SIDE_522FDD07, left + FIVE)
        return product(interval(x0, x1, ONE), interval(x2, x3, ONE))
    return _square_patch_522fdd07(top + ONE, left + ONE, size_ - TWO)


def _edge_positions_522fdd07(
    size_: Integer,
) -> tuple[IntegerTuple, ...]:
    x0 = GRID_SIDE_522FDD07 - size_
    x1 = []
    for x2 in range(x0 + ONE):
        for x3 in range(x0 + ONE):
            if x2 in (ZERO, x0) or x3 in (ZERO, x0):
                x1.append((x2, x3))
    return tuple(x1)


def _interior_positions_522fdd07(
    size_: Integer,
) -> tuple[IntegerTuple, ...]:
    x0 = GRID_SIDE_522FDD07 - size_
    x1 = []
    for x2 in range(x0 + ONE):
        for x3 in range(x0 + ONE):
            if 0 < x2 < x0 and 0 < x3 < x0:
                x1.append((x2, x3))
    return tuple(x1)


def _singleton_clipped_positions_522fdd07() -> tuple[IntegerTuple, ...]:
    x0 = []
    for x1 in range(GRID_SIDE_522FDD07):
        for x2 in range(GRID_SIDE_522FDD07):
            if x1 < FOUR or x1 >= GRID_SIDE_522FDD07 - FOUR or x2 < FOUR or x2 >= GRID_SIDE_522FDD07 - FOUR:
                x0.append((x1, x2))
    return tuple(x0)


def _singleton_interior_positions_522fdd07() -> tuple[IntegerTuple, ...]:
    x0 = []
    for x1 in range(GRID_SIDE_522FDD07):
        for x2 in range(GRID_SIDE_522FDD07):
            if FOUR <= x1 < GRID_SIDE_522FDD07 - FOUR and FOUR <= x2 < GRID_SIDE_522FDD07 - FOUR:
                x0.append((x1, x2))
    return tuple(x0)


def _valid_spec_522fdd07(
    top: Integer,
    left: Integer,
    size_: Integer,
    placed: tuple[tuple[Integer, Integer, Integer, Integer], ...],
) -> Boolean:
    x0 = _square_patch_522fdd07(top, left, size_)
    x1 = _output_patch_522fdd07(top, left, size_)
    for _, x2, x3, x4 in placed:
        x5 = _square_patch_522fdd07(x2, x3, x4)
        x6 = _output_patch_522fdd07(x2, x3, x4)
        if intersection(x0, x5) or intersection(x0, outbox(x5)):
            return F
        if intersection(x1, x6) or intersection(x1, outbox(x6)):
            return F
    return T


def _render_input_522fdd07(
    specs: tuple[tuple[Integer, Integer, Integer, Integer], ...],
) -> Grid:
    x0 = canvas(BACKGROUND_522FDD07, (GRID_SIDE_522FDD07, GRID_SIDE_522FDD07))
    for x1, x2, x3, x4 in specs:
        x5 = _square_patch_522fdd07(x2, x3, x4)
        x0 = fill(x0, x1, x5)
    return x0


def _render_output_522fdd07(
    specs: tuple[tuple[Integer, Integer, Integer, Integer], ...],
) -> Grid:
    x0 = canvas(BACKGROUND_522FDD07, (GRID_SIDE_522FDD07, GRID_SIDE_522FDD07))
    for x1, x2, x3, x4 in specs:
        x5 = _output_patch_522fdd07(x2, x3, x4)
        x0 = fill(x0, x1, x5)
    return x0


def _sample_position_522fdd07(
    size_: Integer,
    used: tuple[tuple[Integer, Integer, Integer, Integer], ...],
) -> IntegerTuple | None:
    if equality(size_, ONE):
        x0 = (
            _singleton_clipped_positions_522fdd07(),
            _singleton_interior_positions_522fdd07(),
        )
    else:
        x0 = (
            _edge_positions_522fdd07(size_),
            _interior_positions_522fdd07(size_),
        )
    x1 = list(x0)
    shuffle(x1)
    for x2 in x1:
        x3 = list(x2)
        shuffle(x3)
        for x4, x5 in x3:
            if _valid_spec_522fdd07(x4, x5, size_, used):
                return (x4, x5)
    return None


def _sample_specs_522fdd07(
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[Integer, Integer, Integer, Integer], ...]:
    while True:
        x0 = choice((F, T, T))
        x1 = FOUR if x0 else FIVE
        x2 = unifint(diff_lb, diff_ub, (THREE, x1))
        x3 = []
        if x0:
            x3.append(ONE)
        while len(x3) < x2:
            x4 = choice(SIZES_522FDD07)
            x3.append(x4)
        shuffle(x3)
        x5 = sample(COLORS_522FDD07, x2)
        x6 = []
        x7 = T
        for x8, x9 in zip(x5, x3):
            x10 = _sample_position_522fdd07(x9, tuple(x6))
            if x10 is None:
                x7 = F
                break
            x11, x12 = x10
            x6.append((x8, x11, x12, x9))
        if flip(x7):
            continue
        x13 = tuple(x6)
        x14 = sum(equality(x15, ONE) for _, _, _, x15 in x13)
        if x14 > ONE:
            continue
        return x13


def generate_522fdd07(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_specs_522fdd07(diff_lb, diff_ub)
        x1 = _render_input_522fdd07(x0)
        x2 = _render_output_522fdd07(x0)
        if equality(x1, x2):
            continue
        return {"input": x1, "output": x2}
