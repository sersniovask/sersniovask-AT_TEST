

def process_output(output, command, rows):
    output_lines = output.decode().splitlines()
    if output_lines[-2] == "OK":
        result = output_lines[-2]
    else:
        result = "Error"
    print(f"\nCurrent command tested: {command}\nresult: {result}")
    row = {"command": command, "result": result}
    rows.append(row)
    return result