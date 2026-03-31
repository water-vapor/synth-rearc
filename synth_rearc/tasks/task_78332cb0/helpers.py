from synth_rearc.core import *


PANEL_SIDE_78332CB0 = FIVE
PANEL_SHAPE_78332CB0 = (PANEL_SIDE_78332CB0, PANEL_SIDE_78332CB0)
BG_COLOR_78332CB0 = SEVEN
SEP_COLOR_78332CB0 = SIX
FG_COLOR_CHOICES_78332CB0 = (ONE, TWO, THREE, FOUR, FIVE, EIGHT, NINE)


def _separator_rows_78332cb0(
    grid: Grid,
) -> tuple[Integer, ...]:
    return tuple(
        x0
        for x0, x1 in enumerate(grid)
        if all(x2 == SEP_COLOR_78332CB0 for x2 in x1)
    )


def _separator_cols_78332cb0(
    grid: Grid,
) -> tuple[Integer, ...]:
    return tuple(
        x0
        for x0 in range(width(grid))
        if all(index(grid, (x1, x0)) == SEP_COLOR_78332CB0 for x1 in range(height(grid)))
    )


def _split_panels_78332cb0(
    grid: Grid,
) -> tuple[Grid, ...]:
    x0 = _separator_rows_78332cb0(grid)
    x1 = _separator_cols_78332cb0(grid)
    x2 = (-ONE,) + x0 + (height(grid),)
    x3 = (-ONE,) + x1 + (width(grid),)
    x4 = []
    for x5, x6 in zip(x2, x2[ONE:]):
        if x6 - x5 == ONE:
            continue
        for x7, x8 in zip(x3, x3[ONE:]):
            if x8 - x7 == ONE:
                continue
            x9 = (x5 + ONE, x7 + ONE)
            x10 = (x6 - x5 - ONE, x8 - x7 - ONE)
            x4.append(crop(grid, x9, x10))
    return tuple(x4)


def _foreground_patch_78332cb0(
    panel: Grid,
) -> Object:
    return first(objects(panel, T, F, T))


def _column_profile_from_right_78332cb0(
    panel: Grid,
) -> tuple[Integer, ...]:
    x0 = mostcolor(panel)
    x1 = []
    for x2 in range(width(panel) - ONE, NEG_ONE, NEG_ONE):
        x3 = ZERO
        for x4 in range(height(panel)):
            if index(panel, (x4, x2)) != x0:
                x3 += ONE
        x1.append(x3)
    return tuple(x1)


def _panel_sort_key_78332cb0(
    panel: Grid,
) -> tuple[Integer, Integer, tuple[Integer, ...]]:
    x0 = _foreground_patch_78332cb0(panel)
    x1 = uppermost(x0) + lowermost(x0)
    x2 = int(rightmost(x0) == width(panel) - ONE)
    x3 = _column_profile_from_right_78332cb0(panel)
    return (-x1, -x2, x3)


def _ordered_panels_78332cb0(
    panels: tuple[Grid, ...],
) -> tuple[Grid, ...]:
    return tuple(sorted(panels, key=_panel_sort_key_78332cb0))


def _output_is_horizontal_78332cb0(
    panels: tuple[Grid, ...],
) -> bool:
    x0 = tuple(
        uppermost(_foreground_patch_78332cb0(x1))
        + lowermost(_foreground_patch_78332cb0(x1))
        for x1 in panels
    )
    return len(set(x0)) == ONE


def _horizontal_separator_78332cb0() -> Grid:
    return canvas(SEP_COLOR_78332CB0, (PANEL_SIDE_78332CB0, ONE))


def _vertical_separator_78332cb0() -> Grid:
    return canvas(SEP_COLOR_78332CB0, (ONE, PANEL_SIDE_78332CB0))


def _stack_horizontal_78332cb0(
    panels: tuple[Grid, ...],
) -> Grid:
    x0 = panels[ZERO]
    x1 = _horizontal_separator_78332cb0()
    for x2 in panels[ONE:]:
        x0 = hconcat(hconcat(x0, x1), x2)
    return x0


def _stack_vertical_78332cb0(
    panels: tuple[Grid, ...],
) -> Grid:
    x0 = panels[ZERO]
    x1 = _vertical_separator_78332cb0()
    for x2 in panels[ONE:]:
        x0 = vconcat(vconcat(x0, x1), x2)
    return x0


def _assemble_output_78332cb0(
    panels: tuple[Grid, ...],
) -> Grid:
    x0 = _ordered_panels_78332cb0(panels)
    return _stack_horizontal_78332cb0(x0) if _output_is_horizontal_78332cb0(x0) else _stack_vertical_78332cb0(x0)


def _assemble_input_layout_78332cb0(
    panels: tuple[Grid, ...],
    layout: str,
) -> Grid:
    if layout == "h":
        return _stack_horizontal_78332cb0(panels)
    if layout == "v":
        return _stack_vertical_78332cb0(panels)
    x0 = _stack_horizontal_78332cb0((panels[ZERO], panels[ONE]))
    x1 = _stack_horizontal_78332cb0((panels[TWO], panels[THREE]))
    x2 = canvas(SEP_COLOR_78332CB0, (ONE, width(x0)))
    return vconcat(vconcat(x0, x2), x1)


def _render_panel_78332cb0(
    patch: Indices,
    color_value: Integer,
) -> Grid:
    return fill(canvas(BG_COLOR_78332CB0, PANEL_SHAPE_78332CB0), color_value, patch)


def _random_connected_patch_78332cb0(
    top: Integer,
    bottom: Integer,
    left: Integer,
    right: Integer,
    size_lo: Integer,
    size_hi: Integer,
) -> Indices | None:
    x0 = tuple((x1, x2) for x1 in range(top, bottom + ONE) for x2 in range(left, right + ONE))
    x1 = max(size_lo, bottom - top + ONE, right - left + ONE)
    x2 = min(size_hi, len(x0))
    if x1 > x2:
        return None
    for _ in range(240):
        x3 = randint(x1, x2)
        x4 = {choice(x0)}
        while len(x4) < x3:
            x5 = set()
            for x6 in x4:
                x5 |= {
                    x7
                    for x7 in dneighbors(x6)
                    if top <= x7[ZERO] <= bottom
                    and left <= x7[ONE] <= right
                    and x7 not in x4
                }
            if len(x5) == ZERO:
                break
            x4.add(choice(tuple(x5)))
        if len(x4) != x3:
            continue
        x8 = frozenset(x4)
        if uppermost(x8) != top:
            continue
        if lowermost(x8) != bottom:
            continue
        if leftmost(x8) != left:
            continue
        if rightmost(x8) != right:
            continue
        return x8
    return None
