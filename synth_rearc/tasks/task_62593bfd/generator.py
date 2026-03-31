from synth_rearc.core import *

from .verifier import verify_62593bfd


TOP_TEMPLATE_STRINGS_62593BFD = (
    "#####/..#../..#..",
    "..#/..#/###/..#/..#",
    "###/#.#/###/.#.",
    "###./#.##/###.",
    "..###/..#../###..",
    "..#./####/..#./..#.",
    ".#../.#../####/.#..",
    "#../#../###/..#/..#",
    ".#/##",
    "##/#.",
)
BOTTOM_TEMPLATE_STRINGS_62593BFD = (
    "##/.#/.#/.#",
    "..#/###",
    ".#./.#./###",
    "###/.#./.#.",
    "#.../####/.#..",
    "....#/.###./.###./.###./#....",
    "#..../.###./.#.#./.###./#...#",
    "#...#/.###./.#.#./.###./#...#",
    ".#./#.#/.#.",
)
GRID_HEIGHT_BOUNDS_62593BFD = (18, 30)
GRID_WIDTH_BOUNDS_62593BFD = (18, 30)
TOP_COUNT_BOUNDS_62593BFD = (2, 4)
BOTTOM_COUNT_BOUNDS_62593BFD = (2, 3)


def _parse_patch_62593bfd(
    text: str,
) -> Indices:
    return frozenset(
        (i, j)
        for i, row in enumerate(text.split("/"))
        for j, value in enumerate(row)
        if value == "#"
    )


def _canonical_patch_62593bfd(
    patch: Indices,
) -> tuple[tuple[int, int], ...]:
    x0 = normalize(patch)
    return tuple(sorted(x0))


def _symmetries_62593bfd(
    patch: Indices,
) -> tuple[Indices, ...]:
    x0 = (
        patch,
        hmirror(patch),
        vmirror(patch),
        dmirror(patch),
        cmirror(patch),
        hmirror(dmirror(patch)),
        vmirror(dmirror(patch)),
        hmirror(vmirror(patch)),
    )
    x1 = {}
    for x2 in x0:
        x3 = normalize(x2)
        x1[_canonical_patch_62593bfd(x3)] = x3
    return tuple(x1.values())


def _build_bank_62593bfd(
    templates: tuple[str, ...],
) -> tuple[Indices, ...]:
    x0 = {}
    for x1 in templates:
        x2 = _parse_patch_62593bfd(x1)
        for x3 in _symmetries_62593bfd(x2):
            x0[_canonical_patch_62593bfd(x3)] = x3
    return tuple(x0.values())


TOP_PATCHES_62593BFD = _build_bank_62593bfd(TOP_TEMPLATE_STRINGS_62593BFD)
BOTTOM_PATCHES_62593BFD = _build_bank_62593bfd(BOTTOM_TEMPLATE_STRINGS_62593BFD)


def _placement_options_62593bfd(
    patch: Indices,
    row: Integer,
    width_: Integer,
    occupied: Indices,
) -> tuple[Indices, ...]:
    x0 = width(patch)
    x1 = []
    for x2 in range(width_ - x0 + ONE):
        x3 = shift(patch, (row, x2))
        if size(intersection(x3, occupied)) == ZERO:
            x1.append(x3)
    return tuple(x1)


def _sample_side_placements_62593bfd(
    patches: tuple[Indices, ...],
    side: str,
    height_: Integer,
    width_: Integer,
) -> tuple[Indices, ...] | None:
    x0 = []
    x1 = frozenset()
    x2 = tuple(sorted(patches, key=lambda x3: (width(x3), height(x3)), reverse=True))
    for x3 in x2:
        x4 = ZERO if side == "top" else subtract(height_, height(x3))
        x5 = _placement_options_62593bfd(x3, x4, width_, x1)
        if len(x5) == ZERO:
            return None
        x6 = choice(x5)
        x0.append(x6)
        x1 = combine(x1, x6)
    return tuple(x0)


def _sample_input_placement_62593bfd(
    output_patch: Indices,
    height_: Integer,
    occupied: Indices,
) -> Indices | None:
    x0 = height(output_patch)
    if x0 > subtract(height_, TWO):
        return None
    x1 = leftmost(output_patch)
    x2 = tuple(
        x3
        for x3 in range(ONE, subtract(subtract(height_, x0), ONE))
    )
    x3 = tuple(sample(x2, len(x2)))
    for x4 in x3:
        x5 = shift(normalize(output_patch), (x4, x1))
        if size(intersection(x5, occupied)) == ZERO:
            return x5
    return None


def _assemble_grid_62593bfd(
    bg: Integer,
    dims: IntegerTuple,
    colored_patches: tuple[tuple[Integer, Indices], ...],
) -> Grid:
    x0 = canvas(bg, dims)
    for x1, x2 in colored_patches:
        x0 = fill(x0, x1, x2)
    return x0


def generate_62593bfd(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = unifint(diff_lb, diff_ub, GRID_HEIGHT_BOUNDS_62593BFD)
        x1 = unifint(diff_lb, diff_ub, GRID_WIDTH_BOUNDS_62593BFD)
        x2 = unifint(diff_lb, diff_ub, TOP_COUNT_BOUNDS_62593BFD)
        x3 = unifint(diff_lb, diff_ub, BOTTOM_COUNT_BOUNDS_62593BFD)
        x4 = x2 + x3
        if x4 > NINE:
            continue
        x5 = choice(interval(ZERO, TEN, ONE))
        x6 = tuple(x7 for x7 in interval(ZERO, TEN, ONE) if x7 != x5)
        x7 = tuple(sample(x6, x4))
        x8 = tuple(choice(TOP_PATCHES_62593BFD) for _ in range(x2))
        x9 = tuple(choice(BOTTOM_PATCHES_62593BFD) for _ in range(x3))
        x10 = _sample_side_placements_62593bfd(x8, "top", x0, x1)
        if x10 is None:
            continue
        x11 = _sample_side_placements_62593bfd(x9, "bottom", x0, x1)
        if x11 is None:
            continue
        x12 = combine(x10, x11)
        x13 = []
        x14 = frozenset()
        failed = False
        for x15 in tuple(sample(x12, len(x12))):
            x16 = _sample_input_placement_62593bfd(x15, x0, x14)
            if x16 is None:
                failed = True
                break
            x13.append((x15, x16))
            x14 = combine(x14, x16)
        if failed:
            continue
        x17 = {tuple(sorted(x18)): x19 for x18, x19 in x13}
        x20 = tuple((x21, x22) for x21, x22 in zip(x7[:x2], x10))
        x21 = tuple((x22, x23) for x22, x23 in zip(x7[x2:], x11))
        x22 = combine(x20, x21)
        x23 = tuple((x24, x17[tuple(sorted(x25))]) for x24, x25 in x22)
        x24 = _assemble_grid_62593bfd(x5, (x0, x1), x23)
        x25 = _assemble_grid_62593bfd(x5, (x0, x1), x22)
        if equality(x24, x25):
            continue
        if verify_62593bfd(x24) != x25:
            continue
        return {"input": x24, "output": x25}
