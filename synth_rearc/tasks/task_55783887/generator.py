from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_55783887


BG_COLORS_55783887 = (FOUR, FIVE, EIGHT)


def _segment_cells_55783887(
    start: IntegerTuple,
    end: IntegerTuple,
) -> tuple[IntegerTuple, ...]:
    return tuple(sorted(connect(start, end)))


def _perpendicular_line_55783887(
    loc: IntegerTuple,
    main_backslash: Boolean,
) -> Indices:
    if main_backslash:
        return combine(shoot(loc, UP_RIGHT), shoot(loc, DOWN_LEFT))
    return combine(shoot(loc, NEG_UNITY), shoot(loc, UNITY))


def _is_diagonal_55783887(
    a: IntegerTuple,
    b: IntegerTuple,
) -> Boolean:
    return abs(a[0] - b[0]) == abs(a[1] - b[1])


def _pick_isolated_noise_55783887(
    candidates: set[IntegerTuple],
    count: Integer,
    anchors: tuple[IntegerTuple, ...],
) -> tuple[IntegerTuple, ...]:
    pool = list(candidates)
    shuffle(pool)
    picked: list[IntegerTuple] = []
    for loc in pool:
        if any(_is_diagonal_55783887(loc, other) for other in (*anchors, *picked)):
            continue
        picked.append(loc)
        if len(picked) == count:
            break
    return tuple(picked)


def generate_55783887(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        bgc = choice(BG_COLORS_55783887)
        h = unifint(diff_lb, diff_ub, (EIGHT, 19))
        w = unifint(diff_lb, diff_ub, (NINE, 18))
        span = min(h, w) - ONE
        if span < FIVE:
            continue
        main_backslash = choice((T, F))
        seglen = unifint(diff_lb, diff_ub, (FIVE, span))
        if main_backslash:
            start = (randint(ZERO, h - seglen - ONE), randint(ZERO, w - seglen - ONE))
            end = add(start, (seglen, seglen))
        else:
            start = (randint(ZERO, h - seglen - ONE), randint(seglen, w - ONE))
            end = (start[0] + seglen, start[1] - seglen)
        segment = _segment_cells_55783887(start, end)
        interior = segment[1:-1]
        npivots = unifint(diff_lb, diff_ub, (ZERO, min(TWO, len(interior))))
        pivots = tuple(sorted(sample(interior, npivots))) if npivots > ZERO else ()

        full_six_lines = frozenset()
        for loc in pivots:
            full_six_lines = combine(full_six_lines, _perpendicular_line_55783887(loc, main_backslash))

        all_cells = set(asindices(canvas(bgc, (h, w))))
        blocked = set(segment) | set(full_six_lines)

        nnoise1 = unifint(diff_lb, diff_ub, (ZERO, TWO))
        noise1 = _pick_isolated_noise_55783887(all_cells - blocked, nnoise1, (start, end))
        if len(noise1) != nnoise1:
            continue

        nnoise6 = unifint(diff_lb, diff_ub, (ZERO, THREE))
        noise6_cands = all_cells - blocked - set(noise1)
        noise6 = _pick_isolated_noise_55783887(noise6_cands, nnoise6, pivots)
        if len(noise6) != nnoise6:
            continue

        gi = canvas(bgc, (h, w))
        gi = fill(gi, ONE, frozenset({start, end}))
        gi = fill(gi, ONE, frozenset(noise1))
        gi = fill(gi, SIX, frozenset(pivots))
        gi = fill(gi, SIX, frozenset(noise6))

        go = underfill(gi, ONE, frozenset(segment))
        go = paint(go, recolor(SIX, full_six_lines))

        if verify_55783887(gi) != go:
            continue
        return {"input": gi, "output": go}
