
import src.send_results_to_write as send_results_to_write
import argparse
import paramiko

# def connect_ssh():
#     ssh_client = paramiko.SSHClient()
#     ssh_client.load_system_host_keys()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh_client.connect('192.168.1.1', username= 'root', password='Admin123')
#     return ssh_client


def connect_ssh():
    parser = argparse.ArgumentParser(description='SSH Connection Parameters')
    parser.add_argument('-I','--ip', type=str, default='192.168.1.1', help='SSH host ip address')
    parser.add_argument('-U','--username', type=str, default='root', help='SSH username')
    parser.add_argument('-P','--password', type=str, default='admin01', help='SSH password', required=True)
    args = parser.parse_args()

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    ip_parts = args.ip.split('.')
    if len(ip_parts) != 4 or not all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts):
        parser.error('Invalid IP address specified. Please provide a valid IP address.')
    while True:
        try:
            ssh_client.connect(args.ip, username=args.username, password=args.password)
            break  
        except paramiko.AuthenticationException:
            print("Authentication failed. Please check your credentials.")
            break
        except paramiko.SSHException as e:
            print("Unable to establish SSH connection:", str(e))
            break
        except Exception as e:
            print("An error occurred:", str(e))
            break
            
    return ssh_client

def connect_shell(router_name, hostname, ssh_client, commands):
    channel = ssh_client.get_transport().open_session()
    channel.get_pty()
    channel.invoke_shell()
    channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r ")
    rows=[]
    send_results_to_write.send_commands(channel, commands[router_name], hostname, rows)
         