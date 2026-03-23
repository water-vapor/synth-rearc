from arc2.core import *

from .verifier import verify_20fb2937


INPUT_SHAPE_20FB2937 = (20, 11)
OUTPUT_SHAPE_20FB2937 = (13, 11)
HEADER_PATCH_20FB2937 = backdrop(frozenset({ORIGIN, TWO_BY_TWO}))
HEADER_LEFTS_20FB2937 = (ZERO, FOUR, EIGHT)
LEGEND_COLS_20FB2937 = (ONE, FIVE, NINE)


def _stamp_patch_20fb2937(
    loc: IntegerTuple,
) -> Indices:
    x0 = subtract(loc, UNITY)
    x1 = add(loc, UNITY)
    x2 = frozenset({x0, x1})
    x3 = backdrop(x2)
    return x3


def _sample_centers_20fb2937(
    total: Integer,
) -> tuple[IntegerTuple, ...]:
    x0 = tuple(
        (i, j)
        for i in range(ONE, 12)
        for j in range(ONE, 10)
    )
    for _ in range(400):
        x1 = tuple()
        for _ in range(total):
            x2 = tuple(
                x3 for x3 in x0
                if all(
                    either(
                        greater(abs(subtract(x3[0], x4[0])), TWO),
                        greater(abs(subtract(x3[1], x4[1])), TWO),
                    )
                    for x4 in x1
                )
            )
            if len(x2) == ZERO:
                break
            x5 = choice(x2)
            x1 = x1 + (x5,)
        if len(x1) != total:
            continue
        x6 = any(i in (ONE, 11) or j in (ONE, NINE) for i, j in x1)
        if not x6:
            continue
        x7 = any(
            either(
                equality(x8[0], x9[0]),
                equality(x8[1], x9[1]),
            )
            for x10, x8 in enumerate(x1)
            for x9 in x1[x10 + ONE:]
        )
        if not x7:
            continue
        return x1
    raise RuntimeError("failed to sample lower marker centers")


def _marker_counts_20fb2937(
    total: Integer,
) -> tuple[Integer, Integer, Integer]:
    x0 = branch(
        equality(total, EIGHT),
        ((TWO, TWO, FOUR), (TWO, THREE, THREE)),
        ((TWO, THREE, FOUR), (THREE, THREE, THREE)),
    )
    x1 = list(choice(x0))
    shuffle(x1)
    x2 = tuple(x1)
    return x2


def _assign_markers_20fb2937(
    centers: tuple[IntegerTuple, ...],
    marker_colors: tuple[Integer, Integer, Integer],
    counts: tuple[Integer, Integer, Integer],
) -> tuple[Integer, ...] | None:
    x0 = len(centers)
    x1 = tuple(
        frozenset(
            x2 for x2 in range(x0)
            if x2 != x3 and both(
                abs(subtract(centers[x2][0], centers[x3][0])) <= THREE,
                abs(subtract(centers[x2][1], centers[x3][1])) <= THREE,
            )
        )
        for x3 in range(x0)
    )
    x2 = sorted(range(x0), key=lambda x3: len(x1[x3]), reverse=True)
    x3 = [None] * x0
    x4 = {x5: x6 for x5, x6 in zip(marker_colors, counts)}

    def dfs(
        depth: int,
    ) -> bool:
        if depth == x0:
            return True
        x5 = x2[depth]
        x6 = list(marker_colors)
        shuffle(x6)
        for x7 in x6:
            if x4[x7] == ZERO:
                continue
            if any(x3[x8] == x7 for x8 in x1[x5]):
                continue
            x3[x5] = x7
            x4[x7] = subtract(x4[x7], ONE)
            if dfs(add(depth, ONE)):
                return True
            x4[x7] = add(x4[x7], ONE)
            x3[x5] = None
        return False

    if dfs(ZERO):
        return tuple(x3)
    return None


def _paint_header_20fb2937(
    grid: Grid,
    colors: tuple[Integer, Integer, Integer],
) -> Grid:
    x0 = grid
    for x1, x2 in zip(HEADER_LEFTS_20FB2937, colors):
        x3 = shift(HEADER_PATCH_20FB2937, (ZERO, x1))
        x0 = fill(x0, x2, x3)
    return x0


def _paint_legend_20fb2937(
    grid: Grid,
    marker_colors: tuple[Integer, Integer, Integer],
) -> Grid:
    x0 = grid
    for x1, x2 in zip(LEGEND_COLS_20FB2937, marker_colors):
        x3 = frozenset({(FOUR, x1)})
        x0 = fill(x0, x2, x3)
    return x0


def _paint_lower_markers_20fb2937(
    grid: Grid,
    centers: tuple[IntegerTuple, ...],
    marker_bag: tuple[Integer, ...],
) -> Grid:
    x0 = grid
    for x1, x2 in zip(centers, marker_bag):
        x3 = add(x1, (SEVEN, ZERO))
        x4 = frozenset({x3})
        x0 = fill(x0, x2, x4)
    return x0


def _paint_output_20fb2937(
    centers: tuple[IntegerTuple, ...],
    marker_bag: tuple[Integer, ...],
    marker_to_paint: dict[Integer, Integer],
) -> Grid:
    x0 = canvas(SEVEN, OUTPUT_SHAPE_20FB2937)
    for x1, x2 in zip(centers, marker_bag):
        x3 = _stamp_patch_20fb2937(x1)
        x4 = marker_to_paint[x2]
        x0 = fill(x0, x4, x3)
    return x0


def generate_20fb2937(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = tuple(x1 for x1 in interval(ZERO, TEN, ONE) if x1 != SEVEN)
        x1 = tuple(sample(x0, THREE))
        x2 = tuple(x3 for x3 in x0 if x3 not in x1)
        x3 = tuple(sample(x2, THREE))
        x4 = choice((EIGHT, EIGHT, NINE))
        x5 = _marker_counts_20fb2937(x4)
        x6 = _sample_centers_20fb2937(x4)
        x10 = _assign_markers_20fb2937(x6, x3, x5)
        if x10 is None:
            continue
        x11 = {x12: x13 for x12, x13 in zip(x3, x1)}
        gi = canvas(SEVEN, INPUT_SHAPE_20FB2937)
        gi = _paint_header_20fb2937(gi, x1)
        gi = _paint_legend_20fb2937(gi, x3)
        gi = fill(gi, SIX, hfrontier((SIX, ZERO)))
        gi = _paint_lower_markers_20fb2937(gi, x6, x10)
        go = _paint_output_20fb2937(x6, x10, x11)
        if verify_20fb2937(gi) != go:
            continue
        return {"input": gi, "output": go}
