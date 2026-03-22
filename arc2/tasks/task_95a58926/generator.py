from arc2.core import *


ACCENT_COLORS_95A58926 = tuple(remove(FIVE, remove(ZERO, interval(ZERO, TEN, ONE))))
PERIODS_95A58926 = (FOUR, FIVE, SIX)


def _line_indices_95a58926(period: int, length: int) -> tuple[int, ...]:
    return tuple(range(period - ONE, length, period))


def _lattice_patch_95a58926(
    rows: tuple[int, ...],
    cols: tuple[int, ...],
    height_value: int,
    width_value: int,
) -> Indices:
    x0 = tuple(product(initset(x1), interval(ZERO, width_value, ONE)) for x1 in rows)
    x1 = tuple(product(interval(ZERO, height_value, ONE), initset(x2)) for x2 in cols)
    return merge(x0 + x1)


def generate_95a58926(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(PERIODS_95A58926)
        x1 = min(FIVE, 30 // x0)
        x2 = min(SIX, 30 // x0)
        x3 = unifint(diff_lb, diff_ub, (THREE, x1))
        x4 = unifint(diff_lb, diff_ub, (TWO, x2))
        x5 = unifint(diff_lb, diff_ub, (ZERO, min(30 - (x3 * x0), x0 - ONE)))
        x6 = unifint(diff_lb, diff_ub, (ZERO, min(30 - (x4 * x0), x0 - ONE)))
        x7 = add(multiply(x3, x0), x5)
        x8 = add(multiply(x4, x0), x6)
        x9 = _line_indices_95a58926(x0, x7)
        x10 = _line_indices_95a58926(x0, x8)
        if len(x9) != x3 or len(x10) != x4:
            continue
        x11 = choice(ACCENT_COLORS_95A58926)
        x12 = canvas(ZERO, (x7, x8))
        x13 = _lattice_patch_95a58926(x9, x10, x7, x8)
        x14 = product(x9, x10)
        x15 = fill(x12, FIVE, x13)
        x16 = fill(x15, x11, x14)
        x17 = x15
        x18 = tuple(x14)
        x19 = min(len(x18), unifint(diff_lb, diff_ub, (ZERO, max(ZERO, len(x18) // THREE))))
        x20 = frozenset(sample(x18, x19)) if x19 > ZERO else frozenset({})
        x21 = fill(x17, x11, x20)
        x22 = difference(x13, x14)
        x23 = tuple(x22)
        x24 = min(
            len(x23),
            unifint(
                diff_lb,
                diff_ub,
                (max(ONE, len(x23) // 20), max(max(ONE, len(x23) // 20), len(x23) // SEVEN)),
            ),
        )
        x25 = frozenset(sample(x23, x24))
        x26 = fill(x21, x11, x25)
        x27 = difference(asindices(x12), x13)
        x28 = tuple(x27)
        x29 = min(
            len(x28),
            unifint(
                diff_lb,
                diff_ub,
                (max(ONE, len(x28) // 18), max(max(ONE, len(x28) // 18), len(x28) // SEVEN)),
            ),
        )
        x30 = frozenset(sample(x28, x29))
        x31 = fill(x26, x11, x30)
        x32 = tuple(i for i in range(x7) if ZERO not in x31[i])
        x33 = tuple(j for j in range(x8) if all(x31[i][j] != ZERO for i in range(x7)))
        if x32 != x9 or x33 != x10:
            continue
        if x31 == x16:
            continue
        return {"input": x31, "output": x16}
