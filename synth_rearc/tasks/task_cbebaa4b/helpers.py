from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass

from synth_rearc.core import *


@dataclass(frozen=True, slots=True)
class PieceCbebaa4b:
    color: Integer
    cells: frozenset[IntegerTuple]
    ports: frozenset[IntegerTuple]
    shape: IntegerTuple
    origin: IntegerTuple = ORIGIN


def _parse_piece_template_cbebaa4b(
    rows: tuple[str, ...],
) -> PieceCbebaa4b:
    cells = set()
    ports = set()
    values = set()
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            if value == ".":
                continue
            if value == "2":
                ports.add((i, j))
                continue
            values.add(int(value))
            cells.add((i, j))
    if len(values) != ONE:
        raise ValueError("piece templates must be single-color")
    return PieceCbebaa4b(
        color=next(iter(values)),
        cells=frozenset(cells),
        ports=frozenset(ports),
        shape=(len(rows), len(rows[ZERO])),
    )


TEMPLATE_PIECES_CBEBAA4B = {
    "arch8": _parse_piece_template_cbebaa4b(
        (
            "2...2",
            "88888",
            ".8.8.",
            ".8.8.",
            ".2.2.",
        )
    ),
    "frame1": _parse_piece_template_cbebaa4b(
        (
            "..2111.",
            ".....12",
            "2....1.",
            "1....1.",
            "1....12",
            "111111.",
        )
    ),
    "host_a": _parse_piece_template_cbebaa4b(
        (
            "2.2.",
            "444.",
            "4442",
            "444.",
            ".2..",
        )
    ),
    "hook5": _parse_piece_template_cbebaa4b(
        (
            "25555",
            "....5",
            "....5",
            "25555",
        )
    ),
    "arch3": _parse_piece_template_cbebaa4b(
        (
            "33333",
            "3...3",
            "2...2",
        )
    ),
    "u6": _parse_piece_template_cbebaa4b(
        (
            "666",
            "6.6",
            "6.6",
            "2.2",
        )
    ),
    "host_b": _parse_piece_template_cbebaa4b(
        (
            "..22.",
            ".444.",
            "24442",
            ".444.",
        )
    ),
    "hook3": _parse_piece_template_cbebaa4b(
        (
            "2..2",
            "3333",
            "3..3",
            "2..3",
            "...3",
            ".233",
        )
    ),
    "hook1": _parse_piece_template_cbebaa4b(
        (
            "2.2..",
            "11111",
            "1...1",
            "1...2",
            "1....",
            "112..",
        )
    ),
    "u8": _parse_piece_template_cbebaa4b(
        (
            "8888",
            "8..8",
            "2..2",
        )
    ),
    "big8": _parse_piece_template_cbebaa4b(
        (
            "......2.",
            "88888882",
            "8.....8.",
            "2.....8.",
            ".....28.",
        )
    ),
    "small8": _parse_piece_template_cbebaa4b(
        (
            "2.2",
            "8.8",
            "888",
        )
    ),
    "joint9": _parse_piece_template_cbebaa4b(
        (
            "99999",
            "9...9",
            "2...9",
            ".2999",
            "..2.2",
        )
    ),
    "host_c": _parse_piece_template_cbebaa4b(
        (
            ".2.....",
            ".444442",
            ".44444.",
            ".44444.",
            "244444.",
            "..2....",
        )
    ),
    "frame3": _parse_piece_template_cbebaa4b(
        (
            "3332..",
            "3....2",
            "3....3",
            "333333",
            ".2..2.",
        )
    ),
    "ladder1": _parse_piece_template_cbebaa4b(
        (
            ".2..2.",
            ".1..1.",
            ".1..1.",
            ".1..1.",
            "111111",
            "2....2",
        )
    ),
    "line7": _parse_piece_template_cbebaa4b(
        (
            "2....2",
            "777777",
        )
    ),
    "tall8": _parse_piece_template_cbebaa4b(
        (
            "2....",
            "88882",
            "8..8.",
            "8..82",
            "8..8.",
            "8..2.",
            "2....",
        )
    ),
    "host_d": _parse_piece_template_cbebaa4b(
        (
            "...2.",
            "2444.",
            ".444.",
            ".4442",
            "..2..",
        )
    ),
    "stem3": _parse_piece_template_cbebaa4b(
        (
            "3",
            "3",
            "3",
            "2",
        )
    ),
    "ring5": _parse_piece_template_cbebaa4b(
        (
            "555555",
            "5....5",
            "5....5",
            "55..55",
            ".2..2.",
        )
    ),
    "frame1_big": _parse_piece_template_cbebaa4b(
        (
            "..211",
            "2...1",
            "1...1",
            "1...1",
            "11111",
            "2...2",
        )
    ),
    "hook3_big": _parse_piece_template_cbebaa4b(
        (
            "..2..2.3",
            "23333333",
            ".......3",
            "23333333",
            ".......3",
        )
    ),
    "rect6": _parse_piece_template_cbebaa4b(
        (
            "2...2",
            "6...6",
            "6...6",
            "66666",
        )
    ),
}


ARCHETYPES_CBEBAA4B = (
    {
        "shape": (22, 22),
        "placements": (
            ("host_a", ORIGIN),
            ("arch3", (-6, -1)),
            ("arch8", (-4, -1)),
            ("frame1", (2, 1)),
            ("hook5", (3, 7)),
        ),
    },
    {
        "shape": (22, 22),
        "placements": (
            ("host_b", ORIGIN),
            ("u6", (-6, -2)),
            ("hook1", (-3, -2)),
            ("hook3", (-3, 3)),
            ("u8", (-5, 3)),
        ),
    },
    {
        "shape": (26, 26),
        "placements": (
            ("host_c", ORIGIN),
            ("big8", (-3, 1)),
            ("frame3", (4, -3)),
            ("ladder1", (8, -3)),
            ("line7", (13, -3)),
        ),
    },
)


def _shift_indices_cbebaa4b(
    indices: frozenset[IntegerTuple],
    offset: IntegerTuple,
) -> frozenset[IntegerTuple]:
    oi, oj = offset
    return frozenset((i + oi, j + oj) for i, j in indices)


def _piece_indices_cbebaa4b(
    piece: PieceCbebaa4b,
    loc: IntegerTuple,
) -> frozenset[IntegerTuple]:
    return _shift_indices_cbebaa4b(piece.cells | piece.ports, loc)


def _bbox_cbebaa4b(
    indices: frozenset[IntegerTuple] | set[IntegerTuple],
) -> tuple[Integer, Integer, Integer, Integer]:
    rows = tuple(i for i, _ in indices)
    cols = tuple(j for _, j in indices)
    return (min(rows), min(cols), max(rows), max(cols))


def _area_cbebaa4b(
    color_indices: frozenset[IntegerTuple],
    red_counts: Counter[IntegerTuple],
) -> Integer:
    x0 = color_indices | set(red_counts)
    r0, c0, r1, c1 = _bbox_cbebaa4b(x0)
    return (r1 - r0 + ONE) * (c1 - c0 + ONE)


def _render_from_positions_cbebaa4b(
    shape: IntegerTuple,
    pieces: tuple[PieceCbebaa4b, ...],
    positions: dict[Integer, IntegerTuple],
) -> Grid:
    h, w = shape
    grid = [[ZERO] * w for _ in range(h)]
    for idx, loc in positions.items():
        piece = pieces[idx]
        for i, j in _shift_indices_cbebaa4b(piece.ports, loc):
            grid[i][j] = TWO
        for i, j in _shift_indices_cbebaa4b(piece.cells, loc):
            grid[i][j] = piece.color
    return tuple(tuple(row) for row in grid)


def extract_pieces_cbebaa4b(
    grid: Grid,
) -> tuple[PieceCbebaa4b, ...]:
    h = len(grid)
    w = len(grid[ZERO])
    seen = [[False] * w for _ in range(h)]
    out = []
    for i in range(h):
        for j in range(w):
            value = grid[i][j]
            if value in (ZERO, TWO) or seen[i][j]:
                continue
            frontier = deque([(i, j)])
            seen[i][j] = True
            cells = []
            while frontier:
                x0, x1 = frontier.popleft()
                cells.append((x0, x1))
                for di, dj in ((-1, ZERO), (ONE, ZERO), (ZERO, -1), (ZERO, ONE)):
                    ni = x0 + di
                    nj = x1 + dj
                    if not (ZERO <= ni < h and ZERO <= nj < w):
                        continue
                    if seen[ni][nj] or grid[ni][nj] != value:
                        continue
                    seen[ni][nj] = True
                    frontier.append((ni, nj))
            ports = set()
            for x0, x1 in cells:
                for di, dj in ((-1, ZERO), (ONE, ZERO), (ZERO, -1), (ZERO, ONE)):
                    ni = x0 + di
                    nj = x1 + dj
                    if ZERO <= ni < h and ZERO <= nj < w and grid[ni][nj] == TWO:
                        ports.add((ni, nj))
            footprint = cells + list(ports)
            r0 = min(x0 for x0, _ in footprint)
            c0 = min(x1 for _, x1 in footprint)
            r1 = max(x0 for x0, _ in footprint)
            c1 = max(x1 for _, x1 in footprint)
            out.append(
                PieceCbebaa4b(
                    color=value,
                    cells=frozenset((x0 - r0, x1 - c0) for x0, x1 in cells),
                    ports=frozenset((x0 - r0, x1 - c0) for x0, x1 in ports),
                    shape=(r1 - r0 + ONE, c1 - c0 + ONE),
                    origin=(r0, c0),
                )
            )
    return tuple(out)


def _host_index_cbebaa4b(
    pieces: tuple[PieceCbebaa4b, ...],
) -> Integer:
    def solid_rect(piece: PieceCbebaa4b) -> Boolean:
        rows = tuple(i for i, _ in piece.cells)
        cols = tuple(j for _, j in piece.cells)
        height = max(rows) - min(rows) + ONE
        width = max(cols) - min(cols) + ONE
        return len(piece.cells) == height * width

    candidates = tuple(idx for idx, piece in enumerate(pieces) if solid_rect(piece))
    if len(candidates) == ZERO:
        raise ValueError("missing host rectangle")
    return max(candidates, key=lambda idx: len(pieces[idx].cells))


def _pair_offsets_cbebaa4b(
    piece_a: PieceCbebaa4b,
    piece_b: PieceCbebaa4b,
) -> dict[IntegerTuple, Integer]:
    out = {}
    for ai, aj in piece_a.ports:
        for bi, bj in piece_b.ports:
            offset = (ai - bi, aj - bj)
            cells_b = _shift_indices_cbebaa4b(piece_b.cells, offset)
            ports_b = _shift_indices_cbebaa4b(piece_b.ports, offset)
            if len(cells_b & piece_a.cells) > ZERO:
                continue
            if len(cells_b & piece_a.ports) > ZERO:
                continue
            if len(ports_b & piece_a.cells) > ZERO:
                continue
            overlap = ports_b & piece_a.ports
            if len(overlap) == ZERO:
                continue
            prior = out.get(offset, ZERO)
            out[offset] = max(prior, len(overlap))
    return out


def _valid_add_cbebaa4b(
    pieces: tuple[PieceCbebaa4b, ...],
    idx: Integer,
    loc: IntegerTuple,
    shape: IntegerTuple,
    color_indices: frozenset[IntegerTuple],
    red_counts: Counter[IntegerTuple],
) -> tuple[Integer, frozenset[IntegerTuple], frozenset[IntegerTuple]] | None:
    piece = pieces[idx]
    h, w = shape
    cells = _shift_indices_cbebaa4b(piece.cells, loc)
    ports = _shift_indices_cbebaa4b(piece.ports, loc)
    occ = cells | ports
    if min(i for i, _ in occ) < ZERO or min(j for _, j in occ) < ZERO:
        return None
    if max(i for i, _ in occ) >= h or max(j for _, j in occ) >= w:
        return None
    red_indices = set(red_counts)
    if len(cells & color_indices) > ZERO:
        return None
    if len(cells & red_indices) > ZERO:
        return None
    if len(ports & color_indices) > ZERO:
        return None
    overlap = ports & red_indices
    if len(overlap) == ZERO:
        return None
    if any(red_counts[port] >= TWO for port in overlap):
        return None
    return (len(overlap), cells, ports)


def _search_positions_cbebaa4b(
    pieces: tuple[PieceCbebaa4b, ...],
    shape: IntegerTuple,
    *,
    exhaustive: Boolean,
) -> dict[Integer, IntegerTuple]:
    host_idx = _host_index_cbebaa4b(pieces)
    host_loc = pieces[host_idx].origin
    pair_offsets = {
        idx: {
            jdx: _pair_offsets_cbebaa4b(pieces[idx], pieces[jdx])
            for jdx in range(len(pieces))
            if idx != jdx
        }
        for idx in range(len(pieces))
    }
    start_colors = _shift_indices_cbebaa4b(pieces[host_idx].cells, host_loc)
    start_reds = Counter(_shift_indices_cbebaa4b(pieces[host_idx].ports, host_loc))
    start_positions = {host_idx: host_loc}
    remaining = tuple(idx for idx in range(len(pieces)) if idx != host_idx)
    best_overlap = -ONE
    best_area = 10 ** 9
    best_grid = None
    best_positions = None
    seen = {}

    def consider(positions, color_indices, red_counts, overlap_total):
        nonlocal best_overlap, best_area, best_grid, best_positions
        area = _area_cbebaa4b(color_indices, red_counts)
        grid = _render_from_positions_cbebaa4b(shape, pieces, positions)
        candidate = (overlap_total, -area, grid)
        current = None if best_grid is None else (best_overlap, -best_area, best_grid)
        if current is None or candidate > current:
            best_overlap = overlap_total
            best_area = area
            best_grid = grid
            best_positions = dict(positions)

    def rec(positions, color_indices, red_counts, rem, overlap_total):
        key = (
            tuple(sorted(positions.items())),
            rem,
            tuple(sorted(red_counts.items())),
        )
        prev = seen.get(key)
        if prev is not None and prev >= overlap_total:
            return
        seen[key] = overlap_total
        max_possible = overlap_total + sum(max(ONE, len(pieces[idx].ports)) for idx in rem)
        if max_possible < best_overlap:
            return
        if len(rem) == ZERO:
            consider(positions, color_indices, red_counts, overlap_total)
            return
        option_sets = []
        for idx in rem:
            posmap = {}
            for jdx, jloc in positions.items():
                for offset in pair_offsets[jdx][idx]:
                    loc = (jloc[ZERO] + offset[ZERO], jloc[ONE] + offset[ONE])
                    placed = _valid_add_cbebaa4b(
                        pieces,
                        idx,
                        loc,
                        shape,
                        color_indices,
                        red_counts,
                    )
                    if placed is None:
                        continue
                    overlap, _, _ = placed
                    prior = posmap.get(loc, ZERO)
                    posmap[loc] = max(prior, overlap)
            if len(posmap) == ZERO:
                continue
            ranked = tuple(sorted((( -n, loc) for loc, n in posmap.items())))
            option_sets.append(( -max(posmap.values()), len(posmap), idx, ranked))
        if len(option_sets) == ZERO:
            return
        option_sets.sort()
        choices = option_sets if exhaustive else option_sets[:ONE]
        for _, _, idx, ranked in choices:
            next_rem = tuple(jdx for jdx in rem if jdx != idx)
            for neg_overlap, loc in ranked:
                placed = _valid_add_cbebaa4b(
                    pieces,
                    idx,
                    loc,
                    shape,
                    color_indices,
                    red_counts,
                )
                if placed is None:
                    continue
                overlap, cells, ports = placed
                positions[idx] = loc
                next_reds = red_counts.copy()
                for port in ports:
                    next_reds[port] += ONE
                rec(
                    positions,
                    color_indices | cells,
                    next_reds,
                    next_rem,
                    overlap_total + overlap,
                )
                del positions[idx]
            if not exhaustive:
                break

    rec(start_positions, start_colors, start_reds, remaining, ZERO)
    if best_positions is None:
        raise ValueError("unable to assemble connector pieces")
    return best_positions


def assemble_output_cbebaa4b(
    grid: Grid,
) -> Grid:
    pieces = extract_pieces_cbebaa4b(grid)
    if len(pieces) < THREE:
        raise ValueError("expected at least three pieces")
    dims = (len(grid), len(grid[ZERO]))
    non_host = tuple(
        piece
        for idx, piece in enumerate(pieces)
        if idx != _host_index_cbebaa4b(pieces)
    )
    exhaustive = len(non_host) > FOUR or any(len(piece.ports) == ONE for piece in non_host)
    positions = _search_positions_cbebaa4b(pieces, dims, exhaustive=exhaustive)
    return _render_from_positions_cbebaa4b(dims, pieces, positions)


def _layout_bounds_cbebaa4b(
    layout: tuple[tuple[PieceCbebaa4b, IntegerTuple], ...],
) -> tuple[Integer, Integer, Integer, Integer]:
    cells = set()
    for piece, loc in layout:
        cells |= _piece_indices_cbebaa4b(piece, loc)
    return _bbox_cbebaa4b(cells)


def _translated_layout_cbebaa4b(
    archetype: dict[str, object],
    host_loc: IntegerTuple,
) -> tuple[tuple[PieceCbebaa4b, IntegerTuple], ...]:
    placements = []
    for name, rel in archetype["placements"]:
        piece = TEMPLATE_PIECES_CBEBAA4B[name]
        placements.append((piece, add(host_loc, rel)))
    return tuple(placements)


def choose_output_layout_cbebaa4b(
    diff_lb: float,
    diff_ub: float,
) -> tuple[IntegerTuple, tuple[tuple[PieceCbebaa4b, IntegerTuple], ...]]:
    if diff_ub < 0.35:
        archetype = ARCHETYPES_CBEBAA4B[ZERO]
    elif diff_lb > 0.65:
        archetype = choice((ARCHETYPES_CBEBAA4B[ONE], ARCHETYPES_CBEBAA4B[TWO]))
    else:
        archetype = choice(ARCHETYPES_CBEBAA4B)
    shape = archetype["shape"]
    raw_layout = tuple((TEMPLATE_PIECES_CBEBAA4B[name], rel) for name, rel in archetype["placements"])
    r0, c0, r1, c1 = _layout_bounds_cbebaa4b(raw_layout)
    lb_i = -r0
    ub_i = shape[ZERO] - r1 - ONE
    lb_j = -c0
    ub_j = shape[ONE] - c1 - ONE
    host_loc = (randint(lb_i, ub_i), randint(lb_j, ub_j))
    return (shape, _translated_layout_cbebaa4b(archetype, host_loc))


def _reserve_bbox_cbebaa4b(
    piece: PieceCbebaa4b,
    loc: IntegerTuple,
    shape: IntegerTuple,
    *,
    margin: Integer = ONE,
) -> frozenset[IntegerTuple]:
    h, w = shape
    occ = _piece_indices_cbebaa4b(piece, loc)
    r0, c0, r1, c1 = _bbox_cbebaa4b(occ)
    top = max(ZERO, r0 - margin)
    left = max(ZERO, c0 - margin)
    bottom = min(h - ONE, r1 + margin)
    right = min(w - ONE, c1 + margin)
    return frozenset((i, j) for i in range(top, bottom + ONE) for j in range(left, right + ONE))


def scatter_input_layout_cbebaa4b(
    shape: IntegerTuple,
    output_layout: tuple[tuple[PieceCbebaa4b, IntegerTuple], ...],
) -> tuple[tuple[PieceCbebaa4b, IntegerTuple], ...] | None:
    host_piece, host_loc = output_layout[ZERO]
    placements = [(host_piece, host_loc)]
    reserved = set(_reserve_bbox_cbebaa4b(host_piece, host_loc, shape, margin=TWO))
    remaining = list(output_layout[ONE:])
    remaining.sort(key=lambda item: len(item[ZERO].cells) + len(item[ZERO].ports), reverse=True)
    for piece, out_loc in remaining:
        candidates = []
        hi = shape[ZERO] - piece.shape[ZERO]
        hj = shape[ONE] - piece.shape[ONE]
        for i in range(hi + ONE):
            for j in range(hj + ONE):
                loc = (i, j)
                if loc == out_loc:
                    continue
                patch = _reserve_bbox_cbebaa4b(piece, loc, shape, margin=ONE)
                if len(patch & reserved) > ZERO:
                    continue
                candidates.append(loc)
        if len(candidates) == ZERO:
            return None
        loc = choice(tuple(candidates))
        placements.append((piece, loc))
        reserved |= _reserve_bbox_cbebaa4b(piece, loc, shape, margin=ONE)
    return tuple(placements)


def render_layout_cbebaa4b(
    shape: IntegerTuple,
    layout: tuple[tuple[PieceCbebaa4b, IntegerTuple], ...],
) -> Grid:
    grid = canvas(ZERO, shape)
    for piece, loc in layout:
        ports = shift(piece.ports, loc)
        cells = recolor(piece.color, shift(piece.cells, loc))
        grid = fill(grid, TWO, ports)
        grid = paint(grid, cells)
    return grid
