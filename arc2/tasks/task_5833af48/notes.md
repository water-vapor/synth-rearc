`arc2_sonnet45_summary.jsonl` was discarded. It describes the task as a 4-way symmetry completion problem, but the official examples do not support that: the output is not formed by mirroring a sparse seed.

`arc2_opus46_summary.json` was used only as a rough starting hint. Its core idea is right, but it needs one correction: the right-hand `C/8` region is sometimes an upscaled display of a smaller coarse placement map, so the verifier must recover that coarse map before stamping.

The rule supported by the official examples is:
- find the unique non-`0/2/8` color `C`
- locate the largest solid `C` rectangle and crop it conceptually as the output canvas
- in the upper instruction band, use the `{2, 8}` rectangle as the stamp motif and the `{C, 8}` rectangle as the placement map
- when the placement map is displayed in uniform `k x k` blocks, downscale it back to its coarse grid
- fill the cropped `C` rectangle, then stamp the left-hand 8-pattern into every coarse-map cell marked with `8`
