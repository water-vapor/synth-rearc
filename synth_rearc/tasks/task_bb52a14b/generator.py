from synth_rearc.core import *


_DIM = 22
_MOTIF_DIM = 3
_FRAGMENT_SHAPES = (
    frozenset({(0, 0)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (1, 0)}),
    frozenset({(0, 0), (0, 1), (0, 2)}),
    frozenset({(0, 0), (1, 0), (2, 0)}),
    frozenset({(0, 0), (1, 0), (1, 1)}),
    frozenset({(0, 1), (1, 0), (1, 1)}),
)


def _window_bb52a14b(loc: IntegerTuple) -> Indices:
    i, j = loc
    return frozenset(
        (a, b)
        for a in range(i, i + _MOTIF_DIM)
        for b in range(j, j + _MOTIF_DIM)
    )


def _padded_window_bb52a14b(loc: IntegerTuple) -> Indices:
    i, j = loc
    return frozenset(
        (a, b)
        for a in range(max(ZERO, i - ONE), min(_DIM, i + _MOTIF_DIM + ONE))
        for b in range(max(ZERO, j - ONE), min(_DIM, j + _MOTIF_DIM + ONE))
    )


def _paint_pattern_bb52a14b(
    grid: Grid,
    pattern: Grid,
    loc: IntegerTuple,
) -> Grid:
    return paint(grid, shift(asobject(pattern), loc))


def _template_bb52a14b() -> Grid:
    cells = tuple(sorted(asindices(canvas(ZERO, (_MOTIF_DIM, _MOTIF_DIM)))))
    while True:
        nfours = choice((FOUR, FOUR, FIVE, FIVE, SIX))
        fours = frozenset(sample(cells, nfours))
        if height(fours) != _MOTIF_DIM or width(fours) != _MOTIF_DIM:
            continue
        rem = tuple(sorted(difference(frozenset(cells), fours)))
        neights = randint(ONE, len(rem) - ONE)
        eights = frozenset(sample(rem, neights))
        ones = difference(frozenset(rem), eights)
        grid = canvas(ZERO, (_MOTIF_DIM, _MOTIF_DIM))
        grid = fill(grid, FOUR, fours)
        grid = fill(grid, EIGHT, eights)
        grid = fill(grid, ONE, ones)
        return grid


def _noise_bb52a14b(
    grid: Grid,
    blocked: Indices,
    diff_lb: float,
    diff_ub: float,
) -> Grid:
    target = unifint(diff_lb, diff_ub, (18, 34))
    noise = frozenset()
    attempts = ZERO
    while len(noise) < target and attempts < 800:
        attempts += ONE
        shape = choice(_FRAGMENT_SHAPES)
        loci = randint(ZERO, _DIM - height(shape))
        locj = randint(ZERO, _DIM - width(shape))
        patch = shift(shape, (loci, locj))
        if len(intersection(patch, blocked)) != ZERO:
            continue
        if len(intersection(patch, noise)) != ZERO:
            continue
        color = choice((ONE, EIGHT))
        noise = combine(noise, patch)
        grid = fill(grid, color, patch)
    return grid


def generate_bb52a14b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _template_bb52a14b()
        x1 = replace(x0, FOUR, ZERO)
        x2 = choice((ONE, ONE, TWO, TWO))
        x3 = [(i, j) for i in range(_DIM - _MOTIF_DIM + ONE) for j in range(_DIM - _MOTIF_DIM + ONE)]
        shuffle(x3)
        x4 = []
        x5 = frozenset()
        x6 = frozenset()
        for x7 in x3:
            x8 = _window_bb52a14b(x7)
            x9 = _padded_window_bb52a14b(x7)
            if len(intersection(x9, x6)) != ZERO:
                continue
            x4.append(x7)
            x5 = combine(x5, x8)
            x6 = combine(x6, x9)
            if len(x4) == x2 + ONE:
                break
        if len(x4) != x2 + ONE:
            continue
        x10 = x4[0]
        x11 = tuple(x4[1:])
        x12 = canvas(ZERO, (_DIM, _DIM))
        x12 = _paint_pattern_bb52a14b(x12, x0, x10)
        for x13 in x11:
            x12 = _paint_pattern_bb52a14b(x12, x1, x13)
        x12 = _noise_bb52a14b(x12, x6, diff_lb, diff_ub)
        x14 = tuple(sorted(occurrences(x12, asobject(x1))))
        x15 = tuple(sorted(x11))
        if x14 != x15:
            continue
        x16 = ofcolor(x0, FOUR)
        x17 = lbind(shift, x16)
        x18 = mapply(x17, x11)
        x19 = fill(x12, FOUR, x18)
        return {"input": x12, "output": x19}
