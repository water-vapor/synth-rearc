from synth_rearc.core import *


BACKGROUND_BC93EC48 = SEVEN
COLORS_BC93EC48 = remove(BACKGROUND_BC93EC48, interval(ZERO, TEN, ONE))
GRID_SIDES_BC93EC48 = (EIGHT, EIGHT, TEN, TEN, 12, 14, 16, 18)
CORNER_TURNS_BC93EC48 = (
    ("tl", ZERO),
    ("tr", ONE),
    ("br", TWO),
    ("bl", THREE),
)
COPY_TARGETS_BC93EC48 = (
    ("bl", "tl"),
    ("tl", "tr"),
    ("tr", "br"),
    ("br", "bl"),
)


def _normalize_patch_bc93ec48(patch: Indices) -> Indices:
    x0 = uppermost(patch)
    x1 = leftmost(patch)
    return shift(patch, (-x0, -x1))


def _rot90_patch_bc93ec48(patch: Indices) -> Indices:
    x0 = height(patch)
    x1 = frozenset((j, x0 - i - ONE) for i, j in patch)
    return _normalize_patch_bc93ec48(x1)


def _rotate_patch_bc93ec48(
    patch: Indices,
    turns: Integer,
) -> Indices:
    x0 = patch
    for _ in range(turns):
        x0 = _rot90_patch_bc93ec48(x0)
    return x0


def _top_motif_bc93ec48() -> Indices:
    x0 = choice(("hbar", "vbar", "square", "ell"))
    if x0 == "hbar":
        x1 = choice((TWO, TWO, THREE, THREE, FOUR, FIVE))
        return frozenset((ZERO, j) for j in range(x1))
    if x0 == "vbar":
        x1 = choice((TWO, TWO, THREE, THREE, FOUR, FIVE))
        return frozenset((i, ZERO) for i in range(x1))
    if x0 == "square":
        return frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)})
    while True:
        x1 = choice((TWO, TWO, THREE, THREE, FOUR))
        x2 = choice((TWO, TWO, THREE, THREE, FOUR))
        if x1 + x2 - ONE <= FIVE:
            break
    x3 = choice((ZERO, x1 - ONE))
    x4 = frozenset((ZERO, j) for j in range(x1))
    x5 = frozenset((i, x3) for i in range(x2))
    return combine(x4, x5)


def _distractor_patch_bc93ec48() -> Indices:
    x0 = choice(("singleton", "bar", "bar", "square", "ell"))
    if x0 == "singleton":
        return frozenset({ORIGIN})
    if x0 == "bar":
        x1 = choice((TWO, TWO, THREE, THREE, FOUR))
        x2 = choice((frozenset((ZERO, j) for j in range(x1)), frozenset((i, ZERO) for i in range(x1))))
        return x2
    if x0 == "square":
        return frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)})
    x1 = _top_motif_bc93ec48()
    x2 = randint(ZERO, THREE)
    return _rotate_patch_bc93ec48(x1, x2)


def _halo_bc93ec48(patch: Indices) -> Indices:
    x0 = set(patch)
    for x1 in patch:
        x0.update(dneighbors(x1))
    return frozenset(x0)


def _move_to_corner_bc93ec48(
    patch: Patch,
    corner: str,
    side: Integer,
) -> Patch:
    x0 = decrement(side)
    if corner == "tl":
        x1 = invert(ulcorner(patch))
    elif corner == "tr":
        x1 = subtract((ZERO, x0), urcorner(patch))
    elif corner == "br":
        x1 = subtract((x0, x0), lrcorner(patch))
    else:
        x1 = subtract((x0, ZERO), llcorner(patch))
    return shift(patch, x1)


def generate_bc93ec48(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = size(GRID_SIDES_BC93EC48)
    while True:
        x1 = unifint(diff_lb, diff_ub, (ZERO, x0 - ONE))
        x2 = GRID_SIDES_BC93EC48[x1]
        x3 = unifint(diff_lb, diff_ub, (THREE, SIX))
        x4 = tuple(sample(COLORS_BC93EC48, x3))
        gi = canvas(BACKGROUND_BC93EC48, (x2, x2))
        x5 = frozenset()
        x6 = {x7: frozenset() for x7 in COLORS_BC93EC48}
        x7 = tuple()
        x8 = True
        x9 = list(CORNER_TURNS_BC93EC48)
        if choice((T, F, F)):
            del x9[randint(ZERO, len(x9) - ONE)]
        for x10, x11 in x9:
            x12 = _top_motif_bc93ec48()
            x13 = _rotate_patch_bc93ec48(x12, x11)
            x14 = _move_to_corner_bc93ec48(x13, x10, x2)
            x15 = choice(x4)
            x16 = _halo_bc93ec48(x14)
            if len(intersection(x14, x5)) > ZERO or len(intersection(x16, x6[x15])) > ZERO:
                x8 = False
                break
            x17 = recolor(x15, x14)
            gi = paint(gi, x17)
            x5 = combine(x5, x14)
            x6[x15] = combine(x6[x15], x14)
            x7 = x7 + ((x10, x17),)
        if not x8:
            continue
        x18 = dict(x7)
        x19 = tuple()
        for x20, x21 in COPY_TARGETS_BC93EC48:
            if x20 not in x18:
                continue
            x22 = _move_to_corner_bc93ec48(x18[x20], x21, x2)
            x19 = x19 + (x22,)
        x20 = frozenset()
        x21 = True
        for x22 in x19:
            x23 = toindices(x22)
            if len(intersection(x23, x20)) > ZERO:
                x21 = False
                break
            x20 = combine(x20, x23)
        if not x21:
            continue
        x23 = frozenset()
        for _, x24 in x7:
            x23 = combine(x23, _halo_bc93ec48(toindices(x24)))
        for x24 in x19:
            x23 = combine(x23, _halo_bc93ec48(toindices(x24)))
        x24 = min(EIGHT, divide(x2, TWO))
        x25 = randint(max(THREE, x24 - TWO), x24)
        x26 = True
        for _ in range(x25):
            x27 = False
            for _ in range(200):
                x28 = _distractor_patch_bc93ec48()
                x29 = height(x28)
                x30 = width(x28)
                x31 = randint(ZERO, x2 - x29)
                x32 = randint(ZERO, x2 - x30)
                x33 = shift(x28, (x31, x32))
                x34 = choice(x4 if choice((T, T, F)) else COLORS_BC93EC48)
                x35 = _halo_bc93ec48(x33)
                if (
                    ulcorner(x33) == ORIGIN
                    or urcorner(x33) == (ZERO, x2 - ONE)
                    or llcorner(x33) == (x2 - ONE, ZERO)
                    or lrcorner(x33) == (x2 - ONE, x2 - ONE)
                ):
                    continue
                if len(intersection(x33, x23)) > ZERO:
                    continue
                if len(intersection(x33, x5)) > ZERO:
                    continue
                if len(intersection(x35, x6[x34])) > ZERO:
                    continue
                x36 = recolor(x34, x33)
                gi = paint(gi, x36)
                x5 = combine(x5, x33)
                x6[x34] = combine(x6[x34], x33)
                x27 = True
                break
            if not x27:
                x26 = False
                break
        if not x26:
            continue
        go = gi
        for x37 in x19:
            go = paint(go, x37)
        if gi == go:
            continue
        return {"input": gi, "output": go}
