from scapy.all import sr1, srp, send, wrpcap, IP, TCP, UDP, DNS, DNSQR
from random import randint


ftp_pkt = IP(dst='195.144.107.198')/TCP(sport=20, dport=21, flags="S")
ftp_res = sr1(ftp_pkt)

wrpcap("./output/FTP_Connection_Start_2001CS61.pcap", [ftp_pkt, ftp_res])