from __future__ import annotations

from arc2.core import *


GRID_HEIGHT_BOUNDS_C87289BB = (8, 13)
GRID_WIDTH_BOUNDS_C87289BB = (10, 18)
STREAM_HEIGHT_OPTIONS_C87289BB = (THREE, FOUR, FOUR, FIVE)
STREAM_GAP_OPTIONS_C87289BB = (TWO, THREE, THREE, FOUR)


def _segment_clear_c87289bb(
    start: Integer,
    end: Integer,
    segments: tuple[tuple[Integer, Integer], ...],
) -> bool:
    return all(end < other_start - ONE or start > other_end + ONE for other_start, other_end in segments)


def _stream_columns_c87289bb(width: Integer) -> tuple[Integer, ...]:
    while True:
        x0 = randint(ZERO, min(TWO, width - THREE))
        x1 = [x0]
        while True:
            if len(x1) >= THREE and choice((F, F, T)):
                break
            x2 = x1[-ONE] + choice(STREAM_GAP_OPTIONS_C87289BB)
            if x2 >= width:
                break
            x1.append(x2)
            if len(x1) >= SIX:
                break
        if THREE <= len(x1) <= SIX:
            return tuple(x1)


def _segment_candidates_c87289bb(
    columns: tuple[Integer, ...],
    width: Integer,
    segments: tuple[tuple[Integer, Integer], ...],
    used: frozenset[Integer],
) -> list[tuple[tuple[Integer, Integer], tuple[Integer, ...]]]:
    x0: list[tuple[tuple[Integer, Integer], tuple[Integer, ...]]] = []
    for x1, x2 in enumerate(columns[:-ONE]):
        if x1 in used or x1 + ONE in used:
            continue
        x3 = columns[x1 + ONE]
        if x3 - x2 not in (TWO, THREE):
            continue
        if x2 == ZERO or x3 == width - ONE:
            continue
        if not _segment_clear_c87289bb(x2, x3, segments):
            continue
        x0.extend([((x2, x3), (x1, x1 + ONE))] * THREE)
    for x1, x2 in enumerate(columns):
        if x1 in used:
            continue
        for x3 in (TWO, THREE, FOUR):
            x4 = x2
            x5 = x2 + x3 - ONE
            if x2 > ZERO and x5 < width - ONE:
                x6 = sum(x4 <= x7 <= x5 for x7 in columns)
                if x6 == ONE and _segment_clear_c87289bb(x4, x5, segments):
                    x0.append(((x4, x5), (x1,)))
            x4 = x2 - x3 + ONE
            x5 = x2
            if x4 > ZERO and x2 < width - ONE:
                x6 = sum(x4 <= x7 <= x5 for x7 in columns)
                if x6 == ONE and _segment_clear_c87289bb(x4, x5, segments):
                    x0.append(((x4, x5), (x1,)))
        x3 = x2 - ONE
        x4 = x2 + ONE
        if x3 > ZERO and x4 < width - ONE:
            x5 = sum(x3 <= x6 <= x4 for x6 in columns)
            if x5 == ONE and _segment_clear_c87289bb(x3, x4, segments):
                x0.extend([((x3, x4), (x1,))] * TWO)
    return x0


def _block_segments_c87289bb(columns: tuple[Integer, ...], width: Integer) -> tuple[tuple[Integer, Integer], ...]:
    while True:
        x0 = choice((ONE, ONE, TWO)) if len(columns) >= FOUR else ONE
        x1: list[tuple[Integer, Integer]] = []
        x2 = frozenset()
        for _ in range(x0):
            x3 = _segment_candidates_c87289bb(columns, width, tuple(x1), x2)
            if len(x3) == ZERO:
                break
            x4, x5 = choice(x3)
            x1.append(x4)
            x2 = combine(x2, frozenset(x5))
        x6 = sum(any(start <= col <= end for start, end in x1) for col in columns)
        if ONE <= len(x1) <= TWO and x6 < len(columns):
            return tuple(sorted(x1))


def _exit_column_c87289bb(col: Integer, segment: tuple[Integer, Integer] | None, width: Integer) -> Integer:
    if segment is None:
        return col
    x0, x1 = segment
    if x0 == ZERO:
        return x1 + ONE
    if x1 == width - ONE:
        return x0 - ONE
    if col - x0 < x1 - col:
        return x0 - ONE
    return x1 + ONE


def _render_streams_c87289bb(
    grid: Grid,
    columns: tuple[Integer, ...],
    top: Integer,
    bottom: Integer,
    color: Integer,
) -> Grid:
    x0 = tuple(connect((top, x1), (bottom, x1)) for x1 in columns)
    return fill(grid, color, merge(x0))


def _render_input_c87289bb(
    dims: IntegerTuple,
    stream_height: Integer,
    columns: tuple[Integer, ...],
    segments: tuple[tuple[Integer, Integer], ...],
) -> Grid:
    x0 = canvas(ZERO, dims)
    x1 = _render_streams_c87289bb(x0, columns, ZERO, stream_height - ONE, EIGHT)
    x2 = tuple(connect((stream_height + ONE, x3), (stream_height + ONE, x4)) for x3, x4 in segments)
    x3 = fill(x1, TWO, merge(x2))
    return x3


def _render_output_c87289bb(
    dims: IntegerTuple,
    stream_height: Integer,
    columns: tuple[Integer, ...],
    segments: tuple[tuple[Integer, Integer], ...],
) -> Grid:
    x0 = _render_input_c87289bb(dims, stream_height, columns, segments)
    x1 = {}
    for x2, x3 in segments:
        for x4 in range(x2, x3 + ONE):
            x1[x4] = (x2, x3)
    x2 = stream_height
    x3 = dims[ZERO] - ONE
    x4 = tuple(
        combine(
            connect((x2, x5), (x2, _exit_column_c87289bb(x5, x1.get(x5), dims[ONE]))),
            connect(
                (x2, _exit_column_c87289bb(x5, x1.get(x5), dims[ONE])),
                (x3, _exit_column_c87289bb(x5, x1.get(x5), dims[ONE])),
            ),
        )
        for x5 in columns
    )
    x5 = fill(x0, EIGHT, merge(x4))
    return x5


def generate_c87289bb(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, GRID_HEIGHT_BOUNDS_C87289BB)
        x1 = unifint(diff_lb, diff_ub, GRID_WIDTH_BOUNDS_C87289BB)
        x2 = choice(tuple(x3 for x3 in STREAM_HEIGHT_OPTIONS_C87289BB if x3 <= x0 - FOUR))
        x3 = _stream_columns_c87289bb(x1)
        x4 = _block_segments_c87289bb(x3, x1)
        gi = _render_input_c87289bb((x0, x1), x2, x3, x4)
        go = _render_output_c87289bb((x0, x1), x2, x3, x4)
        if gi != go:
            return {"input": gi, "output": go}
