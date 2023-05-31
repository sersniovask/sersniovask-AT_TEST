import csv
from datetime import datetime


def write_to_file(rows, hostname):
    fields = ["command", "result"]
    now = datetime.now()
    date = now.strftime("%d of %b %Y-%X")
    try:
        with open(f"sersniovask-AT_TEST/AT_TEST/results/test_results_{hostname}_{date}.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
    except IOError as err:
        print(f"Error occurred while writing to file: {str(err)}")
    except Exception as err:
        print(f"Error occurred: {str(err)}")
 

