from synth_rearc.core import *


def _reconstructs_53b68214(
    I: Grid,
    obj: Object,
    bgc: int,
    width_: int,
    offset: IntegerTuple,
) -> bool:
    x0 = difference(obj, shift(obj, offset))
    x1 = canvas(bgc, (TEN, width_))
    x2 = interval(ZERO, TEN, ONE)
    x3 = lbind(shift, x0)
    x4 = lbind(multiply, offset)
    x5 = compose(x3, x4)
    x6 = mapply(x5, x2)
    x7 = paint(x1, x6)
    x8 = crop(x7, ORIGIN, shape(I))
    return equality(x8, I)


def verify_53b68214(I: Grid) -> Grid:
    x0 = fgpartition(I)
    x1 = merge(x0)
    x2 = mostcolor(I)
    x3 = width(I)
    x4 = astuple(TEN, x3)
    x5 = canvas(x2, x4)
    x6 = interval(ONE, SIX, ONE)
    x7 = invert(TEN)
    x8 = interval(x7, TEN, ONE)
    x9 = product(x6, x8)
    x10 = remove(ORIGIN, x9)
    x11 = lbind(intersection, x1)
    x12 = lbind(shift, x1)
    x13 = compose(x11, x12)
    x14 = toindices(x1)
    x15 = lbind(intersection, x14)
    x16 = lbind(shift, x14)
    x17 = compose(x15, x16)
    x18 = compose(size, x13)
    x19 = compose(size, x17)
    x20 = fork(equality, x18, x19)
    x21 = chain(positive, size, x13)
    x22 = fork(both, x20, x21)
    x23 = sfilter(x10, x22)
    x24 = lambda x: _reconstructs_53b68214(I, x1, x2, x3, x)
    x25 = sfilter(x23, x24)
    x26 = branch(positive(size(x25)), x25, x23)
    x27 = compose(size, x13)
    x28 = valmax(x26, x27)
    x29 = compose(size, x13)
    x30 = matcher(x29, x28)
    x31 = sfilter(x26, x30)
    x32 = fork(multiply, first, last)
    x33 = argmax(x31, x32)
    x34 = interval(ZERO, TEN, ONE)
    x35 = lbind(shift, x1)
    x36 = lbind(multiply, x33)
    x37 = compose(x35, x36)
    x38 = mapply(x37, x34)
    x39 = paint(x5, x38)
    return x39
