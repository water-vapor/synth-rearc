from synth_rearc.core import *

from .verifier import verify_3a301edc


NONZERO_COLORS_3A301EDC = remove(ZERO, interval(ZERO, TEN, ONE))
INNER_DIM_OFFSETS_3A301EDC = (-ONE, ZERO, ZERO, ONE)
BORDER_WIDTHS_3A301EDC = (ONE, TWO)


def _rect_patch_3a301edc(
    top: Integer,
    left: Integer,
    height_: Integer,
    width_: Integer,
) -> Indices:
    x0 = frozenset(
        {
            (top, left),
            (top + height_ - ONE, left + width_ - ONE),
        }
    )
    return backdrop(x0)


def _centered_span_3a301edc(
    center_: Integer,
    target: Integer,
    limit: Integer,
) -> tuple[Integer, Integer]:
    half = target // TWO
    if even(target):
        radius = min(half, center_, limit - center_)
        size_ = 2 * radius
    else:
        radius = min(half, center_, limit - ONE - center_)
        size_ = 2 * radius + ONE
    start = center_ - size_ // TWO
    return start, size_


def _surround_patch_3a301edc(
    grid_h: Integer,
    grid_w: Integer,
    top: Integer,
    left: Integer,
    outer_h: Integer,
    outer_w: Integer,
    inner_h: Integer,
    inner_w: Integer,
) -> Indices:
    center_i = top + outer_h // TWO
    center_j = left + outer_w // TWO
    target_h = outer_h + 2 * inner_h
    target_w = outer_w + 2 * inner_w
    surround_top, surround_h = _centered_span_3a301edc(center_i, target_h, grid_h)
    surround_left, surround_w = _centered_span_3a301edc(center_j, target_w, grid_w)
    return _rect_patch_3a301edc(surround_top, surround_left, surround_h, surround_w)


def generate_3a301edc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(400):
        inner_h = unifint(diff_lb, diff_ub, (ONE, FOUR))
        inner_w = inner_h + choice(INNER_DIM_OFFSETS_3A301EDC)
        if not ONE <= inner_w <= FOUR:
            continue
        border_w = choice(BORDER_WIDTHS_3A301EDC)
        outer_h = inner_h + 2 * border_w
        outer_w = inner_w + 2 * border_w
        top = unifint(diff_lb, diff_ub, (TWO, inner_h + THREE))
        left = unifint(diff_lb, diff_ub, (TWO, inner_w + THREE))
        min_h = max(11, top + outer_h + inner_h + ONE)
        max_h = min(30, top + outer_h + inner_h + 10)
        min_w = max(11, left + outer_w + inner_w + ONE)
        max_w = min(30, left + outer_w + inner_w + 10)
        if min_h > max_h or min_w > max_w:
            continue
        h = unifint(diff_lb, diff_ub, (min_h, max_h))
        w = unifint(diff_lb, diff_ub, (min_w, max_w))
        outer_color, inner_color = sample(NONZERO_COLORS_3A301EDC, TWO)

        outer_patch = _rect_patch_3a301edc(top, left, outer_h, outer_w)
        inner_patch = _rect_patch_3a301edc(top + border_w, left + border_w, inner_h, inner_w)
        surround_patch = _surround_patch_3a301edc(
            h,
            w,
            top,
            left,
            outer_h,
            outer_w,
            inner_h,
            inner_w,
        )

        gi = canvas(ZERO, (h, w))
        gi = fill(gi, outer_color, outer_patch)
        gi = fill(gi, inner_color, inner_patch)

        go = canvas(ZERO, (h, w))
        go = fill(go, inner_color, surround_patch)
        go = fill(go, outer_color, outer_patch)
        go = fill(go, inner_color, inner_patch)

        if gi == go:
            continue
        if verify_3a301edc(gi) != go:
            continue
        return {"input": gi, "output": go}

    raise RuntimeError("failed to generate example for 3a301edc")
