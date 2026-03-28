from synth_rearc.core import *

from .verifier import verify_281123b4


PANEL_SHAPE_281123B4 = (FOUR, FOUR)
INPUT_PANEL_COLORS_281123B4 = (EIGHT, FIVE, NINE, FOUR)
SEPARATOR_281123B4 = canvas(THREE, (FOUR, ONE))
ALL_PANEL_CELLS_281123B4 = totuple(asindices(canvas(ZERO, PANEL_SHAPE_281123B4)))
PANEL_DENSITY_BOUNDS_281123B4 = {
    EIGHT: (FIVE, 11),
    FIVE: (SEVEN, 12),
    NINE: (SIX, NINE),
    FOUR: (SIX, TEN),
}


def _sample_patch_281123b4(
    diff_lb: float,
    diff_ub: float,
    color_: Integer,
) -> Indices:
    x0 = unifint(diff_lb, diff_ub, PANEL_DENSITY_BOUNDS_281123B4[color_])
    x1 = sample(ALL_PANEL_CELLS_281123B4, x0)
    return frozenset(x1)


def _render_panel_281123b4(
    color_: Integer,
    patch: Indices,
) -> Grid:
    x0 = canvas(ZERO, PANEL_SHAPE_281123B4)
    x1 = fill(x0, color_, patch)
    return x1


def _render_output_281123b4(
    panels: tuple[Grid, Grid, Grid, Grid],
) -> Grid:
    x0 = canvas(ZERO, PANEL_SHAPE_281123B4)
    x1 = fill(x0, FIVE, ofcolor(panels[1], FIVE))
    x2 = fill(x1, EIGHT, ofcolor(panels[0], EIGHT))
    x3 = fill(x2, FOUR, ofcolor(panels[3], FOUR))
    x4 = fill(x3, NINE, ofcolor(panels[2], NINE))
    return x4


def _assemble_input_281123b4(
    panels: tuple[Grid, Grid, Grid, Grid],
) -> Grid:
    x0 = hconcat(panels[0], SEPARATOR_281123B4)
    x1 = hconcat(x0, panels[1])
    x2 = hconcat(x1, SEPARATOR_281123B4)
    x3 = hconcat(x2, panels[2])
    x4 = hconcat(x3, SEPARATOR_281123B4)
    x5 = hconcat(x4, panels[3])
    return x5


def generate_281123b4(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        patches = tuple(
            _sample_patch_281123b4(diff_lb, diff_ub, color_)
            for color_ in INPUT_PANEL_COLORS_281123B4
        )
        panels = tuple(
            _render_panel_281123b4(color_, patch)
            for color_, patch in zip(INPUT_PANEL_COLORS_281123B4, patches)
        )
        gi = _assemble_input_281123b4(panels)
        go = _render_output_281123b4(panels)
        x0 = palette(go)
        x1 = contained(EIGHT, x0)
        x2 = contained(FOUR, x0)
        x3 = contained(NINE, x0)
        x4 = greater(numcolors(go), THREE)
        if not both(both(x1, x2), both(x3, x4)):
            continue
        if verify_281123b4(gi) != go:
            continue
        return {"input": gi, "output": go}
