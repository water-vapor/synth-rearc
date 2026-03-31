from synth_rearc.core import *

from .helpers import apply_variant_grid_d35bdbdc
from .helpers import build_layout_grids_d35bdbdc
from .helpers import LAYOUT_FAMILIES_D35BDBDC
from .helpers import NON_FIVE_COLORS_D35BDBDC
from .verifier import verify_d35bdbdc


def _target_map_d35bdbdc(
    kept_indices: tuple[int, ...],
    motif_count: int,
) -> dict[int, int]:
    removed = [idx for idx in range(motif_count) if idx not in kept_indices]
    shuffle(removed)
    return {keep: target for keep, target in zip(kept_indices, removed)}


def _center_colors_d35bdbdc(
    outer_colors: tuple[int, ...],
    kept_indices: tuple[int, ...],
    target_map: dict[int, int],
) -> tuple[int, ...]:
    x0 = [choice(NON_FIVE_COLORS_D35BDBDC) for _ in outer_colors]
    for x1 in range(len(outer_colors)):
        if choice((T, F, F)):
            x0[x1] = outer_colors[x1]
        elif choice((T, F, F)):
            x0[x1] = outer_colors[choice(tuple(range(len(outer_colors))))]
    for x2 in kept_indices:
        x0[x2] = outer_colors[target_map[x2]]
    return tuple(x0)


def generate_d35bdbdc(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    del diff_lb, diff_ub
    while True:
        x0 = choice(LAYOUT_FAMILIES_D35BDBDC)
        x1 = len(x0["motifs"])
        x2 = tuple(sample(NON_FIVE_COLORS_D35BDBDC, x1))
        x3 = _target_map_d35bdbdc(x0["kept_indices"], x1)
        x4 = _center_colors_d35bdbdc(x2, x0["kept_indices"], x3)
        x5, x6 = build_layout_grids_d35bdbdc(x0, x2, x4, x3)
        x7 = choice(tuple(range(EIGHT)))
        x8 = apply_variant_grid_d35bdbdc(x5, x7)
        x9 = apply_variant_grid_d35bdbdc(x6, x7)
        if equality(x8, x9):
            continue
        if verify_d35bdbdc(x8) != x9:
            continue
        return {"input": x8, "output": x9}
