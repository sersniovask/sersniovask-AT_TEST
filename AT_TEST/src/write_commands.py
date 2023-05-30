import csv
from datetime import datetime


def write_to_file(rows, hostname):
    fields = ["command", "result"]
    now = datetime.now()
    date = now.strftime(f"%d'th of %b %Y-%X")
    with open(f"results/test_results_{hostname}_{date}.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames= fields)
        writer.writeheader()
        writer.writerows(rows)
 

