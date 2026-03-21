from arc2.core import *


def _bbox_cells(top: int, left: int, height0: int, width0: int) -> frozenset[tuple[int, int]]:
    return frozenset(
        (i, j)
        for i in range(top, top + height0)
        for j in range(left, left + width0)
    )


def _expanded_cells(
    top: int,
    left: int,
    height0: int,
    width0: int,
    pad: int,
    shape0: tuple[int, int],
) -> frozenset[tuple[int, int]]:
    h, w = shape0
    return frozenset(
        (i, j)
        for i in range(max(ZERO, top - pad), min(h, top + height0 + pad))
        for j in range(max(ZERO, left - pad), min(w, left + width0 + pad))
    )


def _connected(indices: frozenset[tuple[int, int]]) -> bool:
    if len(indices) == ZERO:
        return False
    pending = {next(iter(indices))}
    seen = set()
    while len(pending) > ZERO:
        loc = pending.pop()
        if loc in seen:
            continue
        seen.add(loc)
        pending |= {
            nbr for nbr in dneighbors(loc) if nbr in indices and nbr not in seen
        }
    return len(seen) == len(indices)


def _sample_holes(
    rect: tuple[int, int, int, int],
    force_border: bool,
) -> frozenset[tuple[int, int]] | None:
    top, left, height0, width0 = rect
    cells = tuple(_bbox_cells(top, left, height0, width0))
    border = tuple(
        (i, j)
        for i, j in cells
        if i in (top, top + height0 - ONE) or j in (left, left + width0 - ONE)
    )
    area = height0 * width0
    lo = ONE if area <= 24 else TWO
    hi = min(max(lo, area // 4), max(TWO, area // 6 + TWO))
    for _ in range(200):
        nholes = randint(lo, hi)
        holes = set(sample(cells, nholes))
        if force_border and not any(loc in holes for loc in border):
            continue
        greens = frozenset(set(cells) - holes)
        if not _connected(greens):
            continue
        rows = tuple(i for i, _ in greens)
        cols = tuple(j for _, j in greens)
        if min(rows) != top or max(rows) != top + height0 - ONE:
            continue
        if min(cols) != left or max(cols) != left + width0 - ONE:
            continue
        return frozenset(holes)
    return None


def _halo(centers: frozenset[tuple[int, int]], shape0: tuple[int, int]) -> frozenset[tuple[int, int]]:
    h, w = shape0
    return frozenset(
        (i, j)
        for loc in centers
        for i, j in neighbors(loc)
        if 0 <= i < h and 0 <= j < w
    )


def _render_scene(
    shape0: tuple[int, int],
    rectangles: tuple[tuple[int, int, int, int], ...],
    holesets: tuple[frozenset[tuple[int, int]], ...],
    noise: frozenset[tuple[int, int]],
) -> dict:
    gi = canvas(ZERO, shape0)
    all_holes = frozenset()
    for rect, holes in zip(rectangles, holesets):
        top, left, height0, width0 = rect
        cells = _bbox_cells(top, left, height0, width0)
        gi = fill(gi, THREE, cells)
        gi = fill(gi, TWO, holes)
        all_holes = all_holes | holes
    gi = fill(gi, TWO, noise)
    go = fill(gi, ONE, _halo(all_holes, shape0) - all_holes)
    return {"input": gi, "output": go}


def generate_a04b2602(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height0 = unifint(diff_lb, diff_ub, (10, 20))
        width0 = unifint(diff_lb, diff_ub, (16, 28))
        shape0 = (height0, width0)
        nrects = choice((TWO, THREE, THREE))
        rectangles = []
        footprint = frozenset()
        for idx in range(nrects):
            placed = False
            for _ in range(200):
                rh = randint(4, min(10, height0))
                rw = randint(4, min(12, width0))
                top = randint(ZERO, height0 - rh)
                left = randint(ZERO, width0 - rw)
                rect = (top, left, rh, rw)
                pad = ONE if idx < nrects - ONE else ZERO
                zone = _expanded_cells(top, left, rh, rw, pad, shape0)
                if len(footprint & zone) > ZERO:
                    continue
                rectangles.append(rect)
                footprint = footprint | zone
                placed = True
                break
            if not placed:
                rectangles = []
                break
        if len(rectangles) != nrects:
            continue
        holesets = []
        border_holes = ZERO
        for rect in rectangles:
            holes = _sample_holes(rect, choice((True, False)))
            if holes is None:
                holesets = []
                break
            top, left, rh, rw = rect
            if any(
                i in (top, top + rh - ONE) or j in (left, left + rw - ONE)
                for i, j in holes
            ):
                border_holes += ONE
            holesets.append(holes)
        if len(holesets) != nrects:
            continue
        if border_holes == ZERO:
            continue
        rectcells = frozenset().union(*(_bbox_cells(*rect) for rect in rectangles))
        holecells = frozenset().union(*holesets)
        halo = _halo(holecells, shape0) - holecells
        near = frozenset().union(
            *(
                _expanded_cells(top, left, rh, rw, TWO, shape0) - _bbox_cells(top, left, rh, rw)
                for top, left, rh, rw in rectangles
            )
        )
        allcells = frozenset(
            (i, j) for i in range(height0) for j in range(width0)
        )
        overwrite_cands = tuple(halo - rectcells)
        stable_near_cands = tuple((near - halo) - rectcells)
        far_cands = tuple((allcells - near) - rectcells)
        nholes = len(holecells)
        nover = min(len(overwrite_cands), randint(ZERO, min(TWO, max(ONE, nholes // 4))))
        nnoise = randint(max(ONE, nholes // TWO), max(TWO, nholes + THREE))
        nstable = max(ZERO, nnoise - nover)
        nnear = min(len(stable_near_cands), randint(ZERO, nstable))
        nfar = min(len(far_cands), nstable - nnear)
        if nover + nnear + nfar == ZERO:
            continue
        noise = set(sample(overwrite_cands, nover)) if nover > ZERO else set()
        if nnear > ZERO:
            noise |= set(sample(stable_near_cands, nnear))
        if nfar > ZERO:
            noise |= set(sample(far_cands, nfar))
        scene = _render_scene(shape0, tuple(rectangles), tuple(holesets), frozenset(noise))
        if scene["input"] == scene["output"]:
            continue
        if numcolors(scene["input"]) != THREE:
            continue
        if numcolors(scene["output"]) != FOUR:
            continue
        if len(colorfilter(objects(scene["input"], T, F, F), THREE)) != nrects:
            continue
        return scene
