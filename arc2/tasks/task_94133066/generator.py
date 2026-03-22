from arc2.core import *


COLOR_POOL_94133066 = (TWO, THREE, FOUR, FIVE, EIGHT)
SYMMETRIES_94133066 = (rot90, rot180, rot270, dmirror, cmirror, hmirror, vmirror)
RELATIONS_94133066 = (
    ("above", "left"),
    ("above", None),
    ("above", "right"),
    (None, "left"),
    (None, "right"),
    ("below", "left"),
    ("below", None),
    ("below", "right"),
)
CORNERS_94133066 = ("tl", "tr", "bl", "br")


def _corner_positions_94133066(h: int, w: int) -> dict[str, IntegerTuple]:
    return {
        "tl": (ONE, ONE),
        "tr": (ONE, w - TWO),
        "bl": (h - TWO, ONE),
        "br": (h - TWO, w - TWO),
    }


def _sample_motif_94133066(
    h: int,
    w: int,
    blocked: set[IntegerTuple],
    diff_lb: float,
    diff_ub: float,
) -> Indices:
    cells = [
        (i, j)
        for i in range(TWO, h - TWO)
        for j in range(TWO, w - TWO)
        if (i, j) not in blocked
    ]
    target_hi = min(16, max(8, len(cells) // 3))
    for _ in range(200):
        target = unifint(diff_lb, diff_ub, (8, target_hi))
        start = choice(cells)
        motif = {start}
        frontier = [start]
        while len(motif) < target:
            sources = list(frontier if frontier and randint(0, 4) < 3 else motif)
            shuffle(sources)
            grown = False
            for source in sources:
                neighbors = list(dneighbors(source))
                shuffle(neighbors)
                for cell in neighbors:
                    i, j = cell
                    if not (TWO <= i < h - TWO and TWO <= j < w - TWO):
                        continue
                    if cell in blocked or cell in motif:
                        continue
                    motif.add(cell)
                    frontier.append(cell)
                    grown = True
                    break
                if grown:
                    break
            if not grown:
                break
        if len(motif) < max(7, target - 3):
            continue
        accent_target = randint(1, max(1, len(motif) // 4))
        motif_list = list(motif)
        shuffle(motif_list)
        for source in motif_list:
            if len(motif) >= target + accent_target:
                break
            neighbors = list(dneighbors(source))
            shuffle(neighbors)
            for cell in neighbors:
                i, j = cell
                if not (TWO <= i < h - TWO and TWO <= j < w - TWO):
                    continue
                if cell in blocked or cell in motif:
                    continue
                motif.add(cell)
                break
        motif = frozenset(motif)
        if both(height(motif) > ONE, width(motif) > ONE):
            return motif
    raise RuntimeError("failed to sample motif for 94133066")


def _marker_object_94133066(
    grid: Grid,
    marker_colors: tuple[int, int, int],
) -> Object:
    x0 = objects(grid, T, F, T)
    x1 = sizefilter(x0, ONE)
    x2 = compose(rbind(contained, marker_colors), color)
    x3 = sfilter(x1, x2)
    return merge(x3)


def _sample_layout_94133066(
    h: int,
    w: int,
    mh: int,
    mw: int,
    diff_lb: float,
    diff_ub: float,
) -> tuple[tuple[int, int], IntegerTuple, IntegerTuple]:
    for _ in range(200):
        gap = unifint(diff_lb, diff_ub, (2, 5))
        vertical, horizontal = choice(RELATIONS_94133066)
        min_h = max(h, mh) + 2
        min_w = max(w, mw) + 2
        if vertical is not None:
            min_h = max(min_h, h + mh + gap + 2)
        if horizontal is not None:
            min_w = max(min_w, w + mw + gap + 2)
        if min_h > 30 or min_w > 30:
            continue
        board_h = unifint(diff_lb, diff_ub, (max(18, min_h), 30))
        board_w = unifint(diff_lb, diff_ub, (max(18, min_w), 30))
        rect_i = randint(1, board_h - h - 1)
        rect_j = randint(1, board_w - w - 1)
        marker_i_lb = 1
        marker_i_ub = board_h - mh - 1
        marker_j_lb = 1
        marker_j_ub = board_w - mw - 1
        if vertical == "above":
            marker_i_ub = rect_i - mh - gap
        elif vertical == "below":
            marker_i_lb = rect_i + h + gap
        if horizontal == "left":
            marker_j_ub = rect_j - mw - gap
        elif horizontal == "right":
            marker_j_lb = rect_j + w + gap
        if marker_i_lb > marker_i_ub or marker_j_lb > marker_j_ub:
            continue
        marker_i = randint(marker_i_lb, marker_i_ub)
        marker_j = randint(marker_j_lb, marker_j_ub)
        return (board_h, board_w), (rect_i, rect_j), (marker_i, marker_j)
    raise RuntimeError("failed to place components for 94133066")


def generate_94133066(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (8, 13))
        w = unifint(diff_lb, diff_ub, (8, 13))
        missing_corner = choice(CORNERS_94133066)
        active_corners = tuple(
            corner for corner in CORNERS_94133066 if corner != missing_corner
        )
        chosen_colors = sample(COLOR_POOL_94133066, 4)
        marker_colors = tuple(chosen_colors[:3])
        motif_color = chosen_colors[3]
        corner_positions = _corner_positions_94133066(h, w)
        blocked = {corner_positions[corner] for corner in active_corners}
        motif = _sample_motif_94133066(h, w, blocked, diff_lb, diff_ub)
        crop = canvas(ONE, (h, w))
        for corner, color0 in zip(active_corners, marker_colors):
            crop = fill(crop, color0, {corner_positions[corner]})
        crop = fill(crop, motif_color, motif)
        transform = choice(SYMMETRIES_94133066)
        output = transform(crop)
        if output == crop:
            continue
        marker_object = normalize(_marker_object_94133066(output, marker_colors))
        mh, mw = shape(marker_object)
        dims, rect_ul, marker_ul = _sample_layout_94133066(
            h,
            w,
            mh,
            mw,
            diff_lb,
            diff_ub,
        )
        grid = canvas(ZERO, dims)
        grid = paint(grid, shift(asobject(crop), rect_ul))
        # The outside singleton markers are a translated copy of the output marker layout.
        grid = paint(grid, shift(marker_object, marker_ul))
        return {"input": grid, "output": output}
