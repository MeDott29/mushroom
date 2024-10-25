import os
import socket
import paramiko
import netifaces
from pathlib import Path
import shared_memory_dict
from git import Repo

def get_network_machines():
    """Scan local network for available machines"""
    local_ips = []
    for interface in netifaces.interfaces():
        addrs = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addrs:
            for addr in addrs[netifaces.AF_INET]:
                ip = addr['addr']
                if ip.startswith('192.168.') or ip.startswith('10.'):
                    local_ips.append(ip)
    return local_ips

def create_shared_memory(machine_name):
    """Create shared memory segment for each machine"""
    shared_mem = shared_memory_dict.SharedMemoryDict(
        name=f'network_shared_{machine_name}',
        size=1024
    )
    return shared_mem

def setup_git_repo(machine_ip, ssh_key_path, username, machine_number):
    """Set up Git repository on remote machine"""
    try:
        # Setup SSH client
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            machine_ip,
            username=username,
            key_filename=ssh_key_path
        )

        # Create unique repo name for this machine
        repo_name = f"network-node-{machine_number}"
        
        # Commands to execute on remote machine
        commands = [
            f"mkdir -p ~/repos/{repo_name}",
            f"cd ~/repos/{repo_name}",
            "git init",
            f"echo '# Network Node {machine_number}\n\nThis is an automatically generated repository for network node {machine_number}.' > README.md",
            "git add README.md",
            'git commit -m "Initial commit"',
        ]

        # Execute commands
        for cmd in commands:
            stdin, stdout, stderr = client.exec_command(cmd)
            stdout.channel.recv_exit_status()

        # Setup shared memory
        shared_mem = create_shared_memory(f"machine_{machine_number}")
        shared_mem['status'] = 'initialized'
        
        return True, repo_name
    
    except Exception as e:
        return False, str(e)
    finally:
        client.close()

def main():
    # Configuration
    ssh_key_path = os.path.expanduser('~/.ssh/id_rsa')
    username = os.getenv('USER')
    
    # Get network machines
    machines = get_network_machines()
    
    # Setup repos on each machine
    results = []
    for i, machine_ip in enumerate(machines, 1):
        success, result = setup_git_repo(
            machine_ip,
            ssh_key_path,
            username,
            i
        )
        results.append({
            'machine_ip': machine_ip,
            'success': success,
            'result': result
        })
    
    # Print results
    print("\nSetup Results:")
    for result in results:
        status = "SUCCESS" if result['success'] else "FAILED"
        print(f"\nMachine {result['machine_ip']}: {status}")
        print(f"Details: {result['result']}")

if __name__ == "__main__":
    main()