from synth_rearc.core import *


PALETTE_59341089 = (FIVE, SEVEN, EIGHT)
PALETTE_SIZE_RANGE_59341089 = (TWO, THREE)


def _sample_input_59341089(colors: tuple[int, ...]) -> Grid:
    return tuple(tuple(choice(colors) for _ in range(THREE)) for _ in range(THREE))


def generate_59341089(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, PALETTE_SIZE_RANGE_59341089)
        x1 = tuple(sample(PALETTE_59341089, x0))
        gi = _sample_input_59341089(x1)
        x2 = palette(gi)
        x3 = size(x2)
        if x3 != x0:
            continue
        x4 = vmirror(gi)
        x5 = hconcat(x4, gi)
        go = hconcat(x5, x5)
        return {"input": gi, "output": go}
