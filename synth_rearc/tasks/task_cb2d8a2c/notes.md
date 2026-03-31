# cb2d8a2c

Each `1/2` object is a single anchored bar. The bar becomes solid `2` in the
output, and the number of `1` cells encodes the snake offset: `count(1) + 1`
cells away from the bar both before the turn and on the detour lane beyond the
bar's free end. The bars are ordered from the seed side, and the single `3`
path threads through them in that order.
