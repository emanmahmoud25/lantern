# Issue #1: Add `list --done` Option

## 1. Issue Description

The `list` command did not provide an option to display only completed tasks.

Users needed a way to filter tasks based on their completion status.

## 2. Cause of the Issue

The command did not handle the completed task status correctly.

## 3. Proposed Solution

Add a `--done` option to the `list` command.

This option allows users to display only tasks that have been marked as completed.

## 4. Implementation

The `list` command was updated to support the `--done` option.

When this option is provided, the application filters the tasks and displays only completed tasks.

## 5. Acceptance Criteria

- `lantern list --done` displays only completed tasks.
- Incomplete tasks are excluded from the output.

## 6. Expected Usage

```bash
python lantern.py list --done