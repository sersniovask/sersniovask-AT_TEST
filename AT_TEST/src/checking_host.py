import paramiko


def hostname_check(ssh_client):
    stdin, stdout, stderr = ssh_client.exec_command("cat /proc/sys/kernel/hostname")
    hostname = stdout.read().decode()
    if "RUTX" in hostname:
        print(f"Successfully connected to {hostname}")
        return "RUTX", hostname
    elif "RUT9" in hostname:
        print(f"Successfully connected to {hostname}")
        return "RUT9", hostname
    elif "TRM2" in hostname:
        print(f"Successfully connected to {hostname}")
    else:
        print("Not RUT or TRM2 device!")
    #return hostname