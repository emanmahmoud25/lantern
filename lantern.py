
import argparse
from tasks import add_task, list_tasks
from export import export_csv

# Create the main parser
parser = argparse.ArgumentParser(
    description="Lantern Task Tracker"
)

# Create subcommands
sub = parser.add_subparsers(dest="command")

# Add command
add_parser = sub.add_parser("add")
add_parser.add_argument("title")

# List command
list_parser = sub.add_parser("list")
list_parser.add_argument(
    "--sort",
    action="store_true",
    help="Sort tasks by title"
)
list_parser.add_argument(
    "--done",
    action="store_true",
    help="Show only completed tasks"
)

# Export command
export_parser = sub.add_parser("export")
export_parser.add_argument(
    "--csv",
    action="store_true",
    help="Export tasks to CSV"
)

if __name__ == "__main__":
    args = parser.parse_args()

    if args.command == "add":
        task = add_task(args.title)
        print(f"Task added: {task['title']}")

    elif args.command == "list":
        tasks = list_tasks()

        if not tasks:
            print("No tasks found.")
        else:
            if args.sort:
                tasks = sorted(
                    tasks,
                    key=lambda x: x.get("title", "")
                )

            for task in tasks:
                print(task)

    elif args.command == "export":
        if args.csv:
            tasks = list_tasks()
            export_csv(tasks)
