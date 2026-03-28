from synth_rearc.core import *


_MOTIFS = (
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, TWO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE), (TWO, ONE), (TWO, TWO)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (TWO, TWO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, ONE), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, TWO)}),
    frozenset({(ZERO, TWO), (ONE, ONE), (ONE, TWO), (TWO, ZERO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, TWO), (ONE, ONE), (TWO, ZERO), (TWO, TWO)}),
)


def _make_lattice(
    side: Integer,
    linec: Integer,
) -> Grid:
    rows = tuple(range(THREE, side, FOUR))
    cols = tuple(range(THREE, side, FOUR))
    linepatch = frozenset((i, j) for i in rows for j in range(side)) | frozenset(
        (i, j) for i in range(side) for j in cols
    )
    return fill(canvas(ZERO, (side, side)), linec, linepatch)


def _stamp_all(
    grid: Grid,
    motif: Indices,
    rows: Tuple[Integer, ...],
    cols: Tuple[Integer, ...],
    value: Integer,
) -> Grid:
    anchors = product(rows, cols)
    shifter = lbind(shift, motif)
    patch = mapply(shifter, anchors)
    return fill(grid, value, patch)


def generate_92e50de0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    sizes = (23, 25, 27, 29)
    palette = interval(ONE, TEN, ONE)
    while True:
        side = sizes[unifint(diff_lb, diff_ub, (ZERO, THREE))]
        linec = choice(palette)
        motifc = choice(remove(linec, palette))
        motif = choice(_MOTIFS)
        srcs = tuple(range(ZERO, side - TWO, FOUR))
        sr = choice(srcs)
        sc = choice(srcs)

        gi = _make_lattice(side, linec)
        gi = fill(gi, motifc, shift(motif, (sr, sc)))

        rstart = ZERO if (sr // FOUR) % TWO == ZERO else FOUR
        cstart = ZERO if (sc // FOUR) % TWO == ZERO else FOUR
        rows = tuple(range(rstart, side, EIGHT))
        cols = tuple(range(cstart, side, EIGHT))
        go = _stamp_all(_make_lattice(side, linec), motif, rows, cols, motifc)
        return {"input": gi, "output": go}
