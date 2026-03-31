from math import isqrt

from synth_rearc.core import *

from .helpers import NON_HOST_CORNERS_F560132C
from .helpers import place_patch_in_square_corner_f560132c, shape_variants_f560132c, square_indices_f560132c


def _assemble_non_host_f560132c(
    host: Indices,
    pieces: dict[str, Indices],
    side: int,
):
    x0 = square_indices_f560132c(side)
    x1 = {x2: shape_variants_f560132c(x3) for x2, x3 in pieces.items()}
    x2 = ("tr", "bl", "br")

    def x3(
        idx: int,
        occupied: Indices,
        placed: tuple[tuple[str, Indices], ...],
    ):
        if idx == THREE:
            return placed if frozenset(x0 - occupied) == host else None
        x4 = x2[idx]
        for x5 in x1[x4]:
            x6 = place_patch_in_square_corner_f560132c(x5, side, x4)
            if len(frozenset(x6 & occupied)) > ZERO:
                continue
            x7 = x3(
                increment(idx),
                frozenset(occupied | x6),
                placed + ((x4, x6),),
            )
            if x7 is not None:
                return x7
        return None

    x4 = x3(ZERO, frozenset(), ())
    if x4 is None:
        raise ValueError("could not reassemble non-host pieces")
    return {x5: x6 for x5, x6 in x4}


def verify_f560132c(
    I: Grid,
) -> Grid:
    x0 = objects(I, T, F, T)
    x1 = tuple(x2 for x2 in x0 if size(x2) == ONE)
    x2 = tuple(x3 for x3 in x0 if size(x3) > ONE)
    x3 = None
    x4 = ()
    for x5 in x2:
        x6 = tuple(
            x7 for x7 in x1
            if uppermost(x5) <= uppermost(x7) <= lowermost(x5)
            and leftmost(x5) <= leftmost(x7) <= rightmost(x5)
        )
        if len(x6) == FOUR:
            x3 = x5
            x4 = x6
            break
    if x3 is None:
        raise ValueError("missing host object")
    x5 = frozenset(normalize(toindices(x3) | frozenset(merge(apply(toindices, x4)))))
    x6 = tuple(x7 for x7 in x2 if x7 != x3)
    if len(x6) != THREE:
        raise ValueError("expected exactly three non-host pieces")
    x7 = argmin(x6, leftmost)
    x8 = tuple(x9 for x9 in x6 if x9 != x7)
    x9 = argmax(x8, size)
    x10 = other(x8, x9)
    x11 = {
        "tr": frozenset(normalize(toindices(x9))),
        "bl": frozenset(normalize(toindices(x10))),
        "br": frozenset(normalize(toindices(x7))),
    }
    x12 = size(x5) + sum(size(x13) for x13 in x11.values())
    x13 = isqrt(x12)
    if x13 * x13 != x12:
        raise ValueError("piece area does not form a square")
    x14 = _assemble_non_host_f560132c(x5, x11, x13)
    x15 = {first(toindices(x16)): color(x16) for x16 in x4}
    x16 = tuple(sorted({x17 for x17, _ in x15}))
    x17 = tuple(sorted({x18 for _, x18 in x15}))
    if len(x16) != TWO or len(x17) != TWO:
        raise ValueError("expected a 2x2 color key")
    x18 = x15[(x16[0], x17[0])]
    x19 = x15[(x16[0], x17[1])]
    x20 = x15[(x16[1], x17[0])]
    x21 = x15[(x16[1], x17[1])]
    x22 = canvas(x18, (x13, x13))
    x22 = fill(x22, x19, x14["tr"])
    x22 = fill(x22, x20, x14["bl"])
    x22 = fill(x22, x21, x14["br"])
    return x22
