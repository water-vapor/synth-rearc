from synth_rearc.core import *

from .verifier import verify_817e6c09


GRID_HEIGHT_817E6C09 = SEVEN
BLOCK_SIZE_817E6C09 = TWO
MIN_WIDTH_817E6C09 = FIVE
MAX_WIDTH_817E6C09 = 18
MAX_BLOCKS_817E6C09 = NINE
GAP_CHOICES_817E6C09 = (ONE, TWO, TWO, THREE)
MARGIN_CHOICES_817E6C09 = (ZERO, ZERO, ONE, TWO)


def _block_patch_817e6c09(
    top: Integer,
    left: Integer,
) -> Indices:
    x0 = interval(top, top + BLOCK_SIZE_817E6C09, ONE)
    x1 = interval(left, left + BLOCK_SIZE_817E6C09, ONE)
    return product(x0, x1)


def _sample_layout_817e6c09() -> tuple[Integer, tuple[tuple[Integer, Integer], ...]] | None:
    x0 = randint(TWO, MAX_BLOCKS_817E6C09)
    x1 = choice(MARGIN_CHOICES_817E6C09)
    x2 = choice(MARGIN_CHOICES_817E6C09)
    x3 = [x1]
    for _ in range(x0 - ONE):
        x3.append(x3[-ONE] + choice(GAP_CHOICES_817E6C09))
    x4 = x3[-ONE] + BLOCK_SIZE_817E6C09 + x2
    if x4 < MIN_WIDTH_817E6C09 or x4 > MAX_WIDTH_817E6C09:
        return None
    x5 = tuple(interval(ZERO, GRID_HEIGHT_817E6C09 - ONE, ONE))
    x6 = []
    x7 = []
    for x8 in x3:
        x9 = list(x5)
        shuffle(x9)
        x10 = False
        for x11 in x9:
            x12 = _block_patch_817e6c09(x11, x8)
            if all(manhattan(x12, x13) > ONE for x13 in x7):
                x6.append((x11, x8))
                x7.append(x12)
                x10 = True
                break
        if not x10:
            return None
    return x4, tuple(x6)


def _render_input_817e6c09(
    width_value: Integer,
    blocks: tuple[tuple[Integer, Integer], ...],
) -> Grid:
    x0 = canvas(ZERO, (GRID_HEIGHT_817E6C09, width_value))
    x1 = x0
    for x2, x3 in blocks:
        x4 = _block_patch_817e6c09(x2, x3)
        x1 = fill(x1, TWO, x4)
    return x1


def _render_output_817e6c09(
    gi: Grid,
    blocks: tuple[tuple[Integer, Integer], ...],
) -> Grid:
    x0 = gi
    x1 = len(blocks) - ONE
    for x2, (x3, x4) in enumerate(blocks):
        if (x1 - x2) % TWO == ZERO:
            x5 = _block_patch_817e6c09(x3, x4)
            x0 = fill(x0, EIGHT, x5)
    return x0


def generate_817e6c09(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = _sample_layout_817e6c09()
        if x0 is None:
            continue
        x1, x2 = x0
        gi = _render_input_817e6c09(x1, x2)
        go = _render_output_817e6c09(gi, x2)
        if gi == go:
            continue
        if verify_817e6c09(gi) != go:
            continue
        return {"input": gi, "output": go}
