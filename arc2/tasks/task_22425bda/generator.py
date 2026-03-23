from __future__ import annotations

from arc2.core import *

from .helpers import line_sort_key_22425bda, output_from_lines_22425bda, paint_lines_22425bda


LINE_COLORS_22425BDA = tuple(v for v in interval(ZERO, TEN, ONE) if v != SEVEN)
TEMPLATE_OPTIONS_22425BDA = (
    "cross",
    "triple",
    "triple",
    "quad",
    "quad",
    "nested",
    "nested",
    "sweep",
)


def _sample_colors_22425bda(n: int) -> tuple[int, ...]:
    return tuple(sample(LINE_COLORS_22425BDA, n))


def _cross_lines_22425bda(n: int, colors: tuple[int, ...]) -> tuple[tuple[int, str, int], ...]:
    x0 = randint(ONE, n - TWO)
    if choice((T, F)):
        x1 = x0
    else:
        x1 = randint(ONE, n - TWO)
        while x1 == x0:
            x1 = randint(ONE, n - TWO)
    return (
        (colors[ZERO], "v", x1),
        (colors[ONE], "h", x0),
    )


def _triple_lines_22425bda(n: int, colors: tuple[int, ...]) -> tuple[tuple[int, str, int], ...]:
    x0 = randint(TWO, n - FOUR)
    x1 = randint(x0 + TWO, n - TWO)
    x2 = min(TWO, x1 - x0 - ONE)
    x3 = randint(ZERO, x2)
    return (
        (colors[ZERO], "h", x0),
        (colors[ONE], "v", x1),
        (colors[TWO], "d", x3),
    )


def _quad_lines_22425bda(n: int, colors: tuple[int, ...]) -> tuple[tuple[int, str, int], ...]:
    x0 = randint(THREE, n - FIVE)
    x1 = x0 - choice((ONE, TWO))
    x2 = x0 + choice((THREE, FOUR))
    x3 = choice((ONE, ONE, TWO))
    if x1 <= x3:
        x1 = x3 + ONE
    if x2 >= n - ONE:
        x2 = n - TWO
    return (
        (colors[ZERO], "v", x1),
        (colors[ONE], "h", x0),
        (colors[TWO], "d", x3),
        (colors[THREE], "v", x2),
    )


def _nested_lines_22425bda(n: int, colors: tuple[int, ...]) -> tuple[tuple[int, str, int], ...]:
    x0 = randint(max(THREE, divide(n, TWO) - ONE), n - SEVEN)
    x1 = x0 + TWO
    x2 = x1 + TWO
    x3 = randint(max(THREE, divide(n, TWO) - ONE), n - FIVE)
    x4 = x3 + TWO
    return (
        (colors[ZERO], "v", x2),
        (colors[ONE], "h", x4),
        (colors[TWO], "v", x1),
        (colors[THREE], "h", x3),
        (colors[FOUR], "v", x0),
    )


def _sweep_lines_22425bda(n: int, colors: tuple[int, ...]) -> tuple[tuple[int, str, int], ...]:
    x0 = divide(n, TWO) - ONE
    x1 = choice((FOUR, SIX if n >= 16 else FOUR))
    x2 = TWO * x0 + x1 - (n - ONE)
    if x2 <= ONE or x2 >= n - TWO or x2 == x0 - FOUR:
        x0 = divide(n, TWO)
        x2 = TWO * x0 + x1 - (n - ONE)
    return (
        (colors[ZERO], "a", TWO * x0 - FOUR),
        (colors[ONE], "v", x2),
        (colors[TWO], "d", -FOUR),
        (colors[THREE], "h", x0),
        (colors[FOUR], "d", x1),
        (colors[FIVE], "a", TWO * x0 + x1),
    )


def _candidate_lines_22425bda(
    template: str,
    n: int,
    colors: tuple[int, ...],
) -> tuple[tuple[int, str, int], ...]:
    if template == "cross":
        return _cross_lines_22425bda(n, colors)
    if template == "triple":
        return _triple_lines_22425bda(n, colors)
    if template == "quad":
        return _quad_lines_22425bda(n, colors)
    if template == "nested":
        return _nested_lines_22425bda(n, colors)
    return _sweep_lines_22425bda(n, colors)


def _template_size_22425bda(
    diff_lb: float,
    diff_ub: float,
    template: str,
) -> int:
    if template == "cross":
        return unifint(diff_lb, diff_ub, (SEVEN, 13))
    if template == "triple":
        return unifint(diff_lb, diff_ub, (TEN, 16))
    if template == "quad":
        return unifint(diff_lb, diff_ub, (TEN, 16))
    if template == "nested":
        return unifint(diff_lb, diff_ub, (12, 18))
    return unifint(diff_lb, diff_ub, (14, 20))


def _template_color_count_22425bda(template: str) -> int:
    if template == "cross":
        return TWO
    if template == "triple":
        return THREE
    if template == "quad":
        return FOUR
    if template == "nested":
        return FIVE
    return SIX


def generate_22425bda(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        x0 = choice(TEMPLATE_OPTIONS_22425BDA)
        x1 = _template_size_22425bda(diff_lb, diff_ub, x0)
        x2 = _sample_colors_22425bda(_template_color_count_22425bda(x0))
        x3 = _candidate_lines_22425bda(x0, x1, x2)
        x4 = paint_lines_22425bda((x1, x1), SEVEN, x3)
        x5 = tuple(sorted(x3, key=lambda x6: line_sort_key_22425bda(x4, x6)))
        if x5 != x3:
            continue
        x6 = output_from_lines_22425bda(x3)
        if len(set(line_sort_key_22425bda(x4, x7)[:TWO] for x7 in x3)) != len(x3):
            continue
        return {"input": x4, "output": x6}
