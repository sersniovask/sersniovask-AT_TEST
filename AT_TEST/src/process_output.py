

def process_output(output, command, rows):
    try:
        output_lines = output.decode().splitlines()
        if output_lines[-2] == "OK":
            result = output_lines[-2]
        else:
            result = "Error"
        print(f"\nCurrent command tested: {command}\nResult: {result}")
        row = {"command": command, "result": result}
        rows.append(row)
        return result
    except IndexError:
        print("Error: Unexpected output format. Failed to extract result.")
        return "Error"
    except Exception as err:
        print(f"Error occurred: {str(err)}")
        return "Error"
