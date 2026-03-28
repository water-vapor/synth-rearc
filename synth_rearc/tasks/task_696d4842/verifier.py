from synth_rearc.core import *


def _trace_path_696d4842(
    cells: Indices,
) -> tuple[IntegerTuple, ...]:
    endpoints = tuple(
        sorted(
            cell
            for cell in cells
            if equality(size(intersection(dneighbors(cell), cells)), ONE)
        )
    )
    current = endpoints[ZERO]
    previous = None
    ordered = [current]
    while len(ordered) < len(cells):
        next_cells = tuple(
            sorted(
                nbr for nbr in intersection(dneighbors(current), cells)
                if nbr != previous
            )
        )
        if len(next_cells) == ZERO:
            break
        nxt = next_cells[ZERO]
        ordered.append(nxt)
        previous = current
        current = nxt
    return tuple(ordered)


def _gap_info_696d4842(
    ordered: tuple[IntegerTuple, ...],
    dot: IntegerTuple,
    occupied: Indices,
) -> tuple[tuple[IntegerTuple, ...], tuple[IntegerTuple, ...]] | None:
    endpoints = (ordered[ZERO], ordered[-ONE])
    for endpoint_index, endpoint in enumerate(endpoints):
        aligned = equality(endpoint[ZERO], dot[ZERO]) or equality(endpoint[ONE], dot[ONE])
        if not aligned:
            continue
        segment = tuple(
            sorted(
                connect(endpoint, dot),
                key=lambda cell: abs(cell[ZERO] - endpoint[ZERO]) + abs(cell[ONE] - endpoint[ONE]),
            )
        )
        if intersection(frozenset(segment), occupied) != frozenset({endpoint, dot}):
            continue
        gap_cells = tuple(cell for cell in segment if cell != endpoint and cell != dot)
        ordered_to_endpoint = ordered if endpoint_index == ONE else tuple(reversed(ordered))
        return ordered_to_endpoint, gap_cells
    return None


def verify_696d4842(I: Grid) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = tuple(sorted((x2 for x2 in x0 if equality(size(x2), ONE)), key=ulcorner))
    x2 = [x3 for x3 in x0 if greater(size(x3), ONE)]
    x3 = toindices(merge(x0))
    x4 = I
    for x5 in x1:
        x6 = first(toindices(x5))
        x7 = color(x5)
        for x8, x9 in enumerate(tuple(x2)):
            x10 = toindices(x9)
            x11 = _trace_path_696d4842(x10)
            x12 = _gap_info_696d4842(x11, x6, x3)
            if x12 is None:
                continue
            x13, x14 = x12
            x15 = color(x9)
            x16 = len(x14)
            x4 = fill(x4, x15, frozenset(x14))
            x4 = fill(x4, x7, frozenset(x13[:x16]))
            x2.pop(x8)
            break
    return x4
