from arc2.core import *

from .verifier import verify_845d6e51


SHAPES_845D6E51 = (
    frozenset({(0, 0), (1, 0)}),
    frozenset({(0, 0), (0, 1), (1, 0)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)}),
    frozenset({(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)}),
)
COLORS_845D6E51 = (ONE, TWO, FOUR, SEVEN, EIGHT)
DIVIDER_ROW_845D6E51 = THREE
MAX_GRID_SIDE_845D6E51 = 18
TOP_RIGHT_OFFSET_845D6E51 = THREE


def _shape_variants_845d6e51(x0: Patch) -> tuple[Indices, ...]:
    x1 = normalize(toindices(x0))
    x2 = canvas(ZERO, shape(x1))
    x3 = fill(x2, ONE, x1)
    x4 = (
        ofcolor(x3, ONE),
        ofcolor(rot90(x3), ONE),
        ofcolor(rot180(x3), ONE),
        ofcolor(rot270(x3), ONE),
        ofcolor(hmirror(x3), ONE),
        ofcolor(vmirror(x3), ONE),
        ofcolor(dmirror(x3), ONE),
        ofcolor(cmirror(x3), ONE),
    )
    return tuple(dict.fromkeys(x4))


def _buffer_845d6e51(x0: Indices) -> Indices:
    x1 = mapply(neighbors, x0)
    return combine(x0, x1)


def _paint_indices_845d6e51(
    x0: Grid,
    x1: Integer,
    x2: Indices,
) -> Grid:
    return fill(x0, x1, x2)


def generate_845d6e51(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, FOUR))
        x1 = sample(tuple(range(len(SHAPES_845D6E51))), x0)
        x2 = sample(COLORS_845D6E51, x0)
        x3 = randint(ZERO, ONE)
        x4: list[tuple[int, int, Indices]] = []
        for x5, x6 in zip(x1, x2):
            x7 = choice(_shape_variants_845d6e51(SHAPES_845D6E51[x5]))
            x8 = randint(ZERO, DIVIDER_ROW_845D6E51 - height(x7))
            x9 = shift(x7, (x8, x3))
            x4.append((x5, x6, x9))
            x3 = add(rightmost(x9), randint(TWO, THREE))
        x10 = maximum(apply(rightmost, tuple(x11 for _, _, x11 in x4)))
        x11 = add(x10, randint(ONE, TWO))
        if x11 > 12:
            continue
        x12 = unifint(diff_lb, diff_ub, (TEN, MAX_GRID_SIDE_845D6E51))
        x13 = randint(ZERO, TWO) > ZERO
        x14 = None
        if x13:
            x15, x16, _ = choice(x4)
            x17 = choice(_shape_variants_845d6e51(SHAPES_845D6E51[x15]))
            x18 = randint(ZERO, DIVIDER_ROW_845D6E51 - height(x17))
            x19 = add(x11, TOP_RIGHT_OFFSET_845D6E51)
            x20 = add(x19, width(x17))
            if x20 > MAX_GRID_SIDE_845D6E51:
                continue
            x21 = max(TEN, x20)
            x22 = randint(x21, MAX_GRID_SIDE_845D6E51)
            x23 = randint(x19, subtract(x22, width(x17)))
            x14 = (x15, x16, shift(x17, (x18, x23)))
            x24 = x22
        else:
            x24 = randint(max(TEN, add(x11, FOUR)), MAX_GRID_SIDE_845D6E51)
        x25 = canvas(ZERO, (x12, x24))
        x26 = frozenset((DIVIDER_ROW_845D6E51, j) for j in range(x11 + ONE))
        x27 = frozenset((i, x11) for i in range(DIVIDER_ROW_845D6E51 + ONE))
        x28 = combine(x26, x27)
        x29 = _paint_indices_845d6e51(x25, FIVE, x28)
        x30 = x29
        x31 = dict()
        x32 = _buffer_845d6e51(x28)
        for x33, x34, x35 in x4:
            x31[x33] = x34
            x29 = _paint_indices_845d6e51(x29, x34, x35)
            x30 = _paint_indices_845d6e51(x30, x34, x35)
            x32 = combine(x32, _buffer_845d6e51(x35))
        x36: list[tuple[int, Indices]] = []
        if x14 is not None:
            x37, _, x38 = x14
            x29 = _paint_indices_845d6e51(x29, THREE, x38)
            x30 = _paint_indices_845d6e51(x30, x31[x37], x38)
            x36.append((x37, x38))
            x32 = combine(x32, _buffer_845d6e51(x38))
        x39 = randint(max(THREE, x0), min(TEN, add(x0, FIVE)))
        x40 = list(x1)
        while len(x40) < x39:
            x40.append(choice(x1))
        shuffle(x40)
        x41 = False
        for x42 in x40:
            x43 = False
            for _ in range(200):
                x44 = choice(_shape_variants_845d6e51(SHAPES_845D6E51[x42]))
                x45 = subtract(x12, height(x44))
                x46 = subtract(x24, width(x44))
                if x45 <= DIVIDER_ROW_845D6E51 or x46 < ZERO:
                    x41 = True
                    break
                x47 = randint(DIVIDER_ROW_845D6E51 + ONE, x45)
                x48 = randint(ZERO, x46)
                x49 = shift(x44, (x47, x48))
                if len(intersection(x49, x32)) > ZERO:
                    continue
                x29 = _paint_indices_845d6e51(x29, THREE, x49)
                x30 = _paint_indices_845d6e51(x30, x31[x42], x49)
                x36.append((x42, x49))
                x32 = combine(x32, _buffer_845d6e51(x49))
                x43 = True
                break
            if x41 or not x43:
                x41 = True
                break
        if x41:
            continue
        if len(x36) < x0:
            continue
        if verify_845d6e51(x29) != x30:
            continue
        return {"input": x29, "output": x30}
