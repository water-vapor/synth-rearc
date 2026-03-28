Work in `/home/vapor/projects/realm/re-arc-2/re-arc`.

`DATASET`, `SPLIT`, and `TASK_ID` are provided externally.

**Goal**
Implement a new synthetic RE-ARC task package for `TASK_ID`, using the official puzzle at `data/official/DATASET/SPLIT/TASK_ID.json`, in original RE-ARC style.

Deliver:
- `verify_TASKID`
- `generate_TASKID`
- 1000 verified generated examples
- `artifacts/DATASET/SPLIT/TASK_ID/task.json`
- `artifacts/DATASET/SPLIT/TASK_ID/previews/originals.png`
- `artifacts/DATASET/SPLIT/TASK_ID/previews/preview_01.png`
- `artifacts/DATASET/SPLIT/TASK_ID/previews/preview_02.png`
- `artifacts/DATASET/SPLIT/TASK_ID/previews/preview_03.png`

Do not modify the original monolithic RE-ARC task files in `dsl.py`, `utils.py`, `generators.py`, or `verifiers.py`.

**Read First**
Before writing code:
1. Read `dsl_quickref.md` fully.
2. Then open `dsl.py` itself for any primitive you actually plan to use.
3. Read the official puzzle json at `data/official/DATASET/SPLIT/TASK_ID.json`.

**Where To Write**
Write new code only in:

```text
synth_rearc/tasks/task_TASKID/
  __init__.py
  verifier.py
  generator.py
  helpers.py      # optional, task-local only
  notes.md        # optional
```

Use the shared synthetic RE-ARC infrastructure:
- `synth_rearc/core.py`
- `synth_rearc/dsl_ext.py`
- `synth_rearc/shared/build.py`
- `synth_rearc/shared/render.py`
- `synth_rearc/shared/discovery.py`

`__init__.py` must expose:
- `TASK_ID = "TASK_ID"`
- `generate = generate_TASKID`
- `verify = verify_TASKID`
- `REFERENCE_TASK_PATH = "data/official/DATASET/SPLIT/TASK_ID.json"`

Put shared logic in the right place:
- If it is only useful for this puzzle, use `helpers.py`.
- If it is genuinely reusable across puzzles and low-level, add it to `synth_rearc/dsl_ext.py`.
- Never add a task-specific high-level helper to `synth_rearc/dsl_ext.py`.

Do not add:
- `sys.path` hacks
- task-local builder scripts
- ad hoc plotting scripts
- edits to the original monolithic RE-ARC task files

**Build And Outputs**
Use the `arc` conda env.

If needed, confirm that the task package is discoverable:

```bash
conda run --no-capture-output -n arc python - <<'PY'
from synth_rearc.shared.discovery import list_task_ids
print(list_task_ids())
PY
```

Before building, verify the verifier on the official examples:

```bash
conda run --no-capture-output -n arc python -m synth_rearc.shared.verify --dataset DATASET --split SPLIT --task TASK_ID
```

Then build the generated artifacts:

```bash
conda run --no-capture-output -n arc python -m synth_rearc.shared.build --dataset DATASET --split SPLIT --task TASK_ID --n-examples 1000
```

Then verify the generated examples:

```bash
./scripts/synth_rearc_verify_generated_all.sh --dataset DATASET --split SPLIT --task TASK_ID
```

The build command should generate:
- `artifacts/DATASET/SPLIT/TASK_ID/task.json`
- `artifacts/DATASET/SPLIT/TASK_ID/previews/originals.png`
- `artifacts/DATASET/SPLIT/TASK_ID/previews/preview_01.png`
- `artifacts/DATASET/SPLIT/TASK_ID/previews/preview_02.png`
- `artifacts/DATASET/SPLIT/TASK_ID/previews/preview_03.png`

**Quality Bar**
This should look and feel like original RE-ARC code, not custom glue code.

Verifier requirements:
- Use original RE-ARC verifier style: `x0`, `x1`, `x2`, ...
- Use DSL composition, not ad hoc imperative solver code unless unavoidable.
- Default to a self-contained `verifier.py`.
- Do not import from `helpers.py` in the verifier unless that helper is also used constructively by `generator.py`.
- Do not hide the solver in `helpers.py` as `solve_TASKID`.
- Treat `verifiers.py` as the style reference for verifier structure, not previously generated task packages.

Generator requirements:
- Match original RE-ARC generator style.
- Construct the latent structure explicitly, then derive the output from it.
- Do not use the verifier as the main definition of the task.
- Optimize for distribution match, not just rule correctness.

Minimum workflow:
1. Read `dsl_quickref.md` and the official puzzle.
2. Inspect RE-ARC code for style; use `synth_rearc` code for packaging/infrastructure only.
3. Infer the rule and characterize the input distribution.
4. Implement `verify_TASKID`.
5. Validate on official examples.
6. Implement `generate_TASKID`.
7. Wire `__init__.py`.
8. Run the shared builder.
9. Run generated-example verification.
10. Check that `task.json`, `originals.png`, and the 3 preview sheets exist.
11. Open at least one generated preview image and sanity-check it visually.
12. If the visuals are off-distribution, revise and rebuild.

Validation gates:
- official examples: exact verifier match
- generated examples: all satisfy `verify_TASKID(input) == output`
- generated examples: visually resemble the official task family
- artifacts are produced by the shared builder, not manual scripts

If genuinely blocked on rule inference, stop and say so. Otherwise finish the task end-to-end.
