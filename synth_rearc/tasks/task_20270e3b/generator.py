from synth_rearc.core import *

from .helpers import build_base_piece_20270e3b
from .helpers import build_source_piece_above_20270e3b
from .helpers import build_source_piece_corner_20270e3b
from .helpers import render_input_20270e3b
from .helpers import render_output_20270e3b
from .verifier import verify_20270e3b


MAX_DIM_20270E3B = 30


def generate_20270e3b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        marker_len = choice((ONE, ONE, ONE, THREE, THREE))
        use_corner_source = marker_len == ONE and uniform(0.0, 1.0) < 0.45
        base_obj, base_anchor = build_base_piece_20270e3b(diff_lb, diff_ub, marker_len)
        if use_corner_source:
            source_obj, source_anchor = build_source_piece_corner_20270e3b(diff_lb, diff_ub)
        else:
            source_obj, source_anchor = build_source_piece_above_20270e3b(diff_lb, diff_ub, marker_len)
        base_piece = combine(toindices(base_obj), base_anchor)
        source_piece = combine(toindices(source_obj), source_anchor)
        base_h, base_w = shape(base_piece)
        source_h, source_w = shape(source_piece)
        gap = randint(2, 5)
        margin = randint(0, 1)
        orient = choice(("h", "v"))
        if orient == "h":
            h = max(base_h, source_h) + randint(0, 2) + margin * TWO
            w = base_w + source_w + gap + margin * TWO
            if h > MAX_DIM_20270E3B or w > MAX_DIM_20270E3B:
                continue
            base_offset = (
                margin + randint(ZERO, h - margin * TWO - base_h),
                margin,
            )
            source_offset = (
                margin + randint(ZERO, h - margin * TWO - source_h),
                margin + base_w + gap,
            )
        else:
            h = base_h + source_h + gap + margin * TWO
            w = max(base_w, source_w) + randint(0, 2) + margin * TWO
            if h > MAX_DIM_20270E3B or w > MAX_DIM_20270E3B:
                continue
            base_offset = (
                margin,
                margin + randint(ZERO, w - margin * TWO - base_w),
            )
            source_offset = (
                margin + base_h + gap,
                margin + randint(ZERO, w - margin * TWO - source_w),
            )
        base_obj_abs = shift(base_obj, base_offset)
        base_anchor_abs = shift(base_anchor, base_offset)
        source_obj_abs = shift(source_obj, source_offset)
        source_anchor_abs = shift(source_anchor, source_offset)
        gi = render_input_20270e3b(
            (h, w),
            base_obj_abs,
            base_anchor_abs,
            source_obj_abs,
            source_anchor_abs,
        )
        go = render_output_20270e3b(
            base_obj_abs,
            base_anchor_abs,
            source_obj_abs,
            source_anchor_abs,
        )
        if height(go) > MAX_DIM_20270E3B or width(go) > MAX_DIM_20270E3B:
            continue
        moved_source = shift(
            source_obj_abs,
            add(subtract(ulcorner(base_anchor_abs), ulcorner(source_anchor_abs)), UP),
        )
        contribution = difference(toindices(moved_source), toindices(base_obj_abs))
        if size(contribution) < marker_len + 2:
            continue
        if verify_20270e3b(gi) != go:
            continue
        return {"input": gi, "output": go}
