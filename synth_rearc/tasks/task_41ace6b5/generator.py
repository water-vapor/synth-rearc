from synth_rearc.core import *


SIDE_LENGTHS_41ACE6B5 = (9, 11, 13, 15)


def _scaffold_41ace6b5(
    side: Integer,
    row2: Integer,
) -> Grid:
    x0 = canvas(SEVEN, (side, side))
    x1 = interval(ZERO, side, TWO)
    x2 = frozenset((row2, x3) for x3 in x1)
    x3 = fill(x0, TWO, x2)
    x4 = frozenset((increment(row2), x5) for x5 in x1)
    x5 = fill(x3, FIVE, x4)
    return x5


def _render_input_41ace6b5(
    side: Integer,
    row2: Integer,
    eight_counts: tuple[Integer, ...],
    one_counts: tuple[Integer, ...],
) -> Grid:
    x0 = _scaffold_41ace6b5(side, row2)
    x1 = interval(ONE, side, TWO)
    for x2, x3, x4 in zip(x1, eight_counts, one_counts):
        x5 = subtract(subtract(side, x3), x4)
        x6 = frozenset((x7, x2) for x7 in interval(x5, add(x5, x3), ONE))
        x0 = fill(x0, EIGHT, x6)
        x7 = frozenset((x8, x2) for x8 in interval(add(x5, x3), side, ONE))
        x0 = fill(x0, ONE, x7)
    return x0


def _render_output_41ace6b5(
    side: Integer,
    row2: Integer,
    eight_depth: Integer,
    one_counts: tuple[Integer, ...],
) -> Grid:
    x0 = _scaffold_41ace6b5(side, row2)
    x1 = interval(ONE, side, TWO)
    x2 = interval(add(subtract(row2, eight_depth), ONE), increment(row2), ONE)
    x3 = frozenset((x4, x5) for x4 in x2 for x5 in x1)
    x0 = fill(x0, EIGHT, x3)
    for x6, x7 in zip(x1, one_counts):
        x8 = frozenset((x9, x6) for x9 in interval(increment(row2), add(increment(row2), x7), ONE))
        x0 = fill(x0, ONE, x8)
        x9 = frozenset((x10, x6) for x10 in interval(add(increment(row2), x7), side, ONE))
        x0 = fill(x0, NINE, x9)
    return x0


def generate_41ace6b5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = subtract(len(SIDE_LENGTHS_41ACE6B5), ONE)
    while True:
        x1 = SIDE_LENGTHS_41ACE6B5[unifint(diff_lb, diff_ub, (ZERO, x0))]
        x2 = x1 // TWO
        x3 = TWO if x1 == NINE else choice((TWO, THREE, THREE))
        x4 = unifint(diff_lb, diff_ub, (max(TWO, subtract(x3, ONE)), subtract(x1, FOUR)))
        x5 = [x3 for _ in range(x2)]
        if both(greater(x3, TWO), choice((T, F))):
            x6 = randint(ZERO, subtract(x2, ONE))
            x5[x6] = subtract(x3, ONE)
        x7 = tuple(x5)
        x8 = [None for _ in range(x2)]
        x9 = tuple(range(x2))
        x10 = tuple(sample(x9, min(x2, choice((ONE, ONE, TWO)))))
        if choice((T, F)):
            x11 = choice(x10)
            x8[x11] = x4
            x10 = tuple(x12 for x12 in x10 if x12 != x11)
        for x13 in x10:
            x8[x13] = increment(x4)
        for x14, x15 in enumerate(x7):
            if x8[x14] is not None:
                continue
            x16 = min(add(x4, TWO), subtract(subtract(x1, x15), ONE))
            x17 = subtract(subtract(x1, x15), ONE)
            x8[x14] = unifint(diff_lb, diff_ub, (x16, x17))
        x18 = tuple(x8)
        x19 = tuple(subtract(subtract(x1, x20), x21) for x20, x21 in zip(x18, x7))
        if len(set(x19)) == ONE:
            x22 = randint(ZERO, subtract(x2, ONE))
            x23 = other(tuple(range(x2)), x22) if x2 == TWO else choice(tuple(x24 for x24 in range(x2) if x24 != x22))
            x25 = max(increment(x4), subtract(subtract(x1, x7[x22]), TWO))
            x18 = tuple(
                x25 if x26 == x22 else (x4 if x26 == x23 else x27)
                for x26, x27 in enumerate(x18)
            )
            x19 = tuple(subtract(subtract(x1, x28), x29) for x28, x29 in zip(x18, x7))
        x20 = _render_input_41ace6b5(x1, x4, x7, x19)
        x21 = _render_output_41ace6b5(x1, x4, x3, x19)
        if x20 == x21:
            continue
        return {"input": x20, "output": x21}
