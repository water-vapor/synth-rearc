from arc2.core import *


def _rect_patch(top: int, left: int, bottom: int, right: int) -> Indices:
    return frozenset((i, j) for i in range(top, bottom + ONE) for j in range(left, right + ONE))


def _reserve_patch(patch: Patch, pad: int = ONE) -> Indices:
    x0 = uppermost(patch) - pad
    x1 = leftmost(patch) - pad
    x2 = lowermost(patch) + pad
    x3 = rightmost(patch) + pad
    return _rect_patch(x0, x1, x2, x3)


def _build_component(
    top: int,
    left: int,
    bottom: int,
    right: int,
    specs: tuple[tuple[str, int, str], ...],
) -> tuple[Indices, Indices]:
    cells = set(_rect_patch(top, left, bottom, right))
    marks = set()
    for side, position, mode in specs:
        if side == "left":
            marks |= {(position, left - ONE), (position, left)}
            if mode == "out":
                cells.add((position, left - ONE))
            else:
                cells.discard((position, left))
        elif side == "right":
            marks |= {(position, right), (position, right + ONE)}
            if mode == "out":
                cells.add((position, right + ONE))
            else:
                cells.discard((position, right))
        elif side == "top":
            marks |= {(top - ONE, position), (top, position)}
            if mode == "out":
                cells.add((top - ONE, position))
            else:
                cells.discard((top, position))
        else:
            marks |= {(bottom, position), (bottom + ONE, position)}
            if mode == "out":
                cells.add((bottom + ONE, position))
            else:
                cells.discard((bottom, position))
    return frozenset(cells), frozenset(marks)


def _component_specs(top: int, left: int, bottom: int, right: int) -> tuple[tuple[str, int, str], ...]:
    height = bottom - top + ONE
    width = right - left + ONE
    sides = ["left", "right", "top", "bottom"]
    nsides = choice((TWO, TWO, THREE))
    chosen = sample(sides, nsides)
    specs = []
    for side in chosen:
        if side in ("left", "right"):
            position = randint(top + ONE, bottom - ONE)
        else:
            position = randint(left + ONE, right - ONE)
        mode = choice(("in", "out"))
        specs.append((side, position, mode))
    return tuple(specs)


def _candidate_component(
    zone: tuple[int, int, int, int],
    reserved: Indices,
    large: bool,
) -> tuple[Indices, Indices, Indices] | None:
    top, left, bottom, right = zone
    zheight = bottom - top + ONE
    zwidth = right - left + ONE
    hmin = FOUR if large else THREE
    wmin = FIVE if large else FOUR
    hub = min(EIGHT if large else SIX, zheight)
    wub = min(TEN if large else SIX, zwidth)
    if hub < hmin or wub < wmin:
        return None
    for _ in range(200):
        height = randint(hmin, hub)
        width = randint(wmin, wub)
        a = randint(top, bottom - height + ONE)
        b = randint(left, right - width + ONE)
        c = a + height - ONE
        d = b + width - ONE
        specs = _component_specs(a, b, c, d)
        cells, marks = _build_component(a, b, c, d, specs)
        footprint = combine(cells, marks)
        reserve = _reserve_patch(footprint, ONE)
        if len(intersection(reserve, reserved)) != ZERO:
            continue
        if uppermost(footprint) < ZERO or leftmost(footprint) < ZERO:
            continue
        return cells, marks, reserve
    return None


def _host_layout(height: int, width: int) -> tuple[tuple[int, int, int, int], tuple[int, int, int, int]]:
    for _ in range(200):
        top1 = randint(ZERO, THREE)
        left1 = randint(ZERO, THREE)
        cut_top_lb = top1 + FIVE
        cut_top_ub = height - TEN
        cut_left_lb = left1 + FIVE
        cut_left_ub = width - TEN
        if cut_top_lb > cut_top_ub or cut_left_lb > cut_left_ub:
            continue
        top2 = randint(cut_top_lb, cut_top_ub)
        left2 = randint(cut_left_lb, cut_left_ub)
        bottom1_lb = top2 + TWO
        bottom1_ub = min(top2 + EIGHT, height - SIX)
        right1_lb = left2 + TWO
        right1_ub = min(left2 + EIGHT, width - SIX)
        bottom2_lb = top2 + SIX
        bottom2_ub = height - ONE - randint(ZERO, THREE)
        right2_lb = left2 + SIX
        right2_ub = width - ONE - randint(ZERO, THREE)
        if bottom1_lb > bottom1_ub or right1_lb > right1_ub:
            continue
        if bottom2_lb > bottom2_ub or right2_lb > right2_ub:
            continue
        bottom1 = randint(bottom1_lb, bottom1_ub)
        right1 = randint(right1_lb, right1_ub)
        bottom2 = randint(bottom2_lb, bottom2_ub)
        right2 = randint(right2_lb, right2_ub)
        return (top1, left1, bottom1, right1), (top2, left2, bottom2, right2)
    raise RuntimeError("failed to place host regions")


def generate_9b5080bb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    from .verifier import verify_9b5080bb

    colors = interval(ONE, TEN, ONE)
    while True:
        bgc, innerc, host1c, host2c = sample(colors, FOUR)
        dim = unifint(diff_lb, diff_ub, (20, 30))
        host1_rect, host2_rect = _host_layout(dim, dim)
        top1, left1, bottom1, right1 = host1_rect
        top2, left2, bottom2, right2 = host2_rect
        gi = canvas(bgc, (dim, dim))
        host1 = _rect_patch(top1, left1, bottom1, right1)
        host2 = _rect_patch(top2, left2, bottom2, right2)
        gi = fill(gi, host1c, host1)
        gi = fill(gi, host2c, host2)
        go = gi
        zones = [
            ((top1 + TWO, left1 + TWO, top2 - THREE, right1 - TWO), host1c, host2c, T),
            ((top2 + TWO, left2 + TWO, bottom2 - TWO, right2 - TWO), host2c, host1c, T),
        ]
        if choice((T, F)):
            zones.append(((top2 + TWO, left2 + TWO, bottom2 - TWO, right2 - TWO), host2c, host1c, F))
        reserved = frozenset({})
        placements = []
        failed = F
        for zone, hostc, markc, large in zones:
            ztop, zleft, zbottom, zright = zone
            if ztop > zbottom or zleft > zright:
                failed = T
                break
            x0 = _candidate_component(zone, reserved, large)
            if x0 is None:
                failed = T
                break
            cells, marks, reserve = x0
            placements.append((hostc, markc, cells, marks))
            reserved = combine(reserved, reserve)
        if failed:
            continue
        for _, markc, cells, marks in placements:
            gi = fill(gi, innerc, cells)
            go = fill(go, innerc, cells)
            go = fill(go, markc, marks)
        if numcolors(gi) != FOUR or numcolors(go) != FOUR:
            continue
        if choice((T, F)):
            gi = hmirror(gi)
            go = hmirror(go)
        if choice((T, F)):
            gi = vmirror(gi)
            go = vmirror(go)
        if verify_9b5080bb(gi) != go:
            continue
        return {"input": gi, "output": go}
