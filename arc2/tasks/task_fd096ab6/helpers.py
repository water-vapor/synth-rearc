from __future__ import annotations

from functools import lru_cache

from arc2.core import *


def _in_bounds_fd096ab6(
    patch: Indices,
    dims: tuple[Integer, Integer],
) -> Boolean:
    h, w = dims
    return all(ZERO <= i < h and ZERO <= j < w for i, j in patch)


def cover_anchors_fd096ab6(
    template: Indices,
    cells: Indices,
    dims: tuple[Integer, Integer],
    blocked: Indices = frozenset(),
) -> tuple[IntegerTuple, ...]:
    candidates = {}
    for cell in cells:
        for point in template:
            anchor = subtract(cell, point)
            if anchor in candidates:
                continue
            placed = shift(template, anchor)
            if not _in_bounds_fd096ab6(placed, dims):
                continue
            if len(intersection(placed, blocked)) > ZERO:
                continue
            covered = frozenset(loc for loc in placed if loc in cells)
            if len(covered) > ZERO:
                candidates[anchor] = covered
    if len(candidates) == ZERO:
        raise ValueError("no template placements cover the target cells")
    lookup = {
        cell: tuple(sorted(anchor for anchor, covered in candidates.items() if cell in covered))
        for cell in cells
    }

    @lru_cache(maxsize=None)
    def search(
        remaining_cells: tuple[IntegerTuple, ...],
    ) -> tuple[IntegerTuple, ...] | None:
        if len(remaining_cells) == ZERO:
            return ()
        remaining = frozenset(remaining_cells)
        pivot = min(remaining)
        best = None
        options = tuple(
            sorted(
                lookup[pivot],
                key=lambda anchor: (
                    -len(intersection(candidates[anchor], remaining)),
                    anchor,
                ),
            )
        )
        for anchor in options:
            uncovered = tuple(sorted(difference(remaining, candidates[anchor])))
            tail = search(uncovered)
            if tail is None:
                continue
            proposal = tuple(sorted((anchor,) + tail))
            if best is None or len(proposal) < len(best) or (
                len(proposal) == len(best) and proposal < best
            ):
                best = proposal
        return best

    result = search(tuple(sorted(cells)))
    if result is None:
        raise ValueError("failed to cover the target cells")
    return result


def completed_partition_fd096ab6(
    template: Indices,
    cells: Indices,
    value: Integer,
    dims: tuple[Integer, Integer],
    blocked: Indices = frozenset(),
) -> Object:
    anchors = cover_anchors_fd096ab6(template, cells, dims, blocked)
    pieces = frozenset(recolor(value, shift(template, anchor)) for anchor in anchors)
    return merge(pieces)
