# Lantern Task Tracker

Lantern is a simple command-line task tracker written in Python. It lets you add tasks, list them (all, only completed, or sorted by title), and export them to a CSV file.

## Installation and Usage

Requirements: Python 3.

Clone the repository and run Lantern from its folder:

```bash
git clone https://github.com/emanmahmoud25/lantern.git
cd lantern
```

Examples:

```bash
python lantern.py --help
python lantern.py add "Buy milk"
python lantern.py list
python lantern.py list --done
python lantern.py list --sort
python lantern.py export --csv
```

## Commands

- `add <title>`: Add a new task.
- `list`: Show all tasks.
- `list --done`: Show only completed tasks.
- `list --sort`: Show tasks sorted by title.
- `export --csv`: Export the tasks to `tasks.csv`.

## Documentation

See the [Usage Guide](docs/usage.md) for more details.

## Contributing

Contributions are welcome. Please read the [Contributing Guidelines](CONTRIBUTING.md) first.

## Team

| Name               | Role      | GitHub Username |
| ------------------ | --------- | --------------- |
| Eman Mahmoud Ahmed | Student A | emanmahmoud25   |
| Mohamed Hesham     | Student B | Mohamed-hesham-21 |