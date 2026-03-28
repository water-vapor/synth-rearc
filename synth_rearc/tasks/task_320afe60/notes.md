`arc2_opus46_summary.json` was consistent with the official examples and I used it as the working hint.

`arc2_sonnet45_summary.jsonl` was rejected. It claims the left/right destination depends on vertical position and on the topmost object's horizontal placement, but the official examples contradict that: the deciding feature is local to each object. An object goes to the right edge and turns green exactly when its bounding box has gaps on one side only; all other objects go to the left edge and turn red.
