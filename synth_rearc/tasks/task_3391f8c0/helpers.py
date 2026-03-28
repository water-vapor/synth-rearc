from synth_rearc.core import *


BASE_PROTOTYPES_3391F8C0 = (
    frozenset({(ZERO, ZERO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, TWO), (ONE, ONE), (TWO, ONE)}),
    frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (ONE, TWO), (TWO, ONE)}),
    frozenset({(ZERO, ZERO), (ZERO, TWO), (ONE, ONE), (TWO, ZERO), (TWO, ONE), (TWO, TWO)}),
    frozenset({(ZERO, ZERO), (ZERO, ONE), (ZERO, TWO), (ONE, ZERO), (ONE, TWO), (TWO, TWO)}),
)

TRANSFORMS_3391F8C0 = (
    identity,
    hmirror,
    vmirror,
    compose(hmirror, vmirror),
    dmirror,
    cmirror,
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)

NONZERO_COLORS_3391F8C0 = interval(ONE, TEN, ONE)


def _build_prototype_library_3391f8c0() -> tuple[Indices, ...]:
    x0 = []
    for x1 in BASE_PROTOTYPES_3391F8C0:
        for x2 in TRANSFORMS_3391F8C0:
            x3 = normalize(x2(x1))
            if x3 not in x0:
                x0.append(x3)
    return tuple(x0)


PROTOTYPE_LIBRARY_3391F8C0 = _build_prototype_library_3391f8c0()


def sample_family_counts_3391f8c0(
    diff_lb: float,
    diff_ub: float,
) -> tuple[int, int]:
    if choice((T, F)):
        x0 = unifint(diff_lb, diff_ub, (TWO, FIVE))
        x1 = unifint(diff_lb, diff_ub, (ONE, TWO))
    else:
        x0 = unifint(diff_lb, diff_ub, (ONE, TWO))
        x1 = unifint(diff_lb, diff_ub, (TWO, FIVE))
    return x0, x1


def _expanded_rect_3391f8c0(
    anchor: IntegerTuple,
    max_h: int,
    max_w: int,
) -> tuple[int, int, int, int]:
    return (anchor[0] - ONE, anchor[1] - ONE, anchor[0] + max_h, anchor[1] + max_w)


def _rectangles_overlap_3391f8c0(
    a: tuple[int, int, int, int],
    b: tuple[int, int, int, int],
) -> bool:
    x0 = a[2] < b[0]
    x1 = b[2] < a[0]
    x2 = a[3] < b[1]
    x3 = b[3] < a[1]
    return not (x0 or x1 or x2 or x3)


def _sample_anchors_3391f8c0(
    height_value: int,
    width_value: int,
    max_h: int,
    max_w: int,
    count: int,
) -> tuple[IntegerTuple, ...] | None:
    x0 = list(product(range(ONE, height_value - max_h), range(ONE, width_value - max_w)))
    shuffle(x0)
    x1 = []
    x2 = []
    for x3 in x0:
        x4 = _expanded_rect_3391f8c0(x3, max_h, max_w)
        x5 = any(_rectangles_overlap_3391f8c0(x4, x6) for x6 in x2)
        if x5:
            continue
        x1.append(x3)
        x2.append(x4)
        if len(x1) == count:
            return tuple(x1)
    return None


def sample_layout_3391f8c0(
    diff_lb: float,
    diff_ub: float,
    max_h: int,
    max_w: int,
    count: int,
) -> tuple[int, int, tuple[IntegerTuple, ...]] | None:
    x0 = (count + TWO) // THREE
    x1 = (count + x0 - ONE) // x0
    x2 = max(max_h + FOUR, x0 * (max_h + TWO))
    x3 = max(max_w + FOUR, x1 * (max_w + TWO))
    if x2 > 18 or x3 > 18:
        return None
    for _ in range(64):
        x4 = unifint(diff_lb, diff_ub, (x2, 18))
        x5 = unifint(diff_lb, diff_ub, (x3, 18))
        x6 = _sample_anchors_3391f8c0(x4, x5, max_h, max_w, count)
        if x6 is not None:
            return x4, x5, x6
    return None


def render_scene_3391f8c0(
    height_value: int,
    width_value: int,
    color_a: int,
    proto_a: Indices,
    anchors_a: tuple[IntegerTuple, ...],
    color_b: int,
    proto_b: Indices,
    anchors_b: tuple[IntegerTuple, ...],
) -> Grid:
    x0 = canvas(ZERO, (height_value, width_value))
    for x1 in anchors_a:
        x2 = shift(proto_a, x1)
        x0 = paint(x0, recolor(color_a, x2))
    for x3 in anchors_b:
        x4 = shift(proto_b, x3)
        x0 = paint(x0, recolor(color_b, x4))
    return x0
