`arc2_opus46_summary.json` was consistent with the official examples and I used it as the working hint.

`arc2_sonnet45_summary.jsonl` was discarded. Its "three corrupted copies to be repaired" story does not fit the training pairs: the outputs are not consensus reconstructions. The stable rule is that the input contains three panels separated by full-height `6` columns, each panel has three left-to-right non-background monochrome components, and the output keeps the left component from panel 1, the middle component from panel 2, and the right component from panel 3.
