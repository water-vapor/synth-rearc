from synth_rearc.core import *


COLOR_BAG_12eac192 = (
    ONE,
    ONE,
    ONE,
    FIVE,
    SEVEN,
    SEVEN,
    EIGHT,
    EIGHT,
    EIGHT,
)

SMALL_SIZE_BAG_12eac192 = (
    ONE,
    ONE,
    ONE,
    TWO,
    TWO,
)

LARGE_SIZE_BAG_12eac192 = (
    THREE,
    THREE,
    FOUR,
    FOUR,
    FOUR,
    FIVE,
)

PATCH_TRANSFORMS_12eac192 = (
    identity,
    hmirror,
    vmirror,
    compose(hmirror, vmirror),
    dmirror,
    cmirror,
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)


def _variants_12eac192(patch: Patch) -> tuple[Patch, ...]:
    out = []
    for transform in PATCH_TRANSFORMS_12eac192:
        candidate = normalize(transform(patch))
        if candidate not in out:
            out.append(candidate)
    return tuple(out)


def _bank_12eac192(*patches: Patch) -> tuple[Patch, ...]:
    out = []
    for patch in patches:
        for candidate in _variants_12eac192(patch):
            if candidate not in out:
                out.append(candidate)
    return tuple(out)


PATCHES_BY_SIZE_12eac192 = {
    ONE: _bank_12eac192(frozenset({ORIGIN})),
    TWO: _bank_12eac192(frozenset({ORIGIN, RIGHT})),
    THREE: _bank_12eac192(
        frozenset({ORIGIN, RIGHT, (0, 2)}),
        frozenset({ORIGIN, DOWN, (1, 1)}),
    ),
    FOUR: _bank_12eac192(
        frozenset({ORIGIN, RIGHT, (0, 2), (0, 3)}),
        frozenset({ORIGIN, RIGHT, DOWN, UNITY}),
        frozenset({ORIGIN, DOWN, (2, 0), (2, 1)}),
        frozenset({ORIGIN, RIGHT, UNITY, (1, 2)}),
    ),
    FIVE: _bank_12eac192(
        frozenset({ORIGIN, RIGHT, (0, 2), DOWN, UNITY}),
    ),
}


def _pick_dims_12eac192(
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Integer]:
    if choice((F, F, F, T)):
        h = unifint(diff_lb, diff_ub, (THREE, FIVE))
        w = unifint(diff_lb, diff_ub, (THREE, FIVE))
        return h, w
    h = unifint(diff_lb, diff_ub, (FIVE, NINE))
    w = choice((SEVEN, EIGHT, EIGHT, EIGHT, EIGHT, NINE))
    return h, w


def _pick_component_counts_12eac192(
    area: Integer,
    diff_lb: float,
    diff_ub: float,
) -> tuple[Integer, Integer]:
    if area <= 16:
        return (
            unifint(diff_lb, diff_ub, (ONE, TWO)),
            unifint(diff_lb, diff_ub, (ONE, THREE)),
        )
    if area <= 36:
        return (
            unifint(diff_lb, diff_ub, (TWO, FOUR)),
            unifint(diff_lb, diff_ub, (THREE, SIX)),
        )
    if area <= 56:
        return (
            unifint(diff_lb, diff_ub, (THREE, FIVE)),
            unifint(diff_lb, diff_ub, (FIVE, NINE)),
        )
    return (
        unifint(diff_lb, diff_ub, (FOUR, SIX)),
        unifint(diff_lb, diff_ub, (SEVEN, 12)),
    )


def _placement_ok_12eac192(
    grid: Grid,
    patch: Patch,
    color_value: Integer,
) -> tuple[Boolean, Boolean]:
    cells = toindices(patch)
    touched = F
    for cell in cells:
        if index(grid, cell) != ZERO:
            return F, F
    for cell in cells:
        for nbr in dneighbors(cell):
            if nbr in cells:
                continue
            value = index(grid, nbr)
            if value is None or value == ZERO:
                continue
            touched = T
            if value == color_value:
                return F, F
    return T, touched


def _find_location_12eac192(
    grid: Grid,
    patch: Patch,
    color_value: Integer,
    prefer_touch: Boolean,
) -> IntegerTuple | None:
    h, w = shape(grid)
    ph, pw = shape(patch)
    locations = [(i, j) for i in range(h - ph + ONE) for j in range(w - pw + ONE)]
    shuffle(locations)
    touched = []
    plain = []
    for loc in locations:
        placed = shift(patch, loc)
        ok, is_touched = _placement_ok_12eac192(grid, placed, color_value)
        if not ok:
            continue
        if is_touched:
            touched.append(loc)
        else:
            plain.append(loc)
    if prefer_touch and len(touched) > ZERO:
        return choice(touched)
    if len(touched) > ZERO and choice((T, T, F)):
        return choice(touched)
    if len(plain) > ZERO:
        return choice(plain)
    if len(touched) > ZERO:
        return choice(touched)
    return None


def _paint_component_12eac192(
    grid: Grid,
    patch: Patch,
    color_value: Integer,
) -> Grid:
    return fill(grid, color_value, patch)


def generate_12eac192(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h, w = _pick_dims_12eac192(diff_lb, diff_ub)
        area = h * w
        nlarge, nsmall = _pick_component_counts_12eac192(area, diff_lb, diff_ub)
        ncols = branch(area <= 16, THREE, choice((THREE, FOUR, FOUR)))
        palette_in = tuple(sample((ONE, FIVE, SEVEN, EIGHT), ncols))
        color_bag = tuple(value for value in COLOR_BAG_12eac192 if value in palette_in)

        large_specs = []
        for _ in range(nlarge):
            sz = choice(LARGE_SIZE_BAG_12eac192)
            patch = choice(PATCHES_BY_SIZE_12eac192[sz])
            color_value = choice(color_bag)
            large_specs.append((patch, color_value))
        small_specs = []
        for _ in range(nsmall):
            sz = choice(SMALL_SIZE_BAG_12eac192)
            patch = choice(PATCHES_BY_SIZE_12eac192[sz])
            color_value = choice(color_bag)
            small_specs.append((patch, color_value))

        gi = canvas(ZERO, (h, w))
        go = canvas(ZERO, (h, w))
        placed = []
        failed = F

        for patch, color_value in large_specs + small_specs:
            prefer_touch = len(placed) > ZERO and choice((T, T, F))
            loc = _find_location_12eac192(gi, patch, color_value, prefer_touch)
            if loc is None:
                failed = T
                break
            shifted = shift(patch, loc)
            gi = _paint_component_12eac192(gi, shifted, color_value)
            out_color = branch(size(shifted) <= TWO, THREE, color_value)
            go = _paint_component_12eac192(go, shifted, out_color)
            placed.append((color_value, shifted))

        if failed:
            continue

        fg = area - colorcount(gi, ZERO)
        changed = colorcount(go, THREE)
        nobj = size(objects(gi, T, F, T))
        used = tuple(value for value in palette(gi) if value != ZERO)
        bgcount = colorcount(gi, ZERO)
        if not (size(used) >= branch(area <= 16, TWO, THREE)):
            continue
        if any(bgcount <= colorcount(gi, value) for value in used):
            continue
        if nobj != len(placed):
            continue
        if not (area * 2 // FIVE <= fg <= area * 7 // TEN + ONE):
            continue
        if not (THREE <= changed <= fg - TWO):
            continue
        if nlarge == ZERO or nsmall == ZERO:
            continue
        if colorcount(gi, THREE) != ZERO:
            continue
        return {"input": gi, "output": go}
