from arc2.core import *

from .helpers import (
    box_patch_f21745ec,
    pattern_patch_f21745ec,
    place_boxes_f21745ec,
    sample_inner_patch_f21745ec,
)


def generate_f21745ec(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        side = unifint(diff_lb, diff_ub, (19, 24))
        target_dims = (
            unifint(diff_lb, diff_ub, (FIVE, EIGHT)),
            unifint(diff_lb, diff_ub, (FIVE, EIGHT)),
        )
        same_count = unifint(diff_lb, diff_ub, (TWO, FOUR))
        distractor_count = unifint(diff_lb, diff_ub, (ONE, TWO))
        distractor_dims = []
        seen_dims = {target_dims}
        while len(distractor_dims) < distractor_count:
            dims = (
                unifint(diff_lb, diff_ub, (FOUR, EIGHT)),
                unifint(diff_lb, diff_ub, (FOUR, EIGHT)),
            )
            if dims in seen_dims:
                continue
            distractor_dims.append(dims)
            seen_dims.add(dims)
        specs = [{"dims": target_dims, "keep": True} for _ in range(same_count)]
        specs.extend({"dims": dims, "keep": False} for dims in distractor_dims)
        shuffle(specs)
        dims_seq = tuple(spec["dims"] for spec in specs)
        locs = place_boxes_f21745ec(side, dims_seq)
        if locs is None:
            continue
        colors = sample(interval(ONE, TEN, ONE), len(specs))
        template_idx = choice(tuple(idx for idx, spec in enumerate(specs) if spec["keep"]))
        inner_dims = (target_dims[0] - TWO, target_dims[1] - TWO)
        inner_patch = sample_inner_patch_f21745ec(diff_lb, diff_ub, inner_dims)
        target_patch = pattern_patch_f21745ec(target_dims, inner_patch)
        gi = canvas(ZERO, (side, side))
        go = canvas(ZERO, (side, side))
        for idx, spec in enumerate(specs):
            loc = locs[idx]
            dims = spec["dims"]
            col = colors[idx]
            frame_patch = box_patch_f21745ec(loc, dims)
            if spec["keep"]:
                painted_patch = shift(target_patch, loc)
                go = fill(go, col, painted_patch)
                if idx == template_idx:
                    gi = fill(gi, col, painted_patch)
                else:
                    gi = fill(gi, col, frame_patch)
                continue
            gi = fill(gi, col, frame_patch)
        return {"input": gi, "output": go}
