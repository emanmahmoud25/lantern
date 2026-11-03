
import csv
import io


def export_csv(tasks):
    """Convert tasks into CSV text."""
    output = io.StringIO()

    fieldnames = ["title", "done"]
    writer = csv.DictWriter(output, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(tasks)

    return output.getvalue()
