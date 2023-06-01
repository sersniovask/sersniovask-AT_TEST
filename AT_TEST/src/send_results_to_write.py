import time
import src.write_to_file as write_to_file
def prGreen(skk): return"\033[92m {}\033[00m" .format(skk)
def prRed(skk): return"\033[91m {}\033[00m" .format(skk)

def process_output(output, command, rows):
    try:
        output_lines = output.decode().splitlines()
        if output_lines[-2] == "OK":
            result = output_lines[-2]
        else:
            result = "Error"
        
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
                    print(f"""
                           Current command tested: {command}
                           Result: {result}
                          {prGreen(f"Okay count:{ok_count}")}
                          {prRed(f"Error count: {error_count}")}
                          """)
                    CURSOR_UP = "\033[1A"
                    CLEAR = "\x1b[2K"
                    print(5*(CURSOR_UP + CLEAR)+ CURSOR_UP, end="")
                   
                else:
                    time.sleep(0.1)
                    if not channel.recv_ready():
                        break
        except Exception as err:
            print(f"Error occurred: {str(err)}")
            break
    
    write_to_file.write_to_file(rows, hostname)
    
    print(f"""
           Total commands: {ok_count + error_count}
          {prGreen(f"Total okays:{ok_count}")} 
          {prRed(f"Total errors:{error_count}")}""")