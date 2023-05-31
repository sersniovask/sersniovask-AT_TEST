import os
import json


def get_commands():
    try:
        current_directory = os.getcwd()
        relative_path = "AT_TEST/at_commands.json"
        cmd_path = os.path.join(current_directory, relative_path)
        with open(cmd_path, "r") as command_file:
            commands = json.load(command_file)
        return commands
    except FileNotFoundError:
        print("Command file not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON file.")
        return None
    except Exception as err:
        print("An error occurred:", str(err))
        return None