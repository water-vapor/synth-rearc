`arc2_opus46_summary.json` was the useful hint here. Its key detail is that any nonzero lattice-intersection cell acts as a marker for the motif immediately down-right of it.

`arc2_sonnet45_summary.jsonl` is incomplete because it treats only non-`0`/non-`8` cells as markers. The official examples show that `8` can also be a marker. In training pair 1, the cell at `(5, 10)` is `8` in the input and still triggers the down-right motif to fill with `8`s in the output.

The corrected rule is: every nonzero cell at a `(5k, 5m)` lattice intersection is cleared back to `0`, and the fixed hollow motif directly down-right of that intersection has its interior zero cells filled with that marker color.
