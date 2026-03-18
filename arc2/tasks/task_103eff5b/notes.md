`arc2_opus46_summary.json` was used as the working hint and matched the official examples.

`arc2_sonnet45_summary.jsonl` was discarded. It describes the transformation as a vertical level mapping, but the actual rule is stricter: the small colored motif is cropped to its bounding box, rotated 90 degrees clockwise, and then uniformly block-upscaled so its nonzero support matches the large `8` template exactly.
