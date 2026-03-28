from synth_rearc.core import *

from .verifier import verify_1da012fc


TEMPLATES_1DA012FC = (
    (
        "####",
        ".##.",
    ),
    (
        ".#.#.",
        "#####",
        ".#.#.",
    ),
    (
        ".##.",
        "####",
        ".##.",
    ),
    (
        ".#.",
        "###",
        ".#.",
    ),
    (
        "######",
        ".####.",
        "##..##",
    ),
    (
        ".###.",
        "#####",
        "#####",
        ".#.#.",
    ),
    (
        "#...#",
        "#####",
        ".###.",
        "##.##",
    ),
    (
        ".###.",
        "#.#.#",
        "..#..",
    ),
    (
        ".###.",
        "##.##",
        ".###.",
    ),
    (
        ".#..#.",
        "######",
        "..##..",
    ),
)


def _parse_template_1da012fc(
    rows: tuple[str, ...],
) -> Indices:
    cells = {(i, j) for i, row in enumerate(rows) for j, value in enumerate(row) if value == "#"}
    return frozenset(cells)


def _hmirror_patch_1da012fc(
    patch: Indices,
) -> Indices:
    w = max(j for _, j in patch)
    return frozenset((i, w - j) for i, j in patch)


def _vmirror_patch_1da012fc(
    patch: Indices,
) -> Indices:
    h = max(i for i, _ in patch)
    return frozenset((h - i, j) for i, j in patch)


def _variant_pool_1da012fc() -> tuple[Indices, ...]:
    variants = set()
    for rows in TEMPLATES_1DA012FC:
        patch = _parse_template_1da012fc(rows)
        for candidate in (patch, _hmirror_patch_1da012fc(patch), _vmirror_patch_1da012fc(patch), _vmirror_patch_1da012fc(_hmirror_patch_1da012fc(patch))):
            variants.add(normalize(candidate))
    return tuple(variants)


VARIANTS_1DA012FC = _variant_pool_1da012fc()


def _bbox_1da012fc(
    patch: Indices,
) -> tuple[int, int, int, int]:
    rows = tuple(i for i, _ in patch)
    cols = tuple(j for _, j in patch)
    return min(rows), min(cols), max(rows), max(cols)


def _expand_1da012fc(
    patch: Indices,
    dims: tuple[int, int],
    radius: int = 1,
) -> Indices:
    h, w = dims
    out = set()
    for i, j in patch:
        for di in range(-radius, radius + 1):
            for dj in range(-radius, radius + 1):
                ni, nj = i + di, j + dj
                if 0 <= ni < h and 0 <= nj < w:
                    out.add((ni, nj))
    return frozenset(out)


def _shift_indices_1da012fc(
    patch: Indices,
    offset: tuple[int, int],
) -> Indices:
    di, dj = offset
    return frozenset((i + di, j + dj) for i, j in patch)


def _marker_positions_1da012fc(
    nmarkers: int,
    box_h: int,
    box_w: int,
) -> tuple[tuple[int, int], ...] | None:
    for _ in range(50):
        ngroups = randint((nmarkers + 1) // 2, nmarkers)
        counts = [1] * ngroups
        for idx in sample(tuple(range(ngroups)), nmarkers - ngroups):
            counts[idx] = 2
        row_pool = tuple(range(1, box_h - 1))
        if len(row_pool) < ngroups:
            return None
        rows = sorted(sample(row_pool, ngroups))
        if ngroups > 1 and box_h >= 6:
            gaps = tuple(b - a for a, b in zip(rows, rows[1:]))
            if min(gaps) < 2:
                continue
        left_col = randint(1, max(1, box_w - 3))
        right_lb = min(box_w - 2, left_col + 2)
        right_ub = box_w - 2
        if right_lb > right_ub:
            continue
        right_col = randint(right_lb, right_ub)
        positions = []
        for row, count in zip(rows, counts):
            if count == 1:
                positions.append((row, choice((left_col, right_col))))
            else:
                positions.extend(((row, left_col), (row, right_col)))
        return tuple(sorted(positions))
    return None


def _shape_choices_1da012fc(
    nmarkers: int,
) -> tuple[Indices, ...]:
    if nmarkers <= len(VARIANTS_1DA012FC):
        return tuple(sample(VARIANTS_1DA012FC, nmarkers))
    return tuple(choice(VARIANTS_1DA012FC) for _ in range(nmarkers))


def _valid_anchor_1da012fc(
    patch: Indices,
    dims: tuple[int, int],
    blocked: Indices,
    col_lb: int,
    col_ub: int,
) -> tuple[tuple[int, int], ...]:
    h, w = dims
    _, _, patch_bottom, patch_right = _bbox_1da012fc(patch)
    out = []
    for i in range(h - patch_bottom):
        for j in range(col_lb, col_ub - patch_right + 1):
            shifted = _shift_indices_1da012fc(patch, (i, j))
            if len(intersection(shifted, blocked)) > 0:
                continue
            out.append((i, j))
    return tuple(out)


def _place_shapes_1da012fc(
    patches: tuple[Indices, ...],
    dims: tuple[int, int],
    blocked: Indices,
    col_lb: int,
    col_ub: int,
) -> tuple[Indices, ...] | None:
    placed = []
    reserved = blocked
    last_anchor = (-1, -1)
    for patch in patches:
        anchors = _valid_anchor_1da012fc(patch, dims, reserved, col_lb, col_ub)
        anchors = tuple(anchor for anchor in anchors if anchor > last_anchor)
        if len(anchors) == 0:
            return None
        if len(anchors) > 12:
            picks = sample(anchors, 12)
            anchor = min(picks, key=lambda ij: (ij[0], randint(0, 5), ij[1]))
        else:
            anchor = choice(anchors)
        shifted = _shift_indices_1da012fc(patch, anchor)
        placed.append(shifted)
        reserved = combine(reserved, _expand_1da012fc(shifted, dims))
        last_anchor = anchor
    return tuple(order(tuple(placed), ulcorner))


def generate_1da012fc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    colors = remove(ZERO, interval(ZERO, TEN, ONE))
    for _ in range(400):
        nmarkers = unifint(diff_lb, diff_ub, (THREE, FIVE))
        h = unifint(diff_lb, diff_ub, (14, 22))
        w = unifint(diff_lb, diff_ub, (20, 28))
        box_h = unifint(diff_lb, diff_ub, (nmarkers + 3, min(10, h - 3)))
        box_w = unifint(diff_lb, diff_ub, (6, min(8, w - 8)))
        legend_left = choice((T, F))
        box_i = randint(0, h - box_h)
        if legend_left:
            box_j = randint(1, max(1, min(3, w - box_w - 8)))
            col_lb = box_j + box_w + 2
            col_ub = w - 1
        else:
            box_j = randint(max(0, w - box_w - 4), w - box_w - 1)
            col_lb = 0
            col_ub = box_j - 2
        if col_ub - col_lb < 5:
            continue
        marker_positions = _marker_positions_1da012fc(nmarkers, box_h, box_w)
        if marker_positions is None:
            continue
        marker_colors = sample(remove(FIVE, colors), nmarkers + 1)
        placeholder = marker_colors[0]
        marker_colors = tuple(marker_colors[1:])
        patches = _shape_choices_1da012fc(nmarkers)
        box = backdrop(frozenset({(box_i, box_j), (box_i + box_h - 1, box_j + box_w - 1)}))
        placed = _place_shapes_1da012fc(patches, (h, w), _expand_1da012fc(box, (h, w)), col_lb, col_ub)
        if placed is None:
            continue
        gi = fill(canvas(ZERO, (h, w)), FIVE, box)
        for marker_color, (mi, mj) in zip(marker_colors, marker_positions):
            gi = fill(gi, marker_color, frozenset({(box_i + mi, box_j + mj)}))
        for patch in placed:
            gi = fill(gi, placeholder, patch)
        go = gi
        for marker_color, patch in zip(marker_colors, placed):
            go = fill(go, marker_color, patch)
        if gi == go:
            continue
        if verify_1da012fc(gi) != go:
            continue
        return {"input": gi, "output": go}
    raise RuntimeError("failed to generate 1da012fc example")
