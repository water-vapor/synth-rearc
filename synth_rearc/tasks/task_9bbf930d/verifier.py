from synth_rearc.core import *

from .helpers import trace_launcher_9bbf930d, tunnel_maps_9bbf930d


def verify_9bbf930d(
    I: Grid,
) -> Grid:
    x0, x1 = tunnel_maps_9bbf930d(I)
    x2 = I
    x3 = height(I)
    for x4 in range(x3):
        x5 = trace_launcher_9bbf930d(I, x4, x0, x1)
        if x5 == (x4, ZERO):
            continue
        x2 = fill(x2, SEVEN, {(x4, ZERO)})
        x2 = fill(x2, SIX, {x5})
    return x2
