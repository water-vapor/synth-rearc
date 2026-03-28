from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    apply_layers_to_rectangle_40f6cd08,
    bbox_to_patch_40f6cd08,
)


def _anchor_layers_40f6cd08(
    depth: Integer,
) -> tuple[tuple[int, int, int, int], ...]:
    anchor = choice(("center", "center", "left", "bottom"))
    margin = choice((TWO, THREE, FOUR))
    layers = []
    for _ in range(depth):
        if anchor == "center":
            layers.append((margin, margin, margin, margin))
        elif anchor == "left":
            layers.append((margin, ZERO, margin, margin))
        else:
            layers.append((margin, margin, ZERO, margin))
        margin += choice((ONE, ONE, TWO))
    return tuple(layers)


def _minimum_dims_40f6cd08(
    layers: tuple[tuple[int, int, int, int], ...],
) -> IntegerTuple:
    min_h = max(top + bottom + ONE for top, left, bottom, right in layers)
    min_w = max(left + right + ONE for top, left, bottom, right in layers)
    return min_h, min_w


def _sample_rect_dims_40f6cd08(
    diff_lb: float,
    diff_ub: float,
    layers: tuple[tuple[int, int, int, int], ...],
) -> IntegerTuple:
    min_h, min_w = _minimum_dims_40f6cd08(layers)
    h_lb = max(SIX, min_h + ONE)
    h_ub = max(h_lb, min(18, min_h + TEN))
    w_lb = max(SEVEN, min_w + TWO)
    w_ub = max(w_lb, min(20, min_w + 12))
    return (
        unifint(diff_lb, diff_ub, (h_lb, h_ub)),
        unifint(diff_lb, diff_ub, (w_lb, w_ub)),
    )


def _separated_40f6cd08(
    rect: tuple[int, int, int, int],
    placed: tuple[tuple[int, int, int, int], ...],
    gap: Integer,
) -> Boolean:
    i0, j0, h, w = rect
    for pi, pj, ph, pw in placed:
        if not (i0 + h + gap <= pi or pi + ph + gap <= i0 or j0 + w + gap <= pj or pj + pw + gap <= j0):
            return False
    return True


def _place_rectangles_40f6cd08(
    dims: IntegerTuple,
    rect_dims: tuple[IntegerTuple, ...],
) -> tuple[tuple[int, int, int, int], ...] | None:
    h, w = dims
    order_ids = tuple(sorted(range(len(rect_dims)), key=lambda idx: rect_dims[idx][ZERO] * rect_dims[idx][ONE], reverse=True))
    placed = {}
    done = ()
    gap = choice((ONE, ONE, TWO))
    for idx in order_ids:
        rh, rw = rect_dims[idx]
        rows = tuple(range(ONE, h - rh))
        cols = tuple(range(ONE, w - rw))
        cands = [
            (i0, j0, rh, rw)
            for i0 in rows
            for j0 in cols
            if _separated_40f6cd08((i0, j0, rh, rw), done, gap)
        ]
        if len(cands) == ZERO:
            return None
        rect = choice(cands)
        placed[idx] = rect
        done = done + (rect,)
    return tuple(placed[idx] for idx in range(len(rect_dims)))


def generate_40f6cd08(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice((TWO, TWO, THREE))
        x1 = choice((TWO, TWO, THREE))
        x2 = sample(interval(ONE, TEN, ONE), x1 + ONE)
        x3 = first(x2)
        x4 = x2[ONE:]
        x5 = _anchor_layers_40f6cd08(x1)
        x6 = tuple((x4[k],) + x5[k] for k in range(x1))
        x7 = tuple(_sample_rect_dims_40f6cd08(diff_lb, diff_ub, x5) for _ in range(x0))
        x8 = (
            unifint(diff_lb, diff_ub, (24, 30)),
            unifint(diff_lb, diff_ub, (24, 30)),
        )
        x9 = _place_rectangles_40f6cd08(x8, x7)
        if x9 is None:
            continue
        x10 = choice(interval(ZERO, x0, ONE))
        x11 = canvas(ZERO, x8)
        for x12 in x9:
            x13 = bbox_to_patch_40f6cd08(x12)
            x11 = fill(x11, x3, x13)
        x14 = apply_layers_to_rectangle_40f6cd08(x11, bbox_to_patch_40f6cd08(x9[x10]), x6)
        x15 = x11
        for x16 in x9:
            x15 = apply_layers_to_rectangle_40f6cd08(x15, bbox_to_patch_40f6cd08(x16), x6)
        if x14 != x15:
            return {"input": x14, "output": x15}
