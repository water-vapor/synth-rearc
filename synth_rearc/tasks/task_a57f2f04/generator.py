from synth_rearc.core import *

from .helpers import ANCHORS_A57F2F04, render_input_block_a57f2f04, render_output_block_a57f2f04


NONZERO_COLORS_A57F2F04 = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN)
OUTER_PAD_A57F2F04 = TWO


def _touches_all_sides_a57f2f04(
    cells: set[IntegerTuple],
    dims: IntegerTuple,
) -> bool:
    x0, x1 = dims
    return (
        any(i == ZERO for i, _ in cells)
        and any(i == decrement(x0) for i, _ in cells)
        and any(j == ZERO for _, j in cells)
        and any(j == decrement(x1) for _, j in cells)
    )


def _connected_a57f2f04(
    cells: set[IntegerTuple],
) -> bool:
    x0 = [next(iter(cells))]
    x1 = set()
    while x0:
        x2 = x0.pop()
        if x2 in x1:
            continue
        x1.add(x2)
        x3 = {x4 for x4 in dneighbors(x2) if x4 in cells and x4 not in x1}
        x0.extend(x3)
    return len(x1) == len(cells)


def _fallback_tile_a57f2f04(
    color_value: Integer,
    dims: IntegerTuple,
) -> Grid:
    x0, x1 = dims
    x2 = {(ZERO, j) for j in range(x1)}
    x3 = {(i, ZERO) for i in range(ONE, x0)}
    x4 = {(decrement(x0), j) for j in range(ONE, x1)}
    x5 = combine(combine(x2, x3), x4)
    x6 = canvas(ZERO, dims)
    return fill(x6, color_value, x5)


def _sample_tile_a57f2f04(
    color_value: Integer,
) -> Grid:
    x0 = choice((TWO, TWO, THREE, THREE, FOUR))
    x1 = choice((TWO, THREE, THREE, FOUR, FIVE))
    x2 = [(i, j) for i in range(x0) for j in range(x1)]
    x3 = x0 * x1
    x4 = min(subtract(x3, ONE), max(THREE, add(x0, x1)))
    for _ in range(200):
        x5 = randint(x4, subtract(x3, ONE))
        x6 = set(sample(x2, x5))
        if not _touches_all_sides_a57f2f04(x6, (x0, x1)):
            continue
        if not _connected_a57f2f04(x6):
            continue
        x7 = canvas(ZERO, (x0, x1))
        return fill(x7, color_value, x6)
    return _fallback_tile_a57f2f04(color_value, (x0, x1))


def _extra_span_a57f2f04(
    size_value: Integer,
) -> Integer:
    if size_value == ONE:
        return ZERO
    x0 = tuple(range(ONE, size_value))
    return choice((ZERO, ZERO, ZERO) + x0)


def _boxes_separate_a57f2f04(
    box_a: Tuple[int, int, int, int],
    box_b: Tuple[int, int, int, int],
) -> bool:
    ar0, ac0, ar1, ac1 = box_a
    br0, bc0, br1, bc1 = box_b
    return (
        ar1 + ONE < br0
        or br1 + ONE < ar0
        or ac1 + ONE < bc0
        or bc1 + ONE < ac0
    )


def _find_origin_a57f2f04(
    grid_shape: IntegerTuple,
    block_shape: IntegerTuple,
    boxes: list[Tuple[int, int, int, int]],
) -> IntegerTuple | None:
    x0, x1 = grid_shape
    x2, x3 = block_shape
    x4 = list(
        product(
            range(OUTER_PAD_A57F2F04, x0 - x2 - OUTER_PAD_A57F2F04 + ONE),
            range(OUTER_PAD_A57F2F04, x1 - x3 - OUTER_PAD_A57F2F04 + ONE),
        )
    )
    shuffle(x4)
    for x5 in x4:
        x6, x7 = x5
        x8 = (x6, x7, x6 + x2 - ONE, x7 + x3 - ONE)
        if all(_boxes_separate_a57f2f04(x8, x9) for x9 in boxes):
            return x5
    return None


def generate_a57f2f04(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (18, 30))
        x1 = unifint(diff_lb, diff_ub, (18, 30))
        x2 = choice((ONE, TWO, TWO, THREE))
        x3 = sample(NONZERO_COLORS_A57F2F04, x2)
        x4 = []
        x5 = ZERO
        for x6 in x3:
            x7 = _sample_tile_a57f2f04(x6)
            x8, x9 = shape(x7)
            x10 = choice((TWO, TWO, THREE, THREE, FOUR))
            x11 = choice((TWO, TWO, THREE, THREE, FOUR, FIVE))
            x12 = add(multiply(x8, x10), _extra_span_a57f2f04(x8))
            x13 = add(multiply(x9, x11), _extra_span_a57f2f04(x9))
            x14 = choice(ANCHORS_A57F2F04)
            x15 = render_input_block_a57f2f04(x7, (x12, x13), x14)
            x16 = render_output_block_a57f2f04(x15)
            x4.append((x15, x16, (x12, x13)))
            x5 = add(x5, multiply(x12, x13))
        if x5 * TWO >= x0 * x1:
            continue
        x17 = canvas(EIGHT, (x0, x1))
        x18 = x17
        x19: list[Tuple[int, int, int, int]] = []
        x20 = F
        for x21, x22, x23 in x4:
            x24 = _find_origin_a57f2f04((x0, x1), x23, x19)
            if x24 is None:
                x20 = T
                break
            x25, x26 = x23
            x27, x28 = x24
            x29 = (x27, x28, x27 + x25 - ONE, x28 + x26 - ONE)
            x19.append(x29)
            x30 = shift(asobject(x21), x24)
            x31 = shift(asobject(x22), x24)
            x17 = paint(x17, x30)
            x18 = paint(x18, x31)
        if x20:
            continue
        if mostcolor(x17) != EIGHT:
            continue
        if x17 == x18:
            continue
        return {"input": x17, "output": x18}
