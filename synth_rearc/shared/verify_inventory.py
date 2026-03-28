from __future__ import annotations

import argparse
import json
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from synth_rearc.shared.paths import ARTIFACTS_ROOT, REPO_ROOT, TASKS_ROOT


ID_PATTERN = re.compile(r"^[0-9a-f]{8}$")
TASK_ID_PATTERN = re.compile(r'^TASK_ID\s*=\s*"([^"]+)"', re.MULTILINE)
SOURCE_ORDER = ("logs", "artifacts", "tasks")


@dataclass
class SourceReport:
    name: str
    ids: set[str] = field(default_factory=set)
    issues: list[str] = field(default_factory=list)


def _relative(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return str(path)


def _load_json(path: Path):
    with open(path, "r") as fp:
        return json.load(fp)


def _check_task_id_shape(report: SourceReport, task_id: str, *, path: Path) -> None:
    if not ID_PATTERN.fullmatch(task_id):
        report.issues.append(
            f"{_relative(path)}: expected 8-character lowercase hex puzzle id, found {task_id!r}"
        )


def collect_log_ids(logs_dir: Path) -> SourceReport:
    report = SourceReport(name="logs")
    if not logs_dir.is_dir():
        report.issues.append(f"{_relative(logs_dir)}: directory does not exist")
        return report

    for path in sorted(logs_dir.glob("*.json")):
        task_id = path.stem.removesuffix("_cc")
        report.ids.add(task_id)
        _check_task_id_shape(report, task_id, path=path)
        try:
            payload = _load_json(path)
        except Exception as exc:
            report.issues.append(f"{_relative(path)}: failed to parse JSON: {type(exc).__name__}: {exc}")
            continue
        if not isinstance(payload, dict):
            report.issues.append(f"{_relative(path)}: expected JSON object payload")
            continue
        payload_task_id = payload.get("puzzle_id")
        if payload_task_id is None:
            report.issues.append(f"{_relative(path)}: missing puzzle_id field")
            continue
        if payload_task_id != task_id:
            report.issues.append(
                f"{_relative(path)}: puzzle_id {payload_task_id!r} does not match filename id {task_id!r}"
            )

    return report


def collect_artifact_ids(artifacts_dir: Path) -> SourceReport:
    report = SourceReport(name="artifacts")
    if not artifacts_dir.is_dir():
        report.issues.append(f"{_relative(artifacts_dir)}: directory does not exist")
        return report

    for dataset_dir in sorted(path for path in artifacts_dir.iterdir() if path.is_dir()):
        for split_dir in sorted(path for path in dataset_dir.iterdir() if path.is_dir()):
            for path in sorted(item for item in split_dir.iterdir() if item.is_dir()):
                task_id = path.name
                report.ids.add(task_id)
                _check_task_id_shape(report, task_id, path=path)
                task_json_path = path / "task.json"
                if not task_json_path.is_file():
                    report.issues.append(f"{_relative(path)}: missing task.json")

    return report


def _extract_declared_task_id(init_path: Path) -> str | None:
    text = init_path.read_text()
    match = TASK_ID_PATTERN.search(text)
    if match is None:
        return None
    return match.group(1)


def collect_task_ids(tasks_dir: Path) -> SourceReport:
    report = SourceReport(name="tasks")
    if not tasks_dir.is_dir():
        report.issues.append(f"{_relative(tasks_dir)}: directory does not exist")
        return report

    for path in sorted(tasks_dir.iterdir()):
        if not path.is_dir() or not path.name.startswith("task_"):
            continue
        task_id = path.name.removeprefix("task_")
        report.ids.add(task_id)
        _check_task_id_shape(report, task_id, path=path)

        init_path = path / "__init__.py"
        if not init_path.is_file():
            report.issues.append(f"{_relative(path)}: missing __init__.py")
            continue

        try:
            declared_task_id = _extract_declared_task_id(init_path)
        except Exception as exc:
            report.issues.append(
                f"{_relative(init_path)}: failed to read TASK_ID: {type(exc).__name__}: {exc}"
            )
            continue

        if declared_task_id is None:
            report.issues.append(f"{_relative(init_path)}: missing TASK_ID declaration")
            continue
        if declared_task_id != task_id:
            report.issues.append(
                f"{_relative(init_path)}: TASK_ID {declared_task_id!r} does not match directory id {task_id!r}"
            )

    return report


def find_subset_mismatches(reports: list[SourceReport]) -> dict[tuple[str, ...], list[str]]:
    source_to_ids = {report.name: report.ids for report in reports}
    groups: dict[tuple[str, ...], list[str]] = defaultdict(list)
    all_ids = set().union(*(report.ids for report in reports))
    for task_id in sorted(all_ids):
        present_in = tuple(name for name in SOURCE_ORDER if task_id in source_to_ids[name])
        if len(present_in) != len(SOURCE_ORDER):
            groups[present_in].append(task_id)
    return dict(sorted(groups.items(), key=lambda item: (len(item[0]), item[0])))


def print_report(reports: list[SourceReport], subset_mismatches: dict[tuple[str, ...], list[str]]) -> None:
    for report in reports:
        print(f"{report.name}: {len(report.ids)} ids")

    if not subset_mismatches:
        shared_count = len(reports[0].ids) if reports else 0
        print(f"pass: all {shared_count} puzzle ids appear in logs, artifacts, and tasks")
    else:
        mismatch_count = sum(len(ids) for ids in subset_mismatches.values())
        print(f"fail: {mismatch_count} puzzle ids do not appear in all three sources")
        for present_in, task_ids in subset_mismatches.items():
            label = " + ".join(present_in) if present_in else "none"
            print(f"{label}: {' '.join(task_ids)}")

    issues = [issue for report in reports for issue in report.issues]
    if issues:
        print("issues:")
        for issue in issues:
            print(f"  {issue}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Verify puzzle ids match across logs/, artifacts/, and synth_rearc/tasks/."
    )
    parser.add_argument("--logs-dir", type=Path, default=REPO_ROOT / "logs")
    parser.add_argument("--artifacts-dir", type=Path, default=ARTIFACTS_ROOT)
    parser.add_argument("--tasks-dir", type=Path, default=TASKS_ROOT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    reports = [
        collect_log_ids(args.logs_dir),
        collect_artifact_ids(args.artifacts_dir),
        collect_task_ids(args.tasks_dir),
    ]
    subset_mismatches = find_subset_mismatches(reports)
    print_report(reports, subset_mismatches)
    has_issues = any(report.issues for report in reports)
    return 0 if not subset_mismatches and not has_issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
