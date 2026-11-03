import argparse
from tasks import add_task, list_tasks

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
                print(tasks)