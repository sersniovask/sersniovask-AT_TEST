import time
import src.write_to_file as write_to_file

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
  
  
def send_commands(channel, commands, hostname, rows):
    ok_count = 0
    error_count = 0
    for command in commands:
        try:
            channel.send("$>" + command + "\n")
            
            while True:
                if channel.recv_ready():
                    output = channel.recv(1024)
                    result = process_output(output, command, rows)
                    if result == "OK":
                        ok_count += 1
                    else:
                        error_count += 1
                   
                else:
                    time.sleep(0.1)
                    if not channel.recv_ready():
                        break
        except Exception as err:
            print(f"Error occurred: {str(err)}")
            break
    write_to_file.write_to_file(rows, hostname)
    print(f"\nTotal commands: {ok_count + error_count}\nTotal okays: {ok_count}\nTotal errors: {error_count}")