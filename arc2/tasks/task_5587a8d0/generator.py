from arc2.core import *


COLORS = remove(SEVEN, interval(ZERO, TEN, ONE))


def _compact_shape(card: int) -> Indices:
    x0 = {(ZERO, ZERO)}
    while len(x0) < card:
        x1 = set()
        for x2 in x0:
            x1.update(dneighbors(x2))
        x1.difference_update(x0)
        x3 = []
        for x4 in x1:
            x5 = frozenset(x0 | {x4})
            x6 = height(x5)
            x7 = width(x5)
            x8 = abs(subtract(x6, x7))
            x9 = x6 * x7
            x10 = x6 + x7
            x11 = abs(x4[0]) + abs(x4[1])
            x3.append(((x8, x9, x10, x11), x4))
        x9 = min(x10 for x10, _ in x3)
        x11 = [x12 for x10, x12 in x3 if x10 == x9]
        x0.add(choice(x11))
    return normalize(frozenset(x0))


def _shape_for_count(card: int) -> Indices:
    if card == ONE:
        return frozenset({ORIGIN})
    x0 = []
    for x1 in interval(ONE, increment(card), ONE):
        if card % x1 == ZERO:
            x2 = card // x1
            x3 = min(x1, x2)
            x4 = max(x1, x2)
            if both(greater(x3, ONE), greater(THREE, subtract(x4, x3))):
                x0.append((x1, x2))
    if len(x0) > ZERO and choice((T, F)):
        x3 = choice(x0)
        x4 = frozenset((i, j) for i in range(x3[0]) for j in range(x3[1]))
        if choice((T, F)):
            return dmirror(x4)
        return x4
    return _compact_shape(card)


def _expand(patch: Indices) -> Indices:
    x0 = set()
    for x1, x2 in patch:
        for x3 in (-ONE, ZERO, ONE):
            for x4 in (-ONE, ZERO, ONE):
                x0.add((x1 + x3, x2 + x4))
    return frozenset(x0)


def _placements(patch: Indices, h: int, w: int, blocked: Indices) -> list[Indices]:
    x0 = []
    x1 = height(patch)
    x2 = width(patch)
    for x3 in range(h - x1 + ONE):
        for x4 in range(w - x2 + ONE):
            x5 = shift(patch, (x3, x4))
            if len(intersection(x5, blocked)) == ZERO:
                x0.append(x5)
    return x0


def _build_output(colors: tuple[int, ...]) -> Grid:
    x0 = len(colors)
    x1 = 2 * x0 - 1
    x2 = canvas(colors[-1], (x1, x1))
    for x3, x4 in enumerate(colors[:-1]):
        x5 = frozenset((i, j) for i in range(x3, x1 - x3) for j in range(x3, x1 - x3))
        x2 = fill(x2, x4, box(x5))
    return x2


def generate_5587a8d0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (TWO, SIX))
        x1 = unifint(diff_lb, diff_ub, (x0 + TWO, x0 + SEVEN))
        x2 = tuple(sorted(sample(interval(ONE, increment(x1), ONE), x0), reverse=True))
        x3 = sum(x2)
        x4 = max(SIX, x0 + THREE, int((TWO * x3) ** 0.5))
        x5 = unifint(diff_lb, diff_ub, (x4, min(18, x4 + FIVE)))
        x6 = unifint(diff_lb, diff_ub, (x4, min(18, x4 + FIVE)))
        x7 = tuple(sample(COLORS, x0))
        x8 = canvas(SEVEN, (x5, x6))
        x9 = frozenset()
        x10 = frozenset()
        x11 = []
        x12 = False
        for x13 in x2:
            x14 = _shape_for_count(x13)
            x15 = _placements(x14, x5, x6, x10)
            if len(x15) == ZERO:
                x12 = True
                break
            x16 = choice(x15)
            x11.append(x16)
            x9 = combine(x9, x16)
            x10 = combine(x10, _expand(x16))
        if x12:
            continue
        for x13, x14 in zip(x7, x11):
            x8 = fill(x8, x13, x14)
        x17 = _build_output(x7)
        return {"input": x8, "output": x17}
