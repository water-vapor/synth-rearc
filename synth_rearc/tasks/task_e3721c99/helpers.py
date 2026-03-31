from synth_rearc.core import *


GRID_SHAPE_E3721C99 = (30, 30)
LEGEND_COLORS_E3721C99 = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT)
BODY_HOLE_COUNTS_E3721C99 = (ZERO, ONE, TWO, THREE, FOUR, FIVE)
BODY_SIZE_OPTIONS_E3721C99 = {
    ZERO: ((FOUR, FOUR), (FOUR, FIVE), (FIVE, FIVE), (FIVE, SIX), (SIX, SIX), (SIX, SEVEN)),
    ONE: ((FIVE, FIVE), (FIVE, SIX), (SIX, SIX), (SIX, SEVEN), (SEVEN, SEVEN), (SEVEN, EIGHT)),
    TWO: ((FIVE, SEVEN), (SIX, SEVEN), (SIX, EIGHT), (SEVEN, EIGHT), (SEVEN, NINE), (EIGHT, EIGHT)),
    THREE: ((SIX, EIGHT), (SEVEN, EIGHT), (SEVEN, NINE), (EIGHT, NINE), (EIGHT, TEN), (NINE, NINE)),
    FOUR: ((SEVEN, EIGHT), (SEVEN, NINE), (EIGHT, NINE), (EIGHT, TEN), (NINE, TEN), (TEN, TEN)),
    FIVE: ((EIGHT, NINE), (EIGHT, TEN), (NINE, TEN), (NINE, 11), (TEN, 11), (11, 11)),
}
PATCH_TRANSFORMS_E3721C99 = (
    identity,
    hmirror,
    vmirror,
    compose(hmirror, vmirror),
    dmirror,
    cmirror,
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)
BODY_PATTERNS_E3721C99 = {
    ZERO: (
        ("..##", ".###", "####", "##.."),
        ("...##", "..###", "#####", "####."),
        (".###..", "######", "######", ".###.."),
    ),
    ONE: (
        (".###.", "##.##", "##.##", ".####"),
        ("..#.", "####", "#..#", "####", "###."),
        (".####.", ".#..##", "##..#.", "##.##.", ".####.", "...#.."),
    ),
    TWO: (
        ("...######", "..##...##", ".#######.", "##...##..", "#######..", ".###....."),
        ("...####", ".###.##", "####..#", "##.####", "##..###", ".#####."),
        (".#.....", "#######", "#.#..##", "#.#..##", "######.", ".#....."),
        (".###.....", "##.####..", "#...#.#..", "##..###..", ".#######.", "......###", ".......##"),
    ),
    THREE: (
        ("..##..", "#####.", "#.#.#.", "######", "#.###.", "###..."),
        ("...####..", "..###.###", ".####.###", "#.#######", "#..#####.", "##..####.", ".#######.", ".##..###.", ".##..##..", ".#####..."),
    ),
    FOUR: (
        ("....####", "...###.#", ".#####.#", "####.###", "##.#.###", "########", "##.####.", ".#####.."),
        ("...######.", ".###..####", "####.##..#", "#..###...#", "#...###..#", "##..#.####", ".####...##", "...####.#.", "......###."),
    ),
    FIVE: (
        (".....#######.....", "....####...####..", "....#..#.....####", "...##..#....##.##", "..##...#...##..#.", ".###...#..##...#.", "##.########....#.", "#...###.##.....#.", "#....#...#....##.", "##...#...#...##..", ".#############..."),
    ),
}


def normalize_patch_e3721c99(
    patch: Patch,
) -> Indices:
    return normalize(toindices(patch))


def pattern_to_patch_e3721c99(
    pattern: tuple[str, ...],
) -> Indices:
    return frozenset(
        (i, j)
        for i, row in enumerate(pattern)
        for j, value in enumerate(row)
        if value == "#"
    )


def hole_count_e3721c99(
    patch: Patch,
) -> Integer:
    if len(patch) == ZERO:
        return ZERO
    x0 = normalize_patch_e3721c99(patch)
    x1 = canvas(ZERO, shape(x0))
    x2 = fill(x1, EIGHT, x0)
    x3 = objects(x2, T, F, F)
    x4 = colorfilter(x3, ZERO)
    x5 = compose(flip, rbind(bordering, x2))
    x6 = sfilter(x4, x5)
    return size(x6)


def legend_patch_e3721c99(
    nholes: Integer,
    vertical: Boolean,
) -> Indices:
    if nholes == ZERO:
        return frozenset(
            (i, j)
            for i in range(THREE)
            for j in range(THREE)
        )
    if vertical:
        x0 = add(double(nholes), ONE)
        x1 = frozenset(
            (i, j)
            for i in range(x0)
            for j in range(THREE)
        )
        x2 = frozenset((i, ONE) for i in range(ONE, x0, TWO))
        return difference(x1, x2)
    x0 = add(double(nholes), ONE)
    x1 = frozenset(
        (i, j)
        for i in range(THREE)
        for j in range(x0)
    )
    x2 = frozenset((ONE, j) for j in range(ONE, x0, TWO))
    return difference(x1, x2)


def _interior_seeds_e3721c99(
    height_value: Integer,
    width_value: Integer,
    nholes: Integer,
) -> tuple[IntegerTuple, ...] | None:
    x0 = tuple(
        (i, j)
        for i in range(height_value)
        for j in range(width_value)
    )
    if len(x0) < nholes:
        return None
    for _ in range(160):
        x1 = tuple(sample(x0, nholes))
        x2 = T
        for x3, x4 in enumerate(x1):
            for x5 in x1[x3 + ONE:]:
                if manhattan(initset(x4), initset(x5)) <= TWO:
                    x2 = F
                    break
            if not x2:
                break
        if x2:
            return x1
    return None


def _grow_holes_e3721c99(
    height_value: Integer,
    width_value: Integer,
    seeds: tuple[IntegerTuple, ...],
) -> Indices:
    x0 = [set((x1,)) for x1 in seeds]
    x1 = len(seeds)
    x2 = max(x1, min((height_value * width_value) // FOUR, x1 + randint(ZERO, max(THREE, x1 + TWO))))
    x3 = sum(len(x4) for x4 in x0)
    x4 = ZERO
    while x3 < x2 and x4 < 320:
        x4 += ONE
        x5 = randint(ZERO, len(x0) - ONE)
        x6 = set()
        for x7 in x0[x5]:
            for x8 in dneighbors(x7):
                if ZERO <= x8[ZERO] < height_value and ZERO <= x8[ONE] < width_value:
                    x6.add(x8)
        x6 = [x9 for x9 in x6 if x9 not in x0[x5]]
        shuffle(x6)
        x7 = F
        for x8 in x6:
            x9 = F
            for x10, x11 in enumerate(x0):
                if x10 == x5:
                    continue
                if x8 in x11:
                    x9 = T
                    break
                for x12 in x11:
                    if manhattan(initset(x8), initset(x12)) <= ONE:
                        x9 = T
                        break
                if x9:
                    break
            if x9:
                continue
            x0[x5].add(x8)
            x3 += ONE
            x7 = T
            break
        if not x7:
            continue
    return frozenset((x5 + ONE, x6 + ONE) for x7 in x0 for x5, x6 in x7)


def _boundary_cells_e3721c99(
    patch: Patch,
) -> tuple[IntegerTuple, ...]:
    x0 = normalize_patch_e3721c99(patch)
    x1 = []
    for x2 in x0:
        for x3 in dneighbors(x2):
            if x3 not in x0:
                x1.append(x2)
                break
    return tuple(x1)


def _connected_patch_e3721c99(
    patch: Patch,
) -> Boolean:
    if len(patch) == ZERO:
        return F
    x0 = normalize_patch_e3721c99(patch)
    x1 = canvas(ZERO, shape(x0))
    x2 = fill(x1, EIGHT, x0)
    x3 = objects(x2, T, F, T)
    return equality(size(x3), ONE)


def _roughen_patch_e3721c99(
    patch: Patch,
    nholes: Integer,
) -> Indices:
    x0 = normalize_patch_e3721c99(patch)
    x1 = randint(ZERO, max(ONE, len(x0) // SIX))
    x2 = ZERO
    x3 = ZERO
    while x2 < x1 and x3 < 400:
        x3 += ONE
        x4 = _boundary_cells_e3721c99(x0)
        if len(x4) == ZERO:
            break
        x5 = choice(x4)
        x6 = normalize_patch_e3721c99(remove(x5, x0))
        if len(x6) < max(FIVE, add(double(nholes), FOUR)):
            continue
        if not _connected_patch_e3721c99(x6):
            continue
        if hole_count_e3721c99(x6) != nholes:
            continue
        x0 = x6
        x2 += ONE
    return x0


def sample_body_patch_e3721c99(
    nholes: Integer,
) -> Indices:
    x0 = choice(BODY_PATTERNS_E3721C99[nholes])
    x1 = pattern_to_patch_e3721c99(x0)
    x2 = choice(PATCH_TRANSFORMS_E3721C99)(x1)
    return normalize_patch_e3721c99(x2)


for x0 in BODY_HOLE_COUNTS_E3721C99:
    if hole_count_e3721c99(legend_patch_e3721c99(x0, F)) != x0:
        raise ValueError(f"invalid horizontal legend motif for {x0} holes")
    if hole_count_e3721c99(legend_patch_e3721c99(x0, T)) != x0:
        raise ValueError(f"invalid vertical legend motif for {x0} holes")
    for x1 in BODY_PATTERNS_E3721C99[x0]:
        if hole_count_e3721c99(pattern_to_patch_e3721c99(x1)) != x0:
            raise ValueError(f"invalid body motif for {x0} holes")
