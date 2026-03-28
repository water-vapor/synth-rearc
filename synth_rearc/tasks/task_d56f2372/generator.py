from synth_rearc.core import *


FG_COLORS_D56F2372 = tuple(remove(ZERO, interval(ZERO, TEN, ONE)))
TARGET_HEIGHTS_D56F2372 = (THREE, FOUR, FOUR, FIVE, FIVE, SIX)
TARGET_WIDTHS_D56F2372 = {
    THREE: (FIVE,),
    FOUR: (FIVE, SEVEN),
    FIVE: (FIVE, SEVEN),
    SIX: (SEVEN, NINE),
}
NOBJECTS_D56F2372 = (FOUR, FOUR, FIVE)
GAPS_D56F2372 = (ONE, TWO, TWO)


def _rows_to_patch_d56f2372(
    rows: tuple[frozenset[int], ...],
    width_value: Integer,
) -> Patch:
    center = width_value // TWO
    cells = set()
    for i, offsets in enumerate(rows):
        for offset in offsets:
            cells.add((i, center - offset))
            if offset > ZERO:
                cells.add((i, center + offset))
    return frozenset(cells)


def _sample_reaches_d56f2372(
    height_value: Integer,
    max_reach: Integer,
) -> tuple[Integer, ...]:
    while True:
        reaches = [randint(ZERO, min(ONE, max_reach))]
        for row in range(ONE, height_value):
            prev = reaches[-ONE]
            choices = tuple(range(max(ZERO, prev - TWO), min(max_reach, prev + TWO) + ONE))
            weighted = []
            for value in choices:
                weight = ONE
                if row < height_value // TWO and value >= prev:
                    weight += ONE
                if row > height_value // TWO and value <= prev:
                    weight += ONE
                if ZERO < row < height_value - ONE and value == max_reach:
                    weight += ONE
                weighted.extend((value,) * weight)
            reaches.append(choice(tuple(weighted)))
        if reaches[-ONE] > ONE:
            continue
        if maximum(reaches) != max_reach:
            continue
        if not any(value == max_reach for value in reaches[ONE:-ONE]):
            continue
        return tuple(reaches)


def _sample_symmetric_patch_d56f2372(
    diff_lb: float,
    diff_ub: float,
) -> Patch:
    while True:
        height_value = choice(TARGET_HEIGHTS_D56F2372)
        width_value = choice(TARGET_WIDTHS_D56F2372[height_value])
        max_reach = width_value // TWO
        reaches = _sample_reaches_d56f2372(height_value, max_reach)
        rows = []
        for row_index, reach in enumerate(reaches):
            offsets = {reach}
            for offset in range(reach):
                if choice((T, T, F)):
                    offsets.add(offset)
            if reach > ZERO and ZERO < row_index < height_value - ONE and choice((T, T, F)):
                offsets.discard(ZERO)
            if len(offsets) == ZERO:
                offsets.add(reach)
            rows.append(frozenset(offsets))
        patch = _rows_to_patch_d56f2372(tuple(rows), width_value)
        if shape(patch) != (height_value, width_value):
            continue
        if patch == hmirror(patch):
            continue
        if size(patch) < height_value + width_value - TWO:
            continue
        if size(backdrop(patch)) - size(patch) < TWO:
            continue
        if size(patch) > height_value * width_value - TWO:
            continue
        return patch


def _sample_asymmetric_patch_d56f2372(
    diff_lb: float,
    diff_ub: float,
) -> Patch:
    for _ in range(200):
        base = _sample_symmetric_patch_d56f2372(diff_lb, diff_ub)
        height_value, width_value = shape(base)
        center = width_value // TWO
        for _ in range(80):
            row = randint(ZERO, height_value - ONE)
            offset = randint(ONE, center)
            side = choice((ZERO, ONE))
            col = center - offset if side == ZERO else center + offset
            cells = set(base)
            if (row, col) in cells:
                if len(cells) <= FIVE:
                    continue
                cells.remove((row, col))
            else:
                cells.add((row, col))
            patch = normalize(frozenset(cells))
            height2, width2 = shape(patch)
            if patch == vmirror(patch):
                continue
            if size(patch) < FIVE:
                continue
            if height2 < TWO or width2 < THREE:
                continue
            if size(backdrop(patch)) - size(patch) < ONE:
                continue
            return patch
    raise RuntimeError("failed to sample asymmetric patch for d56f2372")


def _rectangles_separate_d56f2372(
    top: Integer,
    left: Integer,
    dims: tuple[Integer, Integer],
    placed: tuple[tuple[Integer, Integer, Integer, Integer], ...],
    gap: Integer,
) -> Boolean:
    height_value, width_value = dims
    for other_top, other_left, other_height, other_width in placed:
        rows_disjoint = top + height_value + gap <= other_top or other_top + other_height + gap <= top
        cols_disjoint = left + width_value + gap <= other_left or other_left + other_width + gap <= left
        if not (rows_disjoint or cols_disjoint):
            return F
    return T


def _place_specs_d56f2372(
    specs: tuple[tuple[Patch, Integer, bool], ...],
    grid_shape: tuple[Integer, Integer],
    gap: Integer,
) -> tuple[tuple[Patch, Integer, bool, IntegerTuple], ...] | None:
    grid_height, grid_width = grid_shape
    placed_boxes = ()
    placements = []
    for patch, value, is_target in specs:
        height_value, width_value = shape(patch)
        anchors = [
            astuple(randint(ZERO, grid_height - height_value), randint(ZERO, grid_width - width_value))
            for _ in range(600)
        ]
        shuffle(anchors)
        anchor = None
        for candidate in anchors:
            top, left = candidate
            if _rectangles_separate_d56f2372(top, left, (height_value, width_value), placed_boxes, gap):
                anchor = candidate
                break
        if anchor is None:
            return None
        placements.append((patch, value, is_target, anchor))
        placed_boxes = placed_boxes + ((anchor[ZERO], anchor[ONE], height_value, width_value),)
    return tuple(placements)


def generate_d56f2372(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        nobjects = choice(NOBJECTS_D56F2372)
        target_patch = _sample_symmetric_patch_d56f2372(diff_lb, diff_ub)
        distractors = tuple(
            _sample_asymmetric_patch_d56f2372(diff_lb, diff_ub)
            for _ in range(nobjects - ONE)
        )
        colors = sample(FG_COLORS_D56F2372, nobjects)
        specs = [(target_patch, colors[ZERO], True)]
        specs.extend(
            (patch, value, False)
            for patch, value in zip(distractors, colors[ONE:])
        )
        shuffle(specs)
        max_height = max(shape(patch)[ZERO] for patch, _, _ in specs)
        max_width = max(shape(patch)[ONE] for patch, _, _ in specs)
        grid_height = max(unifint(diff_lb, diff_ub, (20, 24)), max_height + FOUR)
        grid_width = max(unifint(diff_lb, diff_ub, (16, 22)), max_width + FOUR)
        gap = choice(GAPS_D56F2372)
        placements = _place_specs_d56f2372(tuple(specs), (grid_height, grid_width), gap)
        if placements is None:
            continue
        gi = canvas(ZERO, (grid_height, grid_width))
        go = None
        for patch, value, is_target, anchor in placements:
            gi = fill(gi, value, shift(patch, anchor))
            if is_target:
                go = fill(canvas(ZERO, shape(patch)), value, patch)
        if go is None:
            continue
        partitions = fgpartition(gi)
        symmetric = sfilter(partitions, lambda part: equality(part, vmirror(part)))
        if size(symmetric) != ONE:
            continue
        return {"input": gi, "output": go}
