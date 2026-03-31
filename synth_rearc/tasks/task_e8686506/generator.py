from synth_rearc.core import *

from .helpers import (
    build_aux_objects_e8686506,
    build_carrier_object_e8686506,
    expand_patch_e8686506,
    instantiate_template_e8686506,
    rectangle_patch_e8686506,
    render_output_e8686506,
    scatter_objects_e8686506,
)
from .verifier import verify_e8686506


def _group_order_e8686506(
    pieces: tuple[dict[str, object], ...],
) -> tuple[str, ...]:
    out = []
    for piece in pieces:
        name = piece["group"]
        if name not in out:
            out.append(name)
    return tuple(out)


def _assign_colors_e8686506(
    groups: tuple[str, ...],
    pool: list[Integer],
) -> dict[str, Integer]:
    return {group: pool.pop() for group in groups}


def generate_e8686506(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(("single", "stack", "frame", "frame"))
        x1 = choice((T, F))
        x2 = choice((T, F))
        x3 = instantiate_template_e8686506(x0, x1, x2)
        x4 = _group_order_e8686506(x3["carrier_layers"])
        x5 = _group_order_e8686506(x3["aux_pieces"])
        x6 = list(range(ONE, TEN))
        shuffle(x6)
        x7 = x6.pop()
        x8 = _assign_colors_e8686506(x4, x6)
        x9 = _assign_colors_e8686506(x5, x6)
        x10 = render_output_e8686506(x3, x8, x9)
        x11 = build_carrier_object_e8686506(x3, x8)
        x12 = build_aux_objects_e8686506(x3, x9)
        x13, x14 = x3["dims"]
        x15 = unifint(diff_lb, diff_ub, (max(12, x13 + 5), 18))
        x16 = unifint(diff_lb, diff_ub, (max(13, x14 + 8), 19))
        if both(x15 <= x13 + 2, x16 <= x14 + 2):
            continue
        x17 = TWO if x15 >= x13 + 5 else ONE
        x18 = TWO if x16 >= x14 + 5 else ONE
        x19 = randint(x17, x15 - x13 - x17)
        x20 = randint(x18, x16 - x14 - x18)
        x21 = shift(x11, (x19, x20))
        x22 = rectangle_patch_e8686506((x19, x20), x3["dims"])
        x23 = expand_patch_e8686506(x22, (x15, x16))
        x24 = scatter_objects_e8686506(x12, x23, (x15, x16))
        if x24 is None:
            continue
        x25 = paint(canvas(x7, (x15, x16)), x21)
        for x26 in x24:
            x25 = paint(x25, x26)
        if x25 == x10:
            continue
        if verify_e8686506(x25) != x10:
            continue
        return {"input": x25, "output": x10}
