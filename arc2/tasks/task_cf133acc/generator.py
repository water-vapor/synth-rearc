from arc2.core import *


def _column_patch_cf133acc(
    col: int,
    start: int,
    stop: int,
) -> Indices:
    return frozenset((i, col) for i in range(start, stop))


def _row_patch_cf133acc(
    row: int,
    start: int,
    stop: int,
    skip: tuple[int, ...],
) -> Indices:
    return frozenset((row, j) for j in range(start, stop) if j not in skip)


def _choose_color_cf133acc(
    avoid: tuple[int, ...],
) -> int:
    x0 = tuple(x1 for x1 in interval(ONE, TEN, ONE) if x1 not in avoid)
    return choice(x0)


def _gap_events_cf133acc(
    grid: Grid,
) -> frozenset[tuple[int, int, int]]:
    h = len(grid)
    w = len(grid[0])
    out = set()
    for i in range(h):
        for j in range(1, w - 1):
            if grid[i][j] != ZERO:
                continue
            left = grid[i][j - 1]
            right = grid[i][j + 1]
            if left != ZERO and left == right:
                out.add((i, j, left))
    return frozenset(out)


def generate_cf133acc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = 15
    x1 = (x0, x0)
    while True:
        x2 = choice((ONE, THREE, THREE, THREE))
        x3 = choice((EIGHT, NINE, NINE, NINE))
        x4 = unifint(diff_lb, diff_ub, (ONE, FIVE))
        x5 = tuple(sorted(sample(interval(ONE, 12, ONE), x4)))
        x6 = ("B",) if equality(x4, ONE) else tuple(choice(("L", "L", "R", "R", "B")) for _ in x5)
        x7 = any(x8 in ("L", "B") for x8 in x6)
        x9 = any(x10 in ("R", "B") for x10 in x6)
        if flip(both(x7, x9)):
            continue
        x11 = {}
        x12 = None
        x13 = None
        for x14, x15 in zip(x5, x6):
            x16 = {}
            if equality(x15, "L"):
                x17 = _choose_color_cf133acc(() if x12 is None else (x12,))
                x16["left"] = x17
                x12 = x17
            elif equality(x15, "R"):
                x18 = _choose_color_cf133acc(() if x13 is None else (x13,))
                x16["right"] = x18
                x13 = x18
            else:
                x19 = choice((T, F, F))
                if x19:
                    x20 = tuple(
                        x21 for x21 in (x12, x13) if flip(equality(x21, None))
                    )
                    x22 = _choose_color_cf133acc(x20)
                    x16["left"] = x22
                    x16["right"] = x22
                    x12 = x22
                    x13 = x22
                else:
                    x23 = _choose_color_cf133acc(() if x12 is None else (x12,))
                    x24 = _choose_color_cf133acc(
                        tuple(x25 for x25 in (x13, x23) if flip(equality(x25, None)))
                    )
                    x16["left"] = x23
                    x16["right"] = x24
                    x12 = x23
                    x13 = x24
            x11[x14] = x16
        x26 = tuple(x27 for x27 in x5 if contained("left", x11[x27]))
        x28 = tuple(x29 for x29 in x5 if contained("right", x11[x29]))
        x30 = last(x26)
        x31 = last(x28)
        x32 = choice(tuple(range(max(increment(x30), NINE), x0)))
        x33 = choice(tuple(range(max(increment(x31), NINE), x0)))
        x34 = _choose_color_cf133acc(() if x12 is None else (x12,))
        x35 = choice((T, F, F, F))
        if x35:
            x36 = x34
        else:
            x36 = _choose_color_cf133acc(() if x13 is None else (x13,))
        x37 = canvas(ZERO, x1)
        x38 = canvas(ZERO, x1)
        x39 = []
        x40 = []
        for x41 in x5:
            x42 = x11[x41]
            x43 = contained("left", x42)
            x44 = contained("right", x42)
            x45 = both(x43, x44)
            x46 = both(x45, equality(x42["left"], x42["right"])) if x45 else F
            if x46:
                x47 = x42["left"]
                x48 = _row_patch_cf133acc(x41, ZERO, x0, (x2, x3))
                x37 = fill(x37, x47, x48)
                x38 = fill(x38, x47, x48)
                x39.append((x41, x47))
                x40.append((x41, x47))
                continue
            if x45:
                x49 = max(add(x2, TWO), FIVE)
                x50 = choice(tuple(range(x49, subtract(x3, ONE))))
                x51 = choice(tuple(range(increment(x50), x3)))
                x52 = _row_patch_cf133acc(x41, ZERO, increment(x50), (x2,))
                x53 = _row_patch_cf133acc(x41, x51, x0, (x3,))
                x37 = fill(x37, x42["left"], x52)
                x38 = fill(x38, x42["left"], x52)
                x37 = fill(x37, x42["right"], x53)
                x38 = fill(x38, x42["right"], x53)
                x39.append((x41, x42["left"]))
                x40.append((x41, x42["right"]))
                continue
            if x43:
                x54 = choice(tuple(range(max(add(x2, TWO), FIVE), min(x3, EIGHT))))
                x55 = _row_patch_cf133acc(x41, ZERO, increment(x54), (x2,))
                x37 = fill(x37, x42["left"], x55)
                x38 = fill(x38, x42["left"], x55)
                x39.append((x41, x42["left"]))
                continue
            x56 = choice(tuple(range(max(add(x2, ONE), FIVE), x3)))
            x57 = _row_patch_cf133acc(x41, x56, x0, (x3,))
            x37 = fill(x37, x42["right"], x57)
            x38 = fill(x38, x42["right"], x57)
            x40.append((x41, x42["right"]))
        x58 = _column_patch_cf133acc(x2, x32, x0)
        x59 = _column_patch_cf133acc(x3, x33, x0)
        x37 = fill(x37, x34, x58)
        x37 = fill(x37, x36, x59)
        x38 = fill(x38, x34, x58)
        x38 = fill(x38, x36, x59)
        x60 = ZERO
        for x61, x62 in x39:
            x63 = _column_patch_cf133acc(x2, x60, increment(x61))
            x38 = fill(x38, x62, x63)
            x60 = increment(x61)
        x64 = _column_patch_cf133acc(x2, x60, x0)
        x38 = fill(x38, x34, x64)
        x65 = ZERO
        for x66, x67 in x40:
            x68 = _column_patch_cf133acc(x3, x65, increment(x66))
            x38 = fill(x38, x67, x68)
            x65 = increment(x66)
        x69 = _column_patch_cf133acc(x3, x65, x0)
        x38 = fill(x38, x36, x69)
        x70 = frozenset(
            {(x71, x2, x72) for x71, x72 in x39} | {(x73, x3, x74) for x73, x74 in x40}
        )
        x75 = _gap_events_cf133acc(x37)
        if flip(equality(x70, x75)):
            continue
        if equality(x37, x38):
            continue
        return {"input": x37, "output": x38}
