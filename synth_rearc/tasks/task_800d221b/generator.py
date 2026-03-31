from __future__ import annotations

from collections import Counter

from synth_rearc.core import *

from .helpers import LAYOUTS_800D221B
from .helpers import count_exact_sep_candidates_800d221b
from .helpers import freeze_grid_800d221b
from .helpers import in_bounds_800d221b
from .helpers import l_path_800d221b
from .helpers import monochrome_centers_800d221b
from .helpers import neighbors4_800d221b
from .helpers import slot_target_800d221b
from .verifier import verify_800d221b


def _slot_rect_800d221b(
    slot: str,
    dims: IntegerTuple,
    center: IntegerTuple,
) -> tuple[Integer, Integer, Integer, Integer] | None:
    h, w = dims
    ci, cj = center
    if slot == "nw":
        rh = randint(TWO, min(SIX, subtract(ci, THREE)))
        rw = randint(TWO, min(SIX, subtract(cj, THREE)))
        top = randint(ZERO, subtract(subtract(ci, THREE), rh))
        left = randint(ZERO, subtract(subtract(cj, THREE), rw))
        return top, left, rh, rw
    if slot == "ne":
        rh = randint(TWO, min(SIX, subtract(ci, THREE)))
        rw = randint(TWO, min(SIX, subtract(subtract(w, cj), FOUR)))
        top = randint(ZERO, subtract(subtract(ci, THREE), rh))
        left = randint(add(cj, FOUR), subtract(w, rw))
        return top, left, rh, rw
    if slot == "sw":
        rh = randint(TWO, min(SIX, subtract(subtract(h, ci), FOUR)))
        rw = randint(TWO, min(SIX, subtract(cj, THREE)))
        top = randint(add(ci, FOUR), subtract(h, rh))
        left = randint(ZERO, subtract(subtract(cj, THREE), rw))
        return top, left, rh, rw
    if slot == "se":
        rh = randint(TWO, min(SIX, subtract(subtract(h, ci), FOUR)))
        rw = randint(TWO, min(SIX, subtract(subtract(w, cj), FOUR)))
        top = randint(add(ci, FOUR), subtract(h, rh))
        left = randint(add(cj, FOUR), subtract(w, rw))
        return top, left, rh, rw
    if slot == "e":
        x0 = subtract(subtract(w, cj), SIX)
        if x0 < TWO:
            return None
        rh = randint(THREE, min(SIX, max(THREE, subtract(h, TWO))))
        rw = randint(TWO, min(FIVE, x0))
        top_lb = max(ZERO, subtract(ci, FOUR))
        top_ub = min(subtract(h, rh), add(ci, ONE))
        if top_lb > top_ub:
            return None
        top = randint(top_lb, top_ub)
        left = randint(add(cj, SIX), subtract(w, rw))
        return top, left, rh, rw
    x0 = subtract(cj, SIX)
    if x0 < TWO:
        return None
    rh = randint(THREE, min(SIX, max(THREE, subtract(h, TWO))))
    rw = randint(TWO, min(FIVE, x0))
    top_lb = max(ZERO, subtract(ci, FOUR))
    top_ub = min(subtract(h, rh), add(ci, ONE))
    if top_lb > top_ub:
        return None
    top = randint(top_lb, top_ub)
    left = randint(ZERO, subtract(subtract(cj, SIX), rw))
    return top, left, rh, rw


def _rect_cells_800d221b(
    rect: tuple[Integer, Integer, Integer, Integer],
) -> set[IntegerTuple]:
    top, left, rh, rw = rect
    return {(i, j) for i in range(top, add(top, rh)) for j in range(left, add(left, rw))}


def _scaffold_for_slot_800d221b(
    slot: str,
    rect: tuple[Integer, Integer, Integer, Integer],
) -> tuple[set[IntegerTuple], IntegerTuple]:
    top, left, rh, rw = rect
    bottom = subtract(add(top, rh), ONE)
    right = subtract(add(left, rw), ONE)
    if slot == "nw":
        cells = {
            (i, add(right, ONE))
            for i in range(top, add(bottom, TWO))
        } | {
            (add(bottom, ONE), j)
            for j in range(left, add(right, TWO))
        }
        return cells, (add(bottom, ONE), add(right, ONE))
    if slot == "ne":
        cells = {
            (i, subtract(left, ONE))
            for i in range(top, add(bottom, TWO))
        } | {
            (add(bottom, ONE), j)
            for j in range(subtract(left, ONE), add(right, ONE))
        }
        return cells, (add(bottom, ONE), subtract(left, ONE))
    if slot == "sw":
        cells = {
            (i, add(right, ONE))
            for i in range(subtract(top, ONE), add(bottom, ONE))
        } | {
            (subtract(top, ONE), j)
            for j in range(left, add(right, TWO))
        }
        return cells, (subtract(top, ONE), add(right, ONE))
    if slot == "se":
        cells = {
            (i, subtract(left, ONE))
            for i in range(subtract(top, ONE), add(bottom, ONE))
        } | {
            (subtract(top, ONE), j)
            for j in range(subtract(left, ONE), add(right, ONE))
        }
        return cells, (subtract(top, ONE), subtract(left, ONE))
    if slot == "e":
        x0 = subtract(left, ONE)
        x1 = add(top, rh // TWO)
        cells = {(i, x0) for i in range(top, add(bottom, ONE))}
        return cells, (x1, x0)
    x0 = add(right, ONE)
    x1 = add(top, rh // TWO)
    cells = {(i, x0) for i in range(top, add(bottom, ONE))}
    return cells, (x1, x0)


def _paint_region_800d221b(
    grid: list[list[Integer]],
    cells: set[IntegerTuple],
    dominant: Integer,
    alternate: Integer,
    noise_quota: Integer,
) -> None:
    x0 = list(cells)
    shuffle(x0)
    x1 = set(x0[:noise_quota])
    for i, j in cells:
        grid[i][j] = alternate if (i, j) in x1 else dominant


def _path_is_clear_800d221b(
    path: frozenset[IntegerTuple],
    dims: IntegerTuple,
    blocked_cells: set[IntegerTuple],
    blocked_neighbors: set[IntegerTuple],
) -> Boolean:
    for cell in path:
        if not in_bounds_800d221b(cell, dims):
            return False
        if cell in blocked_cells:
            return False
        for nb in neighbors4_800d221b(cell):
            if nb in blocked_neighbors:
                return False
    return True


def _route_to_target_800d221b(
    start: IntegerTuple,
    end: IntegerTuple,
    dims: IntegerTuple,
    blocked_cells: set[IntegerTuple],
    blocked_neighbors: set[IntegerTuple],
) -> frozenset[IntegerTuple] | None:
    x0 = ("hv", "vh")
    x1 = list(x0)
    shuffle(x1)
    for x2 in x1:
        x3 = l_path_800d221b(start, end, x2)
        if _path_is_clear_800d221b(x3, dims, blocked_cells, blocked_neighbors):
            return x3
    return None


def _grid_has_valid_separator_pattern_800d221b(
    grid: Grid,
    bg: Integer,
    sep: Integer,
) -> Boolean:
    x0 = monochrome_centers_800d221b(grid, sep)
    if len(x0) != ONE:
        return False
    x1 = tuple(
        x2
        for x2 in difference(palette(grid), initset(bg))
        if len(monochrome_centers_800d221b(grid, x2)) == ONE
    )
    if len(x1) != ONE:
        return False
    x2 = count_exact_sep_candidates_800d221b(grid, bg, sep)
    return both(x1[ZERO] == sep, x2 == ZERO)


def _sample_layout_800d221b(
    diff_lb: float,
    diff_ub: float,
) -> tuple[str, ...]:
    x0 = unifint(diff_lb, diff_ub, (THREE, FIVE))
    x1 = tuple(x2 for x2 in LAYOUTS_800D221B if len(x2) == x0)
    if not x1:
        return choice(LAYOUTS_800D221B)
    return choice(x1)


def generate_800d221b(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_layout_800d221b(diff_lb, diff_ub)
        x1 = unifint(diff_lb, diff_ub, (16, 30))
        x2 = unifint(diff_lb, diff_ub, (16, 30))
        if contained("e", x0) and x2 < 20:
            x2 = 20
        if contained("w", x0) and x2 < 20:
            x2 = 20
        x3 = (x1, x2)
        x4 = randint(SIX, subtract(x1, SEVEN))
        x5 = randint(SIX, subtract(x2, SEVEN))
        if contained("e", x0):
            x5 = min(x5, subtract(x2, EIGHT))
        if contained("w", x0):
            x5 = max(x5, EIGHT)
        x6 = (x4, x5)
        x7 = sample(tuple(interval(ZERO, TEN, ONE)), FOUR)
        x8, x9, x10, x11 = x7
        x12 = [list(repeat(x8, x2)) for _ in range(x1)]
        x13 = {
            (i, j)
            for i in range(subtract(x4, ONE), add(x4, TWO))
            for j in range(subtract(x5, ONE), add(x5, TWO))
        }
        for i, j in x13:
            x12[i][j] = x11
        x14 = set(x13)
        x15: list[dict[str, object]] = []
        x16: list[tuple[str, Integer, Integer]] = []
        x17 = choice((x9, x10))
        x18 = x10 if x17 == x9 else x9
        x19 = choice((ONE, branch(len(x0) == FIVE, TWO, ONE)))
        x20 = set(sample(x0, x19))
        x21 = set()
        x22 = set()
        ok = True
        for x23 in x0:
            x24 = _slot_rect_800d221b(x23, x3, x6)
            if x24 is None:
                ok = False
                break
            x25 = _rect_cells_800d221b(x24)
            x26, x27 = _scaffold_for_slot_800d221b(x23, x24)
            x28 = x18 if x23 in x20 else x17
            x29 = x17 if x28 == x18 else x18
            x30 = len(x25)
            x31 = max(ONE, min(subtract(x30, ONE), randint(ONE, max(ONE, x30 // THREE))))
            if x25 & x14 or x26 & x14:
                ok = False
                break
            if x25 & x21 or x26 & x22:
                ok = False
                break
            _paint_region_800d221b(x12, x25, x28, x29, x31)
            for i, j in x26:
                x12[i][j] = x11
            x21 |= x25
            x22 |= x26
            x14 |= x25 | x26
            x15.append(
                {
                    "slot": x23,
                    "dominant": x28,
                    "region": x25,
                    "scaffold": x26,
                    "root": x27,
                }
            )
            x16.append((x23, x28, x30))
        if not ok:
            continue
        for x23 in x15:
            x24 = x23["slot"]
            x25 = x23["root"]
            x26 = x23["scaffold"]
            x27 = x23["region"]
            x28 = slot_target_800d221b(x6, x24)
            x29 = set()
            for x30 in x15:
                if x30 is x23:
                    continue
                x29 |= x30["region"]
            x30 = difference(x22, x26)
            x31 = _route_to_target_800d221b(x25, x28, x3, x30 | x21, x29 | x30)
            if x31 is None:
                ok = False
                break
            x32 = difference(x31, x26)
            if x32 & x13:
                ok = False
                break
            for i, j in x32:
                x12[i][j] = x11
            x22 |= x32
            x14 |= x32
            x23["branch"] = combine(x26, x31)
        if not ok:
            continue
        x33 = Counter()
        for _, x34, x35 in x16:
            x33[x34] += x35
        if len(x33) != TWO:
            continue
        x34 = {x35: x36 for x35, x36, _ in x16}
        x35 = max(x33, key=lambda x36: (x33[x36], invert(x36)))
        if both(contained("nw", x34), contained("sw", x34)) and x34["nw"] == x34["sw"]:
            x35 = x34["nw"]
        elif both(contained("ne", x34), contained("se", x34)) and x34["ne"] == x34["se"]:
            x35 = x34["ne"]
        if len(set(x33.values())) != TWO:
            continue
        x36 = freeze_grid_800d221b(x12)
        if not _grid_has_valid_separator_pattern_800d221b(x36, x8, x11):
            continue
        x37 = [list(row) for row in x12]
        for x38 in x15:
            for i, j in x38["branch"]:
                x37[i][j] = x38["dominant"]
        x37[x4][x5] = x35
        x38 = freeze_grid_800d221b(x37)
        if x36 == x38:
            continue
        if verify_800d221b(x36) != x38:
            continue
        return {"input": x36, "output": x38}
