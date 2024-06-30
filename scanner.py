#!/usr/bin/env python3

import socket
from termcolor import colored

def scan(targets, ports):
    open_ports = []
    for port in range(1, ports + 1):
        if scan_port(targets, port):
            open_ports.append(port)
    return open_ports

def scan_port(ip, port):
    try:
        skt = socket.socket()
        skt.settimeout(0.5)
        skt.connect((ip, port))
        skt.close()
        print(colored(f"[✓] Port {port} is open", "light_green"))
        return True
    except socket.error:
        return False

ascii_banner = """
  ╦╔═╗  ╔═╗╔═╗╔═╗╔╗╔╔╗╔╔═╗╦═╗
  ║╠═╝  ╚═╗║  ╠═╣║║║║║║║╣ ╠╦╝
  ╩╩    ╚═╝╚═╝╩ ╩╝╚╝╝╚╝╚═╝╩╚═

  - Coded by Namik Ahmedov   
  - https://www.linkedin.com/in/namik-ahmedov-0ab564288
  - https://github.com/robostudio01
"""

print(colored(ascii_banner, "cyan"))

targets = input("[*] Enter Target IP: ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
print(colored("[*] Scanning Target(s)", "yellow"))

if ',' in targets:
    print(colored("[*] Scanning Multiple Targets", "yellow"))
    found_open_ports = False
    for ip_addr in targets.split(','):
        open_ports = scan(ip_addr.strip(), ports)
        if open_ports:
            found_open_ports = True
            print(colored(f"[✓] Open ports for {ip_addr}: {open_ports}", "light_green"))
    if not found_open_ports:
        print(colored("[x] Sorry, but I couldn't scan any port", "red"))
else:
    open_ports = scan(targets, ports)
    if open_ports:
        print(colored(f"[✓] Open ports for {targets}: {open_ports}", "light_green"))
    else:
        print(colored("[x] Sorry, but I couldn't scan any port", "red"))