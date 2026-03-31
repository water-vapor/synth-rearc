from __future__ import annotations

from dataclasses import dataclass

from synth_rearc.core import *


RULE_DIRECTIONS_ABC82100 = (UP, DOWN, LEFT, RIGHT)


@dataclass(frozen=True)
class LegendRuleAbc82100:
    component: Indices
    anchor: IntegerTuple
    direction: IntegerTuple
    source_loc: IntegerTuple
    target_loc: IntegerTuple
    source_color: Integer
    target_color: Integer


def eight_components_abc82100(
    grid: Grid,
) -> tuple[Indices, ...]:
    x0 = objects(grid, T, T, F)
    x1 = colorfilter(x0, EIGHT)
    x2 = tuple(toindices(x3) for x3 in x1)
    return tuple(
        sorted(
            x2,
            key=lambda x3: (
                uppermost(x3),
                leftmost(x3),
                height(x3),
                width(x3),
                size(x3),
            ),
        )
    )


def side_anchor_abc82100(
    component: Indices,
    direction: IntegerTuple,
) -> IntegerTuple:
    x0 = uppermost(component)
    x1 = lowermost(component)
    x2 = leftmost(component)
    x3 = rightmost(component)
    x4 = (x0 + x1) // TWO
    x5 = (x2 + x3) // TWO
    if direction == UP:
        return (x0, x5)
    if direction == DOWN:
        return (x1, x5)
    if direction == LEFT:
        return (x4, x2)
    return (x4, x3)


def legend_rules_abc82100(
    grid: Grid,
) -> tuple[LegendRuleAbc82100, ...]:
    x0 = []
    for x1 in eight_components_abc82100(grid):
        x2 = []
        for x3 in RULE_DIRECTIONS_ABC82100:
            x4 = side_anchor_abc82100(x1, x3)
            x5 = add(x4, x3)
            x6 = add(x5, x3)
            x7 = index(grid, x5)
            x8 = index(grid, x6)
            if x7 in (None, ZERO, EIGHT) or x8 in (None, ZERO, EIGHT):
                continue
            if x7 == x8:
                continue
            x2.append(
                LegendRuleAbc82100(
                    component=x1,
                    anchor=x4,
                    direction=x3,
                    source_loc=x6,
                    target_loc=x5,
                    source_color=x8,
                    target_color=x7,
                )
            )
        if len(x2) != ONE:
            raise ValueError(f"could not infer unique legend rule for {x1}")
        x0.append(x2[ZERO])
    return tuple(
        sorted(
            x0,
            key=lambda x1: (
                uppermost(x1.component),
                leftmost(x1.component),
                size(x1.component),
            ),
        )
    )


def instruction_cells_abc82100(
    grid: Grid,
) -> Indices:
    x0 = frozenset()
    for x1 in legend_rules_abc82100(grid):
        x0 = x0 | frozenset({x1.source_loc, x1.target_loc})
    return x0


def render_output_abc82100(
    grid: Grid,
) -> Grid:
    x0 = legend_rules_abc82100(grid)
    x1 = instruction_cells_abc82100(grid)
    x2 = frozenset(x3.source_color for x3 in x0)
    x3 = canvas(ZERO, shape(grid))
    x4 = difference(difference(palette(grid), frozenset({ZERO, EIGHT})), x2)
    for x5 in x4:
        x6 = difference(ofcolor(grid, x5), x1)
        x3 = fill(x3, x5, x6)
    for x7 in x0:
        x8 = recolor(x7.target_color, x7.component)
        x9 = difference(ofcolor(grid, x7.source_color), x1)
        for x10 in x9:
            x11 = subtract(x10, x7.anchor)
            x12 = shift(x8, x11)
            x3 = paint(x3, x12)
    return x3
