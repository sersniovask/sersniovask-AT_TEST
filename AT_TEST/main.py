import src.read_commands as read_commands
import src.shell_invocation as shell
import src.checking_host as checking_host
import paramiko



def main():
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('192.168.1.1', username= 'root', password='Admin123')
    commands = read_commands.get_commands() 
    name, host = checking_host.hostname_check(ssh_client)
    shell.shell_inv(name, host, ssh_client, commands)
    ssh_client.close()
    
if __name__ == "__main__":
    main()



