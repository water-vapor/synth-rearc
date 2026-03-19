from arc2.core import *

from .verifier import verify_db7260a4


def _floor_patch_db7260a4(
    left: Integer,
    right: Integer,
    bottom: Integer,
    mode: str,
) -> Indices:
    if mode == "full":
        return connect((bottom, left), (bottom, right))
    if mode == "none":
        return frozenset()
    span = randint(ONE, right - left - ONE)
    if mode == "left":
        return connect((bottom, left), (bottom, left + span))
    return connect((bottom, right - span), (bottom, right))


def _draw_group_db7260a4(
    top: Integer,
    bottom: Integer,
    pillars: tuple[Integer, ...],
    modes: tuple[str, ...],
) -> tuple[Indices, tuple[tuple[Integer, Integer, Integer, Integer], ...]]:
    patch = set()
    spans = []
    for col in pillars:
        patch |= set(connect((top, col), (bottom, col)))
    for left, right, mode in zip(pillars, pillars[1:], modes):
        patch |= set(_floor_patch_db7260a4(left, right, bottom, mode))
        if mode == "full":
            spans.append((top, bottom, left, right))
    return frozenset(patch), tuple(spans)


def _sample_pillars_db7260a4() -> tuple[Integer, ...]:
    if choice((T, F)):
        left = randint(TWO, FOUR)
        middle = randint(left + TWO, SIX)
        right = randint(middle + TWO, EIGHT)
        return (left, middle, right)
    left = randint(TWO, FIVE)
    right = randint(left + TWO, NINE)
    return (left, right)


def _sample_partial_mode_db7260a4() -> str:
    return choice(("left", "right", "none"))


def _sample_valid_group_db7260a4(
    band: tuple[Integer, Integer],
) -> tuple[Indices, tuple[Integer, Integer, Integer, Integer]]:
    top, bottom = band
    pillars = _sample_pillars_db7260a4()
    if len(pillars) == TWO:
        patch, spans = _draw_group_db7260a4(top, bottom, pillars, ("full",))
        return patch, first(spans)
    target_idx = choice((ZERO, ONE))
    modes = [_sample_partial_mode_db7260a4(), _sample_partial_mode_db7260a4()]
    modes[target_idx] = "full"
    patch, spans = _draw_group_db7260a4(top, bottom, pillars, tuple(modes))
    return patch, first(spans)


def _sample_invalid_group_db7260a4(
    band: tuple[Integer, Integer],
) -> tuple[Indices, tuple[tuple[Integer, Integer], ...]]:
    top, bottom = band
    pillars = _sample_pillars_db7260a4()
    if len(pillars) == TWO:
        modes = (choice(("left", "right", "none")),)
        if first(modes) == "none":
            modes = (choice(("left", "right")),)
    else:
        modes = (
            _sample_partial_mode_db7260a4(),
            _sample_partial_mode_db7260a4(),
        )
        if modes == ("none", "none"):
            modes = (choice(("left", "right")), choice(("left", "right", "none")))
    patch, _ = _draw_group_db7260a4(top, bottom, pillars, modes)
    spans = tuple(zip(pillars, pillars[1:]))
    return patch, spans


def _target_patch_db7260a4(
    span: tuple[Integer, Integer, Integer, Integer],
) -> Indices:
    top, bottom, left, right = span
    rows = interval(top, bottom, ONE)
    cols = interval(left + ONE, right, ONE)
    return product(rows, cols)


def _marker_for_span_db7260a4(
    span: tuple[Integer, Integer, Integer, Integer],
) -> Integer:
    left = span[2]
    right = span[3]
    if choice((T, F, F)):
        return right
    return randint(left + ONE, right)


def _outside_marker_db7260a4(
    spans: tuple[tuple[Integer, Integer, Integer, Integer], ...],
) -> Integer:
    cols = [
        col
        for col in interval(ONE, TEN, ONE)
        if all(not (left < col <= right) for _, _, left, right in spans)
    ]
    return choice(cols)


def generate_db7260a4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    bands_single = ((THREE, SIX), (THREE, SIX), (TWO, FOUR), (SIX, EIGHT))
    bands_double = ((TWO, FOUR), (SIX, EIGHT))
    while True:
        base = canvas(ZERO, (TEN, TEN))
        fill_case = choice((T, T, F))
        if fill_case:
            use_double = choice((T, F, F))
            bands = bands_double if use_double else (choice(bands_single),)
            target_idx = randint(ZERO, len(bands) - ONE)
            target_span = None
            for idx, band in enumerate(bands):
                if idx == target_idx:
                    patch, target_span = _sample_valid_group_db7260a4(band)
                else:
                    patch, _ = _sample_invalid_group_db7260a4(band)
                base = fill(base, TWO, patch)
            marker_col = _marker_for_span_db7260a4(target_span)
            target_patch = _target_patch_db7260a4(target_span)
            go = fill(base, ONE, target_patch)
        else:
            fallback_valid = choice((T, F))
            if fallback_valid:
                band = choice(bands_single)
                patch, span = _sample_valid_group_db7260a4(band)
                spans = (span,)
                base = fill(base, TWO, patch)
                marker_col = _outside_marker_db7260a4(spans)
            else:
                band = choice(((THREE, SIX), (THREE, SIX), (TWO, FOUR)))
                patch, spans2 = _sample_invalid_group_db7260a4(band)
                base = fill(base, TWO, patch)
                choices = [
                    col
                    for left, right in spans2
                    for col in range(left + ONE, right + ONE)
                ]
                marker_col = choice(choices)
            go = fill(base, ONE, connect((NINE, ZERO), (NINE, NINE)))
        gi = fill(base, ONE, {(ZERO, marker_col)})
        if gi == go:
            continue
        if verify_db7260a4(gi) != go:
            continue
        return {"input": gi, "output": go}
