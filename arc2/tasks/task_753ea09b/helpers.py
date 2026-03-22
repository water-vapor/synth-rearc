from __future__ import annotations

from collections import deque

from arc2.core import *


UPSCALE_753EA09B = THREE


def dominant_fill_color_753ea09b(
    grid: Grid,
) -> Integer:
    bg = mostcolor(grid)
    colors = tuple(color for color in palette(grid) if color != bg)
    return max(colors, key=lambda color: colorcount(grid, color))


def _neighbors8_753ea09b(
    loc: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    i, j = loc
    return tuple(
        (i + di, j + dj)
        for di in (-ONE, ZERO, ONE)
        for dj in (-ONE, ZERO, ONE)
        if not (di == ZERO and dj == ZERO)
    )


def largest_two_eight_components_753ea09b(
    cells: Indices,
) -> tuple[Indices, Indices]:
    source = set(cells)
    seen = set()
    comps: list[Indices] = []
    for cell in sorted(source):
        if cell in seen:
            continue
        comp = {cell}
        frontier = [cell]
        seen.add(cell)
        while frontier:
            loc = frontier.pop()
            for nloc in _neighbors8_753ea09b(loc):
                if nloc in source and nloc not in seen:
                    seen.add(nloc)
                    frontier.append(nloc)
                    comp.add(nloc)
        comps.append(frozenset(comp))
    comps.sort(key=len, reverse=True)
    return tuple(comps[:TWO])  # type: ignore[return-value]


def endpoints_753ea09b(
    component: Indices,
) -> tuple[IntegerTuple, IntegerTuple]:
    ends = []
    for cell in sorted(component):
        degree = sum(nloc in component for nloc in _neighbors8_753ea09b(cell))
        if degree == ONE:
            ends.append(cell)
    if len(ends) >= TWO:
        return ends[ZERO], ends[ONE]
    ordered = tuple(sorted(component))
    return ordered[ZERO], ordered[-ONE]


def perimeter_cycle_753ea09b(
    dims: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    h, w = dims
    out = [(ZERO, j) for j in range(w)]
    out.extend((i, w - ONE) for i in range(ONE, h))
    out.extend((h - ONE, j) for j in range(w - TWO, -ONE, -ONE))
    out.extend((i, ZERO) for i in range(h - TWO, ZERO, -ONE))
    return tuple(out)


def adjacent_endpoint_arcs_753ea09b(
    components: tuple[Indices, Indices],
    dims: IntegerTuple,
) -> tuple[Indices, Indices]:
    cycle = perimeter_cycle_753ea09b(dims)
    where = {cell: idx for idx, cell in enumerate(cycle)}
    labeled = []
    for label, component in enumerate(components):
        x0, x1 = endpoints_753ea09b(component)
        labeled.append((where[x0], x0, label))
        labeled.append((where[x1], x1, label))
    labeled.sort()
    ncycle = len(cycle)
    arcs = []
    for idx, (ia, a, la) in enumerate(labeled):
        ib, b, lb = labeled[(idx + ONE) % len(labeled)]
        if la == lb:
            continue
        patch = set()
        cur = ia
        while True:
            patch.add(cycle[cur])
            if cur == ib:
                break
            cur = (cur + ONE) % ncycle
        arcs.append(frozenset(patch))
    return tuple(arcs[:TWO])  # type: ignore[return-value]


def enclosed_cells_753ea09b(
    barrier: Indices,
    dims: IntegerTuple,
) -> Indices:
    h, w = dims
    scale = UPSCALE_753EA09B
    hh, ww = h * scale + TWO, w * scale + TWO
    blocked = [[False] * ww for _ in range(hh)]
    for i, j in barrier:
        bi = ONE + i * scale
        bj = ONE + j * scale
        for di in range(scale):
            for dj in range(scale):
                blocked[bi + di][bj + dj] = True
    seen = {(ZERO, ZERO)}
    frontier = deque([(ZERO, ZERO)])
    while frontier:
        i, j = frontier.popleft()
        for di, dj in (DOWN, UP, RIGHT, LEFT):
            ni, nj = i + di, j + dj
            if not (ZERO <= ni < hh and ZERO <= nj < ww):
                continue
            if blocked[ni][nj] or (ni, nj) in seen:
                continue
            seen.add((ni, nj))
            frontier.append((ni, nj))
    center = scale // TWO
    inside = set()
    for i in range(h):
        for j in range(w):
            loc = (ONE + i * scale + center, ONE + j * scale + center)
            if loc not in seen:
                inside.add((i, j))
    return frozenset(inside)
