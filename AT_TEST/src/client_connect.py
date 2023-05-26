import paramiko

def client():
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('192.168.1.1', username= 'root', password='Admin123')
    return ssh_client