from synth_rearc.core import *


def _patch_e8686506(
    cells: tuple[IntegerTuple, ...],
) -> Indices:
    return frozenset(cells)


TEMPLATE_SPECS_E8686506 = {
    "single": {
        "dims": (FIVE, FIVE),
        "carrier_layers": (
            {
                "group": "carrier",
                "patch": _patch_e8686506(
                    (
                        (ZERO, ZERO),
                        (ZERO, ONE),
                        (ZERO, THREE),
                        (ZERO, FOUR),
                        (ONE, ZERO),
                        (ONE, FOUR),
                        (TWO, ZERO),
                        (TWO, FOUR),
                        (THREE, ONE),
                        (THREE, THREE),
                        (FOUR, ZERO),
                        (FOUR, ONE),
                        (FOUR, THREE),
                        (FOUR, FOUR),
                    )
                ),
            },
        ),
        "aux_pieces": (
            {"group": "single", "patch": _patch_e8686506(((ZERO, TWO),))},
            {
                "group": "block",
                "patch": _patch_e8686506(
                    (
                        (ONE, ONE),
                        (ONE, TWO),
                        (ONE, THREE),
                        (TWO, ONE),
                        (TWO, TWO),
                        (TWO, THREE),
                    )
                ),
            },
            {"group": "single", "patch": _patch_e8686506(((THREE, ZERO),))},
            {"group": "line", "patch": _patch_e8686506(((THREE, TWO), (FOUR, TWO)))},
            {"group": "single", "patch": _patch_e8686506(((THREE, FOUR),))},
        ),
    },
    "stack": {
        "dims": (EIGHT, FIVE),
        "carrier_layers": (
            {
                "group": "upper",
                "patch": _patch_e8686506(
                    (
                        (ZERO, ONE),
                        (ZERO, TWO),
                        (ZERO, THREE),
                        (ONE, ZERO),
                        (ONE, FOUR),
                        (TWO, ZERO),
                        (TWO, ONE),
                        (TWO, THREE),
                        (TWO, FOUR),
                        (THREE, ONE),
                        (THREE, THREE),
                    )
                ),
            },
            {
                "group": "lower",
                "patch": _patch_e8686506(
                    (
                        (FOUR, ONE),
                        (FOUR, THREE),
                        (FIVE, ZERO),
                        (FIVE, ONE),
                        (FIVE, THREE),
                        (FIVE, FOUR),
                        (SIX, ZERO),
                        (SIX, FOUR),
                        (SEVEN, ONE),
                        (SEVEN, TWO),
                        (SEVEN, THREE),
                    )
                ),
            },
        ),
        "aux_pieces": (
            {"group": "corner", "patch": _patch_e8686506(((ZERO, ZERO),))},
            {"group": "corner", "patch": _patch_e8686506(((ZERO, FOUR),))},
            {
                "group": "top_t",
                "patch": _patch_e8686506(
                    (
                        (ONE, ONE),
                        (ONE, TWO),
                        (ONE, THREE),
                        (TWO, TWO),
                        (THREE, TWO),
                    )
                ),
            },
            {"group": "side", "patch": _patch_e8686506(((THREE, ZERO), (FOUR, ZERO)))},
            {"group": "side", "patch": _patch_e8686506(((THREE, FOUR), (FOUR, FOUR)))},
            {
                "group": "bottom_t",
                "patch": _patch_e8686506(
                    (
                        (FOUR, TWO),
                        (FIVE, TWO),
                        (SIX, ONE),
                        (SIX, TWO),
                        (SIX, THREE),
                    )
                ),
            },
            {"group": "corner", "patch": _patch_e8686506(((SEVEN, ZERO),))},
            {"group": "corner", "patch": _patch_e8686506(((SEVEN, FOUR),))},
        ),
    },
    "frame": {
        "dims": (EIGHT, FIVE),
        "carrier_layers": (
            {
                "group": "carrier",
                "patch": _patch_e8686506(
                    (
                        (ZERO, ONE),
                        (ZERO, TWO),
                        (ZERO, THREE),
                        (ONE, ZERO),
                        (ONE, FOUR),
                        (TWO, ONE),
                        (TWO, THREE),
                        (THREE, ONE),
                        (THREE, THREE),
                        (FOUR, ONE),
                        (FOUR, THREE),
                        (FIVE, ONE),
                        (FIVE, THREE),
                        (SIX, ZERO),
                        (SIX, FOUR),
                        (SEVEN, ONE),
                        (SEVEN, TWO),
                        (SEVEN, THREE),
                    )
                ),
            },
        ),
        "aux_pieces": (
            {"group": "corner", "patch": _patch_e8686506(((ZERO, ZERO),))},
            {"group": "corner", "patch": _patch_e8686506(((ZERO, FOUR),))},
            {
                "group": "top_t",
                "patch": _patch_e8686506(((ONE, ONE), (ONE, TWO), (ONE, THREE), (TWO, TWO))),
            },
            {
                "group": "side",
                "patch": _patch_e8686506(((TWO, ZERO), (THREE, ZERO), (FOUR, ZERO), (FIVE, ZERO))),
            },
            {"group": "middle", "patch": _patch_e8686506(((THREE, TWO), (FOUR, TWO)))},
            {
                "group": "side",
                "patch": _patch_e8686506(((TWO, FOUR), (THREE, FOUR), (FOUR, FOUR), (FIVE, FOUR))),
            },
            {
                "group": "bottom_t",
                "patch": _patch_e8686506(((FIVE, TWO), (SIX, ONE), (SIX, TWO), (SIX, THREE))),
            },
            {"group": "corner", "patch": _patch_e8686506(((SEVEN, ZERO),))},
            {"group": "corner", "patch": _patch_e8686506(((SEVEN, FOUR),))},
        ),
    },
}


def transform_patch_e8686506(
    patch: Indices,
    dims: IntegerTuple,
    flip_vertical: Boolean,
    flip_horizontal: Boolean,
) -> Indices:
    h, w = dims
    out = set()
    for i, j in patch:
        ni = h - ONE - i if flip_vertical else i
        nj = w - ONE - j if flip_horizontal else j
        out.add((ni, nj))
    return frozenset(out)


def instantiate_template_e8686506(
    name: str,
    flip_vertical: Boolean,
    flip_horizontal: Boolean,
) -> dict[str, object]:
    spec = TEMPLATE_SPECS_E8686506[name]
    dims = spec["dims"]
    carrier_layers = tuple(
        {
            "group": layer["group"],
            "patch": transform_patch_e8686506(layer["patch"], dims, flip_vertical, flip_horizontal),
        }
        for layer in spec["carrier_layers"]
    )
    aux_pieces = tuple(
        {
            "group": piece["group"],
            "patch": transform_patch_e8686506(piece["patch"], dims, flip_vertical, flip_horizontal),
        }
        for piece in spec["aux_pieces"]
    )
    return {
        "name": name,
        "dims": dims,
        "carrier_layers": carrier_layers,
        "aux_pieces": aux_pieces,
    }


def build_carrier_object_e8686506(
    spec: dict[str, object],
    carrier_colors: dict[str, Integer],
) -> Object:
    pieces = []
    for layer in spec["carrier_layers"]:
        pieces.append(recolor(carrier_colors[layer["group"]], layer["patch"]))
    return frozenset(cell for piece in pieces for cell in piece)


def build_aux_objects_e8686506(
    spec: dict[str, object],
    aux_colors: dict[str, Integer],
) -> tuple[Object, ...]:
    return tuple(recolor(aux_colors[piece["group"]], piece["patch"]) for piece in spec["aux_pieces"])


def render_output_e8686506(
    spec: dict[str, object],
    carrier_colors: dict[str, Integer],
    aux_colors: dict[str, Integer],
) -> Grid:
    out = canvas(ZERO, spec["dims"])
    for layer in spec["carrier_layers"]:
        out = fill(out, carrier_colors[layer["group"]], layer["patch"])
    for piece in spec["aux_pieces"]:
        out = fill(out, aux_colors[piece["group"]], piece["patch"])
    return out


def rectangle_patch_e8686506(
    upper_left: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    i0, j0 = upper_left
    h, w = dims
    return frozenset((i, j) for i in range(i0, i0 + h) for j in range(j0, j0 + w))


def expand_patch_e8686506(
    patch: Patch,
    dims: IntegerTuple,
    radius: Integer = ONE,
) -> Indices:
    h, w = dims
    out = set()
    for i, j in toindices(patch):
        for di in range(-radius, radius + ONE):
            for dj in range(-radius, radius + ONE):
                ni = i + di
                nj = j + dj
                if both(0 <= ni < h, 0 <= nj < w):
                    out.add((ni, nj))
    return frozenset(out)


def scatter_objects_e8686506(
    objs: tuple[Object, ...],
    forbidden: Patch,
    dims: IntegerTuple,
) -> tuple[Object, ...] | None:
    h, w = dims
    occupied = set(toindices(forbidden))
    blocked = set(expand_patch_e8686506(forbidden, dims))
    order = list(range(len(objs)))
    shuffle(order)
    order.sort(key=lambda k: -size(objs[k]))
    placed: list[Object | None] = [None] * len(objs)
    for idx in order:
        obj = normalize(objs[idx])
        oh = height(obj)
        ow = width(obj)
        candidates = [(i, j) for i in range(h - oh + ONE) for j in range(w - ow + ONE)]
        shuffle(candidates)
        choice_obj = None
        for offset in candidates:
            placed_obj = shift(obj, offset)
            cells = toindices(placed_obj)
            if len(intersection(cells, blocked)) > ZERO:
                continue
            choice_obj = placed_obj
            break
        if choice_obj is None:
            return None
        placed[idx] = choice_obj
        occupied |= toindices(choice_obj)
        blocked |= expand_patch_e8686506(choice_obj, dims)
    return tuple(obj for obj in placed if obj is not None)
