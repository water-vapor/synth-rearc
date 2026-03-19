from arc2.core import *


TL2_da6e95e5 = frozenset({ORIGIN, RIGHT, DOWN})
TR2_da6e95e5 = frozenset({ORIGIN, RIGHT, UNITY})
BL2_da6e95e5 = frozenset({ORIGIN, DOWN, UNITY})
BR2_da6e95e5 = frozenset({RIGHT, DOWN, UNITY})

TL3_da6e95e5 = frozenset({ORIGIN, RIGHT, (0, 2), DOWN, (2, 0)})
TR3_da6e95e5 = frozenset({ORIGIN, RIGHT, (0, 2), (1, 2), (2, 2)})
BL3_da6e95e5 = frozenset({ORIGIN, DOWN, (2, 0), (2, 1), (2, 2)})
BR3_da6e95e5 = frozenset({(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)})

CORNERS_da6e95e5 = {
    TWO: (
        TL2_da6e95e5,
        TR2_da6e95e5,
        BL2_da6e95e5,
        BR2_da6e95e5,
    ),
    THREE: (
        TL3_da6e95e5,
        TR3_da6e95e5,
        BL3_da6e95e5,
        BR3_da6e95e5,
    ),
}

MARGIN_da6e95e5 = {
    TWO: ONE,
    THREE: ZERO,
}

PATCH_TRANSFORMS_da6e95e5 = (
    identity,
    hmirror,
    vmirror,
    compose(hmirror, vmirror),
    dmirror,
    cmirror,
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)


def _variants_da6e95e5(patch: Patch) -> tuple[Patch, ...]:
    out = []
    for transform in PATCH_TRANSFORMS_da6e95e5:
        candidate = normalize(transform(patch))
        if candidate not in out:
            out.append(candidate)
    return tuple(out)


def _bank_da6e95e5(*patches: Patch) -> tuple[Patch, ...]:
    out = []
    for patch in patches:
        for candidate in _variants_da6e95e5(patch):
            if candidate not in out:
                out.append(candidate)
    return tuple(out)


PAYLOADS2_da6e95e5 = _bank_da6e95e5(
    frozenset({ORIGIN, RIGHT, DOWN, UNITY}),
    frozenset({RIGHT, DOWN, UNITY}),
    frozenset({ORIGIN, UNITY}),
    frozenset({ORIGIN, RIGHT, DOWN, UNITY, (2, 0), (2, 1), (2, 2), (1, 2)}),
    frozenset({ORIGIN, RIGHT, (0, 2), UNITY, (2, 0), (2, 1), (2, 2)}),
    frozenset({ORIGIN, RIGHT, (0, 2), UNITY, (1, 1), (2, 0), (2, 2)}),
    frozenset({ORIGIN, RIGHT, (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)}),
    frozenset({ORIGIN, RIGHT, (0, 2), (1, 1), (2, 2)}),
    frozenset({ORIGIN, RIGHT, (0, 2), (1, 1)}),
)

PAYLOADS3_da6e95e5 = _bank_da6e95e5(
    frozenset({ORIGIN, RIGHT, (0, 2), UNITY, (1, 3), (2, 0), (2, 2), (2, 4), (3, 0), (3, 2), (3, 4)}),
    frozenset({(0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 3), (1, 4), (2, 1), (2, 3), (3, 1), (3, 3)}),
    frozenset({(0, 1), (0, 2), (0, 3), (1, 1), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 3)}),
    frozenset({ORIGIN, RIGHT, (0, 2), (0, 3), (0, 4), UNITY, (1, 3), (2, 0), (2, 2), (2, 4), (3, 1), (3, 3)}),
    frozenset({ORIGIN, RIGHT, (0, 2), DOWN, UNITY, (1, 2), (2, 0), (2, 1), (2, 2)}),
    frozenset({ORIGIN, RIGHT, (0, 2), (1, 1), (2, 0), (2, 1), (2, 2)}),
    frozenset({ORIGIN, RIGHT, (0, 2), DOWN, (1, 2), (2, 0), (2, 2)}),
    frozenset({ORIGIN, RIGHT, (0, 2), (0, 3), DOWN, (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)}),
)


def _pick_payload_da6e95e5(marker_size: Integer) -> Patch:
    payloads = branch(marker_size == TWO, PAYLOADS2_da6e95e5, PAYLOADS3_da6e95e5)
    weights = branch(
        marker_size == TWO,
        (THREE, TWO, ONE, THREE, TWO, TWO, TWO, ONE, ONE),
        (THREE, THREE, TWO, TWO, TWO, TWO, ONE, TWO),
    )
    bag = tuple(
        payload
        for payload, weight in pair(payloads, weights)
        for _ in range(weight)
    )
    return choice(bag)


def _group_layout_da6e95e5(
    marker_size: Integer,
    payload: Patch,
) -> dict:
    margin = MARGIN_da6e95e5[marker_size]
    ph, pw = shape(payload)
    pi = marker_size - ONE + margin
    pj = marker_size - ONE + margin
    ti = pi + ph - ONE + margin
    tj = pj + pw - ONE + margin
    gh = ti + marker_size
    gw = tj + marker_size
    corners = CORNERS_da6e95e5[marker_size]
    return {
        "dims": (gh, gw),
        "payload_offset": (pi, pj),
        "corners": (
            shift(corners[ZERO], ORIGIN),
            shift(corners[ONE], (ZERO, tj)),
            shift(corners[TWO], (ti, ZERO)),
            shift(corners[THREE], (ti, tj)),
        ),
    }


def _rects_separate_da6e95e5(
    a: tuple[Integer, Integer, Integer, Integer],
    b: tuple[Integer, Integer, Integer, Integer],
) -> Boolean:
    ai0, aj0, ai1, aj1 = a
    bi0, bj0, bi1, bj1 = b
    return ai1 + ONE < bi0 or bi1 + ONE < ai0 or aj1 + ONE < bj0 or bj1 + ONE < aj0


def _place_groups_da6e95e5(
    groups: list[dict],
) -> list[dict] | None:
    h = 30
    w = 30
    placed = []
    rows = []
    cols = []
    order_ids = list(range(len(groups)))
    shuffle(order_ids)
    for idx in order_ids:
        spec = groups[idx]
        gh, gw = spec["layout"]["dims"]
        locs = [(i, j) for i in range(h - gh + ONE) for j in range(w - gw + ONE)]
        shuffle(locs)
        chosen = None
        for loc in locs:
            ii, jj = loc
            rect = (ii, jj, ii + gh - ONE, jj + gw - ONE)
            if any(not _rects_separate_da6e95e5(rect, other["rect"]) for other in placed):
                continue
            if spec["shared"]:
                if ii in rows or jj in cols:
                    continue
            chosen = rect
            break
        if chosen is None:
            return None
        ii, jj = chosen[ZERO], chosen[ONE]
        spec["origin"] = (ii, jj)
        spec["rect"] = chosen
        placed.append(spec)
        if spec["shared"]:
            rows.append(ii)
            cols.append(jj)
    placed = order(placed, lambda item: item["rect"])
    return list(placed)


def _paint_group_da6e95e5(
    grid: Grid,
    spec: dict,
) -> Grid:
    gi = grid
    oi, oj = spec["origin"]
    payload_color = spec["payload_color"]
    payload = shift(spec["payload"], add(spec["layout"]["payload_offset"], (oi, oj)))
    gi = fill(gi, payload_color, payload)
    for corner in spec["layout"]["corners"]:
        gi = fill(gi, spec["marker_color"], shift(corner, (oi, oj)))
    spec["payload_abs"] = payload
    return gi


def generate_da6e95e5(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    palette_all = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        marker_size = choice((TWO, TWO, THREE))
        ngroups = unifint(diff_lb, diff_ub, (THREE, FIVE))
        bg = choice(palette_all)
        colors = remove(bg, palette_all)
        target_idx = randint(ZERO, ngroups - ONE)
        shared = choice((F, F, F, T))
        if shared:
            marker_palette = sample(colors, ONE)
        else:
            marker_palette = sample(colors, ngroups)
        groups = []
        used_payloads = []
        for idx in range(ngroups):
            payload = _pick_payload_da6e95e5(marker_size)
            if len(used_payloads) > ZERO and choice((T, F)):
                payload = choice(used_payloads)
            used_payloads.append(payload)
            if shared:
                marker_color = marker_palette[ZERO]
            else:
                marker_color = marker_palette[idx]
            payload_colors = remove(marker_color, colors)
            payload_color = branch(idx == target_idx, marker_color, choice(payload_colors))
            layout = _group_layout_da6e95e5(marker_size, payload)
            groups.append(
                {
                    "layout": layout,
                    "marker_color": marker_color,
                    "payload_color": payload_color,
                    "payload": payload,
                    "shared": shared,
                }
            )
        placed = _place_groups_da6e95e5(groups)
        if placed is None:
            continue
        gi = canvas(bg, (30, 30))
        for spec in placed:
            gi = _paint_group_da6e95e5(gi, spec)
        target = extract(placed, lambda item: item["payload_color"] == item["marker_color"])
        go = subgrid(target["payload_abs"], gi)
        objs = objects(gi, T, F, T)
        if numcolors(gi) < FOUR:
            continue
        if size(objs) < add(multiply(ngroups, FIVE), ONE):
            continue
        if colorcount(gi, bg) <= colorcount(gi, target["marker_color"]):
            continue
        if shape(go) == (ONE, ONE):
            continue
        if colorcount(go, target["marker_color"]) < THREE:
            continue
        if not any(row.count(bg) > ZERO for row in go):
            continue
        return {"input": gi, "output": go}
