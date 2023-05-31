
import paramiko
import src.send_results_to_write as send_results_to_write
import argparse

# def connect_ssh():
#     ssh_client = paramiko.SSHClient()
#     ssh_client.load_system_host_keys()
#     ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh_client.connect('192.168.1.1', username= 'root', password='Admin123')
#     return ssh_client


def connect_ssh():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--ip', default='192.168.1.1', help='Specify the IP address')
    parser.add_argument('-u', '--username', default='root', help='Specify the username')
    parser.add_argument('-p', '--password', default='Admin123', help='Specify the password')
    args = parser.parse_args()

    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    while True:
        try:
            ssh_client.connect(args.ip, username=args.username, password=args.password)
            print('Successfully connected to the router!')
            break
        except paramiko.AuthenticationException as e:
            print('Authentication failed.')
            if args.username != 'root':
                args.username = input('Please enter a different username: ')
            elif args.password != 'admin01':
                args.password = input('Please enter a different password: ')
            elif args.ip != '192.168.1.1':
                args.ip = input('Please enter a different IP address: ')
            else:
                print('Incorrect username, password, and IP address provided.')
                break

    return ssh_client

def connect_shell(router_name, hostname, ssh_client, commands):
    channel = ssh_client.get_transport().open_session()
    channel.get_pty()
    channel.invoke_shell()
    #channel.send("service gsmd stop")
    channel.send("socat /dev/tty,raw,echo=0,escape=0x03 /dev/ttyUSB3,raw,setsid,sane,echo=0,nonblock ; stty sane\r ")
    rows=[]
    send_results_to_write.send_commands(channel, commands[router_name], hostname, rows)
         