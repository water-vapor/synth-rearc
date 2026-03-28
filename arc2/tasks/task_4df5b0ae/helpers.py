from arc2.core import *


GRID_SHAPE_4DF5B0AE = (TEN, TEN)
OBJECT_COLORS_4DF5B0AE = (ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, EIGHT, NINE)
SIZE_PROFILES_4DF5B0AE = (
    (ONE, TWO, THREE, FOUR),
    (ONE, THREE, FOUR),
    (ONE, THREE, FIVE),
    (ONE, FOUR, FIVE),
    (ONE, FOUR, SIX, 12),
    (ONE, FIVE, EIGHT),
    (TWO, THREE, FIVE, EIGHT),
    (TWO, FOUR, SIX, NINE),
    (THREE, FOUR, FIVE),
    (THREE, FIVE, SEVEN, EIGHT),
    (FOUR, SIX, NINE),
)
FRAME_PATCH_4DF5B0AE = box(asindices(canvas(SEVEN, GRID_SHAPE_4DF5B0AE)))
BASE_SHAPES_4DF5B0AE = (
    frozenset({(0, 0)}),
    frozenset({(0, 0), (0, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2)}),
    frozenset({(0, 0), (1, 0), (1, 1)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1)}),
    frozenset({(0, 0), (1, 0), (2, 0), (2, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2), (0, 3)}),
    frozenset({(0, 0), (1, 0), (1, 1), (2, 0), (2, 1)}),
    frozenset({(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)}),
    frozenset({(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)}),
    frozenset({(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0)}),
    frozenset({(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1)}),
    frozenset({(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}),
    frozenset({
        (0, 0), (0, 1), (0, 2), (0, 3),
        (1, 0), (1, 1), (1, 2), (1, 3),
        (2, 0), (2, 1), (2, 2), (2, 3),
    }),
)


def _rot90_patch_4df5b0ae(
    patch,
):
    return normalize(vmirror(dmirror(patch)))


def _rot180_patch_4df5b0ae(
    patch,
):
    return normalize(hmirror(vmirror(patch)))


def _rot270_patch_4df5b0ae(
    patch,
):
    return normalize(hmirror(dmirror(patch)))


def _dedupe_patches_4df5b0ae(
    patches,
):
    x0 = []
    x1 = set()
    for x2 in patches:
        x3 = frozenset(normalize(x2))
        if x3 in x1:
            continue
        x1.add(x3)
        x0.append(x3)
    return tuple(x0)


def _shape_variants_4df5b0ae(
    patch,
):
    x0 = (
        identity,
        hmirror,
        vmirror,
        dmirror,
        cmirror,
        _rot90_patch_4df5b0ae,
        _rot180_patch_4df5b0ae,
        _rot270_patch_4df5b0ae,
    )
    return _dedupe_patches_4df5b0ae(tuple(x1(patch) for x1 in x0))


def _build_shapes_by_size_4df5b0ae():
    x0 = {}
    for x1 in BASE_SHAPES_4DF5B0AE:
        for x2 in _shape_variants_4df5b0ae(x1):
            x3 = size(x2)
            x0.setdefault(x3, [])
            if x2 not in x0[x3]:
                x0[x3].append(x2)
    return {x1: tuple(x2) for x1, x2 in x0.items()}


SHAPES_BY_SIZE_4DF5B0AE = _build_shapes_by_size_4df5b0ae()


def _pack_key_4df5b0ae(
    obj,
):
    return (size(obj), uppermost(obj), leftmost(obj), color(obj))


def pack_objects_4df5b0ae(
    objs,
) -> Grid:
    x0 = canvas(SEVEN, GRID_SHAPE_4DF5B0AE)
    x1 = ZERO
    x2 = tuple(sorted(objs, key=_pack_key_4df5b0ae))
    for x3 in x2:
        x4 = normalize(x3)
        x5 = astuple(subtract(GRID_SHAPE_4DF5B0AE[0], height(x4)), x1)
        x6 = shift(x4, x5)
        x0 = paint(x0, x6)
        x1 = add(x1, width(x4))
    return x0


def sample_object_shapes_4df5b0ae(
    diff_lb: float,
    diff_ub: float,
):
    x0 = unifint(diff_lb, diff_ub, (THREE, FOUR))
    x1 = tuple(x2 for x2 in SIZE_PROFILES_4DF5B0AE if len(x2) == x0)
    for _ in range(200):
        x2 = choice(x1)
        x3 = tuple(choice(SHAPES_BY_SIZE_4DF5B0AE[x4]) for x4 in x2)
        x4 = sum(width(x5) for x5 in x3)
        x5 = max(height(x6) for x6 in x3)
        if x4 > GRID_SHAPE_4DF5B0AE[1]:
            continue
        if x4 < SIX:
            continue
        if x5 > SIX:
            continue
        return x3
    return ()


def sample_object_colors_4df5b0ae(
    nobjs: int,
):
    x0 = list(sample(OBJECT_COLORS_4DF5B0AE, nobjs))
    if nobjs > TWO and choice((F, F, T)):
        x1, x2 = sample(range(nobjs), TWO)
        x0[x2] = x0[x1]
    return tuple(x0)


def frame_color_4df5b0ae(
    colors,
):
    x0 = tuple(x1 for x1 in OBJECT_COLORS_4DF5B0AE if x1 not in colors)
    return choice(x0)


def _halo_4df5b0ae(
    patch,
):
    x0 = set(patch)
    for x1 in patch:
        x0 |= set(neighbors(x1))
    return frozenset(x0)


def _candidate_positions_4df5b0ae(
    patch,
    use_frame: bool,
    anchor: bool,
):
    x0, x1 = shape(patch)
    x2 = ONE if use_frame else ZERO
    x3 = ONE if use_frame else ZERO
    x4 = subtract(subtract(GRID_SHAPE_4DF5B0AE[0], x0), x2)
    x5 = subtract(subtract(GRID_SHAPE_4DF5B0AE[1], x1), x3)
    if x4 < x2 or x5 < x3:
        return ()
    x6 = [(x7, x8) for x7 in range(x2, x4 + ONE) for x8 in range(x3, x5 + ONE)]
    if anchor and not use_frame:
        x6 = [
            x7 for x7 in x6
            if x7[0] in (ZERO, x4) or x7[1] in (ZERO, x5)
        ]
    shuffle(x6)
    return tuple(x6)


def place_objects_4df5b0ae(
    shapes,
    colors,
    use_frame: bool,
):
    x0 = tuple(range(len(shapes)))
    x1 = tuple(sorted(x0, key=lambda x2: (size(shapes[x2]), height(shapes[x2]), width(shapes[x2])), reverse=T))
    for _ in range(40):
        x2 = ZERO if use_frame else choice((ZERO, ONE, ONE, TWO))
        x3 = set(x1[:x2])
        x4 = set()
        x5 = {}
        x6 = T
        for x7 in x1:
            x8 = shapes[x7]
            x9 = x7 in x3
            x10 = F
            for x11 in _candidate_positions_4df5b0ae(x8, use_frame, x9):
                x12 = shift(x8, x11)
                x13 = _halo_4df5b0ae(x12)
                if any(x14 in x4 for x14 in x13):
                    continue
                x4 |= set(x13)
                x5[x7] = recolor(colors[x7], x12)
                x10 = T
                break
            if not x10:
                x6 = F
                break
        if x6:
            return tuple(x5[x7] for x7 in x0)
    return ()
