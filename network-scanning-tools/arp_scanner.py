import subprocess
import re
import platform

# run arp command based on OS
def get_arp_table():
    try:
        if platform.system() == "Windows":
            cmd = ["arp", "-a"]
        else:
            cmd = ["arp", "-a"]   # same for linux, but we handle parsing differently if needed

        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout

    except Exception as e:
        print("Error running ARP:", e)
        return ""


# extract IP + MAC
def parse_arp(output):
    entries = set()  # using set to avoid duplicates

    # works for both formats
    pattern = r'(\d+\.\d+\.\d+\.\d+)[^\n]*?([a-fA-F0-9:-]{17})'

    matches = re.findall(pattern, output)

    for ip, mac in matches:
        entries.add((ip, mac))

    return list(entries)


# print table
def show(entries):
    print("\nARP Table:\n")
    print(f"{'IP Address':<18} {'MAC Address'}")
    print("-" * 35)

    for ip, mac in entries:
        print(f"{ip:<18} {mac}")

    print("\nTotal devices found:", len(entries))


# main
def main():
    print("Running ARP Scanner...\n")

    output = get_arp_table()

    if not output:
        print("No output received")
        return

    entries = parse_arp(output)

    if entries:
        show(entries)
    else:
        print("No devices found")


if __name__ == "__main__":
    main()