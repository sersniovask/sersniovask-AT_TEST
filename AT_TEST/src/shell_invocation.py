import getpass
import paramiko
import time
import src.send_commands as send_commands

def shell_inv(router_name, hostname, ssh_client, commands):
    channel = ssh_client.get_transport().open_session()
    channel.get_pty()
    channel.invoke_shell()
    channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r ")
    rows=[]
    send_commands.send_commands(channel, commands[router_name], hostname, rows)
         