from arc2.core import *

from .helpers import cover_anchors_fd096ab6


BG_FD096AB6 = ONE
TEMPLATE_COLOR_FD096AB6 = FOUR
PARTIAL_COLORS_FD096AB6 = (TWO, THREE, FIVE, SIX, SEVEN, EIGHT, NINE)
TEMPLATE_FAMILIES_FD096AB6 = (
    frozenset(
        {
            (ZERO, ONE),
            (ZERO, TWO),
            (ZERO, THREE),
            (ONE, ZERO),
            (ONE, FOUR),
            (TWO, ONE),
            (THREE, ONE),
            (THREE, TWO),
        }
    ),
    frozenset(
        {
            (ZERO, TWO),
            (ZERO, THREE),
            (ONE, ZERO),
            (ONE, ONE),
            (TWO, TWO),
        }
    ),
    frozenset(
        {
            (ZERO, TWO),
            (ONE, ONE),
            (ONE, THREE),
            (TWO, ZERO),
            (TWO, ONE),
            (TWO, THREE),
        }
    ),
)

def _sample_template_fd096ab6(
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    return choice(TEMPLATE_FAMILIES_FD096AB6)


def _sample_subset_fd096ab6(
    template: Indices,
) -> Indices:
    cells = tuple(sorted(template))
    options = tuple(size_value for size_value in (TWO, TWO, THREE, THREE, FOUR, FIVE) if size_value < len(cells))
    count = choice(options) if len(options) > ZERO else len(cells) - ONE
    return frozenset(sample(cells, count))


def _reserve_box_fd096ab6(
    anchor: IntegerTuple,
    dims: tuple[Integer, Integer],
    side: Integer,
) -> Indices:
    top, left = anchor
    height_value, width_value = dims
    return frozenset(
        (i, j)
        for i in range(max(ZERO, top - ONE), min(side, top + height_value + ONE))
        for j in range(max(ZERO, left - ONE), min(side, left + width_value + ONE))
    )


def _sample_anchors_fd096ab6(
    side: Integer,
    template_shape: tuple[Integer, Integer],
    n_copies: Integer,
) -> tuple[IntegerTuple, ...] | None:
    reserved = frozenset()
    anchors = []
    limit_i = side - template_shape[ZERO]
    limit_j = side - template_shape[ONE]
    for _ in range(500):
        candidate = astuple(randint(ZERO, limit_i), randint(ZERO, limit_j))
        blocked = _reserve_box_fd096ab6(candidate, template_shape, side)
        if len(intersection(blocked, reserved)) > ZERO:
            continue
        anchors.append(candidate)
        reserved = combine(reserved, blocked)
        if len(anchors) == n_copies:
            return tuple(anchors)
    return None


def _sample_colors_fd096ab6(
    n_partials: Integer,
) -> tuple[Integer, ...]:
    colors = list(sample(PARTIAL_COLORS_FD096AB6, min(n_partials, len(PARTIAL_COLORS_FD096AB6))))
    if n_partials > len(colors):
        colors.append(choice(colors))
    elif n_partials >= SIX and choice((T, F)):
        colors[-ONE] = choice(colors[:-ONE])
    shuffle(colors)
    return tuple(colors)


def _decoded_matches_fd096ab6(
    gi: Grid,
    go: Grid,
    template: Indices,
    anchors_by_color: dict[Integer, tuple[IntegerTuple, ...]],
) -> Boolean:
    partitions = fgpartition(gi)
    occupied = toindices(merge(partitions))
    decoded = gi
    for part in partitions:
        value = color(part)
        if value == TEMPLATE_COLOR_FD096AB6:
            continue
        cells = toindices(part)
        blocked = difference(occupied, cells)
        anchors = tuple(sorted(cover_anchors_fd096ab6(template, cells, shape(gi), blocked)))
        if anchors != tuple(sorted(anchors_by_color[value])):
            return False
        for anchor in anchors:
            decoded = fill(decoded, value, shift(template, anchor))
    return decoded == go


def generate_fd096ab6(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        template = _sample_template_fd096ab6(diff_lb, diff_ub)
        template_shape = shape(template)
        side = unifint(diff_lb, diff_ub, (20, 30))
        capacity = max(
            FOUR,
            side * side // ((template_shape[ZERO] + TWO) * (template_shape[ONE] + TWO)) - ONE,
        )
        n_partials = unifint(diff_lb, diff_ub, (FOUR, min(EIGHT, capacity)))
        anchors = _sample_anchors_fd096ab6(side, template_shape, add(n_partials, ONE))
        if anchors is None:
            continue
        colors = _sample_colors_fd096ab6(n_partials)
        subsets = tuple(_sample_subset_fd096ab6(template) for _ in range(n_partials))
        dims = (side, side)
        gi = canvas(BG_FD096AB6, dims)
        go = canvas(BG_FD096AB6, dims)
        reference_anchor = first(anchors)
        reference_patch = shift(template, reference_anchor)
        gi = fill(gi, TEMPLATE_COLOR_FD096AB6, reference_patch)
        go = fill(go, TEMPLATE_COLOR_FD096AB6, reference_patch)
        anchors_by_color = {}
        for anchor, value, subset in zip(anchors[ONE:], colors, subsets):
            gi = fill(gi, value, shift(subset, anchor))
            go = fill(go, value, shift(template, anchor))
            anchors_by_color.setdefault(value, []).append(anchor)
        anchors_by_color = {
            value: tuple(sorted(anchor_group))
            for value, anchor_group in anchors_by_color.items()
        }
        if gi == go:
            continue
        if not _decoded_matches_fd096ab6(gi, go, template, anchors_by_color):
            continue
        return {"input": gi, "output": go}
