`arc2_opus46_summary.json` was consistent with the official examples and was used as the initial hypothesis.

`arc2_sonnet45_summary.jsonl` was discarded. It treats the task as "take the substring after the first `88` in each matching row", but that is only an accidental surface pattern on the training set. The actual rule depends on paired `2x2` blocks of `8`s on the same two rows:

- Every `8` in the official inputs belongs to one of these `2x2` marker blocks.
- Each contributing pair of rows contains exactly two such markers.
- The output takes the rectangular strip strictly between the left and right markers, preserving both rows, and stacks those 2-row strips from top to bottom.

The generator therefore samples the latent structure directly: dense non-`8` noise, paired 2-row marker blocks, and non-`8` payload strips between them.
