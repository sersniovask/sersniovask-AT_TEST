
import paramiko
import src.send_commands as send_commands
import argparse

# def connect():
#     ssh_client = paramiko.SSHClient()
#     ssh_client.load_system_host_keys()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh_client.connect('192.168.1.1', username= 'root', password='Admin123')
#     return ssh_client


def connect():
    default_ip = '192.168.1.1'
    default_username = 'root'
    default_password = 'admin01'

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(default_ip, username=default_username, password=default_password)
    except paramiko.AuthenticationException:
        print("Default authentication failed. Please provide the correct credentials.")

        ip = input("Enter the IP address: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        try:
            ssh_client.connect(ip, username=username, password=password)
        except paramiko.AuthenticationException as auth_error:
            print(f"Authentication failed: {str(auth_error)}")
        except paramiko.SSHException as ssh_error:
            print(f"SSH connection failed: {str(ssh_error)}")
        except Exception as err:
            print(f"Error occurred: {str(err)}")
    except Exception as err:
        print(f"Error occurred: {str(err)}")

    return ssh_client


def shell_inv(router_name, hostname, ssh_client, commands):
    channel = ssh_client.get_transport().open_session()
    channel.get_pty()
    channel.invoke_shell()
    channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r ")
    rows=[]
    send_commands.send_commands(channel, commands[router_name], hostname, rows)
         