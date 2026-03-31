from __future__ import annotations

from synth_rearc.core import *

from .verifier import verify_67b4a34d


GRID_SIZE_67B4A34D = 16
HALF_SIZE_67B4A34D = GRID_SIZE_67B4A34D // 2
MASK_SIZE_67B4A34D = 4
DRAW_COLORS_67B4A34D = tuple(remove(THREE, remove(ZERO, interval(ZERO, TEN, ONE))))
BASE_MODES_67B4A34D = ("sum", "bands", "diamond", "checker", "hybrid")


def _sample_mode_params_67b4a34d(
    mode: str,
    ncolors: Integer,
) -> tuple[int, int, int]:
    if mode == "sum":
        return (
            randint(ONE, THREE),
            randint(ONE, THREE),
            randint(ZERO, ncolors - ONE),
        )
    if mode == "bands":
        return (
            randint(ONE, TWO),
            randint(ONE, TWO),
            randint(ZERO, ncolors - ONE),
        )
    if mode == "diamond":
        return (
            randint(ONE, HALF_SIZE_67B4A34D - TWO),
            randint(ONE, TWO),
            randint(ZERO, ncolors - ONE),
        )
    if mode == "checker":
        return (
            randint(ONE, THREE),
            randint(ONE, THREE),
            randint(ONE, TWO),
        )
    return (
        randint(ONE, THREE),
        randint(ONE, TWO),
        randint(ZERO, ncolors - ONE),
    )


def _mode_value_67b4a34d(
    mode: str,
    i: Integer,
    j: Integer,
    params: tuple[int, int, int],
) -> Integer:
    a, b, c = params
    if mode == "sum":
        return a * i + b * j + c
    if mode == "bands":
        return a * max(i, j) + b * min(i, j) + c * ((i + j) % TWO)
    if mode == "diamond":
        return abs(i - a) + abs(j - a) + b * ((i + j + c) % TWO)
    if mode == "checker":
        return i // a + j // b + c * ((i + j) % TWO)
    return a * abs(i - j) + b * (i + j) + c


def _paint_seed_patch_67b4a34d(
    seed: list[list[int]],
    color: Integer,
    patch: Indices,
) -> None:
    for i, j in patch:
        seed[i][j] = color
        seed[j][i] = color


def _build_seed_67b4a34d(
    colors: tuple[int, ...],
    diff_lb: float,
    diff_ub: float,
) -> list[list[int]]:
    ncolors = len(colors)
    mode_a = choice(BASE_MODES_67B4A34D)
    mode_b = choice(BASE_MODES_67B4A34D)
    params_a = _sample_mode_params_67b4a34d(mode_a, ncolors)
    params_b = _sample_mode_params_67b4a34d(mode_b, ncolors)
    offset = randint(ZERO, ncolors - ONE)
    seed = [[ZERO for _ in range(HALF_SIZE_67B4A34D)] for _ in range(HALF_SIZE_67B4A34D)]
    for i in range(HALF_SIZE_67B4A34D):
        for j in range(i, HALF_SIZE_67B4A34D):
            x0 = _mode_value_67b4a34d(mode_a, i, j, params_a)
            x1 = _mode_value_67b4a34d(mode_b, i, j, params_b)
            color = colors[(x0 + x1 + offset) % ncolors]
            seed[i][j] = color
            seed[j][i] = color
    npaint = unifint(diff_lb, diff_ub, (4, 8))
    for _ in range(npaint):
        color = choice(colors)
        motif = choice(("rect", "line", "cross"))
        if motif == "rect":
            h = randint(ONE, THREE)
            w = randint(ONE, FOUR)
            i = randint(ZERO, HALF_SIZE_67B4A34D - h)
            j = randint(ZERO, HALF_SIZE_67B4A34D - w)
            patch = frozenset((ii, jj) for ii in range(i, i + h) for jj in range(j, j + w))
        elif motif == "line":
            if choice((T, F)):
                i = randint(ZERO, HALF_SIZE_67B4A34D - ONE)
                j0 = randint(ZERO, HALF_SIZE_67B4A34D - TWO)
                j1 = randint(j0 + ONE, min(HALF_SIZE_67B4A34D - ONE, j0 + THREE))
                patch = frozenset((i, jj) for jj in range(j0, j1 + ONE))
            else:
                j = randint(ZERO, HALF_SIZE_67B4A34D - ONE)
                i0 = randint(ZERO, HALF_SIZE_67B4A34D - TWO)
                i1 = randint(i0 + ONE, min(HALF_SIZE_67B4A34D - ONE, i0 + THREE))
                patch = frozenset((ii, j) for ii in range(i0, i1 + ONE))
        else:
            i = randint(ONE, HALF_SIZE_67B4A34D - TWO)
            j = randint(ONE, HALF_SIZE_67B4A34D - TWO)
            patch = frozenset(
                {
                    (i, j),
                    (i - ONE, j),
                    (i + ONE, j),
                    (i, j - ONE),
                    (i, j + ONE),
                }
            )
        _paint_seed_patch_67b4a34d(seed, color, patch)
    return seed


def _expand_seed_67b4a34d(
    seed: list[list[int]],
) -> Grid:
    x0 = [tuple(row + row[::-1]) for row in seed]
    x1 = x0 + x0[::-1]
    return tuple(x1)


def _sample_mask_67b4a34d(
    output: Grid,
) -> tuple[Indices, Grid] | None:
    for _ in range(120):
        i = randint(TWO, GRID_SIZE_67B4A34D - MASK_SIZE_67B4A34D - ONE)
        j = randint(TWO, GRID_SIZE_67B4A34D - MASK_SIZE_67B4A34D - ONE)
        if FIVE <= i <= SEVEN and FIVE <= j <= SEVEN:
            continue
        patch = frozenset(
            (ii, jj)
            for ii in range(i, i + MASK_SIZE_67B4A34D)
            for jj in range(j, j + MASK_SIZE_67B4A34D)
        )
        hidden = subgrid(patch, output)
        if len(palette(hidden)) < THREE:
            continue
        trial = fill(output, THREE, patch)
        if verify_67b4a34d(trial) != hidden:
            continue
        return patch, hidden
    return None


def generate_67b4a34d(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    for _ in range(400):
        ncolors = unifint(diff_lb, diff_ub, (SIX, EIGHT))
        colors = tuple(sample(DRAW_COLORS_67B4A34D, ncolors))
        x0 = _build_seed_67b4a34d(colors, diff_lb, diff_ub)
        x1 = _expand_seed_67b4a34d(x0)
        if len(palette(x1)) < SIX:
            continue
        x2 = _sample_mask_67b4a34d(x1)
        if x2 is None:
            continue
        x3, x4 = x2
        x5 = fill(x1, THREE, x3)
        if verify_67b4a34d(x5) != x4:
            continue
        return {"input": x5, "output": x4}
    raise RuntimeError("failed to generate a verified 67b4a34d example")
