import time
import src.write_commands as write_commands
import src.process_output as process_output

def send_commands(channel, commands, hostname, rows):
    ok_count = 0
    error_count = 0
    for command in commands:
        try:
            channel.send("$>" + command + "\n")
            
            while True:
                if channel.recv_ready():
                    output = channel.recv(1024)
                    result = process_output.process_output(output, command, rows)
                    if result == "OK":
                        ok_count += 1
                    else:
                        error_count += 1
                   
                else:
                    time.sleep(0.1)
                    if not channel.recv_ready():
                        break
        except:
            break
    write_commands.write_to_file(rows, hostname)
    print(f"\nTotal commands: {ok_count + error_count}\nTotal okays: {ok_count}\nTotal errors: {error_count}")