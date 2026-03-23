import subprocess
import platform
import re

# function to ping a single host
def ping_host(host):
    # detect OS 
    system = platform.system().lower()

    if system == "windows":
        cmd = ["ping", "-n", "4", host]
    else:
        cmd = ["ping", "-c", "4", host]

    try:
        # run the ping command
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        output = result.stdout

        # check if the host is reachable
        if result.returncode == 0:
            status = "Reachable"
        else:
            status = "Not reachable"

        # extract average response time
        avg_time = get_avg_time(output, system)

        return status, avg_time

    except Exception as e:
        return "Error", str(e)


# function to extract average ping time using regex
def get_avg_time(output, system):
    if system == "windows":
        
        match = re.search(r'Average = (\d+)ms', output)
    else:
        
        match = re.search(r'avg[/=](\d+\.\d+)', output)

    if match:
        return match.group(1) + " ms"
    else:
        return "Not found"

# main function
if __name__ == "__main__":
    print("Ping Scanner")

    choice = input("Do you want to scan multiple hosts? (y/n): ")

    # multiple host scanning
    if choice.lower() == "y":
        hosts_input = input("Enter the hosts: ")
        hosts = hosts_input.split(",")

        print("\nResults:\n")

        # loop through each host
        for host in hosts:
            host = host.strip()  # remove extra spaces

            status, time = ping_host(host)

            print("Host:", host)
            print("Status:", status)
            print("Average time:", time)
            print("-" * 30)

    # single host scanning
    else:
        host = input("Enter IP or hostname: ")

        status, time = ping_host(host)

        print("\nResult:")
        print("Host:", host)
        print("Status:", status)
        print("Average time:", time)