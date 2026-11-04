# Issue #1: Add `list --done` Option

## 1. Issue Description

The `list` command did not provide an option to display only completed tasks.

Users needed a way to filter tasks based on their completion status.

## 2. Proposed Solution

Add a `--done` option to the `list` command.

This option allows users to display only tasks that have been marked as completed.

## 3. Implementation

The `list` command was updated to support the `--done` option.

When this option is provided, the application filters the tasks and displays only completed tasks.

## 4. Acceptance Criteria

- `lantern list --done` displays only completed tasks.
- Incomplete tasks are excluded from the output.

## 5. Expected Usage

python lantern.py list --done