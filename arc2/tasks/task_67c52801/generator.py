from arc2.core import *


def _rectangle_67c52801(
    color_value: int,
    top: int,
    left: int,
    obj_height: int,
    obj_width: int,
) -> Object:
    x0 = frozenset(
        (x1, x2)
        for x1 in range(top, add(top, obj_height))
        for x2 in range(left, add(left, obj_width))
    )
    return recolor(color_value, x0)


def _distribute_67c52801(
    parts: int,
    extra: int,
) -> tuple[int, ...]:
    x0 = [ONE for _ in range(parts)]
    for _ in range(extra):
        x1 = randint(ZERO, decrement(parts))
        x0[x1] = increment(x0[x1])
    return tuple(x0)


def _scatter_rectangles_67c52801(
    top_height: int,
    grid_width: int,
    dims: tuple[tuple[int, int], ...],
) -> tuple[tuple[int, int], ...] | None:
    x0 = sorted(range(len(dims)), key=lambda x1: multiply(dims[x1][0], dims[x1][1]), reverse=True)
    x1 = {}
    x2 = set()
    for x3 in x0:
        x4, x5 = dims[x3]
        x6 = []
        x7 = add(subtract(top_height, x4), ONE)
        x8 = add(subtract(grid_width, x5), ONE)
        for x9 in range(x7):
            for x10 in range(x8):
                x11 = max(ZERO, decrement(x9))
                x12 = min(top_height, add(add(x9, x4), ONE))
                x13 = max(ZERO, decrement(x10))
                x14 = min(grid_width, add(add(x10, x5), ONE))
                x15 = T
                for x16 in range(x11, x12):
                    for x17 in range(x13, x14):
                        if contained((x16, x17), x2):
                            x15 = F
                            break
                    if flip(x15):
                        break
                if x15:
                    x6.append((x9, x10))
        if equality(len(x6), ZERO):
            return None
        x18 = choice(x6)
        x1[x3] = x18
        x19, x20 = x18
        x21 = max(ZERO, decrement(x19))
        x22 = min(top_height, add(add(x19, x4), ONE))
        x23 = max(ZERO, decrement(x20))
        x24 = min(grid_width, add(add(x20, x5), ONE))
        for x25 in range(x21, x22):
            for x26 in range(x23, x24):
                x2.add((x25, x26))
    return tuple(x1[x27] for x27 in range(len(dims)))


def _unique_assignment_67c52801(
    gap_widths: tuple[int, ...],
    dims: tuple[tuple[int, int], ...],
) -> bool:
    def _count(
        gaps_left: tuple[int, ...],
        dims_left: tuple[tuple[int, int], ...],
    ) -> int:
        if equality(len(gaps_left), ZERO):
            return ONE
        x0 = ZERO
        x1 = first(gaps_left)
        for x2, x3 in enumerate(dims_left):
            x4, x5 = x3
            if flip(either(equality(x4, x1), equality(x5, x1))):
                continue
            x6 = dims_left[:x2] + dims_left[increment(x2):]
            x0 = add(x0, _count(gaps_left[ONE:], x6))
            if greater(x0, ONE):
                return x0
        return x0

    return equality(_count(gap_widths, dims), ONE)


def _floor_grid_67c52801(
    grid_height: int,
    grid_width: int,
    floor_color: int,
    gaps: tuple[tuple[int, int], ...],
) -> Grid:
    x0 = canvas(ZERO, (grid_height, grid_width))
    x1 = connect((decrement(grid_height), ZERO), (decrement(grid_height), decrement(grid_width)))
    x2 = fill(x0, floor_color, x1)
    x3 = frozenset(x4 for x5, x6 in gaps for x4 in range(x5, add(x5, x6)))
    x4 = frozenset(
        (subtract(grid_height, TWO), x5)
        for x5 in range(grid_width)
        if flip(contained(x5, x3))
    )
    return fill(x2, floor_color, x4)


def generate_67c52801(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((ONE, TWO, TWO, THREE, THREE))
        x1 = tuple(sorted(sample(interval(ONE, FIVE, ONE), x0)))
        x2 = unifint(diff_lb, diff_ub, (ZERO, THREE))
        x3 = _distribute_67c52801(add(x0, ONE), x2)
        x4 = []
        x5 = x3[ZERO]
        for x6, x7 in enumerate(x1):
            x4.append((x5, x7))
            x5 = add(add(x5, x7), x3[increment(x6)])
        x8 = x5
        if greater(x8, 12):
            continue
        x9 = choice(interval(ONE, TEN, ONE))
        x10 = tuple(x11 for x11 in interval(ONE, TEN, ONE) if flip(equality(x11, x9)))
        x11 = tuple(sample(x10, x0))
        x12 = []
        x13 = []
        for x14, x15 in zip(x1, x11):
            x16 = choice((TWO, TWO, THREE, THREE, FOUR))
            x17 = both(flip(equality(x14, x16)), choice((T, F)))
            x18 = (x14, x16) if x17 else (x16, x14)
            x12.append((x15, x16, x14, x18[ZERO], x18[ONE]))
            x13.append((x18[ZERO], x18[ONE]))
        x18 = tuple((x19[ONE], x19[TWO]) for x19 in x12)
        if flip(_unique_assignment_67c52801(x1, x18)):
            continue
        x19 = maximum(tuple(x20[ONE] for x20 in x12))
        x20 = maximum(tuple(x21[THREE] for x21 in x12))
        x21 = maximum((x19, x20))
        x22 = add(x21, unifint(diff_lb, diff_ub, (ONE, FOUR)))
        x23 = add(x22, TWO)
        x24 = _scatter_rectangles_67c52801(x22, x8, tuple(x13))
        if equality(x24, None):
            continue
        x25 = _floor_grid_67c52801(x23, x8, x9, tuple(x4))
        x26 = x25
        for x27, x28 in zip(x12, x24):
            x29, x30, x31, x32, x33 = x27
            x34, x35 = x28
            x36 = _rectangle_67c52801(x29, x34, x35, x32, x33)
            x26 = paint(x26, x36)
        x37 = _floor_grid_67c52801(x23, x8, x9, tuple(x4))
        for x38, x39 in zip(x12, x4):
            x40, x41, x42, _, _ = x38
            x43, _ = x39
            x44 = add(subtract(x22, x41), ONE)
            x45 = _rectangle_67c52801(x40, x44, x43, x41, x42)
            x37 = paint(x37, x45)
        return {"input": x26, "output": x37}
