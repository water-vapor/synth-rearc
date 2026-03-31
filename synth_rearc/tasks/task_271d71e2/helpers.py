from __future__ import annotations

from synth_rearc.core import *


BG_271D71E2 = SIX
BOX_BG_271D71E2 = ZERO
BASE_271D71E2 = FIVE
GROWTH_271D71E2 = SEVEN
MARKER_271D71E2 = NINE


def _bbox_271d71e2(
    cells: tuple[IntegerTuple, ...] | list[IntegerTuple],
) -> tuple[Integer, Integer, Integer, Integer]:
    rows = tuple(i for i, _ in cells)
    cols = tuple(j for _, j in cells)
    return min(rows), min(cols), max(rows), max(cols)


def _shape_from_bbox_271d71e2(
    bbox: tuple[Integer, Integer, Integer, Integer],
) -> tuple[Integer, Integer]:
    return (bbox[TWO] - bbox[ZERO] + ONE, bbox[THREE] - bbox[ONE] + ONE)


def _connected_nonbg_271d71e2(
    grid: Grid,
) -> tuple[tuple[IntegerTuple, ...], ...]:
    h, w = shape(grid)
    seen: set[IntegerTuple] = set()
    comps: list[tuple[IntegerTuple, ...]] = []
    for i in range(h):
        for j in range(w):
            loc = (i, j)
            if grid[i][j] == BG_271D71E2 or loc in seen:
                continue
            frontier = [loc]
            seen.add(loc)
            comp: list[IntegerTuple] = []
            while frontier:
                x0 = frontier.pop()
                comp.append(x0)
                for x1 in dneighbors(x0):
                    if x1 in seen:
                        continue
                    a, b = x1
                    if 0 <= a < h and 0 <= b < w and grid[a][b] != BG_271D71E2:
                        seen.add(x1)
                        frontier.append(x1)
            comps.append(tuple(comp))
    return tuple(comps)


def _interior_mask_271d71e2(
    grid: Grid,
    box_bbox: tuple[Integer, Integer, Integer, Integer],
) -> tuple[tuple[Integer, ...], ...]:
    r0, c0, r1, c1 = box_bbox
    return tuple(
        tuple(ONE if grid[i][j] == GROWTH_271D71E2 else ZERO for j in range(c0 + ONE, c1))
        for i in range(r0 + ONE, r1)
    )


def _rot180_mask_271d71e2(
    mask: tuple[tuple[Integer, ...], ...],
) -> tuple[tuple[Integer, ...], ...]:
    return tuple(tuple(row[::-1]) for row in mask[::-1])


def _invert_mask_271d71e2(
    mask: tuple[tuple[Integer, ...], ...],
) -> tuple[tuple[Integer, ...], ...]:
    return tuple(tuple(ONE - value for value in row) for row in mask)


def side_rule_271d71e2(
    mask: tuple[tuple[Integer, ...], ...],
    side: str,
) -> tuple[tuple[Integer, ...], ...]:
    h, w = len(mask), len(mask[ZERO])
    n_growth = sum(sum(row) for row in mask)
    if n_growth == h * w:
        return mask
    if n_growth == ZERO:
        if h == ONE or w == ONE:
            return tuple(tuple(ONE for _ in range(w)) for _ in range(h))
        seed = [[ZERO] * w for _ in range(h)]
        seed[ZERO][ZERO if side == "left" else w - ONE] = ONE
        mask = tuple(tuple(row) for row in seed)
    return _invert_mask_271d71e2(_rot180_mask_271d71e2(mask))


def top_rule_271d71e2(
    mask: tuple[tuple[Integer, ...], ...],
) -> tuple[tuple[Integer, ...], ...]:
    h, w = len(mask), len(mask[ZERO])
    n_growth = sum(sum(row) for row in mask)
    if n_growth == h * w:
        return mask
    if w == ONE:
        return tuple((ONE,) for _ in range(h)) if n_growth > ZERO else tuple((ZERO,) for _ in range(h))
    if n_growth == ZERO:
        out = [[ZERO] * w for _ in range(h)]
        out[ZERO][ZERO] = ONE
        return tuple(tuple(row) for row in out)
    filled_rows = tuple(i for i, row in enumerate(mask) if any(row))
    r0 = filled_rows[-ONE]
    k0 = sum(mask[r0])
    out = [[ZERO] * w for _ in range(h)]
    for i in range(min(h, r0 + TWO)):
        for j in range(w):
            out[i][j] = ONE
    if r0 + TWO < h and k0 > ONE:
        for j in range(k0 - ONE):
            out[r0 + TWO][j] = ONE
    return tuple(tuple(row) for row in out)


def bottom_rule_271d71e2(
    mask: tuple[tuple[Integer, ...], ...],
) -> tuple[tuple[Integer, ...], ...]:
    h, w = len(mask), len(mask[ZERO])
    n_growth = sum(sum(row) for row in mask)
    if n_growth == h * w:
        return mask
    if w == ONE:
        return tuple((ONE,) for _ in range(h)) if n_growth > ZERO else tuple((ZERO,) for _ in range(h))
    coords = tuple((i, j) for i, row in enumerate(mask) for j, value in enumerate(row) if value == ONE)
    if len(coords) == ONE and coords[ZERO] == (h - ONE, w - ONE):
        out = [[ONE] * w for _ in range(h)]
        for j in range(w - ONE):
            out[ZERO][j] = ZERO
        return tuple(tuple(row) for row in out)
    if n_growth == ZERO:
        out = [[ZERO] * w for _ in range(h)]
        out[h - ONE][w - ONE] = ONE
        return tuple(tuple(row) for row in out)
    filled_rows = tuple(i for i, row in enumerate(mask) if any(row))
    r0 = filled_rows[ZERO]
    k0 = sum(mask[r0])
    out = [[ZERO] * w for _ in range(h)]
    for i in range(max(ZERO, r0 - ONE), h):
        for j in range(w):
            out[i][j] = ONE
    if r0 - TWO >= ZERO:
        for j in range(max(ZERO, w - k0), w):
            out[r0 - TWO][j] = ONE
    return tuple(tuple(row) for row in out)


def interior_rule_271d71e2(
    mask: tuple[tuple[Integer, ...], ...],
    orientation: str,
) -> tuple[tuple[Integer, ...], ...]:
    if orientation == "left":
        return side_rule_271d71e2(mask, "left")
    if orientation == "right":
        return side_rule_271d71e2(mask, "right")
    if orientation == "top":
        return top_rule_271d71e2(mask)
    return bottom_rule_271d71e2(mask)


def _paint_box_271d71e2(
    grid: list[list[Integer]],
    box_bbox: tuple[Integer, Integer, Integer, Integer],
    interior_mask: tuple[tuple[Integer, ...], ...],
) -> None:
    r0, c0, r1, c1 = box_bbox
    for i in range(r0, r1 + ONE):
        for j in range(c0, c1 + ONE):
            if i in (r0, r1) or j in (c0, c1):
                grid[i][j] = BOX_BG_271D71E2
    for i in range(r0 + ONE, r1):
        for j in range(c0 + ONE, c1):
            grid[i][j] = GROWTH_271D71E2 if interior_mask[i - r0 - ONE][j - c0 - ONE] == ONE else BASE_271D71E2


def _paint_marker_271d71e2(
    grid: list[list[Integer]],
    marker_bbox: tuple[Integer, Integer, Integer, Integer],
) -> None:
    r0, c0, r1, c1 = marker_bbox
    for i in range(r0, r1 + ONE):
        for j in range(c0, c1 + ONE):
            grid[i][j] = MARKER_271D71E2


def _format_grid_271d71e2(
    grid: list[list[Integer]],
) -> Grid:
    return tuple(tuple(row) for row in grid)


def transform_grid_271d71e2(
    grid: Grid,
) -> Grid:
    h, w = shape(grid)
    out = [list(row) for row in canvas(BG_271D71E2, (h, w))]
    comps = _connected_nonbg_271d71e2(grid)
    attached: list[tuple[IntegerTuple, ...]] = []
    detached: list[tuple[IntegerTuple, ...]] = []
    for comp in comps:
        pal = frozenset(grid[i][j] for i, j in comp)
        if pal == frozenset({MARKER_271D71E2}):
            detached.append(comp)
        elif MARKER_271D71E2 in pal:
            attached.append(comp)
        else:
            for i, j in comp:
                out[i][j] = grid[i][j]
    detached_bboxes = tuple(_bbox_271d71e2(comp) for comp in detached)
    used_detached: set[Integer] = set()
    for comp in attached:
        marker_cells = tuple(cell for cell in comp if grid[cell[ZERO]][cell[ONE]] == MARKER_271D71E2)
        box_cells = tuple(cell for cell in comp if grid[cell[ZERO]][cell[ONE]] != MARKER_271D71E2)
        box_bbox = _bbox_271d71e2(box_cells)
        marker_bbox = _bbox_271d71e2(marker_cells)
        interior_mask = _interior_mask_271d71e2(grid, box_bbox)
        ih, iw = len(interior_mask), len(interior_mask[ZERO])
        n_growth = sum(sum(row) for row in interior_mask)
        if marker_bbox[TWO] < box_bbox[ZERO]:
            orientation = "top"
        elif marker_bbox[ZERO] > box_bbox[TWO]:
            orientation = "bottom"
        elif marker_bbox[THREE] < box_bbox[ONE]:
            orientation = "left"
        else:
            orientation = "right"
        out_marker_bbox = marker_bbox
        shift = (ZERO, ZERO)
        if n_growth != ih * iw:
            matched = None
            for det_idx, det_bbox in enumerate(detached_bboxes):
                if det_idx in used_detached:
                    continue
                if _shape_from_bbox_271d71e2(det_bbox) == _shape_from_bbox_271d71e2(marker_bbox):
                    matched = (det_idx, det_bbox)
                    break
            if matched is not None:
                det_idx, det_bbox = matched
                if orientation in ("left", "right") and ih == ONE:
                    if det_bbox[ONE] < marker_bbox[ONE]:
                        new_col = det_bbox[ONE] + TWO
                    else:
                        new_col = det_bbox[ONE] - TWO
                    out_marker_bbox = (marker_bbox[ZERO], new_col, marker_bbox[TWO], new_col)
                    shift = (ZERO, new_col - marker_bbox[ONE])
                elif orientation in ("top", "bottom") and iw == ONE:
                    if det_bbox[ZERO] < marker_bbox[ZERO]:
                        new_row = det_bbox[ZERO] + ONE
                    else:
                        new_row = det_bbox[ZERO] - ONE
                    out_marker_bbox = (new_row, marker_bbox[ONE], new_row, marker_bbox[THREE])
                    shift = (new_row - marker_bbox[ZERO], ZERO)
                else:
                    used_detached.add(det_idx)
                    out_marker_bbox = det_bbox
                    shift = (
                        det_bbox[ZERO] - marker_bbox[ZERO],
                        det_bbox[ONE] - marker_bbox[ONE],
                    )
            elif orientation == "top" and _shape_from_bbox_271d71e2(marker_bbox)[ZERO] > ONE:
                depth = _shape_from_bbox_271d71e2(marker_bbox)[ZERO]
                out_marker_bbox = (
                    marker_bbox[ZERO],
                    marker_bbox[ONE],
                    marker_bbox[ZERO],
                    marker_bbox[THREE],
                )
                shift = (-(depth - ONE), ZERO)
        _paint_marker_271d71e2(out, out_marker_bbox)
        out_box_bbox = (
            box_bbox[ZERO] + shift[ZERO],
            box_bbox[ONE] + shift[ONE],
            box_bbox[TWO] + shift[ZERO],
            box_bbox[THREE] + shift[ONE],
        )
        out_mask = interior_rule_271d71e2(interior_mask, orientation)
        _paint_box_271d71e2(out, out_box_bbox, out_mask)
    for det_idx, det_comp in enumerate(detached):
        if det_idx in used_detached:
            continue
        for i, j in det_comp:
            out[i][j] = MARKER_271D71E2
    return _format_grid_271d71e2(out)


def make_local_component_271d71e2(
    orientation: str,
    interior_mask: tuple[tuple[Integer, ...], ...],
    marker_thickness: Integer = ONE,
    detached_gap: Integer = ZERO,
    detached_mode: str = "none",
) -> dict:
    ih, iw = len(interior_mask), len(interior_mask[ZERO])
    bh, bw = ih + TWO, iw + TWO
    if orientation in ("left", "right"):
        mh, mw = bh, ONE
    else:
        mh, mw = marker_thickness, bw
    if orientation == "left":
        left_margin = mw + detached_gap + mw if detached_mode != "none" else mw
        total_h = bh
        total_w = left_margin + bw
        box_bbox = (ZERO, left_margin, bh - ONE, left_margin + bw - ONE)
        marker_bbox = (ZERO, left_margin - ONE, bh - ONE, left_margin - ONE)
        detached_bbox = (ZERO, ZERO, bh - ONE, ZERO) if detached_mode != "none" else None
    elif orientation == "right":
        total_h = bh
        total_w = bw + mw + (detached_gap + mw if detached_mode != "none" else ZERO)
        box_bbox = (ZERO, ZERO, bh - ONE, bw - ONE)
        marker_bbox = (ZERO, bw, bh - ONE, bw)
        detached_bbox = (
            ZERO,
            bw + ONE + detached_gap,
            bh - ONE,
            bw + ONE + detached_gap,
        ) if detached_mode != "none" else None
    elif orientation == "top":
        top_margin = mh + detached_gap + mh if detached_mode != "none" else mh
        total_h = top_margin + bh
        total_w = bw
        box_bbox = (top_margin, ZERO, top_margin + bh - ONE, bw - ONE)
        marker_bbox = (top_margin - mh, ZERO, top_margin - ONE, bw - ONE)
        detached_bbox = (ZERO, ZERO, mh - ONE, bw - ONE) if detached_mode != "none" else None
    else:
        total_h = bh + mh + (detached_gap + mh if detached_mode != "none" else ZERO)
        total_w = bw
        box_bbox = (ZERO, ZERO, bh - ONE, bw - ONE)
        marker_bbox = (bh, ZERO, bh + mh - ONE, bw - ONE)
        detached_bbox = (
            bh + mh + detached_gap,
            ZERO,
            bh + TWO * mh + detached_gap - ONE,
            bw - ONE,
        ) if detached_mode != "none" else None
    input_grid = [list(row) for row in canvas(BG_271D71E2, (total_h, total_w))]
    output_grid = [list(row) for row in canvas(BG_271D71E2, (total_h, total_w))]
    _paint_box_271d71e2(input_grid, box_bbox, interior_mask)
    _paint_marker_271d71e2(input_grid, marker_bbox)
    if detached_bbox is not None:
        _paint_marker_271d71e2(input_grid, detached_bbox)
    n_growth = sum(sum(row) for row in interior_mask)
    out_marker_bbox = marker_bbox
    out_box_bbox = box_bbox
    keep_detached = detached_mode == "preserve" or n_growth == ih * iw
    if n_growth != ih * iw:
        if detached_mode == "consume" and detached_bbox is not None:
            out_marker_bbox = detached_bbox
            if orientation == "left":
                out_box_bbox = (
                    box_bbox[ZERO],
                    detached_bbox[THREE] + ONE,
                    box_bbox[TWO],
                    detached_bbox[THREE] + bw,
                )
            elif orientation == "right":
                out_box_bbox = (
                    box_bbox[ZERO],
                    detached_bbox[ONE] - bw,
                    box_bbox[TWO],
                    detached_bbox[ONE] - ONE,
                )
            elif orientation == "top":
                out_box_bbox = (
                    detached_bbox[TWO] + ONE,
                    box_bbox[ONE],
                    detached_bbox[TWO] + bh,
                    box_bbox[THREE],
                )
            else:
                out_box_bbox = (
                    detached_bbox[ZERO] - bh,
                    box_bbox[ONE],
                    detached_bbox[ZERO] - ONE,
                    box_bbox[THREE],
                )
            keep_detached = False
        elif detached_mode == "preserve" and detached_bbox is not None:
            if orientation == "left":
                out_marker_bbox = (marker_bbox[ZERO], detached_bbox[ONE] + TWO, marker_bbox[TWO], detached_bbox[ONE] + TWO)
                out_box_bbox = (
                    box_bbox[ZERO],
                    out_marker_bbox[ONE] + ONE,
                    box_bbox[TWO],
                    out_marker_bbox[ONE] + bw,
                )
            elif orientation == "right":
                out_marker_bbox = (marker_bbox[ZERO], detached_bbox[ONE] - TWO, marker_bbox[TWO], detached_bbox[ONE] - TWO)
                out_box_bbox = (
                    box_bbox[ZERO],
                    out_marker_bbox[ONE] - bw,
                    box_bbox[TWO],
                    out_marker_bbox[ONE] - ONE,
                )
            elif orientation == "top":
                out_marker_bbox = (detached_bbox[TWO] + ONE, marker_bbox[ONE], detached_bbox[TWO] + ONE, marker_bbox[THREE])
                out_box_bbox = (
                    out_marker_bbox[TWO] + ONE,
                    box_bbox[ONE],
                    out_marker_bbox[TWO] + bh,
                    box_bbox[THREE],
                )
            else:
                out_marker_bbox = (detached_bbox[ZERO] - ONE, marker_bbox[ONE], detached_bbox[ZERO] - ONE, marker_bbox[THREE])
                out_box_bbox = (
                    out_marker_bbox[ZERO] - bh,
                    box_bbox[ONE],
                    out_marker_bbox[ZERO] - ONE,
                    box_bbox[THREE],
                )
        elif orientation == "top" and marker_thickness > ONE:
            out_marker_bbox = (marker_bbox[ZERO], marker_bbox[ONE], marker_bbox[ZERO], marker_bbox[THREE])
            out_box_bbox = (
                box_bbox[ZERO] - (marker_thickness - ONE),
                box_bbox[ONE],
                box_bbox[TWO] - (marker_thickness - ONE),
                box_bbox[THREE],
            )
    _paint_box_271d71e2(output_grid, out_box_bbox, interior_rule_271d71e2(interior_mask, orientation))
    _paint_marker_271d71e2(output_grid, out_marker_bbox)
    if detached_bbox is not None and keep_detached:
        _paint_marker_271d71e2(output_grid, detached_bbox)
    return {
        "input": _format_grid_271d71e2(input_grid),
        "output": _format_grid_271d71e2(output_grid),
        "marker_shape": (mh, mw) if detached_mode != "none" else None,
    }


def overlay_patch_271d71e2(
    grid: list[list[Integer]],
    patch: Grid,
    offset: IntegerTuple,
) -> None:
    oi, oj = offset
    for i, row in enumerate(patch):
        for j, value in enumerate(row):
            if value != BG_271D71E2:
                grid[oi + i][oj + j] = value

