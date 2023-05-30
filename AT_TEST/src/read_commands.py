import os
import json


def get_commands():
    current_directory = os.getcwd()
    relative_path = "AT_TEST/at_commands.json"
    cmd_path = os.path.join(current_directory, relative_path)
    command_file = open(cmd_path, "r")
    commands = json.load(command_file)
    return commands