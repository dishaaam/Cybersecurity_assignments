import subprocess


# check if nmap is installed
def check_nmap():
    try:
        result = subprocess.run(["nmap", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except:
        return False


# run scan
def run_scan(target, choice):

    if choice == "1":
        # faster host discovery
        cmd = ["nmap", "-sn", target]

    elif choice == "2":
        # faster port scan (top ports)
        cmd = ["nmap", "-F", target]

    elif choice == "3":
        # service detection + faster
        cmd = ["nmap", "-sV", "-T4", target]

    elif choice == "4":
        # OS detection + service detection (better than just -O)
        cmd = ["nmap", "-A", target]

    else:
        print("Invalid choice")
        return

    try:
        print("\nRunning:", " ".join(cmd))
        print("Scanning...\n")

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=60
        )

        print("Scan finished!\n")
        print(result.stdout)

    except subprocess.TimeoutExpired:
        print("Scan timed out")
    except Exception as e:
        print("Error:", e)


# main
def main():
    print("=== Simple Nmap Scanner ===")

    if not check_nmap():
        print("Nmap not found. Install it first.")
        return

    target = input("Enter target IP or network: ")

    print("\nChoose scan type:")
    print("1. Host Discovery (Ping Scan)")
    print("2. Fast Port Scan (Top ports)")
    print("3. Service Scan")
    print("4. Full Scan (OS + services)")

    choice = input("Enter choice: ")

    run_scan(target, choice)


if __name__ == "__main__":
    main()