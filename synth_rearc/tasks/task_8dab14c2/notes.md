The `arc2_sonnet45_summary.jsonl` hint was discarded, while the `arc2_opus46_summary.json` hint was kept only as a rough starting point.

The Sonnet summary describes the task as a generic bilateral-symmetry completion inside rectangular regions. That misses the actual latent structure: the foreground is a single thick `L` made from one horizontal bar and one vertical bar, and the input defects are not arbitrary interior pixels. They are sparse one-cell boundary holes or one-cell adjacent protrusions tied to specific sides of those two bars.

The corrected rule is:
- infer the dense horizontal bar from the high-count rows and the dense vertical bar from the high-count columns
- treat each defect as living on one side of one bar
- mirror it to the opposite side of that same bar, swapping inside/outside status
- a hole on one side becomes a protrusion just beyond the opposite side, and a protrusion becomes a hole on the opposite boundary cell

The Opus hint was directionally right about the bar decomposition and the inside/outside swap, but the actual verifier needs the stricter side-by-side projection logic above, including the overlap split: horizontal top/bottom projections only act on columns outside the vertical overlap, and vertical left/right projections only act on rows outside the horizontal overlap.
