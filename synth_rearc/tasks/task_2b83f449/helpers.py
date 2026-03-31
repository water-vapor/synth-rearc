from __future__ import annotations

from synth_rearc.core import *


def bar_centers_2b83f449(row: tuple[int, ...]) -> tuple[int, ...]:
    centers: list[int] = []
    j = ZERO
    w = len(row)
    while j < w:
        if row[j] != SEVEN:
            j += ONE
            continue
        k = j
        while k < w and row[k] == SEVEN:
            k += ONE
        centers.append((j + k - ONE) // TWO)
        j = k
    return tuple(centers)


def nonzero_segments_2b83f449(row: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    segments: list[tuple[int, int]] = []
    j = ZERO
    w = len(row)
    while j < w:
        if row[j] == ZERO:
            j += ONE
            continue
        k = j
        while k < w and row[k] != ZERO:
            k += ONE
        segments.append((j, k - ONE))
        j = k
    return tuple(segments)


def render_input_2b83f449(
    height: int,
    width: int,
    odd_rows: tuple[tuple[int, ...], ...],
    even_holes: dict[int, tuple[int, ...]],
) -> Grid:
    rows: list[list[int]] = []
    odd_idx = ZERO
    for i in range(height):
        if i % TWO == ONE:
            row = [ZERO] * width
            for center in odd_rows[odd_idx]:
                row[center - ONE:center + TWO] = [SEVEN, SEVEN, SEVEN]
            odd_idx += ONE
            rows.append(row)
            continue
        row = [EIGHT] * width
        if i != height - ONE:
            row[ZERO] = THREE
            row[-ONE] = THREE
        for hole in even_holes.get(i, ()):
            row[hole] = ZERO
        rows.append(row)
    return tuple(tuple(row) for row in rows)


def render_output_2b83f449(grid: Grid) -> Grid:
    h = len(grid)
    w = len(grid[ZERO])
    rows = [list(row) for row in grid]
    centers_by_row: dict[int, tuple[int, ...]] = {}
    for i, row in enumerate(grid):
        centers = bar_centers_2b83f449(row)
        centers_by_row[i] = centers
        for center in centers:
            rows[i][center - ONE] = EIGHT
            rows[i][center] = SIX
            rows[i][center + ONE] = EIGHT
    for i in range(ZERO, h, TWO):
        rows[i] = [EIGHT if value == THREE else value for value in rows[i]]
        above = centers_by_row.get(i - ONE, ())
        below = centers_by_row.get(i + ONE, ())
        supported_cols = tuple(sorted(set(above) | set(below)))
        for col in supported_cols:
            if rows[i][col] != ZERO:
                rows[i][col] = SIX
        left_active = bool(above) and (not below or below[ZERO] > above[ZERO])
        right_active = bool(above) and (not below or below[-ONE] < above[-ONE])
        segments = nonzero_segments_2b83f449(grid[i])
        supported_segments = tuple(
            any(a <= col <= b for col in supported_cols) for a, b in segments
        )
        is_bottom = i == h - ONE
        for idx, (a, b) in enumerate(segments):
            is_first = idx == ZERO
            is_last = idx == len(segments) - ONE
            supported = supported_segments[idx]
            # The edge markers are driven by how the outer bar centers move between odd rows.
            if left_active and (supported or (is_first and not is_bottom)):
                rows[i][a] = THREE
            if right_active and (is_last or (supported and is_first)):
                rows[i][b] = THREE
        if (
            left_active
            and segments
            and segments[ZERO][ZERO] == ZERO
            and supported_segments[ZERO]
            and w > ONE
            and grid[i][ONE] != ZERO
        ):
            if (len(segments) == ONE and not is_bottom) or (
                not below and len(segments) > ONE and not supported_segments[-ONE]
            ):
                rows[i][ONE] = THREE
        if (
            right_active
            and segments
            and segments[-ONE][-ONE] == w - ONE
            and supported_segments[-ONE]
            and not is_bottom
            and w > ONE
            and grid[i][w - TWO] != ZERO
        ):
            rows[i][w - TWO] = THREE
    return tuple(tuple(row) for row in rows)


def random_centers_2b83f449(width: int, count: int) -> tuple[int, ...]:
    count = max(ONE, min(THREE, count))
    for _ in range(200):
        pool = list(range(ONE, width - ONE))
        shuffle(pool)
        picked: list[int] = []
        for candidate in pool:
            if all(abs(candidate - other) >= FOUR for other in picked):
                picked.append(candidate)
                if len(picked) == count:
                    return tuple(sorted(picked))
    raise RuntimeError("failed to sample non-overlapping bar centers")


def mutate_centers_2b83f449(
    width: int,
    previous: tuple[int, ...] | None,
    *,
    allow_empty: bool,
) -> tuple[int, ...]:
    if previous is None or not previous:
        return random_centers_2b83f449(width, choice((ONE, ONE, TWO, TWO, THREE)))
    if allow_empty and uniform(0.0, 1.0) < 0.14:
        return ()
    count = max(ONE, min(THREE, len(previous) + choice((-ONE, ZERO, ZERO, ONE))))
    for _ in range(200):
        anchors = list(previous)
        while len(anchors) < count:
            anchors.append(choice(previous))
        shuffle(anchors)
        proposal: list[int] = []
        for anchor in anchors[:count]:
            for _ in range(40):
                candidate = max(ONE, min(width - TWO, anchor + choice(
                    (-SIX, -FIVE, -FOUR, -THREE, -TWO, -ONE, ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX)
                )))
                if all(abs(candidate - other) >= FOUR for other in proposal):
                    proposal.append(candidate)
                    break
            else:
                break
        if len(proposal) == count:
            return tuple(sorted(proposal))
    return random_centers_2b83f449(width, count)


def sample_even_holes_2b83f449(height: int, width: int) -> dict[int, tuple[int, ...]]:
    holes: dict[int, tuple[int, ...]] = {}
    candidates = tuple(range(TWO, width - TWO))
    for i in range(ZERO, height, TWO):
        count = choice((ZERO, ZERO, ZERO, ONE, ONE, TWO))
        if i == ZERO:
            count = choice((ZERO, ZERO, ONE))
        if not candidates or count == ZERO:
            continue
        shuffled = list(candidates)
        shuffle(shuffled)
        picked: list[int] = []
        for candidate in shuffled:
            if all(abs(candidate - other) >= THREE for other in picked):
                picked.append(candidate)
                if len(picked) == count:
                    break
        if picked:
            holes[i] = tuple(sorted(picked))
    return holes
