`arc2_opus46_summary.json` was useful and consistent with the official examples, so I used it as the starting hypothesis.

I discarded the Sonnet hint for implementation purposes because it overstates the downward propagation as a generic extension toward the border. The official examples are more specific: each broken bar fills its own gap and colors its spine upward until the next higher breakpoint, while the rows below the last broken bar take the color of the pre-existing lower marker already present in that column.
