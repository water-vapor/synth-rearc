from arc2.core import *


def verify_2c0b0aff(I: Grid) -> Grid:
    x0 = replace(I, EIGHT, THREE)
    x1 = objects(x0, T, F, F)
    x2 = colorfilter(x1, THREE)

    def x3(x4: Object) -> Integer:
        x5 = subgrid(x4, I)
        x6 = ofcolor(x5, THREE)
        x7 = sfilter(x6, lambda x8: equality(size(intersection(x6, dneighbors(x8))), FOUR))
        return size(x7)

    x4 = argmax(x2, x3)
    x5 = subgrid(x4, I)
    return x5
