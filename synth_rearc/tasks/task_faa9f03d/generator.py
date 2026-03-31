from synth_rearc.core import *

from .helpers import GRID_SIDE_FAA9F03D
from .helpers import MARKER_COLORS_FAA9F03D
from .helpers import WIRE_COLORS_FAA9F03D
from .helpers import path_length_faa9f03d
from .helpers import polyline_cells_faa9f03d
from .helpers import sample_path_points_faa9f03d
from .helpers import solve_generated_faa9f03d
from .helpers import support_layers_faa9f03d


def _intersections_ok_faa9f03d(
    path_specs: tuple[dict, ...],
) -> Boolean:
    x0 = tuple(polyline_cells_faa9f03d(x1["points"]) for x1 in path_specs)
    x1 = set()
    x2 = set()
    for x3 in range(len(x0)):
        x4 = tuple(path_specs[x3]["points"][ONE:-ONE])
        x1.update(x4)
        for x5 in range(x3 + ONE, len(x0)):
            x6 = intersection(x0[x3], x0[x5])
            x2.update(x6)
    return x1.isdisjoint(x2)


def _sample_specs_faa9f03d(
    diff_lb: float,
    diff_ub: float,
) -> tuple[dict, ...]:
    x0 = choice((TWO, THREE, FOUR))
    x1 = tuple(sample(WIRE_COLORS_FAA9F03D, x0))
    x2 = tuple(choice(tuple(MARKER_COLORS_FAA9F03D)) for _ in range(x0))
    x3 = []
    for x4, x5 in zip(x1, x2):
        x6 = sample_path_points_faa9f03d(GRID_SIDE_FAA9F03D)
        x3.append({"color": x4, "marker": x5, "points": x6})
    x7 = tuple(x3)
    x8 = tuple(path_length_faa9f03d(x9["points"]) for x9 in x7)
    if len(set(x8)) != len(x8):
        raise RuntimeError("duplicate path lengths")
    x10 = merge(tuple(polyline_cells_faa9f03d(x11["points"]) for x11 in x7))
    x12 = sum(
        size(intersection(polyline_cells_faa9f03d(x13["points"]), polyline_cells_faa9f03d(x14["points"])))
        for x13, x14 in zip(x7, x7[ONE:])
    )
    if size(x10) < 18 or not _intersections_ok_faa9f03d(x7):
        raise RuntimeError("bad path geometry")
    return x7


def generate_faa9f03d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    x0 = astuple(GRID_SIDE_FAA9F03D, GRID_SIDE_FAA9F03D)
    for _ in range(400):
        try:
            x1 = _sample_specs_faa9f03d(diff_lb, diff_ub)
        except RuntimeError:
            continue
        x2, x3 = support_layers_faa9f03d(x0, x1)
        if x2 == x3:
            continue
        x4 = solve_generated_faa9f03d(x2)
        if x4 != x3:
            continue
        return {"input": x2, "output": x3}
    raise RuntimeError("failed to generate faa9f03d example")
