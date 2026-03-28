`arc2_opus46_summary.json` was directionally useful: the `2` shape is translated straight toward the `5` object and the output `5` object is a mirrored copy of the translated `2` shape.

The Sonnet summary was rejected because it describes both objects as moving toward each other while preserving the original `5` shape. In the official examples, the `5` input is a fixed 2x2 anchor square, only the `2` shape translates, and the output `5` region is the reflected continuation of the translated `2` shape across the contact side.
