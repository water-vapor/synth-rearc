Work in `/home/vapor/projects/realm/re-arc-2/re-arc`.

**Goal**
Implement a new ARC2 task package for `TASK_ID`, using the official puzzle at `arc2_puzzles/data/training/TASK_ID.json`, in original RE-ARC style.

Deliver:
- `verify_TASKID`
- `generate_TASKID`
- 1000 verified generated examples
- `arc2/artifacts/TASK_ID/task.json`
- `arc2/artifacts/TASK_ID/previews/originals.png`
- `arc2/artifacts/TASK_ID/previews/preview_01.png`
- `arc2/artifacts/TASK_ID/previews/preview_02.png`
- `arc2/artifacts/TASK_ID/previews/preview_03.png`

Do not modify the original monolithic RE-ARC task files in `dsl.py`, `utils.py`, `generators.py`, or `verifiers.py`.

**Read First**
Before writing code:
1. Read `dsl_quickref.md` fully. This is the required high-level summary of `dsl.py`.
2. Then open `dsl.py` itself for any primitive you actually plan to use, especially the less obvious geometry/object primitives.
3. Read the official puzzle json at `arc2_puzzles/data/training/TASK_ID.json`.
4. Look up `TASK_ID` in `arc2_sonnet45_summary.jsonl` and `arc2_opus46_summary.json` and treat the matching `summary` text as an untrusted hint only.

Hint policy for `arc2_sonnet45_summary.jsonl` and `arc2_opus46_summary.json`:
- You should read both. `arc2_opus46_summary.json` should be more "correct" in general, if they conflict with each other.
- If the summary seems consistent with the official examples, you may use it as a starting hypothesis.
- If it seems wrong, incomplete, or misleading, discard it and work out the rule yourself.
- If you discard it, document the mismatch and your corrected understanding in `arc2/tasks/task_TASKID/notes.md`.
- If there is no entry for `TASK_ID`, continue without it.

**Where To Write**
Write new code only in:

```text
arc2/tasks/task_TASKID/
  __init__.py
  verifier.py
  generator.py
  helpers.py      # optional, task-local only
  notes.md        # optional, but required if the summary hint is rejected or corrected
```

Use the shared ARC2 infrastructure that already exists:
- `arc2/core.py`: shared import surface for task code. Import from here.
- `arc2/dsl_ext.py`: only for new low-level reusable primitives.
- `arc2/shared/build.py`: shared build entry point. Do not write task-local build scripts.
- `arc2/shared/render.py`: shared rendering and task-json loading.
- `arc2/shared/discovery.py`: shared task discovery.

`__init__.py` must expose:
- `TASK_ID = "TASK_ID"`
- `generate = generate_TASKID`
- `verify = verify_TASKID`
- `REFERENCE_TASK_PATH = "arc2_puzzles/data/training/TASK_ID.json"`

Put shared logic in the right place:
- If it is only useful for this puzzle, use `helpers.py`.
- If it is genuinely reusable across puzzles and low-level, add it to `arc2/dsl_ext.py`.
- Never add a task-specific high-level helper to `arc2/dsl_ext.py`.

Do not add:
- `sys.path` hacks
- task-local builder scripts
- ad hoc plotting scripts
- edits to the original monolithic RE-ARC task files for ARC2 work

**Build And Outputs**
Use the `arc` conda env:

If needed, confirm that the task package is discoverable:

```bash
conda run --no-capture-output -n arc python - <<'PY'
from arc2.shared.discovery import list_task_ids
print(list_task_ids())
PY
```

Before building, verify the verifier on the official examples:

```bash
conda run --no-capture-output -n arc python -m arc2.shared.verify --task TASK_ID
```

Then build the generated artifacts:

```bash
conda run --no-capture-output -n arc python -m arc2.shared.build --task TASK_ID --n-examples 1000
```

Then verify the generated examples with the convenience wrapper:

```bash
./arc2_verify_generated_all.sh --task TASK_ID
```

Omit `--task` to verify generated examples for all discovered ARC2 tasks.

The build command should generate:
- `arc2/artifacts/TASK_ID/task.json`
- `arc2/artifacts/TASK_ID/previews/originals.png`
- `arc2/artifacts/TASK_ID/previews/preview_01.png`
- `arc2/artifacts/TASK_ID/previews/preview_02.png`
- `arc2/artifacts/TASK_ID/previews/preview_03.png`

**Quality Bar**
This should look and feel like original RE-ARC code, not custom glue code.

Verifier requirements:
- Use original RE-ARC verifier style: `x0`, `x1`, `x2`, ...
- Use DSL composition, not ad hoc imperative solver code unless unavoidable
- Default to a self-contained `verifier.py`
- Do not import from `helpers.py` in the verifier unless the imported helper is also used constructively by `generator.py`
- Do not hide the solver in `helpers.py` as `solve_TASKID` or make `verifier.py` a thin wrapper around helper code
- Treat `verifiers.py` as the style reference for verifier structure, not previously generated `arc2/tasks`

Generator requirements:
- Match original RE-ARC generator style
- Construct the latent structure explicitly, then derive the output from it
- Do not use the verifier as the main definition of the task
- Optimize for distribution match, not just rule correctness

Before implementing, reason concretely about:
- which objects actually matter for the output
- how distractors/noise are produced
- whether noise is sparse or dense
- whether noise is singleton pixels, small fragments, shape motifs, or larger objects
- color usage
- object counts, object sizes, connected-component statistics, occupancy density
- spacing and layout priors

Avoid these failure modes:
- defaulting to generic polyomino or “Tetris” noise without evidence
- inventing a high-level DSL for one task
- trusting the `arc2_sonnet45_summary.jsonl` or `arc2_opus46_summary.json` hint without checking it against the official examples
- stopping after code is written without generating and checking artifacts

Minimum workflow:
1. Read `dsl_quickref.md`, the official puzzle, and the optional summary hint.
2. Decide whether the summary hint is trustworthy. If not, discard it and record that in `notes.md`.
3. Inspect RE-ARC code for style; use ARC2 code for packaging/infrastructure only, not as verifier-style precedent.
4. Infer the rule and characterize the input distribution.
5. Implement `verify_TASKID` and validate it on the official examples with `python -m arc2.shared.verify --task TASK_ID`.
6. Implement `generate_TASKID`.
7. Wire `__init__.py`.
8. Run the shared builder.
9. Run `./arc2_verify_generated_all.sh --task TASK_ID`.
10. Check that `task.json`, `originals.png`, and the 3 preview sheets exist.
11. Open at least one generated preview image and sanity-check it visually.
12. If the visuals are off-distribution, revise and rebuild.

Validation gates:
- official examples: exact verifier match
- generated examples: all satisfy `verify_TASKID(input) == output`
- generated examples: visually resemble the official task family
- artifacts are produced by the shared builder, not manual scripts

Final report:
- 1-3 sentence rule summary
- whether the summary hint was used or discarded
- if discarded, a short note on why
- why the generator matches the task family
- any added primitive and why it was necessary
- official test prediction if requested
- paths to the task package files
- paths to generated data and preview images

If genuinely blocked on rule inference, stop and say so. Otherwise finish the task end-to-end.
