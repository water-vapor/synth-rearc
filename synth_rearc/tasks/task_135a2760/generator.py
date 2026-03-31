from synth_rearc.core import *

from .helpers import HORIZONTAL_MULTI_KINDS_135a2760
from .helpers import VERTICAL_KINDS_135a2760
from .helpers import assemble_horizontal_135a2760
from .helpers import assemble_vertical_135a2760
from .helpers import corrupt_panel_135a2760
from .helpers import odd_length_135a2760
from .helpers import render_panel_135a2760
from .verifier import verify_135a2760


def _color_pool_135a2760(
    bg: int,
    border: int,
) -> tuple[int, ...]:
    return tuple(color for color in interval(ZERO, TEN, ONE) if color not in (bg, border))


def _single_horizontal_example_135a2760(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    bg = choice(interval(ZERO, TEN, ONE))
    border = choice(tuple(color for color in interval(ZERO, TEN, ONE) if color != bg))
    fg = choice(_color_pool_135a2760(bg, border))
    long_dim = odd_length_135a2760(diff_lb, diff_ub, (SEVEN, 25))
    output_panel = render_panel_135a2760("h_alt1", long_dim, fg, border, bg)
    input_panel = corrupt_panel_135a2760(output_panel, bg)
    gi = assemble_horizontal_135a2760((input_panel,), bg)
    go = assemble_horizontal_135a2760((output_panel,), bg)
    return {"input": gi, "output": go}


def _stacked_horizontal_example_135a2760(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    bg = choice(interval(ZERO, TEN, ONE))
    border = choice(tuple(color for color in interval(ZERO, TEN, ONE) if color != bg))
    kinds = list(HORIZONTAL_MULTI_KINDS_135a2760)
    shuffle(kinds)
    fgs = sample(_color_pool_135a2760(bg, border), len(kinds))
    long_dim = unifint(diff_lb, diff_ub, (14, 26))
    output_panels = tuple(render_panel_135a2760(kind, long_dim, fg, border, bg) for kind, fg in zip(kinds, fgs))
    input_panels = tuple(corrupt_panel_135a2760(panel, bg) for panel in output_panels)
    gi = assemble_horizontal_135a2760(input_panels, bg)
    go = assemble_horizontal_135a2760(output_panels, bg)
    return {"input": gi, "output": go}


def _vertical_example_135a2760(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    bg = choice(interval(ZERO, TEN, ONE))
    border = choice(tuple(color for color in interval(ZERO, TEN, ONE) if color != bg))
    kinds = list(VERTICAL_KINDS_135a2760)
    shuffle(kinds)
    fgs = sample(_color_pool_135a2760(bg, border), len(kinds))
    long_dim = unifint(diff_lb, diff_ub, (17, 26))
    output_panels = tuple(render_panel_135a2760(kind, long_dim, fg, border, bg) for kind, fg in zip(kinds, fgs))
    input_panels = tuple(corrupt_panel_135a2760(panel, bg) for panel in output_panels)
    gi = assemble_vertical_135a2760(input_panels, bg)
    go = assemble_vertical_135a2760(output_panels, bg)
    return {"input": gi, "output": go}


def generate_135a2760(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    builders = (
        _single_horizontal_example_135a2760,
        _stacked_horizontal_example_135a2760,
        _vertical_example_135a2760,
    )
    while True:
        example = choice(builders)(diff_lb, diff_ub)
        if example["input"] == example["output"]:
            continue
        if verify_135a2760(example["input"]) != example["output"]:
            continue
        return example
