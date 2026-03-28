Used the Opus summary as the initial hypothesis and rejected the Sonnet summary.

The Sonnet hint describes the output as diagonal rays and quadrant filling. That is too vague and materially misleading for implementation: the official examples are exactly a row of side-by-side dyadic upscales of the original `2x2` seed, with scale factors `1, 2, 4, 8, ...`, each copy shifted upward by `factor - 1` so the seed center stays vertically aligned. There is no nearest-quadrant or ray-casting decision per cell.
