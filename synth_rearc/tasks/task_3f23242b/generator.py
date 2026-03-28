from synth_rearc.core import *


HEIGHT_BOUNDS_3F23242B = (10, 22)
WIDTH_BOUNDS_3F23242B = (10, 24)
MAX_MARKERS_3F23242B = THREE


def _sample_gap_extras_3f23242b(total: int, parts: int) -> tuple[int, ...]:
    gaps = [ZERO for _ in range(parts)]
    for _ in range(total):
        gaps[randint(ZERO, parts - ONE)] += ONE
    return tuple(gaps)


def _paint_motif_3f23242b(grid: Grid, center: tuple[int, int]) -> Grid:
    i, j = center
    top_bar = connect((i - TWO, j - TWO), (i - TWO, j + TWO))
    upper_stem = initset((i - ONE, j))
    left_side = connect((i - ONE, j - TWO), (i + ONE, j - TWO))
    right_side = connect((i - ONE, j + TWO), (i + ONE, j + TWO))
    bottom_row = hfrontier((i + TWO, ZERO))
    bottom_bar = connect((i + TWO, j - TWO), (i + TWO, j + TWO))
    grid = fill(grid, FIVE, top_bar)
    grid = fill(grid, FIVE, upper_stem)
    grid = fill(grid, TWO, left_side)
    grid = fill(grid, TWO, right_side)
    grid = fill(grid, TWO, bottom_row)
    grid = fill(grid, EIGHT, bottom_bar)
    grid = fill(grid, THREE, initset(center))
    return grid


def generate_3f23242b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, HEIGHT_BOUNDS_3F23242B)
        w = unifint(diff_lb, diff_ub, WIDTH_BOUNDS_3F23242B)
        max_markers = min(MAX_MARKERS_3F23242B, (h - TWO) // FIVE)
        if max_markers < ONE:
            continue
        nmarkers = unifint(diff_lb, diff_ub, (ONE, max_markers))
        extra_rows = h - FIVE * nmarkers - TWO
        if extra_rows < ZERO:
            continue
        gap_extras = _sample_gap_extras_3f23242b(extra_rows, nmarkers + ONE)
        tops = []
        top = ONE + gap_extras[ZERO]
        for idx in range(nmarkers):
            tops.append(top)
            if idx < nmarkers - ONE:
                top += FIVE + gap_extras[idx + ONE]
        centers = tuple((top + TWO, randint(THREE, w - FOUR)) for top in tops)
        gi = fill(canvas(ZERO, (h, w)), THREE, frozenset(centers))
        go = canvas(ZERO, (h, w))
        for center in centers:
            go = _paint_motif_3f23242b(go, center)
        if colorcount(gi, THREE) != nmarkers:
            continue
        if colorcount(go, THREE) != nmarkers:
            continue
        return {"input": gi, "output": go}
