import getpass
import paramiko
import time
import write_commands




rows= []

# def shell_inv(router_name, hostname, ssh_client, commands):
#     channel = ssh_client.get_transport().open_session()
#     channel.get_pty()
#     channel.invoke_shell()
#     channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r ")
#     error_count=0
#     ok_count=0
#     for command in commands[router_name]:
#         try:
#             channel.send("$>" + command + "\n")
            
#             while True:
#                 if channel.recv_ready():
#                     output = channel.recv(1024)
#                     output_lines=output.decode().splitlines()
                    
#                     if output_lines[-2] == "OK":
#                         result = output_lines[-2]
#                         ok_count+=1
#                     else:
#                         result = "Error"
#                         error_count+=1
                    
#                     print(f"\nCurrent command tested: {command}\nresult: {result}")
#                     row = {"command":command, "result":result}
#                     rows.append(row)
#                 else:
#                     time.sleep(0.5)
#                     if not(channel.recv_ready()):
#                         break
#         except:
#             break     
#     write_commands.write_to_file(rows, hostname)
#     print(f"\nTotal commands: {ok_count + error_count}\nTotal okays: {ok_count}\nTotal errors: {error_count}")

def invoke_shell(channel):
    channel.get_pty()
    channel.invoke_shell()
    channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r ")

def process_output(output, command):
    output_lines = output.decode().splitlines()
    if output_lines[-2] == "OK":
        result = output_lines[-2]
        ok_count += 1
    else:
        result = "Error"
        error_count += 1
    print(f"\nCurrent command tested: {command}\nresult: {result}")
    row = {"command": command, "result": result}
    rows.append(row)

def send_commands(channel, commands, hostname):
    error_count = 0
    ok_count = 0
    for command in commands:
        try:
            channel.send("$>" + command + "\n")

            while True:
                if channel.recv_ready():
                    output = channel.recv(1024)
                    process_output(output, command)
                else:
                    time.sleep(0.5)
                    if not channel.recv_ready():
                        break
        except:
            break
    write_commands.write_to_file(rows, hostname)
    print(f"\nTotal commands: {ok_count + error_count}\nTotal okays: {ok_count}\nTotal errors: {error_count}")

def shell_inv(router_name, hostname, ssh_client, commands):
    channel = ssh_client.get_transport().open_session()
    invoke_shell(channel)
    send_commands(channel, commands[router_name], hostname)
         