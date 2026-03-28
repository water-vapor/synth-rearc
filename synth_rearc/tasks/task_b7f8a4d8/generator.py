from synth_rearc.core import *

from .verifier import verify_b7f8a4d8


def _tile_starts_b7f8a4d8(size: Integer, gap: Integer, limit: Integer) -> tuple[Integer, ...]:
    x0 = tuple()
    x1 = ONE
    x2 = add(size, gap)
    while x1 < limit:
        x0 = x0 + (x1,)
        x1 = add(x1, x2)
    return x0


def _connect_specials_b7f8a4d8(
    grid: Grid,
    special_cells: dict[Integer, set[IntegerTuple]],
) -> Grid:
    x0 = ofcolor(grid, ZERO)
    x1 = grid
    for x2, x3 in special_cells.items():
        x4 = {x5[0] for x5 in x3}
        for x5 in x4:
            x6 = tuple(x7[1] for x7 in x3 if x7[0] == x5)
            x7 = frozenset((x5, x8) for x8 in range(min(x6), max(x6) + ONE))
            x8 = intersection(x7, x0)
            x1 = fill(x1, x2, x8)
        x9 = {x10[1] for x10 in x3}
        for x10 in x9:
            x11 = tuple(x12[0] for x12 in x3 if x12[1] == x10)
            x12 = frozenset((x13, x10) for x13 in range(min(x11), max(x11) + ONE))
            x13 = intersection(x12, x0)
            x1 = fill(x1, x2, x13)
    return x1


def generate_b7f8a4d8(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, (THREE, FOUR))
        x1 = unifint(diff_lb, diff_ub, (ONE, THREE))
        x2 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        x3 = unifint(diff_lb, diff_ub, (FOUR, SIX))
        x4 = unifint(diff_lb, diff_ub, (ONE, x0))
        x5 = unifint(diff_lb, diff_ub, (ONE, x0))
        x6 = add(add(ONE, multiply(decrement(x2), add(x0, x1))), x4)
        x7 = add(add(ONE, multiply(decrement(x3), add(x0, x1))), x5)
        if x6 > 30 or x7 > 30:
            continue
        x8 = tuple(range(ONE, TEN))
        x9 = choice(x8)
        x10 = tuple(x11 for x11 in x8 if x11 != x9)
        x11 = choice(x10)
        x12 = tuple(x13 for x13 in x10 if x13 != x11)
        x13 = _tile_starts_b7f8a4d8(x0, x1, x6)
        x14 = _tile_starts_b7f8a4d8(x0, x1, x7)
        x15 = tuple(x16 for x16, x17 in enumerate(x13) if add(x17, ONE) < x6)
        x16 = tuple(x17 for x17, x18 in enumerate(x14) if add(x18, ONE) < x7)
        if len(x15) < TWO or len(x16) < TWO:
            continue
        x17 = TWO if len(x15) >= FOUR and len(x16) >= FOUR and choice((T, F)) else ONE
        x18 = sample(x12, x17)
        x19 = list(x15)
        x20 = list(x16)
        shuffle(x19)
        shuffle(x20)
        x21 = []
        x22 = True
        for x23 in x18:
            x24 = choice(("rect", "rect", "hpair", "vpair"))
            x25 = TWO if x24 in ("rect", "vpair") else ONE
            x26 = TWO if x24 in ("rect", "hpair") else ONE
            if len(x19) < x25 or len(x20) < x26:
                x22 = False
                break
            x27 = tuple(sorted(sample(x19, x25)))
            x28 = tuple(sorted(sample(x20, x26)))
            x21.append((x23, x27, x28))
            x19 = [x29 for x29 in x19 if x29 not in x27]
            x20 = [x29 for x29 in x20 if x29 not in x28]
        if not x22:
            continue
        x29: dict[tuple[Integer, Integer], Integer] = {}
        for x30, x31, x32 in x21:
            for x33 in x31:
                for x34 in x32:
                    x29[(x33, x34)] = x30
        x35 = canvas(ZERO, (x6, x7))
        x36 = set()
        x37 = set()
        x38 = {x39: set() for x39 in x18}
        for x39, x40 in enumerate(x13):
            for x41, x42 in enumerate(x14):
                x43 = x29.get((x39, x41), x11)
                for x44 in range(x0):
                    x45 = add(x40, x44)
                    if x45 >= x6:
                        break
                    for x46 in range(x0):
                        x47 = add(x42, x46)
                        if x47 >= x7:
                            break
                        # Draw the uncropped periodic tile and then clip it to the canvas.
                        if x44 in (ZERO, decrement(x0)) or x46 in (ZERO, decrement(x0)):
                            x36.add((x45, x47))
                        else:
                            if x43 == x11:
                                x37.add((x45, x47))
                            else:
                                x38[x43].add((x45, x47))
        x48 = fill(x35, x9, frozenset(x36))
        x49 = fill(x48, x11, frozenset(x37))
        for x50, x51 in x38.items():
            x49 = fill(x49, x50, frozenset(x51))
        x52 = tuple(sorted(colorcount(x49, x53) for x53 in x18))
        if len(x52) == ZERO or maximum(x52) >= colorcount(x49, x11):
            continue
        x54 = _connect_specials_b7f8a4d8(x49, x38)
        if x49 == x54:
            continue
        if verify_b7f8a4d8(x49) != x54:
            continue
        return {"input": x49, "output": x54}
