import src.read_commands as read_commands
import src.shell_invocation as shell
import src.checking_host as checking_host
import paramiko



def main():
    ssh_client = shell.connect()
    commands = read_commands.get_commands() 
    name, host = checking_host.hostname_check(ssh_client)
    shell.shell_inv(name, host, ssh_client, commands)
    ssh_client.close()
    
if __name__ == "__main__":
    main()



