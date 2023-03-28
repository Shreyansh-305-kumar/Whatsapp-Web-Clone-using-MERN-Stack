from scapy.all import sr1, srp, send, wrpcap, IP, UDP, DNS, DNSQR
from random import randint

DNS_IP = "1.1.1.1"


QUERY_SITE = "craigslist.org"


def getDNS():
    dns_query = (
        IP(dst=DNS_IP) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname=QUERY_SITE,qtype="A"))
    )
    dns_response = sr1(dns_query)

    return [dns_query, dns_response]


wrpcap("output/DNS_2001cs86.pcap", getDNS())
