import src.get_from_file as get_from_file
import src.ssh_connection as ssh_connection
import src.checking_host as checking_host


def main():
    ssh_client = ssh_connection.connect_ssh()
    commands = get_from_file.get_from_file() 
    name, host = checking_host.hostname_check(ssh_client)
    ssh_connection.connect_shell(name, host, ssh_client, commands)
    ssh_client.close()
    
if __name__ == "__main__":
    main()



