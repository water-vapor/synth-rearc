from synth_rearc.core import *


MOTIFS_DF9FD884 = {
    ONE: (
        frozenset({(ZERO, ZERO)}),
        frozenset({(ZERO, ZERO), (ONE, ZERO)}),
        frozenset({(ZERO, ZERO), (ONE, ZERO), (TWO, ZERO)}),
    ),
    TWO: (
        frozenset({(ZERO, ZERO), (ZERO, ONE)}),
        frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE)}),
        frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO)}),
        frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ONE)}),
        frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
        frozenset({(ZERO, ZERO), (ONE, ZERO), (ONE, ONE), (TWO, ZERO)}),
        frozenset({(ZERO, ONE), (ONE, ZERO), (ONE, ONE), (TWO, ONE)}),
        frozenset({(ZERO, ZERO), (ZERO, ONE), (ONE, ZERO), (ONE, ONE)}),
    ),
}


def _frame_df9fd884(
    top: Integer,
    left: Integer,
    gapw: Integer,
) -> Indices:
    width0 = add(gapw, TWO)
    topbar = frozenset((top, j) for j in range(left, add(left, width0)))
    legs = frozenset({(add(top, ONE), left), (add(top, ONE), add(add(left, width0), NEG_ONE))})
    return combine(topbar, legs)


def generate_df9fd884(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    cols = remove(FOUR, remove(SEVEN, interval(ONE, TEN, ONE)))
    while True:
        side = choice((EIGHT, NINE))
        gapw = choice((ONE, TWO))
        framew = add(gapw, TWO)
        upper_left = choice((T, F))
        upper_frame_left = ZERO if upper_left else subtract(side, framew)
        lower_frame_left = subtract(side, framew) if upper_left else ZERO
        upper_frame = _frame_df9fd884(ZERO, upper_frame_left, gapw)
        lower_frame = _frame_df9fd884(subtract(side, TWO), lower_frame_left, gapw)
        target_left = leftmost(delta(upper_frame))
        source_left = leftmost(delta(lower_frame))
        motif = choice(MOTIFS_DF9FD884[gapw])
        motif_h = height(motif)
        max_top = subtract(subtract(side, THREE), motif_h)
        if max_top < ONE:
            continue
        src_top = randint(ONE, max_top)
        dst_top = subtract(side, motif_h)
        color0 = choice(cols)
        gi = canvas(SEVEN, (side, side))
        gi = paint(gi, recolor(FOUR, upper_frame))
        gi = paint(gi, recolor(FOUR, lower_frame))
        src_obj = recolor(color0, shift(motif, (src_top, source_left)))
        dst_obj = recolor(color0, shift(motif, (dst_top, target_left)))
        gi = paint(gi, src_obj)
        go = cover(gi, src_obj)
        go = paint(go, dst_obj)
        return {"input": gi, "output": go}
