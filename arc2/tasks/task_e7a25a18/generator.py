from arc2.core import *


def _rect_e7a25a18(
    top: Integer,
    left: Integer,
    h: Integer,
    w: Integer,
) -> Indices:
    return frozenset((i, j) for i in range(top, top + h) for j in range(left, left + w))


def generate_e7a25a18(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    h = 14
    w = 14
    scale = unifint(diff_lb, diff_ub, (ONE, TWO))
    frame_size = 4 * scale + TWO
    top = randint(ONE, h - frame_size)
    left = randint(ONE, w - frame_size)
    motif_top = top + ONE + choice((ZERO, ONE))
    motif_left = left + TWO
    colors = sample((ONE, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE), FOUR)
    template = canvas(ZERO, (double(scale), double(scale)))
    gi = canvas(ZERO, (h, w))
    frame = box(_rect_e7a25a18(top, left, frame_size, frame_size))
    gi = fill(gi, TWO, frame)
    offsets = ((ZERO, ZERO), (ZERO, scale), (scale, ZERO), (scale, scale))
    for color, (di, dj) in zip(colors, offsets):
        block = _rect_e7a25a18(motif_top + di, motif_left + dj, scale, scale)
        gi = fill(gi, color, block)
        block_template = _rect_e7a25a18(di, dj, scale, scale)
        template = fill(template, color, block_template)
    go = canvas(TWO, (frame_size, frame_size))
    go = paint(go, shift(asobject(upscale(template, TWO)), astuple(ONE, ONE)))
    return {"input": gi, "output": go}
