import csv


def export_csv(tasks):
    """Export tasks to a CSV file."""

    # Open the CSV file for writing.
    # Use newline="" to avoid extra blank lines.
    # Use UTF-8 encoding to support different characters.
    with open("tasks.csv", "w", newline="", encoding="utf-8") as f:

        # Create a CSV writer with the required task columns.
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "done"]
        )

        # Write the column names as the first row.
        writer.writeheader()

        # Write all tasks as rows in the CSV file.
        writer.writerows(tasks)

    # Confirm that the export process is complete.
    print("Tasks exported to tasks.csv")