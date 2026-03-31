from __future__ import annotations

from synth_rearc.core import *

from .helpers import (
    alt_bottomright_border_a6f40cea,
    alt_topleft_border_a6f40cea,
    border_indices_a6f40cea,
    hidden_cells_a6f40cea,
    interior_bbox_a6f40cea,
    mono_border_a6f40cea,
    paint_cells_a6f40cea,
    visible_cells_a6f40cea,
)
from .verifier import verify_a6f40cea


def _interior_patch_a6f40cea(
    frame_bbox: tuple[int, int, int, int],
) -> frozenset[tuple[int, int]]:
    ir0, ic0, ir1, ic1 = interior_bbox_a6f40cea(frame_bbox)
    return frozenset((i, j) for i in range(ir0, ir1 + ONE) for j in range(ic0, ic1 + ONE))


def _sample_top_left_bbox_a6f40cea(
    frame_bbox: tuple[int, int, int, int],
    *,
    min_hidden_h: int,
    min_hidden_w: int,
    odd_width: bool,
) -> tuple[int, int, int, int] | None:
    fr0, fc0, fr1, fc1 = frame_bbox
    ir0, ic0, ir1, ic1 = interior_bbox_a6f40cea(frame_bbox)
    if fr0 < TWO or fc0 < TWO:
        return None
    for _ in range(80):
        x0 = randint(ONE, fr0)
        x1 = randint(ONE, fc0)
        x2 = randint(ir0 + min_hidden_h - ONE, ir1)
        x3 = randint(ic0 + min_hidden_w - ONE, ic1)
        x4 = (fr0 - x0, fc0 - x1, x2, x3)
        x5 = x4[THREE] - x4[ONE] + ONE
        if odd_width and x5 % TWO == ZERO:
            continue
        return x4
    return None


def _sample_top_right_bbox_a6f40cea(
    frame_bbox: tuple[int, int, int, int],
    width_value: int,
    *,
    min_hidden_h: int,
    min_hidden_w: int,
) -> tuple[int, int, int, int] | None:
    fr0, _, _, fc1 = frame_bbox
    ir0, ic0, ir1, ic1 = interior_bbox_a6f40cea(frame_bbox)
    if fr0 < TWO or width_value - fc1 - ONE < TWO:
        return None
    for _ in range(80):
        x0 = randint(ONE, fr0)
        x1 = randint(ic0, ic1 - min_hidden_w + ONE)
        x2 = randint(ir0 + min_hidden_h - ONE, ir1)
        x3 = randint(fc1 + ONE, width_value - ONE)
        if x3 - x1 + ONE < min_hidden_w + ONE:
            continue
        return (fr0 - x0, x1, x2, x3)
    return None


def _sample_bottom_left_bbox_a6f40cea(
    frame_bbox: tuple[int, int, int, int],
    height_value: int,
    *,
    min_hidden_h: int,
    min_hidden_w: int,
) -> tuple[int, int, int, int] | None:
    _, fc0, fr1, _ = frame_bbox
    ir0, ic0, ir1, ic1 = interior_bbox_a6f40cea(frame_bbox)
    if fc0 < TWO or height_value - fr1 - ONE < TWO:
        return None
    for _ in range(80):
        x0 = randint(ir0, ir1 - min_hidden_h + ONE)
        x1 = randint(ONE, fc0)
        x2 = randint(fr1 + ONE, height_value - ONE)
        x3 = randint(ic0 + min_hidden_w - ONE, ic1)
        if x2 - x0 + ONE < min_hidden_h + ONE:
            continue
        return (x0, fc0 - x1, x2, x3)
    return None


def _sample_bottom_right_bbox_a6f40cea(
    frame_bbox: tuple[int, int, int, int],
    height_value: int,
    width_value: int,
    *,
    min_hidden_h: int,
    min_hidden_w: int,
) -> tuple[int, int, int, int] | None:
    _, _, fr1, fc1 = frame_bbox
    ir0, ic0, ir1, ic1 = interior_bbox_a6f40cea(frame_bbox)
    if height_value - fr1 - ONE < TWO or width_value - fc1 - ONE < TWO:
        return None
    for _ in range(80):
        x0 = randint(ir0, ir1 - min_hidden_h + ONE)
        x1 = randint(ic0, ic1 - min_hidden_w + ONE)
        x2 = randint(fr1 + ONE, height_value - ONE)
        x3 = randint(fc1 + ONE, width_value - ONE)
        if x2 - x0 + ONE < min_hidden_h + ONE or x3 - x1 + ONE < min_hidden_w + ONE:
            continue
        return (x0, x1, x2, x3)
    return None


def _sample_vertical_bbox_a6f40cea(
    frame_bbox: tuple[int, int, int, int],
    height_value: int,
) -> tuple[int, int, int, int] | None:
    fr0, _, fr1, _ = frame_bbox
    _, ic0, _, ic1 = interior_bbox_a6f40cea(frame_bbox)
    if fr0 < TWO or height_value - fr1 - ONE < TWO:
        return None
    for _ in range(80):
        x0 = randint(ONE, fr0)
        x1 = randint(ic0, ic1 - TWO)
        x2 = randint(fr1 + ONE, height_value - ONE)
        x3 = randint(x1 + ONE, ic1)
        return (fr0 - x0, x1, x2, x3)
    return None


def _relative_hidden_cells_a6f40cea(
    colored_cells: dict[tuple[int, int], int],
    frame_bbox: tuple[int, int, int, int],
) -> dict[tuple[int, int], int]:
    ir0, ic0, _, _ = interior_bbox_a6f40cea(frame_bbox)
    x0 = hidden_cells_a6f40cea(colored_cells, frame_bbox)
    return {(i - ir0, j - ic0): value for (i, j), value in x0.items()}


def _add_latent_a6f40cea(
    latents: list[dict],
    latent: dict,
    visible_used: set[tuple[int, int]],
    hidden_used: set[tuple[int, int]],
    frame_bbox: tuple[int, int, int, int],
) -> bool:
    x0 = visible_cells_a6f40cea(latent["cells"], frame_bbox)
    x1 = hidden_cells_a6f40cea(latent["cells"], frame_bbox)
    if len(x0) == ZERO or len(x1) == ZERO:
        return False
    if len(set(x0) & visible_used) > ZERO:
        return False
    if len(set(x1) & hidden_used) > ZERO:
        return False
    visible_used.update(x0)
    hidden_used.update(x1)
    latents.append(latent)
    return True


def generate_a6f40cea(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    while True:
        height_value = unifint(diff_lb, diff_ub, (18, 30))
        width_value = unifint(diff_lb, diff_ub, (18, 30))
        inside_h = unifint(diff_lb, diff_ub, (6, min(14, height_value - 6)))
        inside_w = unifint(diff_lb, diff_ub, (6, min(14, width_value - 6)))
        if height_value - inside_h - TWO < SIX or width_value - inside_w - TWO < SIX:
            continue
        fr0 = randint(THREE, height_value - inside_h - FOUR)
        fc0 = randint(THREE, width_value - inside_w - FOUR)
        frame_bbox = (fr0, fc0, fr0 + inside_h + ONE, fc0 + inside_w + ONE)
        bg = choice(tuple(range(TEN)))
        x0 = tuple(value for value in range(TEN) if value != bg)
        frame_color = choice(x0)
        x1 = tuple(value for value in x0 if value != frame_color)
        inside_color = bg if choice((T, F)) else choice(x1)
        x2 = tuple(value for value in range(TEN) if value not in {bg, frame_color, inside_color})
        shuffle(x2 := list(x2))
        mono_colors = list(x2[:FOUR])
        pair_colors = []
        x3 = FOUR
        while x3 + ONE < len(x2):
            pair_colors.append((x2[x3], x2[x3 + ONE]))
            x3 += TWO

        grid = canvas(bg, (height_value, width_value))
        if inside_color != bg:
            grid = fill(grid, inside_color, _interior_patch_a6f40cea(frame_bbox))
        grid = fill(grid, frame_color, border_indices_a6f40cea(frame_bbox))

        latents: list[dict] = []
        visible_used: set[tuple[int, int]] = set()
        hidden_used: set[tuple[int, int]] = set()
        slots = ["tl", "tr", "bl", "br", "v"]
        shuffle(slots)

        if len(pair_colors) > ZERO and choice((T, T, F)):
            bbox = _sample_top_left_bbox_a6f40cea(frame_bbox, min_hidden_h=THREE, min_hidden_w=FOUR, odd_width=T)
            if bbox is not None:
                _add_latent_a6f40cea(
                    latents,
                    {"kind": "alt_tl", "bbox": bbox, "cells": alt_topleft_border_a6f40cea(bbox, pair_colors.pop(ZERO))},
                    visible_used,
                    hidden_used,
                    frame_bbox,
                )
            if "tl" in slots:
                slots.remove("tl")

        if len(pair_colors) > ZERO and choice((T, F)):
            bbox = _sample_bottom_right_bbox_a6f40cea(
                frame_bbox,
                height_value,
                width_value,
                min_hidden_h=TWO,
                min_hidden_w=THREE,
            )
            if bbox is not None:
                _add_latent_a6f40cea(
                    latents,
                    {"kind": "alt_br", "bbox": bbox, "cells": alt_bottomright_border_a6f40cea(bbox, pair_colors.pop(ZERO), frame_bbox)},
                    visible_used,
                    hidden_used,
                    frame_bbox,
                )
            if "br" in slots:
                slots.remove("br")

        target_mono = choice((ONE, TWO, TWO, THREE))
        attempts = ZERO
        while len([latent for latent in latents if latent["kind"].startswith("mono")]) < target_mono and attempts < 120:
            attempts += ONE
            if len(slots) == ZERO or len(mono_colors) == ZERO:
                break
            slot = choice(slots)
            color_value = mono_colors.pop(ZERO)
            if slot == "tl":
                bbox = _sample_top_left_bbox_a6f40cea(frame_bbox, min_hidden_h=TWO, min_hidden_w=TWO, odd_width=F)
            elif slot == "tr":
                bbox = _sample_top_right_bbox_a6f40cea(frame_bbox, width_value, min_hidden_h=TWO, min_hidden_w=TWO)
            elif slot == "bl":
                bbox = _sample_bottom_left_bbox_a6f40cea(frame_bbox, height_value, min_hidden_h=TWO, min_hidden_w=TWO)
            elif slot == "br":
                bbox = _sample_bottom_right_bbox_a6f40cea(frame_bbox, height_value, width_value, min_hidden_h=TWO, min_hidden_w=TWO)
            else:
                bbox = _sample_vertical_bbox_a6f40cea(frame_bbox, height_value)
            if bbox is None:
                slots.remove(slot)
                continue
            if slot == "v":
                kind = "mono_v"
            else:
                kind = f"mono_{slot}"
            latent = {"kind": kind, "bbox": bbox, "cells": mono_border_a6f40cea(bbox, color_value)}
            if _add_latent_a6f40cea(latents, latent, visible_used, hidden_used, frame_bbox):
                slots.remove(slot)
            else:
                mono_colors.append(color_value)
                if choice((T, F)):
                    slots.remove(slot)

        if len(latents) < TWO:
            continue

        input_grid = grid
        output_grid = canvas(inside_color, (inside_h, inside_w))
        output_cells = {}
        for latent in latents:
            input_grid = paint_cells_a6f40cea(input_grid, visible_cells_a6f40cea(latent["cells"], frame_bbox))
            output_cells.update(_relative_hidden_cells_a6f40cea(latent["cells"], frame_bbox))
        output_grid = paint_cells_a6f40cea(output_grid, output_cells)
        if verify_a6f40cea(input_grid) != output_grid:
            continue
        if input_grid == output_grid:
            continue
        return {"input": input_grid, "output": output_grid}
