from synth_rearc.core import *


TRANSFORMS_898E7135 = (
    identity,
    rot90,
    rot180,
    rot270,
    hmirror,
    vmirror,
    dmirror,
    cmirror,
)


def _grid_from_patch_898e7135(
    patch: Patch,
) -> Grid:
    x0 = normalize(toindices(patch))
    x1 = canvas(ZERO, shape(x0))
    return fill(x1, ONE, x0)


def canonical_patch_898e7135(
    patch: Patch,
) -> frozenset[IntegerTuple]:
    x0 = _grid_from_patch_898e7135(patch)
    x1 = []
    for x2 in TRANSFORMS_898E7135:
        x3 = frozenset(normalize(ofcolor(x2(x0), ONE)))
        x1.append(x3)
    return min(x1, key=lambda x4: (height(x4), width(x4), tuple(sorted(x4))))


def oriented_variants_898e7135(
    patch: Patch,
) -> tuple[frozenset[IntegerTuple], ...]:
    x0 = _grid_from_patch_898e7135(patch)
    x1 = []
    x2 = set()
    for x3 in TRANSFORMS_898E7135:
        x4 = frozenset(normalize(ofcolor(x3(x0), ONE)))
        if x4 in x2:
            continue
        x2.add(x4)
        x1.append(x4)
    return tuple(x1)


def scaled_local_patch_898e7135(
    patch: Patch,
    factor: Integer,
) -> frozenset[IntegerTuple]:
    x0 = toindices(patch)
    x1 = recolor(ONE, normalize(x0))
    x2 = toindices(upscale(x1, factor))
    x3 = multiply(ulcorner(x0), factor)
    return shift(x2, x3)
