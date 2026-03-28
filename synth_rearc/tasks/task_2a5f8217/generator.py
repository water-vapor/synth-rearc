from itertools import combinations

from synth_rearc.core import *


COLORS_2A5F8217 = (TWO, THREE, FOUR, SIX, SEVEN, EIGHT, NINE)


def _is_connected_2a5f8217(patch: Patch) -> bool:
    cells = tuple(toindices(patch))
    seen = {cells[0]}
    stack = [cells[0]]
    while len(stack) > 0:
        loc = stack.pop()
        for nei in dneighbors(loc):
            if nei in patch and nei not in seen:
                seen.add(nei)
                stack.append(nei)
    return len(seen) == len(cells)


def _build_shape_library_2a5f8217() -> Tuple:
    cells = tuple(product(interval(ZERO, THREE, ONE), interval(ZERO, THREE, ONE)))
    shapes = set()
    for n_cells in range(2, 7):
        for subset in combinations(cells, n_cells):
            patch = frozenset(subset)
            if not _is_connected_2a5f8217(patch):
                continue
            if height(patch) > THREE or width(patch) > THREE:
                continue
            if both(equality(len(patch), multiply(height(patch), width(patch))), greater(len(patch), TWO)):
                continue
            if both(either(hline(patch), vline(patch)), greater(len(patch), TWO)):
                continue
            shapes.add(toindices(normalize(patch)))
    return tuple(sorted(shapes, key=lambda shp: (len(shp), height(shp), width(shp), tuple(sorted(shp)))))


def _clipped_halo_2a5f8217(patch: Patch, side: Integer) -> FrozenSet[IntegerTuple]:
    cells = set()
    for i, j in toindices(patch):
        cells.add((i, j))
        for a, b in dneighbors((i, j)):
            if 0 <= a < side and 0 <= b < side:
                cells.add((a, b))
    return frozenset(cells)


def _placements_2a5f8217(
    shape: Patch,
    side: Integer,
    blocked: FrozenSet[IntegerTuple],
) -> Tuple:
    h = height(shape)
    w = width(shape)
    out = []
    for i in range(side - h + 1):
        for j in range(side - w + 1):
            placed = shift(shape, (i, j))
            halo = _clipped_halo_2a5f8217(placed, side)
            if len(halo & blocked) == 0:
                out.append(placed)
    return tuple(out)


SHAPE_LIBRARY_2A5F8217 = _build_shape_library_2a5f8217()


def generate_2a5f8217(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    n_pairs = unifint(diff_lb, diff_ub, (ONE, FIVE))
    side = max(SIX, add(multiply(TWO, n_pairs), THREE))
    motif_pool = tuple(
        motif for motif in SHAPE_LIBRARY_2A5F8217
        if len(motif) <= branch(greater(n_pairs, THREE), FIVE, SIX)
    )
    while True:
        shape = astuple(side, side)
        gi = canvas(ZERO, shape)
        go = canvas(ZERO, shape)
        blocked = frozenset()
        motifs = sample(motif_pool, n_pairs)
        motifs = tuple(sorted(motifs, key=lambda shp: (-len(shp), -height(shp), -width(shp))))
        colors = tuple(choice(COLORS_2A5F8217) for _ in range(n_pairs))
        success = True
        for motif, value in zip(motifs, colors):
            x0 = _placements_2a5f8217(motif, side, blocked)
            if len(x0) < 2:
                success = False
                break
            x1 = None
            x3 = ()
            for _ in range(12):
                x1 = choice(x0)
                x2 = blocked | _clipped_halo_2a5f8217(x1, side)
                x3 = _placements_2a5f8217(motif, side, x2)
                if len(x3) > 0:
                    break
            if len(x3) == 0:
                success = False
                break
            x2 = blocked | _clipped_halo_2a5f8217(x1, side)
            x4 = choice(x3)
            blocked = x2 | _clipped_halo_2a5f8217(x4, side)
            if choice((T, F)):
                ref_patch, qry_patch = x1, x4
            else:
                ref_patch, qry_patch = x4, x1
            x5 = recolor(value, ref_patch)
            x6 = recolor(ONE, qry_patch)
            x7 = recolor(value, qry_patch)
            gi = paint(gi, x5)
            gi = paint(gi, x6)
            go = paint(go, x5)
            go = paint(go, x7)
        if not success:
            continue
        return {"input": gi, "output": go}
