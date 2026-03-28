from synth_rearc.core import *

from .helpers import (
    GRID_SHAPE_98c475bf,
    MARKER_COLUMNS_98c475bf,
    TEMPLATE_COLORS_98c475bf,
    render_templates_98c475bf,
    template_anchor_rows_98c475bf,
)
from .verifier import verify_98c475bf


def _marker_object_98c475bf(
    specs: tuple[tuple[Integer, Integer], ...],
) -> Object:
    x0, x1 = MARKER_COLUMNS_98c475bf
    return frozenset(
        (x2, (x3, x4))
        for x2, x3 in specs
        for x4 in (x0, x1)
    )


def generate_98c475bf(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = tuple(range(ONE, TEN))
    x1 = GRID_SHAPE_98c475bf
    x2 = astuple(ZERO, x1[1] - ONE)
    while True:
        x3 = unifint(diff_lb, diff_ub, (ONE, TWO))
        x4 = tuple(sample(TEMPLATE_COLORS_98c475bf, x3))
        x5 = tuple(x6 for x6 in TEMPLATE_COLORS_98c475bf if x6 not in x4)
        x6 = choice(x5)
        x7 = tuple(x8 for x8 in x0 if x8 not in x4 and x8 != x6)
        x8 = choice(x7)
        x9 = []
        x10 = list(x4)
        shuffle(x10)
        x11 = frozenset()
        for x12 in x10:
            x13 = list(template_anchor_rows_98c475bf(x12, x1[0]))
            shuffle(x13)
            x14 = None
            for x15 in x13:
                x16 = render_templates_98c475bf(((x12, x15),))
                x17 = intersection(toindices(x11), toindices(x16))
                if len(x17) == ZERO:
                    x14 = x15
                    x11 = x11.union(x16)
                    break
            if x14 is None:
                break
            x9.append((x12, x14))
        if len(x9) != x3:
            continue
        x18 = list(template_anchor_rows_98c475bf(x6, x1[0]))
        shuffle(x18)
        x19 = frozenset((x20, x21) for _, x20 in x9 for x21 in MARKER_COLUMNS_98c475bf)
        x20 = None
        for x21 in x18:
            x22 = render_templates_98c475bf(((x6, x21),))
            x23 = intersection(toindices(x22), x19)
            if len(x23) == ZERO:
                x20 = x21
                break
        if x20 is None:
            continue
        x21 = tuple(sorted(x9, key=lambda x22: x22[1]))
        x22 = render_templates_98c475bf(((x6, x20),))
        x23 = _marker_object_98c475bf(x21)
        x24 = canvas(ZERO, x1)
        x25 = fill(x24, x8, vfrontier(ORIGIN))
        x26 = fill(x25, x8, vfrontier(x2))
        x27 = paint(x26, x22)
        x28 = paint(x27, x23)
        x29 = verify_98c475bf(x28)
        if x28 == x29:
            continue
        return {"input": x28, "output": x29}
