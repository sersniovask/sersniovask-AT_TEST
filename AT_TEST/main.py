import src.read_commands as read_commands
import src.client_connect as client_connect
import src.shell_invocation as shell_invocation
import src.checking_host as checking_host


def main():
    ssh_client   = client_connect.client()
    commands = read_commands.get_commands() 
    rows= []
    name, host = checking_host.hostname_check(ssh_client)
    shell_invocation.shell_inv(name, host, ssh_client, commands)
    ssh_client.close()
    
if __name__ == "__main__":
    main()



