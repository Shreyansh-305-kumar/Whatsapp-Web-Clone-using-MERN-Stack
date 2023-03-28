from scapy.all import sr1, srp, send, wrpcap, Ether, ARP
from random import randint

ARP_IP = "10.0.2.15"
BROADCAST_MAC = "ff:ff:ff:ff:ff:ff"

SRC_PORT = randint(1024, 65535)
HTTPS_PORT = 443


def getARP():
    packet = Ether(dst=BROADCAST_MAC) / ARP(pdst=ARP_IP)
    response, _ = srp(packet, verbose=0)
    return [packet, response[0][1]]


wrpcap("output/ARP_2001cs86.pcap", getARP())
