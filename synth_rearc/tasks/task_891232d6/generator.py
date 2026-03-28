from synth_rearc.core import *


def _run_bounds_891232d6(
    grid: Grid,
    row: Integer,
    col: Integer,
) -> tuple[int, int]:
    x0 = width(grid)
    x1 = col
    while x1 > ZERO and grid[row][x1 - ONE] == SEVEN:
        x1 -= ONE
    x2 = col
    while x2 < x0 - ONE and grid[row][x2 + ONE] == SEVEN:
        x2 += ONE
    return (x1, x2)


def _simulate_891232d6(grid: Grid) -> Grid:
    x0 = [list(x1) for x1 in grid]
    x1 = height(grid)
    x2 = width(grid)

    def trace(row: Integer, col: Integer) -> None:
        x3 = row
        x4 = col
        while ZERO <= x3 < x1 and ZERO <= x4 < x2:
            if x3 == ZERO:
                x0[x3][x4] = SIX
                return
            if grid[x3 - ONE][x4] != SEVEN:
                x0[x3][x4] = TWO
                x3 -= ONE
                continue
            x5 = x3 - ONE
            x6, x7 = _run_bounds_891232d6(grid, x5, x4)
            del x6
            x8 = x7 + ONE
            x9 = both(x8 < x2, all(grid[x3][x10] == ZERO for x10 in range(x4, x8 + ONE)))
            if x9:
                x0[x5][x4] = EIGHT
                x0[x3][x4] = FOUR
                for x10 in range(x4 + ONE, x7 + ONE):
                    x0[x3][x10] = TWO
                x0[x3][x8] = THREE
                x3 = x5
                x4 = x8
                continue
            x0[x3][x4] = SIX
            return

    x11 = tuple(x12 for x12, x13 in enumerate(last(grid)) if x13 == SIX)
    x12 = subtract(x1, TWO)
    for x13 in x11:
        if x12 >= ZERO:
            trace(x12, x13)
    x14 = tuple(tuple(x15) for x15 in x0)
    return x14


def _sample_sources_891232d6(
    width_: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, ...]:
    x0 = min(FOUR, max(ONE, width_ // SIX))
    x1 = unifint(diff_lb, diff_ub, (ONE, x0))
    x2 = list(range(ONE, width_ - ONE))
    shuffle(x2)
    x3: list[int] = []
    for x4 in x2:
        if all(abs(x4 - x5) >= THREE for x5 in x3):
            x3.append(x4)
            if len(x3) == x1:
                break
    return tuple(sorted(x3))


def _place_success_891232d6(
    height_: Integer,
    width_: Integer,
    sevens: set[tuple[int, int]],
    reserved: set[tuple[int, int]],
    start_row: Integer,
    start_col: Integer,
) -> tuple[int, int] | None:
    for _ in range(120):
        x0 = min(EIGHT, start_row)
        if x0 < TWO:
            return None
        x1 = randint(TWO, x0)
        x2 = start_row - x1
        x3 = min(FOUR, start_col)
        x4 = min(SIX, width_ - start_col - TWO)
        if x4 < ZERO:
            return None
        x5 = start_col - randint(ZERO, x3)
        x6 = start_col + randint(ZERO, x4)
        x7 = {(x2, x8) for x8 in range(x5, x6 + ONE)}
        x8 = {(x2 + ONE, x9) for x9 in range(start_col, x6 + TWO)}
        x9 = {(x10, start_col) for x10 in range(x2 + ONE, start_row + ONE)}
        x10 = (x2, x6 + ONE)
        if x6 + ONE >= width_:
            continue
        if any(x11 in sevens or x11 in reserved for x11 in x7):
            continue
        if any(x11 in sevens for x11 in x8 | x9 | {x10}):
            continue
        if (x2, x5 - ONE) in sevens or (x2, x6 + ONE) in sevens:
            continue
        sevens.update(x7)
        reserved.update(x8)
        reserved.update(x9)
        reserved.add(x10)
        return (x2, x6 + ONE)
    return None


def _place_block_891232d6(
    height_: Integer,
    width_: Integer,
    sevens: set[tuple[int, int]],
    reserved: set[tuple[int, int]],
    start_row: Integer,
    start_col: Integer,
) -> bool:
    for _ in range(120):
        x0 = min(SEVEN, start_row)
        if x0 < TWO:
            return False
        x1 = randint(TWO, x0)
        x2 = start_row - x1
        x3 = min(THREE, start_col)
        x4 = min(THREE, width_ - start_col - TWO)
        x5 = start_col - randint(ZERO, x3)
        x6 = start_col + randint(ZERO, x4)
        x7 = {(x2, x8) for x8 in range(x5, x6 + ONE)}
        x8 = {(x9, start_col) for x9 in range(x2 + ONE, start_row + ONE)}
        x9 = choice(tuple(range(start_col + ONE, x6 + TWO)))
        x10 = (x2 + ONE, x9)
        if any(x11 in sevens or x11 in reserved for x11 in x7 | {x10}):
            continue
        if any(x11 in sevens for x11 in x8 | {(x2 + ONE, start_col)}):
            continue
        if (x2, x5 - ONE) in sevens or (x2, x6 + ONE) in sevens:
            continue
        sevens.update(x7)
        sevens.add(x10)
        reserved.update(x8)
        reserved.add((x2 + ONE, start_col))
        return True
    return False


def _add_noise_891232d6(
    height_: Integer,
    width_: Integer,
    target_sevens: Integer,
    sevens: set[tuple[int, int]],
    reserved: set[tuple[int, int]],
) -> None:
    for _ in range(800):
        if len(sevens) >= target_sevens:
            return
        x0 = randint(ZERO, height_ - ONE)
        x1 = randint(ONE, min(THREE, width_)) if choice((True, True, False)) else randint(FOUR, min(SEVEN, width_))
        x2 = randint(ZERO, width_ - x1)
        x3 = {(x0, x4) for x4 in range(x2, x2 + x1)}
        if any(x4 in sevens or x4 in reserved for x4 in x3):
            continue
        if (x0, x2 - ONE) in sevens or (x0, x2 + x1) in sevens:
            continue
        sevens.update(x3)
        if choice((False, False, False, True)) and x0 + ONE < height_:
            x4 = randint(ONE, min(FIVE, x1 + ONE, width_))
            x5 = randint(-ONE, ONE)
            x6 = max(ZERO, min(width_ - x4, x2 + x5))
            x7 = {(x0 + ONE, x8) for x8 in range(x6, x6 + x4)}
            if all(x8 not in sevens and x8 not in reserved for x8 in x7):
                if (x0 + ONE, x6 - ONE) not in sevens and (x0 + ONE, x6 + x4) not in sevens:
                    sevens.update(x7)


def generate_891232d6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (16, 30))
        x1 = unifint(diff_lb, diff_ub, (10, 30))
        x2 = _sample_sources_891232d6(x1, diff_lb, diff_ub)
        if len(x2) == ZERO:
            continue
        x3 = {(x0 - ONE, x4) for x4 in x2}
        x4: set[tuple[int, int]] = set()
        x5 = set(x3)
        x6 = ZERO
        x7 = True
        for x8 in sorted(x2, reverse=True):
            x9 = x8
            x10 = x0 - TWO
            x11 = randint(ONE, min(FIVE, max(ONE, x0 // FIVE)))
            x12 = ZERO
            while x12 < x11 and x10 >= THREE and x9 < x1 - ONE:
                x13 = _place_success_891232d6(x0, x1, x4, x5, x10, x9)
                if x13 is None:
                    break
                x10, x9 = x13
                x12 += ONE
                x6 += ONE
            if x12 == ZERO:
                x7 = False
                break
            x13 = both(choice((False, True, False)), both(x10 >= THREE, x9 < x1 - ONE))
            if x13:
                x14 = _place_block_891232d6(x0, x1, x4, x5, x10, x9)
                if not x14:
                    x5.update((x15, x9) for x15 in range(x10 + ONE))
            else:
                x5.update((x15, x9) for x15 in range(x10 + ONE))
        if not x7:
            continue
        x8 = multiply(x0, x1)
        x9 = randint(max(len(x4) + THREE, x8 // 24), max(len(x4) + SIX, x8 // TEN))
        _add_noise_891232d6(x0, x1, x9, x4, x5)
        x10 = canvas(ZERO, (x0, x1))
        x11 = fill(x10, SEVEN, x4)
        x12 = fill(x11, SIX, x3)
        x13 = _simulate_891232d6(x12)
        x14 = tuple(
            (x15, x16)
            for x15 in range(x0)
            for x16 in range(x1)
            if both(x13[x15][x16] == SIX, x12[x15][x16] != SIX)
        )
        x15 = colorcount(x13, EIGHT)
        if x15 != x6:
            continue
        if x15 > SIX:
            continue
        if len(x14) != len(x2):
            continue
        if x15 < len(x2):
            continue
        return {"input": x12, "output": x13}
