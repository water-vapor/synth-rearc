from synth_rearc.core import *

from .helpers import relocate_cluster_pairs_a25697e4


def verify_a25697e4(
    I: Grid,
) -> Grid:
    x0 = relocate_cluster_pairs_a25697e4(I)
    return x0
