`arc2_opus46_summary.json` was useful and consistent with the official examples, so I used it as the starting hypothesis.

I discarded the Sonnet hint for implementation purposes. Its entry is awkwardly keyed by `puzzle_id`, invents a fifth training-style pair, and leaves the wedge size heuristic wrong.

The reliable rule from the official task is:
- keep the single largest 8-connected nonzero object unchanged
- remove every other nonzero object
- use the singleton sitting on an actual grid corner to choose the wedge corner
- use the most common color among the remaining removed singletons as the wedge color
- use the number of those remaining singletons as the wedge side length
