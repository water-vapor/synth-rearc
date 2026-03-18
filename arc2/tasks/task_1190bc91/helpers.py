from arc2.core import *


TOP_LIKE_1190BC91 = (
    "top",
    "top_start",
    "top_end",
    "bottom",
    "bottom_start",
    "bottom_end",
)
CANONICAL_HORIZONTAL_BARS_1190BC91 = ("left", "top_start")
CANONICAL_VERTICAL_BARS_1190BC91 = ("top", "right_start")


def ordered_main_line_1190bc91(
    obj: Object,
) -> tuple[tuple[Integer, tuple[Integer, Integer]], ...]:
    return order(obj, last)


def horizontal_main_line_1190bc91(
    line: tuple[tuple[Integer, tuple[Integer, Integer]], ...],
) -> Boolean:
    return hline(toindices(frozenset(line)))


def paint_main_line_1190bc91(
    dims: tuple[Integer, Integer],
    line: tuple[tuple[Integer, tuple[Integer, Integer]], ...],
) -> Grid:
    h, w = dims
    horizontal = horizontal_main_line_1190bc91(line)
    out = canvas(ZERO, dims)
    for idx in range(len(line) - ONE, -ONE, -ONE):
        value, (i, j) = line[idx]
        patch = set()
        if horizontal:
            for r in range(h):
                d = abs(r - i)
                cols = (j - d, j + d) if idx <= ONE else (j + d,)
                for c in cols:
                    if ZERO <= c < w:
                        patch.add((r, c))
        else:
            for c in range(w):
                d = abs(c - j)
                rows = (i - d, i + d) if idx <= ONE else (i + d,)
                for r in rows:
                    if ZERO <= r < h:
                        patch.add((r, c))
        out = fill(out, value, frozenset(patch))
    return out


def bar_mask_name_1190bc91(
    bar: Patch,
    line: tuple[tuple[Integer, tuple[Integer, Integer]], ...],
) -> str:
    coords = tuple(loc for _, loc in line)
    horizontal = horizontal_main_line_1190bc91(line)
    rows = tuple(i for i, _ in toindices(bar))
    cols = tuple(j for _, j in toindices(bar))
    if horizontal:
        row = coords[ZERO][ZERO]
        left = coords[ZERO][ONE]
        right = coords[-ONE][ONE]
        center = sum(cols) / len(cols)
        if max(cols) < left:
            return "left"
        if min(cols) > right:
            return "right"
        if max(rows) < row:
            left_center = left + 0.5
            right_center = right - 0.5
            return "top_start" if abs(center - left_center) <= abs(center - right_center) else "top_end"
        if min(rows) > row:
            left_center = left + 0.5
            right_center = right - 0.5
            return "bottom_start" if abs(center - left_center) <= abs(center - right_center) else "bottom_end"
    else:
        col = coords[ZERO][ONE]
        top = coords[ZERO][ZERO]
        bottom = coords[-ONE][ZERO]
        center = sum(rows) / len(rows)
        if max(rows) < top:
            return "top"
        if min(rows) > bottom:
            return "bottom"
        if max(cols) < col:
            top_center = top + 0.5
            bottom_center = bottom - 0.5
            return "left_start" if abs(center - top_center) <= abs(center - bottom_center) else "left_end"
        if min(cols) > col:
            top_center = top + 0.5
            bottom_center = bottom - 0.5
            return "right_start" if abs(center - top_center) <= abs(center - bottom_center) else "right_end"
    raise ValueError("could not classify bar")


def bar_mask_1190bc91(
    dims: tuple[Integer, Integer],
    line: tuple[tuple[Integer, tuple[Integer, Integer]], ...],
    name: str,
) -> Indices:
    h, w = dims
    coords = tuple(loc for _, loc in line)
    horizontal = horizontal_main_line_1190bc91(line)
    patch = set()
    if horizontal:
        row = coords[ZERO][ZERO]
        left = coords[ZERO][ONE]
        right = coords[-ONE][ONE]
        for i in range(h):
            d = abs(i - row)
            if name == "left":
                bound = left - d
                for j in range(max(ZERO, bound)):
                    patch.add((i, j))
            elif name == "right":
                bound = right + d
                for j in range(bound + ONE, w):
                    patch.add((i, j))
            elif name == "top_start" and i < row:
                left_bound = left + ONE - d
                right_bound = left + d
                for j in range(max(ZERO, left_bound + ONE), min(w, right_bound)):
                    patch.add((i, j))
            elif name == "bottom_start" and i > row:
                left_bound = left + ONE - d
                right_bound = left + d
                for j in range(max(ZERO, left_bound + ONE), min(w, right_bound)):
                    patch.add((i, j))
            elif name == "top_end" and i < row:
                left_bound = right - d
                right_bound = right - ONE + d
                for j in range(max(ZERO, left_bound + ONE), min(w, right_bound)):
                    patch.add((i, j))
            elif name == "bottom_end" and i > row:
                left_bound = right - d
                right_bound = right - ONE + d
                for j in range(max(ZERO, left_bound + ONE), min(w, right_bound)):
                    patch.add((i, j))
    else:
        col = coords[ZERO][ONE]
        top = coords[ZERO][ZERO]
        bottom = coords[-ONE][ZERO]
        for i in range(h):
            if name == "left_start":
                bound = min(col - abs(i - top), col - abs(i - (top + ONE)))
                for j in range(max(ZERO, bound)):
                    patch.add((i, j))
            elif name == "right_start":
                bound = max(col + abs(i - top), col + abs(i - (top + ONE)))
                for j in range(bound + ONE, w):
                    patch.add((i, j))
            elif name == "left_end":
                bound = min(col - abs(i - bottom), col - abs(i - (bottom - ONE)))
                for j in range(max(ZERO, bound)):
                    patch.add((i, j))
            elif name == "right_end":
                bound = max(col + abs(i - bottom), col + abs(i - (bottom - ONE)))
                for j in range(bound + ONE, w):
                    patch.add((i, j))
            elif name == "top" and i < top:
                left_bound = col - (top - i)
                right_bound = col + (top - i)
                for j in range(max(ZERO, left_bound + ONE), min(w, right_bound)):
                    patch.add((i, j))
            elif name == "bottom" and i > bottom:
                left_bound = col - (i - bottom)
                right_bound = col + (i - bottom)
                for j in range(max(ZERO, left_bound + ONE), min(w, right_bound)):
                    patch.add((i, j))
    return frozenset(patch)


def segment_candidates_1190bc91(
    patch: Indices,
    horizontal: Boolean,
) -> tuple[Indices, ...]:
    cells = set(patch)
    out = []
    for i, j in sorted(patch):
        other = (i, j + ONE) if horizontal else (i + ONE, j)
        if other in cells:
            out.append(frozenset({(i, j), other}))
    return tuple(out)
