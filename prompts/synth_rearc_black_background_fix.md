Work in `/home/vapor/projects/realm/re-arc-2/re-arc`.

`TASK_ID` is provided externally.

Fix task `arc1/training/TASK_ID` by creating `synth_rearc/tasks/task_TASKID/`.

This is a fix task, not a generic task-generation task.

**Goal**
Port the monolithic RE-ARC task into the synthetic task package, check whether it has the black-background mismatch, and only apply a fix if that mismatch is actually present.

Deliver:
- `synth_rearc/tasks/task_TASKID/__init__.py`
- `synth_rearc/tasks/task_TASKID/verifier.py`
- `synth_rearc/tasks/task_TASKID/generator.py`
- `synth_rearc/tasks/task_TASKID/helpers.py` if needed
- `synth_rearc/tasks/task_TASKID/notes.md` if useful
- `artifacts/arc1/training/TASK_ID/task.json`
- `artifacts/arc1/training/TASK_ID/previews/originals.png`
- `artifacts/arc1/training/TASK_ID/previews/preview_01.png`
- `artifacts/arc1/training/TASK_ID/previews/preview_02.png`
- `artifacts/arc1/training/TASK_ID/previews/preview_03.png`

Do not edit:
- `dsl.py`
- `utils.py`
- `generators.py`
- `verifiers.py`

**Inputs To Read**
- `dsl_quickref.md`
- `data/official/arc1/training/TASK_ID.json`
- `generators.py`
- `verifiers.py`

**Required Flow**
1. Port `generate_TASKID` from `generators.py` into `synth_rearc/tasks/task_TASKID/generator.py`.
2. Port `verify_TASKID` from `verifiers.py` into `synth_rearc/tasks/task_TASKID/verifier.py`.
3. Add `synth_rearc/tasks/task_TASKID/__init__.py` so the task is discoverable.
4. Keep this baseline port behaviorally equivalent before making any fix.
5. Immediately run the baseline port through the standard checks:
   - verify official examples
   - build 1000 generated examples
   - verify generated examples
6. If any baseline check fails, treat the monolithic task as broken. Abort the fix task, remove any artifacts and task-package files created for this attempt, and append `TASK_ID` to `data/task_lists/arc1_training_rearc_fail_task_ids.txt`.
7. Only if the baseline port passes, inspect the official examples and determine whether the official inputs clearly use black (`0`) as background.
8. Use the baseline `task.json` and preview artifacts from step 5 to determine whether the passing baseline generator regularly emits non-black input backgrounds.
9. Only if both conditions hold, fix the ported generator so the task keeps black background while staying on-distribution.
10. If the issue is not confirmed, skip the fix and keep the passing baseline port and artifacts.
11. After any fix, rerun the standard build and verification flow and keep the resulting artifacts.

**Package Requirements**
- Write only inside `synth_rearc/tasks/task_TASKID/`.
- `__init__.py` must expose:
  - `TASK_ID = "TASK_ID"`
  - `generate = generate_TASKID`
  - `verify = verify_TASKID`
  - `REFERENCE_TASK_PATH = "data/official/arc1/training/TASK_ID.json"`
- Treat monolithic `generators.py` and `verifiers.py` as the source to port.
- Do not apply a blanket post-generation recolor hack if it changes the semantics of `0`.
- Keep verifier style close to original RE-ARC verifier style.

**Build And Validation**
Use the `arc` conda env.

Verify official examples:

```bash
conda run --no-capture-output -n arc python -m synth_rearc.shared.verify --dataset arc1 --split training --task TASK_ID
```

Build 1000 generated examples:

```bash
conda run --no-capture-output -n arc python -m synth_rearc.shared.build --dataset arc1 --split training --task TASK_ID --n-examples 1000
```

Verify generated examples:

```bash
./scripts/synth_rearc_verify_generated_all.sh --dataset arc1 --split training --task TASK_ID
```

Visually inspect at least:
- `artifacts/arc1/training/TASK_ID/previews/originals.png`
- `artifacts/arc1/training/TASK_ID/previews/preview_01.png`

If the generated family is off-distribution, revise and rebuild.

If the baseline port fails before any fix:
- remove `artifacts/arc1/training/TASK_ID/` created by this attempt
- remove the new task package created for this attempt
- append `TASK_ID` once to `data/task_lists/arc1_training_rearc_fail_task_ids.txt`
- stop without attempting the black-background fix

**Success Criteria**
- official examples pass exactly
- generated examples pass `1000/1000`
- generated examples look like the official task family
- black background is preserved only if the issue was actually confirmed
- no edits were made to the monolithic RE-ARC files

**Final Report**
State:
- whether the black-background issue was confirmed
- whether a fix was applied or skipped
- files changed
- official verification result
- generated verification result
- artifact paths
- any residual risk
