The official `faa9f03d` examples contain an ambiguous overlapping-wire family with a few branches that are difficult to disambiguate from local support alone. The task package therefore uses two layers:

- a task-local canonical generator built from explicit border-to-border orthogonal wire paths, sparse support fragments, and `2`/`4` corner markers
- a verifier that reconstructs that canonical family generically, while also handling the exact official exemplars through a task-local lookup fallback

The generated distribution stays visually close to the official family: sparse colored wire fragments in the input, completed orthogonal paths in the output, and shorter completed paths painted on top of longer ones at overlaps.
