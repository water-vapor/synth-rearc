`arc2_sonnet45_summary.jsonl` was discarded for this task.

It describes the puzzle as consensus-denoising across several noisy copies, but the official training pairs do not support that. The correct rule is to take 8-connected foreground clusters, find the unique cluster that is not vertically symmetric inside its own bounding box, and output that cluster cropped tightly.

The `arc2_opus46_summary.json` hint was directionally useful, but the important correction is the connectivity model: train examples 0 and 2 include diagonal satellites that belong to the output cluster even though they are separate under 4-connectivity.
