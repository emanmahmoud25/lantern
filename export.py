import csv


def export_csv(tasks):
    """Export tasks to a CSV file."""

    with open("tasks.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "done"]
        )

        writer.writeheader()
        writer.writerows(tasks)

    print("Tasks exported to tasks.csv")