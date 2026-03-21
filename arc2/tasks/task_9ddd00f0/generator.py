from arc2.core import *


def _grid_side_9ddd00f0(order: Integer) -> Integer:
    return order * order + order - ONE


def _render_9ddd00f0(
    order: Integer,
    color_: Integer,
    blocks: tuple[IntegerTuple, ...],
) -> Grid:
    x0 = _grid_side_9ddd00f0(order)
    x1 = canvas(ZERO, (x0, x0))
    x2 = order + ONE
    for x3, x4 in blocks:
        x5 = x3 * x2
        x6 = x4 * x2
        x7 = interval(x5, x5 + order, ONE)
        x8 = interval(x6, x6 + order, ONE)
        x9 = product(x7, x8)
        x1 = fill(x1, color_, x9)
        x10 = initset(astuple(x5 + x3, x6 + x4))
        x1 = fill(x1, ZERO, x10)
    return x1


def _neighbors_9ddd00f0(
    block: IntegerTuple,
    order: Integer,
) -> tuple[IntegerTuple, ...]:
    x0, x1 = block
    x2 = []
    for x3, x4 in ((-ONE, ZERO), (ONE, ZERO), (ZERO, -ONE), (ZERO, ONE)):
        x5 = x0 + x3
        x6 = x1 + x4
        if 0 <= x5 < order and 0 <= x6 < order:
            x2.append((x5, x6))
    return tuple(x2)


def _touch_count_9ddd00f0(
    blocks: tuple[IntegerTuple, ...],
    order: Integer,
) -> Integer:
    x0 = frozenset(x1 for x1, _ in blocks)
    x2 = frozenset(x3 for _, x3 in blocks)
    return sum((ZERO in x0, order - ONE in x0, ZERO in x2, order - ONE in x2))


def _sample_blocks_9ddd00f0(
    order: Integer,
    count: Integer,
) -> tuple[IntegerTuple, ...]:
    x0 = []
    x1 = order - ONE
    for x2 in range(order):
        for x3 in range(order):
            if x2 in (ZERO, x1) or x3 in (ZERO, x1):
                x0.append((x2, x3))
    x4 = tuple(x0)
    while True:
        x5 = {choice(x4)}
        while len(x5) < count:
            x6 = []
            for x7 in x5:
                for x8 in _neighbors_9ddd00f0(x7, order):
                    if x8 not in x5 and x8 not in x6:
                        x6.append(x8)
            x5.add(choice(tuple(x6)))
        x9 = tuple(sorted(x5))
        if _touch_count_9ddd00f0(x9, order) >= TWO:
            return x9


def generate_9ddd00f0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = unifint(diff_lb, diff_ub, (TWO, FIVE))
    x1 = choice(interval(ONE, TEN, ONE))
    x2 = max(TWO, 2 * x0 - 2)
    x3 = min(x0 * x0 - ONE, 2 * x0 + ONE)
    x4 = unifint(diff_lb, diff_ub, (x2, x3))
    x5 = _sample_blocks_9ddd00f0(x0, x4)
    x6 = tuple(sorted(product(interval(ZERO, x0, ONE), interval(ZERO, x0, ONE))))
    gi = _render_9ddd00f0(x0, x1, x5)
    go = _render_9ddd00f0(x0, x1, x6)
    return {"input": gi, "output": go}
