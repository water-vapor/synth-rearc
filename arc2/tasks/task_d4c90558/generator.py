from arc2.core import *


PALETTE_D4C90558 = (ONE, TWO, THREE, FOUR, SIX, SEVEN, EIGHT)


def _frame_parts_d4c90558(
    ulc: IntegerTuple,
    dims: tuple[Integer, Integer],
    thickness: tuple[Integer, Integer, Integer, Integer],
) -> tuple[Indices, Indices]:
    outer_h, outer_w = dims
    top, bottom, left, right = thickness
    outer = backdrop(frozenset({ulc, add(ulc, (outer_h - ONE, outer_w - ONE))}))
    inner_ulc = add(ulc, (top, left))
    inner_lrc = add(ulc, (outer_h - bottom - ONE, outer_w - right - ONE))
    inner = backdrop(frozenset({inner_ulc, inner_lrc}))
    return difference(outer, inner), inner


def _object_spec_d4c90558(
    count: Integer,
    color_value: Integer,
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        hole_h = unifint(diff_lb, diff_ub, (THREE, EIGHT))
        if choice((T, T, F)):
            hole_w_lb = max(THREE, hole_h + ONE)
            hole_w = unifint(diff_lb, diff_ub, (hole_w_lb, min(16, hole_w_lb + 7)))
        else:
            hole_w = unifint(diff_lb, diff_ub, (THREE, 14))
        if hole_h * hole_w < count:
            continue

        top = ONE
        bottom = ONE
        left = ONE
        right = ONE
        nsides = choice((ZERO, ONE, ONE, TWO, TWO, THREE))
        for side in sample(("top", "bottom", "left", "right"), nsides):
            extra = choice((ONE, ONE, TWO))
            if side == "top":
                top = min(THREE, top + extra)
            elif side == "bottom":
                bottom = min(THREE, bottom + extra)
            elif side == "left":
                left = min(THREE, left + extra)
            else:
                right = min(THREE, right + extra)

        outer_h = hole_h + top + bottom
        outer_w = hole_w + left + right
        if outer_h > 14 or outer_w > 18:
            continue

        return {
            "count": count,
            "color": color_value,
            "hole_h": hole_h,
            "hole_w": hole_w,
            "outer_h": outer_h,
            "outer_w": outer_w,
            "thickness": (top, bottom, left, right),
        }


def _row_counts_d4c90558(nobjs: Integer) -> tuple[Integer, ...]:
    if nobjs == TWO:
        return choice(((ONE, ONE), (ONE, ONE), (TWO,)))
    if nobjs == THREE:
        return choice(((ONE, TWO), (TWO, ONE)))
    return (TWO, TWO)


def _arrange_rows_d4c90558(specs: list[dict], row_counts: tuple[Integer, ...]) -> list[list[dict]]:
    ordered = sorted(specs, key=lambda x0: (x0["outer_w"], x0["outer_h"]), reverse=True)
    if row_counts == (ONE, ONE):
        shuffle(ordered)
        return [[ordered[ZERO]], [ordered[ONE]]]
    if row_counts == (TWO,):
        shuffle(ordered)
        return [ordered]
    if row_counts == (ONE, TWO):
        rest = ordered[ONE:]
        shuffle(rest)
        return [[ordered[ZERO]], rest]
    if row_counts == (TWO, ONE):
        rest = ordered[ONE:]
        shuffle(rest)
        return [rest, [ordered[ZERO]]]
    row0 = [ordered[ZERO], ordered[-ONE]]
    row1 = ordered[ONE:-ONE]
    shuffle(row0)
    shuffle(row1)
    return [row0, row1]


def _place_rows_d4c90558(rows: list[list[dict]]) -> tuple[Integer, Integer, list[dict]] | None:
    row_specs = []
    total_h = ZERO
    for row in rows:
        band_h = max(item["outer_h"] for item in row) + choice((ZERO, ZERO, ONE, TWO))
        row_gap = ZERO if row is rows[-ONE] else choice((ONE, TWO, TWO, THREE, FOUR))
        widths = [item["outer_w"] for item in row]
        min_gap = ZERO
        if len(row) == TWO:
            min_gap = choice((TWO, THREE, FOUR, FIVE, SIX))
        min_w = sum(widths) + min_gap
        row_specs.append(
            {
                "items": row,
                "band_h": band_h,
                "row_gap": row_gap,
                "min_gap": min_gap,
                "min_w": min_w,
            }
        )
        total_h += band_h + row_gap

    top_margin = choice((ZERO, ZERO, ONE, TWO))
    bottom_margin = choice((ZERO, ZERO, ONE, TWO))
    grid_h = max(18, total_h + top_margin + bottom_margin)
    grid_w = max(18, max(row["min_w"] for row in row_specs) + choice((ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX)))
    if grid_h > 30 or grid_w > 30:
        return None

    placed = []
    row_top = top_margin
    for row_spec in row_specs:
        items = row_spec["items"]
        band_h = row_spec["band_h"]
        slack_h = band_h - max(item["outer_h"] for item in items)
        min_w = row_spec["min_w"]
        slack_w = grid_w - min_w
        if len(items) == ONE:
            left_margin = randint(ZERO, slack_w)
            item = items[ZERO]
            top_offset = randint(ZERO, slack_h)
            placed.append(
                {
                    **item,
                    "ulc": (row_top + top_offset, left_margin),
                }
            )
        else:
            left_margin = randint(ZERO, slack_w)
            slack_w -= left_margin
            extra_gap = randint(ZERO, slack_w)
            gap = row_spec["min_gap"] + extra_gap
            item0, item1 = items
            top_offset0 = randint(ZERO, band_h - item0["outer_h"])
            top_offset1 = randint(ZERO, band_h - item1["outer_h"])
            ulc0 = (row_top + top_offset0, left_margin)
            ulc1 = (row_top + top_offset1, left_margin + item0["outer_w"] + gap)
            placed.append({**item0, "ulc": ulc0})
            placed.append({**item1, "ulc": ulc1})
        row_top += band_h + row_spec["row_gap"]

    return grid_h, grid_w, placed


def generate_d4c90558(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        nobjs = unifint(diff_lb, diff_ub, (TWO, FOUR))
        counts = tuple(sorted(sample(tuple(interval(TWO, TEN, ONE)), nobjs)))
        colors = sample(PALETTE_D4C90558, nobjs)
        specs = [
            _object_spec_d4c90558(count, color_value, diff_lb, diff_ub)
            for count, color_value in zip(counts, colors)
        ]
        rows = _arrange_rows_d4c90558(specs, _row_counts_d4c90558(nobjs))
        placed_layout = _place_rows_d4c90558(rows)
        if placed_layout is None:
            continue

        grid_h, grid_w, placed = placed_layout
        gi = canvas(ZERO, (grid_h, grid_w))
        for item in placed:
            frame, inner = _frame_parts_d4c90558(
                item["ulc"],
                (item["outer_h"], item["outer_w"]),
                item["thickness"],
            )
            gi = fill(gi, item["color"], frame)
            gray_cells = frozenset(sample(tuple(inner), item["count"]))
            gi = fill(gi, FIVE, gray_cells)

        ordered = sorted(placed, key=lambda x0: (x0["count"], x0["color"]))
        go = canvas(ZERO, (nobjs, counts[-ONE]))
        for row_index, item in enumerate(ordered):
            go = fill(go, item["color"], connect((row_index, ZERO), (row_index, item["count"] - ONE)))

        if gi != go:
            return {"input": gi, "output": go}
