from arc2.core import *


def _diagonal_only_halo_396d80d7(
    shell: Indices,
) -> Indices:
    x0 = mapply(ineighbors, shell)
    x1 = mapply(dneighbors, shell)
    x2 = difference(x0, x1)
    x3 = difference(x2, shell)
    return x3


def _normalize_family_396d80d7(
    accent: Indices,
    shell: Indices,
) -> tuple[Indices, Indices, Indices]:
    halo = _diagonal_only_halo_396d80d7(shell)
    full = shell | accent | halo
    offset = astuple(-uppermost(full), -leftmost(full))
    return shift(accent, offset), shift(shell, offset), shift(halo, offset)


def _diamond_family_396d80d7(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices, Indices]:
    h = unifint(diff_lb, diff_ub, (ONE, THREE))
    w = unifint(diff_lb, diff_ub, (ONE, THREE))
    if h == w == ONE:
        if choice((T, F)):
            h = TWO
        else:
            w = TWO
    accent = frozenset((i, j) for i in range(h) for j in range(w))
    shell = frozenset(
        (i, j)
        for i in range(-TWO, h + TWO)
        for j in range(-TWO, w + TWO)
        if min(abs(i - a) + abs(j - b) for a, b in accent) == TWO
    )
    return _normalize_family_396d80d7(accent, shell)


def _ladder_family_396d80d7(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Indices, Indices, Indices]:
    n_pairs = unifint(diff_lb, diff_ub, (TWO, FOUR))
    even_rows = tuple(range(ZERO, multiply(TWO, n_pairs), TWO))
    odd_rows = tuple(range(ONE, multiply(TWO, n_pairs), TWO))
    shell = frozenset()
    for row in even_rows:
        shell |= frozenset({(row, ONE), (row, TWO), (row, FOUR), (row, FIVE)})
    for row in odd_rows:
        shell |= frozenset({(row, ZERO), (row, THREE), (row, SIX)})
    accent_rows = even_rows if len(even_rows) == ONE else tuple(even_rows[ONE:])
    n_accent = randint(ONE, max(ONE, len(accent_rows) - (ONE if len(accent_rows) > TWO else ZERO)))
    chosen_rows = frozenset(sample(accent_rows, n_accent))
    accent = frozenset((row, THREE) for row in chosen_rows)
    return _normalize_family_396d80d7(accent, shell)


def _centered_offset_396d80d7(
    span: Integer,
) -> Integer:
    full = multiply(FOUR, FOUR)
    base = divide(full - span, TWO)
    lo = max(ZERO, base - ONE)
    hi = min(full - span, base + ONE)
    return randint(lo, hi)


def generate_396d80d7(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    color_options = remove(SEVEN, interval(ONE, TEN, ONE))
    shell_color, accent_color = sample(color_options, TWO)
    if choice((T, F)):
        accent, shell, halo = _diamond_family_396d80d7(diff_lb, diff_ub)
    else:
        accent, shell, halo = _ladder_family_396d80d7(diff_lb, diff_ub)
    motif = accent | shell | halo
    row_offset = _centered_offset_396d80d7(height(motif))
    col_offset = _centered_offset_396d80d7(width(motif))
    offset = astuple(row_offset, col_offset)
    accent = shift(accent, offset)
    shell = shift(shell, offset)
    halo = shift(halo, offset)
    gi = canvas(SEVEN, (16, 16))
    gi = fill(gi, shell_color, shell)
    gi = fill(gi, accent_color, accent)
    go = fill(gi, accent_color, halo)
    return {"input": gi, "output": go}
