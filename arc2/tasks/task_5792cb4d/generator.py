from arc2.core import *

from .verifier import verify_5792cb4d


ACTIVE_COLORS_5792CB4D = (ONE, TWO, FOUR, FIVE, SIX, SEVEN, NINE)
GRID_SHAPE_5792CB4D = (TEN, TEN)
MIN_PATH_LENGTH_5792CB4D = EIGHT
MAX_PATH_LENGTH_5792CB4D = 28


def _inside_playfield_5792cb4d(
    x0: IntegerTuple,
) -> Boolean:
    x1, x2 = x0
    return ZERO < x1 < NINE and ZERO < x2 < NINE


def _direction_order_5792cb4d(
    x0: IntegerTuple,
    x1: frozenset[IntegerTuple],
    x2: IntegerTuple | None,
) -> tuple[IntegerTuple, ...]:
    x3 = []
    for x4 in (UP, DOWN, LEFT, RIGHT):
        x5 = add(x0, x4)
        if flip(_inside_playfield_5792cb4d(x5)):
            continue
        if x5 in x1:
            continue
        x6 = sum(x7 in x1 for x7 in dneighbors(x5))
        if x6 != ONE:
            continue
        x8 = THREE if x4 == x2 else ONE
        x3.extend(repeat(x4, x8))
    shuffle(x3)
    x9 = []
    x10 = set()
    for x11 in x3:
        if x11 in x10:
            continue
        x10.add(x11)
        x9.append(x11)
    return tuple(x9)


def _grow_path_5792cb4d(
    x0: list[IntegerTuple],
    x1: set[IntegerTuple],
    x2: Integer,
) -> tuple[IntegerTuple, ...] | None:
    if len(x0) == x2:
        return tuple(x0)
    x3 = x0[-ONE]
    x4 = subtract(x3, x0[-TWO]) if len(x0) > ONE else None
    x5 = _direction_order_5792cb4d(x3, frozenset(x1), x4)
    for x6 in x5:
        x7 = add(x3, x6)
        x0.append(x7)
        x1.add(x7)
        x8 = _grow_path_5792cb4d(x0, x1, x2)
        if x8 is not None:
            return x8
        x0.pop()
        x1.remove(x7)
    return None


def _turn_count_5792cb4d(
    x0: tuple[IntegerTuple, ...],
) -> Integer:
    x1 = tuple(subtract(x2, x3) for x2, x3 in zip(x0[ONE:], x0))
    return sum(x2 != x3 for x2, x3 in zip(x1[ONE:], x1))


def _sample_path_5792cb4d(
    x0: Integer,
) -> tuple[IntegerTuple, ...] | None:
    for _ in range(160):
        x1 = (randint(ONE, EIGHT), randint(ONE, EIGHT))
        x2 = _grow_path_5792cb4d([x1], {x1}, x0)
        if x2 is None:
            continue
        x3 = height(frozenset(x2))
        x4 = width(frozenset(x2))
        x5 = _turn_count_5792cb4d(x2)
        if x3 == ONE or x4 == ONE:
            continue
        if x5 == ZERO:
            continue
        return x2
    return None


def _color_sequence_5792cb4d(
    diff_lb: float,
    diff_ub: float,
    x0: Integer,
) -> tuple[Integer, ...]:
    x1 = min(SIX, x0)
    x2 = unifint(diff_lb, diff_ub, (FOUR, x1))
    x3 = tuple(sample(ACTIVE_COLORS_5792CB4D, x2))
    x4 = list(x3)
    while len(x4) < x0:
        x4.append(choice(x3))
    shuffle(x4)
    return tuple(x4)


def _render_path_5792cb4d(
    x0: tuple[IntegerTuple, ...],
    x1: tuple[Integer, ...],
) -> Grid:
    x2 = canvas(EIGHT, GRID_SHAPE_5792CB4D)
    x3 = frozenset((x4, x5) for x4, x5 in zip(x1, x0))
    return paint(x2, x3)


def generate_5792cb4d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (MIN_PATH_LENGTH_5792CB4D, MAX_PATH_LENGTH_5792CB4D))
        x1 = _sample_path_5792cb4d(x0)
        if x1 is None:
            continue
        x2 = _color_sequence_5792cb4d(diff_lb, diff_ub, x0)
        x3 = tuple(reversed(x2))
        if x2 == x3:
            continue
        gi = _render_path_5792cb4d(x1, x2)
        go = _render_path_5792cb4d(x1, x3)
        if verify_5792cb4d(gi) != go:
            continue
        return {"input": gi, "output": go}
