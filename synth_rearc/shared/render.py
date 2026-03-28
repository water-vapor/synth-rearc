from __future__ import annotations

import json
from pathlib import Path
import zipfile

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize

from synth_rearc.shared.paths import REPO_ROOT


ARC_CMAP = ListedColormap([
    "#000",
    "#0074D9",
    "#FF4136",
    "#2ECC40",
    "#FFDC00",
    "#AAAAAA",
    "#F012BE",
    "#FF851B",
    "#7FDBFF",
    "#870C25",
])
ARC_NORM = Normalize(vmin=0, vmax=9)


def _axes_at(axes, n_examples: int, row: int, col: int):
    if n_examples == 1:
        return axes[row]
    return axes[row, col]


def save_example_sheet(
    examples: list[dict],
    path: Path,
    *,
    title: str | None = None,
    show_index: bool = True,
) -> None:
    if not examples:
        raise ValueError("expected at least one example to render")
    path.parent.mkdir(parents=True, exist_ok=True)
    figure, axes = plt.subplots(2, len(examples), figsize=(len(examples) * 2.4, 5.4))
    for idx, example in enumerate(examples):
        top_ax = _axes_at(axes, len(examples), 0, idx)
        bottom_ax = _axes_at(axes, len(examples), 1, idx)
        top_ax.imshow(example["input"], cmap=ARC_CMAP, norm=ARC_NORM)
        bottom_ax.imshow(example["output"], cmap=ARC_CMAP, norm=ARC_NORM)
        top_ax.axis("off")
        bottom_ax.axis("off")
        if show_index:
            top_ax.set_title(f"{idx:02d}", fontsize=8)
    if title is not None:
        figure.suptitle(title, fontsize=14)
    figure.tight_layout()
    figure.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(figure)


def _load_json_payload(path: Path):
    if path.exists():
        with open(path, "r") as fp:
            return json.load(fp)
    relative_path = path.relative_to(REPO_ROOT).as_posix()
    for archive_name in ("arc_original.zip", "re_arc.zip"):
        archive_path = REPO_ROOT / archive_name
        if not archive_path.exists():
            continue
        with zipfile.ZipFile(archive_path) as zf:
            if relative_path in zf.namelist():
                with zf.open(relative_path) as fp:
                    return json.load(fp)
    raise FileNotFoundError(path)


def load_task_examples(path: Path) -> list[dict]:
    payload = _load_json_payload(path)
    if isinstance(payload, dict) and "train" in payload and "test" in payload:
        return payload["train"] + payload["test"]
    if isinstance(payload, list):
        return payload
    raise ValueError(f"unsupported task payload in {path}")


def save_preview_batches(
    examples: list[dict],
    previews_dir: Path,
    *,
    chunk_size: int = 10,
    max_examples: int = 30,
) -> list[Path]:
    previews_dir.mkdir(parents=True, exist_ok=True)
    rendered_paths: list[Path] = []
    preview_examples = examples[:max_examples]
    for chunk_idx in range(0, len(preview_examples), chunk_size):
        batch = preview_examples[chunk_idx:chunk_idx + chunk_size]
        if not batch:
            continue
        path = previews_dir / f"preview_{chunk_idx // chunk_size + 1:02d}.png"
        save_example_sheet(batch, path)
        rendered_paths.append(path)
    return rendered_paths
