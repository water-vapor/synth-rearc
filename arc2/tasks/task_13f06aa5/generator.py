from arc2.core import *


SIDES_13f06aa5 = ("top", "bottom", "left", "right")
NONZERO_COLORS_13f06aa5 = remove(ZERO, interval(ZERO, TEN, ONE))
BODY_OFFSETS_13f06aa5 = {
    "top": (
        (ZERO, -TWO),
        (ZERO, -ONE),
        (ZERO, ONE),
        (ZERO, TWO),
        (ONE, -ONE),
        (ONE, ZERO),
        (ONE, ONE),
    ),
    "bottom": (
        (-ONE, -ONE),
        (-ONE, ZERO),
        (-ONE, ONE),
        (ZERO, -TWO),
        (ZERO, -ONE),
        (ZERO, ONE),
        (ZERO, TWO),
    ),
    "left": (
        (-TWO, ZERO),
        (-ONE, ZERO),
        (-ONE, ONE),
        (ZERO, ONE),
        (ONE, ZERO),
        (ONE, ONE),
        (TWO, ZERO),
    ),
    "right": (
        (-TWO, ZERO),
        (-ONE, -ONE),
        (-ONE, ZERO),
        (ZERO, -ONE),
        (ONE, -ONE),
        (ONE, ZERO),
        (TWO, ZERO),
    ),
}


def _shape_indices_13f06aa5(
    side: str,
    tip: IntegerTuple,
) -> Indices:
    i, j = tip
    return frozenset((i + di, j + dj) for di, dj in BODY_OFFSETS_13f06aa5[side]) | frozenset({tip})


def _shape_object_13f06aa5(
    side: str,
    tip: IntegerTuple,
    body: Integer,
    marker: Integer,
) -> Object:
    i, j = tip
    out = {(marker, tip)}
    for di, dj in BODY_OFFSETS_13f06aa5[side]:
        out.add((body, (i + di, j + dj)))
    return frozenset(out)


def _trace_cells_13f06aa5(
    side: str,
    tip: IntegerTuple,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    i, j = tip
    if side == "top":
        return frozenset((k, j) for k in range(i - TWO, ZERO, -TWO))
    if side == "bottom":
        return frozenset((k, j) for k in range(i + TWO, h - ONE, TWO))
    if side == "left":
        return frozenset((i, k) for k in range(j - TWO, ZERO, -TWO))
    return frozenset((i, k) for k in range(j + TWO, w - ONE, TWO))


def _border_cells_13f06aa5(
    side: str,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    if side == "top":
        return frozenset((ZERO, j) for j in range(w))
    if side == "bottom":
        return frozenset((h - ONE, j) for j in range(w))
    if side == "left":
        return frozenset((i, ZERO) for i in range(h))
    return frozenset((i, w - ONE) for i in range(h))


def _corner_cells_13f06aa5(
    sides: tuple[str, ...],
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    used = set(sides)
    out = set()
    if "top" in used and "left" in used:
        out.add((ZERO, ZERO))
    if "top" in used and "right" in used:
        out.add((ZERO, w - ONE))
    if "bottom" in used and "left" in used:
        out.add((h - ONE, ZERO))
    if "bottom" in used and "right" in used:
        out.add((h - ONE, w - ONE))
    return frozenset(out)


def _candidate_tips_13f06aa5(
    side: str,
    dims: IntegerTuple,
) -> list[IntegerTuple]:
    h, w = dims
    if side in ("top", "bottom"):
        rows = range(TWO, h - TWO)
        cols = range(TWO, w - TWO)
        return [(i, j) for i in rows for j in cols]
    rows = range(TWO, h - TWO)
    cols = range(TWO, w - TWO)
    return [(i, j) for i in rows for j in cols]


def _fits_13f06aa5(
    cells: Indices,
    dims: IntegerTuple,
) -> Boolean:
    h, w = dims
    return all(ZERO <= i < h and ZERO <= j < w for i, j in cells)


def _touches_shape_13f06aa5(
    cells: Indices,
    occupied: Indices,
) -> Boolean:
    for cell in cells:
        if cell in occupied:
            return T
        if any(nbr in occupied for nbr in dneighbors(cell)):
            return T
    return F


def _valid_tip_13f06aa5(
    side: str,
    tip: IntegerTuple,
    dims: IntegerTuple,
    specs: tuple[dict, ...],
    occupied_shapes: Indices,
    occupied_traces: Indices,
) -> Boolean:
    shape_cells = _shape_indices_13f06aa5(side, tip)
    trace_cells = _trace_cells_13f06aa5(side, tip, dims)
    if not _fits_13f06aa5(shape_cells, dims):
        return F
    if _touches_shape_13f06aa5(shape_cells, occupied_shapes):
        return F
    if shape_cells & occupied_traces:
        return F
    if trace_cells & occupied_shapes:
        return F
    if trace_cells & occupied_traces:
        return F
    if side in ("top", "bottom"):
        if any(spec["side"] in ("top", "bottom") and spec["tip"][ONE] == tip[ONE] for spec in specs):
            return F
    if side in ("left", "right"):
        if any(spec["side"] in ("left", "right") and spec["tip"][ZERO] == tip[ZERO] for spec in specs):
            return F
    return T


def _pick_sides_13f06aa5(
    diff_lb: float,
    diff_ub: float,
) -> tuple[str, ...]:
    n = unifint(diff_lb, diff_ub, (ONE, THREE))
    if n == ONE:
        return (choice(SIDES_13f06aa5),)
    if n == TWO:
        return tuple(sample(SIDES_13f06aa5, TWO))
    pools = (
        ("top", "left", "right"),
        ("bottom", "left", "right"),
        ("top", "bottom", "left"),
        ("top", "bottom", "right"),
    )
    return choice(pools)


def _render_output_13f06aa5(
    gi: Grid,
    specs: tuple[dict, ...],
    dims: IntegerTuple,
) -> Grid:
    go = gi
    for spec in specs:
        go = fill(go, spec["marker"], spec["trace"])
        go = fill(go, spec["marker"], spec["border"])
    return fill(go, ZERO, _corner_cells_13f06aa5(tuple(spec["side"] for spec in specs), dims))


def generate_13f06aa5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        sides = _pick_sides_13f06aa5(diff_lb, diff_ub)
        hmin = 13 if len(sides) == THREE or ("top" in sides and "bottom" in sides) else 11
        wmin = 13 if len(sides) == THREE or ("left" in sides and "right" in sides) else 11
        h = unifint(diff_lb, diff_ub, (hmin, 18))
        w = unifint(diff_lb, diff_ub, (wmin, 18))
        dims = (h, w)
        colors = sample(NONZERO_COLORS_13f06aa5, len(sides) + TWO)
        bg = colors[ZERO]
        body = colors[ONE]
        markers = colors[TWO:]
        specs = []
        occupied_shapes = frozenset()
        occupied_traces = frozenset()
        failed = F
        for side, marker in zip(sides, markers):
            candidates = _candidate_tips_13f06aa5(side, dims)
            shuffle(candidates)
            tip = None
            for candidate in candidates:
                if _valid_tip_13f06aa5(
                    side,
                    candidate,
                    dims,
                    tuple(specs),
                    occupied_shapes,
                    occupied_traces,
                ):
                    tip = candidate
                    break
            if tip is None:
                failed = T
                break
            shape_obj = _shape_object_13f06aa5(side, tip, body, marker)
            shape_cells = toindices(shape_obj)
            trace_cells = _trace_cells_13f06aa5(side, tip, dims)
            border_cells = _border_cells_13f06aa5(side, dims)
            specs.append(
                {
                    "side": side,
                    "tip": tip,
                    "marker": marker,
                    "shape": shape_obj,
                    "trace": trace_cells,
                    "border": border_cells,
                }
            )
            occupied_shapes = occupied_shapes | shape_cells
            occupied_traces = occupied_traces | trace_cells
        if failed:
            continue
        gi = canvas(bg, dims)
        for spec in specs:
            gi = paint(gi, spec["shape"])
        go = _render_output_13f06aa5(gi, tuple(specs), dims)
        if colorcount(gi, ZERO) != ZERO:
            continue
        if len(specs) == ZERO:
            continue
        if size(objects(gi, F, F, T)) != len(specs):
            continue
        if leastcolor(gi) == ZERO:
            continue
        if colorcount(go, ZERO) == ZERO and len(specs) >= TWO and not (
            ("top" in sides or "bottom" in sides) and ("left" in sides or "right" in sides)
        ):
            continue
        return {"input": gi, "output": go}
