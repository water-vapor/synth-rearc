from synth_rearc.core import *


HOLE_TO_COLOR_0a2355a6 = {
    ONE: ONE,
    TWO: THREE,
    THREE: TWO,
    FOUR: FOUR,
}

MOTIF_PATTERNS_0a2355a6 = {
    ONE: (
        ("888", "8.8", "888"),
        ("8888", "8..8", "8888"),
        ("88888", "8...8", "88888"),
        ("8888", "8..8", "8..8", "8888"),
    ),
    TWO: (
        ("888", "8.8", "888", "8.8", "888"),
        ("8888", "8..8", "8888", "8..8", "8888"),
        ("888..", "8.8..", "88888", "8...8", "88888"),
        ("..888", "888.8", "8.8.8", "888.8", "..888"),
    ),
    THREE: (
        ("888", "8.8", "888", "8.8", "888", "8.8", "888"),
        ("88888", "8.8.8", "88888", "8.8..", "8.8..", "888.."),
        (".8888", ".8..8", ".8..8", "88888", "8.8..", "8888.", "8..8.", "8888."),
        ("88888", "8...8", "88888", "8...8", "88888", "8...8", "88888"),
    ),
    FOUR: (
        ("888.......", "8.88888888", "888.8..8.8", "..88888888"),
        ("888", "8.8", "888", "8.8", "888", "8.8", "888", "8.8", "888"),
        ("88888", "8.8.8", "88888", "8.8.8", "88888"),
    ),
}

PIECE_TRANSFORMS_0a2355a6 = (
    identity,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
)


def pattern_to_patch_0a2355a6(pattern: tuple[str, ...]) -> Patch:
    return frozenset((i, j) for i, row in enumerate(pattern) for j, value in enumerate(row) if value == "8")


def hole_count_0a2355a6(patch: Patch) -> Integer:
    if len(patch) == ZERO:
        return ZERO
    x0 = normalize(toindices(patch))
    x1 = canvas(ZERO, shape(x0))
    x2 = fill(x1, EIGHT, x0)
    x3 = objects(x2, T, F, F)
    x4 = colorfilter(x3, ZERO)
    x5 = compose(flip, rbind(bordering, x2))
    x6 = sfilter(x4, x5)
    return size(x6)


def color_for_holes_0a2355a6(nholes: Integer) -> Integer:
    return HOLE_TO_COLOR_0a2355a6[nholes]


def transformed_patch_0a2355a6(patch: Patch) -> Patch:
    x0 = normalize(toindices(patch))
    x1 = choice(PIECE_TRANSFORMS_0a2355a6)(x0)
    return normalize(toindices(x1))


def crop_pair_0a2355a6(inp: Grid, out: Grid) -> tuple[Grid, Grid]:
    x0 = ofcolor(inp, EIGHT)
    x1 = max(ZERO, uppermost(x0) - randint(ZERO, ONE))
    x2 = max(ZERO, leftmost(x0) - randint(ZERO, ONE))
    x3 = min(len(inp) - ONE, lowermost(x0) + randint(ZERO, ONE))
    x4 = min(len(inp[ZERO]) - ONE, rightmost(x0) + randint(ZERO, ONE))
    x5 = (x3 - x1 + ONE, x4 - x2 + ONE)
    x6 = (x1, x2)
    x7 = crop(inp, x6, x5)
    x8 = crop(out, x6, x5)
    return x7, x8


MOTIF_BANK_0a2355a6 = {
    nholes: tuple(pattern_to_patch_0a2355a6(pattern) for pattern in patterns)
    for nholes, patterns in MOTIF_PATTERNS_0a2355a6.items()
}

for nholes, patches in MOTIF_BANK_0a2355a6.items():
    for patch in patches:
        if hole_count_0a2355a6(patch) != nholes:
            raise ValueError(f"invalid 0a2355a6 motif for hole count {nholes}")
