from synth_rearc.core import *


def _ring_objects_afe3afe9(
    I: Grid,
) -> tuple[Object, ...]:
    x0 = objects(I, T, F, T)
    x1 = sfilter(x0, lambda o: equality(size(o), EIGHT))
    x2 = sfilter(x1, lambda o: both(equality(height(o), THREE), equality(width(o), THREE)))
    x3 = sfilter(x2, lambda o: equality(index(I, add(ulcorner(o), UNITY)), ZERO))
    return tuple(sorted(x3, key=ulcorner))


def _compact_grid_afe3afe9(
    objs: tuple[Object, ...],
) -> Grid:
    x0 = tuple(sorted({uppermost(o) for o in objs}))
    x1 = tuple(sorted({leftmost(o) for o in objs}))
    x2 = frozenset(
        (color(o), (x0.index(uppermost(o)), x1.index(leftmost(o))))
        for o in objs
    )
    x3 = canvas(ZERO, (size(x0), size(x1)))
    x4 = paint(x3, x2)
    return x4


def _pack_row_afe3afe9(
    row: tuple[Integer, ...],
    to_right: Boolean,
) -> tuple[Integer, ...]:
    x0 = tuple(v for v in row if v != ZERO)
    x1 = repeat(ZERO, len(row) - len(x0))
    return branch(to_right, x1 + x0, x0 + x1)


def _pack_rows_afe3afe9(
    G: Grid,
    to_right: Boolean,
) -> Grid:
    return tuple(_pack_row_afe3afe9(row, to_right) for row in G)


def _pack_cols_afe3afe9(
    G: Grid,
    to_bottom: Boolean,
) -> Grid:
    x0 = dmirror(G)
    x1 = _pack_rows_afe3afe9(x0, to_bottom)
    x2 = dmirror(x1)
    return x2


def verify_afe3afe9(I: Grid) -> Grid:
    x0 = ofcolor(I, ONE)
    x1 = _ring_objects_afe3afe9(I)
    x2 = _compact_grid_afe3afe9(x1)
    x3 = hline(x0)
    x4 = equality(uppermost(x0), ZERO)
    x5 = equality(lowermost(x0), decrement(height(I)))
    x6 = equality(leftmost(x0), ZERO)
    x7 = _pack_rows_afe3afe9(x2, T)
    x8 = _pack_rows_afe3afe9(x2, F)
    x9 = _pack_cols_afe3afe9(x2, F)
    x10 = _pack_cols_afe3afe9(x2, T)
    x11 = branch(x4, x7, x8)
    x12 = branch(x6, x9, x10)
    x13 = branch(x3, x11, x12)
    return x13
