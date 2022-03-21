#!/usr/bin/env python3

import os
import threading
import time

def check_root_uid():
    if os.getuid() != 0:
        exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'.")

def host_discovery(ip):
    print("Thread 1:\tDiscovery host by CIDR\n")
    os.system("nmap -sn {ip} -oX /tmp/host_discovery.xml")

def services_scan(ip):
    print("Thread 2:\tScanning services\n")
    os.system("nmap -sCV -A -p- {ip} -oX /tmp/services.xml")
    
if __name__ == '__main__':
    check_root_uid()
    os.system("clear")
    cidrNotation = input(r"Insert your CIDR: ")
    thread1 = threading.Thread(target = host_discovery, args=(cidrNotation,))
    thread2 = threading.Thread(target = services_scan, args=(cidrNotation,))
    # starting threads
    thread1.start()
    thread2.start()
    # joining threads
    thread1.join()
    thread2.join()
