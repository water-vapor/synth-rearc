from arc2.core import *
from .verifier import verify_414297c0


def _transform_mask_414297c0(
    mask: frozenset[IntegerTuple],
    rot: Integer,
    flip: Boolean,
) -> frozenset[IntegerTuple]:
    cells = mask
    if flip:
        cells = frozenset((i, -j) for i, j in cells)
    for _ in range(rot):
        cells = frozenset((j, -i) for i, j in cells)
    return cells


def _mask_family_414297c0() -> tuple[frozenset[IntegerTuple], ...]:
    bases = (
        frozenset({(-1, 0), (0, -1), (0, 1), (1, -1)}),
        frozenset({(-1, -1), (-1, 1), (0, 1), (1, -1), (1, 0), (1, 1)}),
        frozenset({(-1, -1), (0, -1), (0, 1), (1, 1)}),
        frozenset({(-1, 0), (0, -1), (0, 1), (1, 0)}),
        frozenset({(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 1)}),
        frozenset({(-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)}),
        frozenset({(0, -1), (0, 1), (1, 0)}),
        frozenset({(-1, -1), (-1, 0), (0, -1), (1, 1)}),
        frozenset({(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)}),
    )
    family = {
        _transform_mask_414297c0(mask, rot, flip)
        for mask in bases
        for rot in range(FOUR)
        for flip in (False, True)
    }
    return tuple(sorted(family, key=lambda mask: (len(mask), tuple(sorted(mask)))))


MASK_FAMILY_414297c0 = _mask_family_414297c0()


def _boxes_touch_414297c0(
    a: tuple[int, int, int, int],
    b: tuple[int, int, int, int],
) -> Boolean:
    # Boxes represent full 3x3 influence zones; touching means 8-neighbor merging.
    ai, aj, ah, aw = a
    bi, bj, bh, bw = b
    row_far = ai + ah < bi or bi + bh < ai
    col_far = aj + aw < bj or bj + bw < aj
    return not (row_far or col_far)


def _sample_centers_414297c0(
    h: Integer,
    w: Integer,
    n: Integer,
) -> tuple[IntegerTuple, ...] | None:
    cells = [(i, j) for i in range(ONE, h - ONE) for j in range(ONE, w - ONE)]
    shuffle(cells)
    centers: list[IntegerTuple] = []
    boxes: list[tuple[int, int, int, int]] = []
    for loc in cells:
        box = (loc[0] - ONE, loc[1] - ONE, THREE, THREE)
        if any(_boxes_touch_414297c0(box, other) for other in boxes):
            continue
        centers.append(loc)
        boxes.append(box)
        if len(centers) == n:
            return tuple(centers)
    return None


def _sample_boxes_414297c0(
    h: Integer,
    w: Integer,
    rect_box: tuple[int, int, int, int],
    n: Integer,
) -> tuple[tuple[int, int, int, int], ...] | None:
    candidates = []
    for i in range(h - TWO):
        for j in range(w - TWO):
            box = (i, j, THREE, THREE)
            if _boxes_touch_414297c0(box, rect_box):
                continue
            candidates.append(box)
    shuffle(candidates)
    chosen: list[tuple[int, int, int, int]] = []
    for box in candidates:
        if any(_boxes_touch_414297c0(box, other) for other in chosen):
            continue
        chosen.append(box)
        if len(chosen) == n:
            return tuple(chosen)
    return None


def generate_414297c0(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (16, 30))
        w = unifint(diff_lb, diff_ub, (16, 30))
        rect_h = unifint(diff_lb, diff_ub, (6, min(15, h - 4)))
        rect_w = unifint(diff_lb, diff_ub, (6, min(15, w - 4)))
        if rect_h * rect_w > (h * w) // THREE:
            continue
        max_targets = min(FIVE, max(TWO, rect_h * rect_w // 24 + ONE))
        n_targets = unifint(diff_lb, diff_ub, (2, max_targets))
        centers = _sample_centers_414297c0(rect_h, rect_w, n_targets)
        if centers is None:
            continue
        n_distractors = unifint(diff_lb, diff_ub, (0, 2))
        colors = [color for color in range(ONE, TEN) if color != TWO]
        bgc = choice(colors)
        colors.remove(bgc)
        if len(colors) < n_targets + n_distractors:
            continue
        chosen_colors = sample(colors, n_targets + n_distractors)
        target_colors = tuple(chosen_colors[:n_targets])
        distractor_colors = tuple(chosen_colors[n_targets:])
        target_masks = tuple(choice(MASK_FAMILY_414297c0) for _ in range(n_targets))
        distractor_masks = tuple(choice(MASK_FAMILY_414297c0) for _ in range(n_distractors))
        nonzero_count = (
            rect_h * rect_w
            + sum(len(mask) + ONE for mask in target_masks)
            + sum(len(mask) + ONE for mask in distractor_masks)
        )
        if h * w - nonzero_count <= rect_h * rect_w:
            continue
        rect_i = randint(ZERO, h - rect_h)
        rect_j = randint(ZERO, w - rect_w)
        rect_box = (rect_i, rect_j, rect_h, rect_w)
        motif_boxes = _sample_boxes_414297c0(h, w, rect_box, n_targets + n_distractors)
        if motif_boxes is None:
            continue
        gi = canvas(ZERO, (h, w))
        go = canvas(bgc, (rect_h, rect_w))
        rect_patch = backdrop(frozenset({
            (rect_i, rect_j),
            (rect_i + rect_h - ONE, rect_j + rect_w - ONE),
        }))
        gi = fill(gi, bgc, rect_patch)
        for (ci, cj), color, mask in zip(centers, target_colors, target_masks):
            gi = fill(gi, color, frozenset({(rect_i + ci, rect_j + cj)}))
            go = fill(go, color, frozenset({(ci, cj)}))
            go = fill(go, TWO, shift(mask, (ci, cj)))
        for box, color, mask in zip(motif_boxes[:n_targets], target_colors, target_masks):
            bi, bj, _, _ = box
            center = (bi + ONE, bj + ONE)
            gi = fill(gi, TWO, shift(mask, center))
            gi = fill(gi, color, frozenset({center}))
        for box, color, mask in zip(motif_boxes[n_targets:], distractor_colors, distractor_masks):
            bi, bj, _, _ = box
            center = (bi + ONE, bj + ONE)
            gi = fill(gi, TWO, shift(mask, center))
            gi = fill(gi, color, frozenset({center}))
        if verify_414297c0(gi) != go:
            continue
        return {"input": gi, "output": go}
