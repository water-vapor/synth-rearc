from arc2.core import *


def _window_patch_9caba7c3(start: IntegerTuple) -> frozenset[IntegerTuple]:
    return frozenset(
        (start[0] + i, start[1] + j)
        for i in range(THREE)
        for j in range(THREE)
    )


def _maximal_windows_9caba7c3(grid: Grid) -> tuple[IntegerTuple, ...]:
    x0 = interval(ZERO, THREE, ONE)
    x1 = []
    x2 = len(grid)
    x3 = len(grid[0])
    for i in range(x2 - TWO):
        for j in range(x3 - TWO):
            x4 = crop(grid, (i, j), THREE_BY_THREE)
            x5 = tuple(x4[a][b] for a in x0 for b in x0)
            if not all(v in (TWO, FIVE) for v in x5):
                continue
            if x4[ONE][ONE] != FIVE:
                continue
            x6 = frozenset(
                (i + a, j + b)
                for a in x0
                for b in x0
                if grid[i + a][j + b] == TWO
            )
            if len(x6) == ZERO:
                continue
            x1.append(((i, j), x6))
    return tuple(loc for loc, reds in x1 if not any(reds < reds2 for _, reds2 in x1))


def _chebyshev_9caba7c3(a: IntegerTuple, b: IntegerTuple) -> int:
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def generate_9caba7c3(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple((i, j) for i in range(THREE) for j in range(THREE) if (i, j) != (ONE, ONE))
    while True:
        x1 = unifint(diff_lb, diff_ub, (48, 62)) / 100
        x2 = []
        x3 = []
        while len(x2) < FOUR:
            x4 = (randint(ZERO, 16), randint(ZERO, 16))
            x5 = _window_patch_9caba7c3(x4)
            if any(x5 & box for box in x3):
                continue
            x2.append(x4)
            x3.append(x5)
        x6 = {}
        x7 = []
        for x8 in x2:
            x9 = unifint(diff_lb, diff_ub, (ONE, SIX))
            x10 = frozenset((x8[0] + a, x8[1] + b) for a, b in sample(x0, x9))
            x6[x8] = x10
            x7.append(x10)
        x11 = False
        for a in range(len(x7)):
            for b in range(a + ONE, len(x7)):
                if any(
                    _chebyshev_9caba7c3(ca, cb) <= TWO
                    for ca in x7[a]
                    for cb in x7[b]
                ):
                    x11 = True
                    break
            if x11:
                break
        if x11:
            continue
        x12 = [
            [FIVE if uniform(ZERO, ONE) < x1 else ZERO for _ in range(19)]
            for _ in range(19)
        ]
        for x13 in x2:
            for i, j in _window_patch_9caba7c3(x13):
                x12[i][j] = FIVE
            for i, j in x6[x13]:
                x12[i][j] = TWO
        x14 = frozenset().union(*x3)
        x15 = set(x2)
        x16 = format_grid(x12)
        x17 = set(_maximal_windows_9caba7c3(x16))
        while x17 != x15:
            x18 = tuple(loc for loc in x17 if loc not in x15)
            if len(x18) == ZERO:
                break
            for x19 in x18:
                x20 = tuple(
                    cell
                    for cell in _window_patch_9caba7c3(x19)
                    if cell not in x14 and x12[cell[0]][cell[1]] == FIVE
                )
                if len(x20) == ZERO:
                    x11 = True
                    break
                x21 = choice(x20)
                x12[x21[0]][x21[1]] = ZERO
            if x11:
                break
            x16 = format_grid(x12)
            x17 = set(_maximal_windows_9caba7c3(x16))
        if x11 or x17 != x15:
            continue
        x22 = [row[:] for row in x12]
        for x23 in x2:
            for i, j in _window_patch_9caba7c3(x23):
                if x22[i][j] == FIVE:
                    x22[i][j] = SEVEN
            x22[x23[0] + ONE][x23[1] + ONE] = FOUR
        return {
            "input": format_grid(x12),
            "output": format_grid(x22),
        }
