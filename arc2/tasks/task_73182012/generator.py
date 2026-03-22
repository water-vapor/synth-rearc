from arc2.core import *


GRID_SIZE_73182012 = 12
SEED_SIZE_73182012 = 4
MOTIF_SIZE_73182012 = 8
NONZERO_COLORS_73182012 = remove(ZERO, interval(ZERO, TEN, ONE))
SEED_TRANSFORMS_73182012 = (identity, rot90, rot180, rot270, hmirror, vmirror, dmirror, cmirror)
SEED_TEMPLATES_73182012 = (
    (
        (ZERO, ZERO, ZERO, ONE),
        (ZERO, TWO, TWO, ONE),
        (ZERO, TWO, THREE, THREE),
        (ONE, ONE, THREE, FOUR),
    ),
    (
        (ZERO, ZERO, ZERO, ONE),
        (ZERO, ZERO, ONE, ONE),
        (ZERO, ONE, TWO, THREE),
        (ONE, ONE, THREE, ZERO),
    ),
    (
        (ZERO, ONE, ONE, ZERO),
        (ONE, TWO, TWO, THREE),
        (ONE, TWO, FOUR, FOUR),
        (ZERO, THREE, FOUR, ZERO),
    ),
    (
        (ONE, ZERO, ZERO, TWO),
        (ZERO, TWO, THREE, FOUR),
        (ZERO, THREE, FIVE, FOUR),
        (TWO, FOUR, FOUR, SIX),
    ),
)


def _colorize_template_73182012(template: Grid) -> Grid:
    x0 = maximum(palette(template))
    x1 = sample(NONZERO_COLORS_73182012, x0)
    x2 = {add(x3, ONE): x1[x3] for x3 in range(x0)}
    return tuple(tuple(x2.get(x4, ZERO) for x4 in x5) for x5 in template)


def _seed_to_motif_73182012(seed: Grid) -> Grid:
    x0 = hconcat(seed, vmirror(seed))
    x1 = vconcat(x0, hmirror(x0))
    return x1


def _place_motif_73182012(
    motif: Grid,
    top: int,
    left: int,
) -> Grid:
    x0 = canvas(ZERO, (GRID_SIZE_73182012, GRID_SIZE_73182012))
    x1 = tuple(x2 for x2 in palette(motif) if x2 != ZERO)
    for x2 in x1:
        x3 = ofcolor(motif, x2)
        x4 = shift(x3, (top, left))
        x0 = fill(x0, x2, x4)
    return x0


def generate_73182012(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(SEED_TEMPLATES_73182012)
        x1 = _colorize_template_73182012(x0)
        x2 = choice(SEED_TRANSFORMS_73182012)(x1)
        x3 = _seed_to_motif_73182012(x2)
        x4 = unifint(diff_lb, diff_ub, (ZERO, subtract(GRID_SIZE_73182012, MOTIF_SIZE_73182012)))
        x5 = unifint(diff_lb, diff_ub, (ZERO, subtract(GRID_SIZE_73182012, MOTIF_SIZE_73182012)))
        x6 = _place_motif_73182012(x3, x4, x5)
        x7 = difference(asindices(x2), ofcolor(x2, ZERO))
        x8 = objects(x6, F, F, T)
        if size(x7) < SIX:
            continue
        if size(palette(x2)) < THREE:
            continue
        if size(x8) != ONE:
            continue
        return {"input": x6, "output": x2}
