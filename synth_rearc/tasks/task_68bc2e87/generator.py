from synth_rearc.core import *

from .verifier import verify_68bc2e87


_CHAIN_MODES_68bc2e87 = (
    "down_right",
    "down_left",
    "up_right",
    "up_left",
    "down",
    "up",
    "right",
    "left",
    "down",
    "up",
    "right",
    "left",
)

_THIN_MODES_68bc2e87 = ("down", "up", "right", "left")


def _rect_patch_68bc2e87(bounds: tuple[int, int, int, int]) -> Indices:
    t, l, b, r = bounds
    return box(frozenset({(t, l), (b, r)}))


def _shift_box_68bc2e87(
    bounds: tuple[int, int, int, int],
    offset: tuple[int, int],
) -> tuple[int, int, int, int]:
    oi, oj = offset
    t, l, b, r = bounds
    return (t + oi, l + oj, b + oi, r + oj)


def _span_68bc2e87(
    boxes: tuple[tuple[int, int, int, int], ...],
) -> tuple[int, int, int, int]:
    top = min(t for t, _, _, _ in boxes)
    left = min(l for _, l, _, _ in boxes)
    bottom = max(b for _, _, b, _ in boxes)
    right = max(r for _, _, _, r in boxes)
    return top, left, bottom, right


def _visible_sizes_68bc2e87(
    boxes: tuple[tuple[int, int, int, int], ...],
) -> tuple[int, ...]:
    covered = set()
    out = []
    for bounds in boxes[::-1]:
        patch = _rect_patch_68bc2e87(bounds)
        visible = difference(patch, covered)
        out.append(len(visible))
        covered |= patch
    return tuple(out[::-1])


def _choose_child_68bc2e87(
    parent: tuple[int, int, int, int],
    mode: str,
    final: bool,
    thin: bool,
) -> tuple[int, int, int, int] | None:
    t, l, b, r = parent
    if thin:
        if mode not in _THIN_MODES_68bc2e87:
            return None
        if mode in {"down", "up"}:
            if r - l < TWO:
                return None
            width = randint(TWO, min(FIVE, r - l))
            cl = randint(l + ONE, r - width + ONE)
            cr = cl + width - ONE
            height = choice((TWO, THREE))
            if mode == "down":
                ct = randint(b - ONE, b)
                cb = ct + height - ONE
                if cb <= b:
                    return None
            else:
                cb = randint(t, t + ONE)
                ct = cb - height + ONE
                if ct >= t:
                    return None
            return (ct, cl, cb, cr)
        if b - t < TWO:
            return None
        height = randint(TWO, min(FIVE, b - t))
        ct = randint(t + ONE, b - height + ONE)
        cb = ct + height - ONE
        width = choice((TWO, THREE))
        if mode == "right":
            cl = randint(r - ONE, r)
            cr = cl + width - ONE
            if cr <= r:
                return None
        else:
            cr = randint(l, l + ONE)
            cl = cr - width + ONE
            if cl >= l:
                return None
        return (ct, cl, cb, cr)
    min_dim = THREE if final else FOUR
    min_step = ONE if final else TWO
    max_step = SIX
    if mode == "down_right":
        if b - t < TWO or r - l < TWO:
            return None
        ct = randint(t + ONE, b - ONE)
        cl = randint(l + ONE, r - ONE)
        cb = b + randint(min_step, max_step)
        cr = r + randint(min_step, max_step)
        candidate = (ct, cl, cb, cr)
    elif mode == "down_left":
        if b - t < TWO or r - l < TWO:
            return None
        ct = randint(t + ONE, b - ONE)
        cr = randint(l + ONE, r - ONE)
        cb = b + randint(min_step, max_step)
        cl = l - randint(min_step, max_step)
        candidate = (ct, cl, cb, cr)
    elif mode == "up_right":
        if b - t < TWO or r - l < TWO:
            return None
        cb = randint(t + ONE, b - ONE)
        cl = randint(l + ONE, r - ONE)
        ct = t - randint(min_step, max_step)
        cr = r + randint(min_step, max_step)
        candidate = (ct, cl, cb, cr)
    elif mode == "up_left":
        if b - t < TWO or r - l < TWO:
            return None
        cb = randint(t + ONE, b - ONE)
        cr = randint(l + ONE, r - ONE)
        ct = t - randint(min_step, max_step)
        cl = l - randint(min_step, max_step)
        candidate = (ct, cl, cb, cr)
    elif mode == "down":
        if b - t < TWO or r - l < min_dim + ONE:
            return None
        ct = randint(t + ONE, b - ONE)
        cl = randint(l + ONE, r - min_dim)
        cr = randint(cl + min_dim - ONE, r - ONE)
        cb = b + randint(min_step, max_step)
        candidate = (ct, cl, cb, cr)
    elif mode == "up":
        if b - t < TWO or r - l < min_dim + ONE:
            return None
        cb = randint(t + ONE, b - ONE)
        cl = randint(l + ONE, r - min_dim)
        cr = randint(cl + min_dim - ONE, r - ONE)
        ct = t - randint(min_step, max_step)
        candidate = (ct, cl, cb, cr)
    elif mode == "right":
        if r - l < TWO or b - t < min_dim + ONE:
            return None
        cl = randint(l + ONE, r - ONE)
        ct = randint(t + ONE, b - min_dim)
        cb = randint(ct + min_dim - ONE, b - ONE)
        cr = r + randint(min_step, max_step)
        candidate = (ct, cl, cb, cr)
    else:
        if r - l < TWO or b - t < min_dim + ONE:
            return None
        cr = randint(l + ONE, r - ONE)
        ct = randint(t + ONE, b - min_dim)
        cb = randint(ct + min_dim - ONE, b - ONE)
        cl = l - randint(min_step, max_step)
        candidate = (ct, cl, cb, cr)
    ct, cl, cb, cr = candidate
    if cb - ct + ONE < min_dim or cr - cl + ONE < min_dim:
        return None
    return candidate


def generate_68bc2e87(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    colors = (ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, NINE)
    dims = (18, 19)
    while True:
        count = choice((FOUR, FOUR, FIVE, FIVE, FIVE))
        palette_pick = tuple(sample(colors, count))
        first_h = unifint(diff_lb, diff_ub, (SEVEN, 11))
        first_w = unifint(diff_lb, diff_ub, (SEVEN, 12))
        boxes = [(ZERO, ZERO, first_h - ONE, first_w - ONE)]
        success = T
        for idx in range(ONE, count):
            final = idx == count - ONE
            thin = final and choice((T, F, F, F))
            modes = _THIN_MODES_68bc2e87 if thin else _CHAIN_MODES_68bc2e87
            candidates = list(modes)
            shuffle(candidates)
            placed = None
            for mode in candidates:
                for _ in range(24):
                    candidate = _choose_child_68bc2e87(boxes[-ONE], mode, final, thin)
                    if candidate is None:
                        continue
                    if candidate in boxes:
                        continue
                    placed = candidate
                    break
                if placed is not None:
                    break
            if placed is None:
                success = F
                break
            boxes.append(placed)
        if flip(success):
            continue
        span = _span_68bc2e87(tuple(boxes))
        top, left, bottom, right = span
        total_h = bottom - top + ONE
        total_w = right - left + ONE
        if total_h > dims[ZERO] or total_w > dims[ONE]:
            continue
        if total_h < 12 or total_w < 12:
            continue
        offset = (
            randint(ZERO, dims[ZERO] - total_h) - top,
            randint(ZERO, dims[ONE] - total_w) - left,
        )
        placed_boxes = tuple(_shift_box_68bc2e87(bounds, offset) for bounds in boxes)
        heights = tuple(b - t + ONE for t, _, b, _ in placed_boxes)
        widths = tuple(r - l + ONE for _, l, _, r in placed_boxes)
        if max(heights) < EIGHT or max(widths) < EIGHT:
            continue
        visible_sizes = _visible_sizes_68bc2e87(placed_boxes)
        if any(v < SIX for v in visible_sizes):
            continue
        gi = canvas(EIGHT, dims)
        for value, bounds in zip(palette_pick, placed_boxes):
            gi = fill(gi, value, _rect_patch_68bc2e87(bounds))
        if mostcolor(gi) != EIGHT:
            continue
        go = tuple((value,) for value in palette_pick)
        if verify_68bc2e87(gi) != go:
            continue
        return {"input": gi, "output": go}
