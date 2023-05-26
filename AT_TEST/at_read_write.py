import csv
import os
import json
from datetime import datetime


def write_to_file(rows, hostname):
    fields = ["command", "result"]
    now = datetime.now()
    date = now.strftime(f"%d'th of %b %Y_%X")
    with open(f"test_results_{hostname}_{date}.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames= fields)
        writer.writeheader()
        writer.writerows(rows)
 

def get_commands():
    current_directory = os.getcwd()
    relative_path = "at_commands.json"
    cmd_path = os.path.join(current_directory, relative_path)
    command_file = open(cmd_path, "r")
    commands = json.load(command_file)
    return commands