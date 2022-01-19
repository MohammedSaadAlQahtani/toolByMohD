from scapy.all import *
RED='\033[91m'
BOLD='\033[1m'
RESET='\033[0;0m'
dataEntered=str(input(f"{RED}{BOLD}[+]... Enter Any Type of information that you want to be in the packets\t{RESET}"))
fakePackets=Ether()/IP()/TCP()/dataEntered
sourceMac=str(input(f"{RED}{BOLD}[+]... Enter The Source Mac Address\t{RESET}"))
destinationMac=str(input(f"{RED}{BOLD}[+]... Enter The Destination Mac Address\t{RESET}"))
sourceIP=str(input(f"{RED}{BOLD}[+]... Enter The Source IP Address\t{RESET}"))
destinationIP=str(input(f"{RED}{BOLD}[+]... Enter The Destination IP Address\t{RESET}"))
fakePackets.src=str(sourceMac)
fakePackets.dst=str(destinationMac)
fakePackets[IP].src=str(sourceIP)
fakePackets[IP].dst=str(destinationIP)
fakePackets[TCP].flags='S'
print(f"{RED}{BOLD}[+]... This is your packets before sending {RESET}")
print(fakePackets.show())
amountOfPackets=input(f"{RED}{BOLD}[+]... How many number of packets that you want to send?\t{RESET}")

p=sendp(fakePackets,iface="eth0",count=amountOfPackets)