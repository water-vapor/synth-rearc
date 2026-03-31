from synth_rearc.core import *

from .helpers import erase_markers_8b9c3697
from .helpers import paint_routes_8b9c3697
from .helpers import route_specs_8b9c3697


def verify_8b9c3697(
    I: Grid,
) -> Grid:
    x0 = route_specs_8b9c3697(I)
    x1 = erase_markers_8b9c3697(I)
    x2 = paint_routes_8b9c3697(x1, x0)
    return x2
