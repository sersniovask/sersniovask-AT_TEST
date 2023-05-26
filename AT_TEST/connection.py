import paramiko
import time
import getpass
import at_read_write
import client_connect


ssh_client = client_connect.client()
commands = at_read_write.get_commands() 
rows= []

def shell_inv(router_name, hostname):
    channel = ssh_client.get_transport().open_session()
    channel.get_pty()
    channel.invoke_shell()
    channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r ")
    error_count=0
    ok_count=0
    for command in commands[router_name]:
        try:
            channel.send("$>" + command + "\n")
            
            while True:
                if channel.recv_ready():
                    output = channel.recv(1024)
                    output_lines=output.decode().splitlines()
                    
                    if output_lines[-2] == "OK":
                        result = output_lines[-2]
                        ok_count+=1
                    else:
                        result = "Error"
                        error_count+=1
                    
                    print(f"\nCurrent command tested: {command}\nresult: {result}")
                    row = {"command":command, "result":result}
                    rows.append(row)
                else:
                    time.sleep(0.5)
                    if not(channel.recv_ready()):
                        break
        except KeyboardInterrupt:
            break     
    at_read_write.write_to_file(rows, hostname)
    print(f"\nTotal commands: {ok_count + error_count}\nTotal okays: {ok_count}\nTotal errors: {error_count}")
                   

def hostname_check():
    stdin, stdout, stderr = ssh_client.exec_command("cat /proc/sys/kernel/hostname")
    hostname = stdout.read().decode()
    if "RUTX" in hostname:
        print(f"Successfully connected to {hostname}")
        shell_inv("RUTX", hostname)
    elif "RUT9" in hostname:
        print(f"Successfully connected to {hostname}")
        shell_inv("RUT9", hostname)
    elif "TRM2" in hostname:
        print(f"Successfully connected to {hostname}")
    else:
        print("Not RUT or TRM2 device!")
    return hostname

hostname_check() 
ssh_client.close()
