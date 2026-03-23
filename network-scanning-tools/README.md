# Network Scanning Tools

## Project Description

This project contains three Python programs used for basic network scanning.
The tools use system commands to check network connectivity, view connected devices, and perform network scans.

The three tools included are:

* Python 3
* Ping Scanner
* ARP Scanner
* Nmap Scanner

---

## How to Install Nmap

### Windows:

1. Go to https://nmap.org/download.html
2. Download and install Nmap
3. Make sure "Add to PATH" is selected during installation

---

## How to Run Each Program

Open terminal in the project folder and run:

### Ping Scanner

python ping_scanner.py

### ARP Scanner

python arp_scanner.py

### Nmap Scanner

python nmap_scanner.py

---

## Example Usage

### Ping Scanner

Input:
google.com, 127.0.0.1

Output:

* Shows whether each host is reachable
* Displays average response time

---

### ARP Scanner

Input:
(No input required)

Output:

* Displays list of IP and MAC addresses
* Shows number of devices connected

---

### Nmap Scanner

#### 1. Host Discovery 

Input:
Target: google.com
Choice: 1

Output:
Nmap scan report for google.com
Host is up
OS: Windows

---

#### 2. Fast Port Scan 

Input:
Target: google.com
Choice: 2

Output:
PORT     STATE SERVICE
80/tcp   open  http
443/tcp  open  https
OS: Windows

---

#### 3. Service Scan 

Input:
Target: 127.0.0.1
Choice: 3

Output:
PORT     STATE SERVICE VERSION
80/tcp   open  http    Apache
OS: Windows

---

#### 4. Full Scan 

Input:
Target: 127.0.0.1
Choice: 4

Output:
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
OS: Windows


---

## Screenshots

Screenshots of the program outputs:

* ping_output.png
* arp_output.png
* nmap_output1.png
* nmap_output2.png
* nmap_output3.png
* nmap_output4_1.png
* nmap_output4_2.png
