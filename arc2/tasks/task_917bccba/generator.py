from arc2.core import *


_GRID_SIZE_917BCCBA = 12
_FRAME_SIDE_BOUNDS_917BCCBA = (FIVE, EIGHT)
_OUTER_MARGIN_917BCCBA = TWO


def generate_917bccba(
    diff_lb: float,
    diff_ub: float,
) -> dict:
    dims = (_GRID_SIZE_917BCCBA, _GRID_SIZE_917BCCBA)
    cols = remove(ZERO, interval(ZERO, TEN, ONE))
    while True:
        framec, linec = sample(cols, TWO)
        side = unifint(diff_lb, diff_ub, _FRAME_SIDE_BOUNDS_917BCCBA)
        slack = _GRID_SIZE_917BCCBA - side
        top = unifint(diff_lb, diff_ub, (_OUTER_MARGIN_917BCCBA, slack - _OUTER_MARGIN_917BCCBA))
        left = unifint(diff_lb, diff_ub, (_OUTER_MARGIN_917BCCBA, slack - _OUTER_MARGIN_917BCCBA))
        bottom = top + side - ONE
        right = left + side - ONE
        row = unifint(diff_lb, diff_ub, (top + ONE, bottom - ONE))
        col = unifint(diff_lb, diff_ub, (left + ONE, right - ONE))
        frame = box(frozenset({(top, left), (bottom, right)}))
        cross = combine(hfrontier((row, ZERO)), vfrontier((ZERO, col)))
        target = (top, right)
        moved = combine(hfrontier(target), vfrontier(target))
        gi = fill(canvas(ZERO, dims), linec, cross)
        gi = fill(gi, framec, frame)
        go = fill(canvas(ZERO, dims), linec, moved)
        go = fill(go, framec, frame)
        if equality(gi, go):
            continue
        from .verifier import verify_917bccba

        if verify_917bccba(gi) != go:
            continue
        return {"input": gi, "output": go}
