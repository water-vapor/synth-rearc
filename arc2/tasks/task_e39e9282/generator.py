from arc2.core import *


SIDE_LABELS_E39E9282 = ("top", "bottom", "left", "right")


def _expanded_box_e39e9282(anchor: IntegerTuple) -> Tuple[int, int, int, int]:
    ai, aj = anchor
    return (ai - ONE, ai + THREE, aj - ONE, aj + THREE)


def _boxes_overlap_e39e9282(a: Tuple[int, int, int, int], b: Tuple[int, int, int, int]) -> bool:
    return not (a[ONE] < b[ZERO] or b[ONE] < a[ZERO] or a[THREE] < b[TWO] or b[THREE] < a[TWO])


def _marker_index_e39e9282(anchor: IntegerTuple, marker: Tuple[str, int]) -> IntegerTuple:
    ai, aj = anchor
    side, offset = marker
    if side == "top":
        return (ai - ONE, aj + offset)
    if side == "bottom":
        return (ai + THREE, aj + offset)
    if side == "left":
        return (ai + offset, aj - ONE)
    return (ai + offset, aj + THREE)


def _project_marker_e39e9282(anchor: IntegerTuple, marker: Tuple[str, int], color_value: Integer) -> Tuple[IntegerTuple, ...]:
    ai, aj = anchor
    side, offset = marker
    step = ONE if color_value == FIVE else TWO
    source = _marker_index_e39e9282(anchor, marker)
    if side == "top":
        target = (ai - ONE + step, aj + offset)
    elif side == "bottom":
        target = (ai + THREE - step, aj + offset)
    elif side == "left":
        target = (ai + offset, aj - ONE + step)
    else:
        target = (ai + offset, aj + THREE - step)
    if color_value == FIVE:
        return (source, target)
    return (target,)


def _available_markers_e39e9282(anchor: IntegerTuple, shape_value: IntegerTuple) -> Tuple[Tuple[str, int], ...]:
    ai, aj = anchor
    h, w = shape_value
    markers = []
    if ai > ZERO:
        markers.extend(("top", k) for k in range(THREE))
    if ai + THREE < h:
        markers.extend(("bottom", k) for k in range(THREE))
    if aj > ZERO:
        markers.extend(("left", k) for k in range(THREE))
    if aj + THREE < w:
        markers.extend(("right", k) for k in range(THREE))
    return tuple(markers)


def _choose_markers_e39e9282(anchor: IntegerTuple, shape_value: IntegerTuple) -> Tuple[Tuple[str, int], ...]:
    markers = _available_markers_e39e9282(anchor, shape_value)
    grouped = {label: tuple(marker for marker in markers if marker[ZERO] == label) for label in SIDE_LABELS_E39E9282}
    mode = choice(("single", "pair", "pair", "segment", "segment", "triple"))
    if mode == "single":
        return (choice(markers),)
    if mode == "pair":
        count = min(TWO, len(markers))
        return tuple(sample(markers, count))
    segment_sides = tuple(label for label, entries in grouped.items() if len(entries) >= TWO)
    if mode == "segment" and len(segment_sides) > ZERO:
        label = choice(segment_sides)
        entries = grouped[label]
        start = randint(ZERO, len(entries) - TWO)
        return entries[start:start + TWO]
    triple_sides = tuple(label for label, entries in grouped.items() if len(entries) == THREE)
    if len(triple_sides) > ZERO:
        label = choice(triple_sides)
        return grouped[label]
    count = min(TWO, len(markers))
    return tuple(sample(markers, count))


def _render_input_e39e9282(shape_value: IntegerTuple, blocks: Tuple[Tuple[Integer, IntegerTuple, Tuple[Tuple[str, int], ...]], ...]) -> Grid:
    gi = canvas(EIGHT, shape_value)
    for color_value, anchor, markers in blocks:
        ai, aj = anchor
        patch = shift(frozenset({(i, j) for i in range(THREE) for j in range(THREE)}), anchor)
        gi = fill(gi, color_value, patch)
        for marker in markers:
            gi = fill(gi, NINE, initset(_marker_index_e39e9282(anchor, marker)))
    return gi


def _render_output_e39e9282(shape_value: IntegerTuple, blocks: Tuple[Tuple[Integer, IntegerTuple, Tuple[Tuple[str, int], ...]], ...]) -> Grid:
    go = canvas(EIGHT, shape_value)
    for color_value, anchor, markers in blocks:
        ai, aj = anchor
        if color_value == SIX:
            patch = shift(frozenset({(i, j) for i in range(THREE) for j in range(THREE)}), anchor)
            go = fill(go, SIX, patch)
        for marker in markers:
            for target in _project_marker_e39e9282(anchor, marker, color_value):
                go = fill(go, NINE, initset(target))
    return go


def generate_e39e9282(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        h = unifint(diff_lb, diff_ub, (NINE, 18))
        w = unifint(diff_lb, diff_ub, (NINE, 18))
        shape_value = (h, w)
        capacity = max(ONE, ((h + TWO) // FIVE) * ((w + TWO) // FIVE))
        nblocks = randint(ONE, min(SIX, capacity))
        nfives = randint(ZERO, nblocks - ONE)
        colors = [FIVE] * nfives + [SIX] * (nblocks - nfives)
        shuffle(colors)
        anchors = []
        expanded = []
        success = True
        for _ in range(nblocks):
            candidates = []
            for ai in range(h - TWO):
                for aj in range(w - TWO):
                    box_value = _expanded_box_e39e9282((ai, aj))
                    if all(not _boxes_overlap_e39e9282(box_value, other) for other in expanded):
                        candidates.append((ai, aj))
            if len(candidates) == ZERO:
                success = False
                break
            anchor = choice(candidates)
            anchors.append(anchor)
            expanded.append(_expanded_box_e39e9282(anchor))
        if not success:
            continue
        blocks = []
        for color_value, anchor in zip(colors, anchors):
            markers = _choose_markers_e39e9282(anchor, shape_value)
            blocks.append((color_value, anchor, markers))
        blocks_value = tuple(blocks)
        gi = _render_input_e39e9282(shape_value, blocks_value)
        go = _render_output_e39e9282(shape_value, blocks_value)
        if gi == go:
            continue
        return {"input": gi, "output": go}
