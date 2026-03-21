from arc2.core import *


MOTIF_TRANSFORMS_9A4BB226 = (
    identity,
    hmirror,
    vmirror,
    compose(hmirror, vmirror),
    dmirror,
    cmirror,
    compose(hmirror, dmirror),
    compose(vmirror, dmirror),
)

SCENE_TRANSFORMS_9A4BB226 = (
    identity,
    hmirror,
    vmirror,
    compose(hmirror, vmirror),
)

LAYOUTS_9A4BB226 = (
    ((2, 3), (4, 8), (9, 7), (10, 3)),
    ((2, 2), (2, 8), (6, 8), (9, 2)),
    ((1, 2), (2, 8), (7, 2), (9, 8)),
    ((1, 2), (1, 8), (6, 8), (8, 2)),
)

TARGET_BASE_PATTERNS_9A4BB226 = (
    ((0, 0, 0), (1, 2, 2), (1, 0, 0)),
    ((0, 1, 1), (0, 2, 2), (0, 1, 2)),
    ((0, 1, 2), (1, 0, 0), (2, 1, 0)),
    ((0, 1, 1), (1, 1, 1), (2, 2, 2)),
)

DISTRACTOR_BASE_PATTERNS_9A4BB226 = (
    ((0, 0, 0), (1, 1, 0), (1, 0, 0)),
    ((0, 1, 0), (1, 0, 1), (1, 1, 1)),
    ((0, 1, 1), (1, 1, 1), (0, 1, 0)),
    ((0, 0, 0), (1, 1, 0), (1, 1, 0)),
    ((0, 1, 1), (0, 1, 0), (0, 1, 1)),
    ((0, 1, 1), (0, 0, 0), (1, 1, 0)),
    ((0, 1, 1), (1, 0, 1), (1, 0, 0)),
    ((0, 1, 1), (1, 1, 0), (0, 1, 1)),
    ((0, 1, 1), (1, 0, 1), (1, 1, 0)),
    ((0, 1, 1), (0, 0, 0), (1, 0, 1)),
    ((0, 1, 0), (1, 0, 0), (0, 1, 1)),
    ((0, 0, 1), (1, 1, 1), (1, 1, 0)),
)


def _motif_variants_9a4bb226(patterns: tuple[Grid, ...]) -> tuple[Grid, ...]:
    out = []
    for pattern in patterns:
        for transform in MOTIF_TRANSFORMS_9A4BB226:
            candidate = transform(pattern)
            if candidate not in out:
                out.append(candidate)
    return tuple(out)


TARGET_PATTERNS_9A4BB226 = _motif_variants_9a4bb226(TARGET_BASE_PATTERNS_9A4BB226)
DISTRACTOR_PATTERNS_9A4BB226 = _motif_variants_9a4bb226(DISTRACTOR_BASE_PATTERNS_9A4BB226)


def _render_pattern_9a4bb226(
    pattern: Grid,
    colors: tuple[Integer, ...],
) -> Grid:
    return tuple(tuple(colors[value] for value in row) for row in pattern)


def _paint_pattern_9a4bb226(
    grid: Grid,
    pattern: Grid,
    loc: IntegerTuple,
) -> Grid:
    return paint(grid, shift(asobject(pattern), loc))


def generate_9a4bb226(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    del diff_lb, diff_ub
    colors = tuple(remove(ZERO, interval(ZERO, TEN, ONE)))
    layout = list(choice(LAYOUTS_9A4BB226))
    shuffle(layout)
    palette = sample(colors, NINE)
    target = _render_pattern_9a4bb226(choice(TARGET_PATTERNS_9A4BB226), tuple(palette[:THREE]))
    distractor_palettes = (
        tuple(palette[THREE:FIVE]),
        tuple(palette[FIVE:SEVEN]),
        tuple(palette[SEVEN:NINE]),
    )
    distractors = [
        _render_pattern_9a4bb226(choice(DISTRACTOR_PATTERNS_9A4BB226), palette_pair)
        for palette_pair in distractor_palettes
    ]
    shuffle(distractors)
    gi = canvas(ZERO, (15, 15))
    gi = _paint_pattern_9a4bb226(gi, target, layout[ZERO])
    for patch, loc in zip(distractors, layout[ONE:]):
        gi = _paint_pattern_9a4bb226(gi, patch, loc)
    transform = choice(SCENE_TRANSFORMS_9A4BB226)
    gi = transform(gi)
    go = transform(target)
    return {"input": gi, "output": go}
