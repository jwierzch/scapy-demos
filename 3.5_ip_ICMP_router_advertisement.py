#!/usr/bin/python
from scapy.all import *


eth_inteface = "Intel(R) Ethernet Connection (13) I219-LM"
src_mac='00:50:56:AA:AA:AA'  
dst_mac='00:50:56:FF:FF:FF'
broadcast_mac='FF:FF:FF:FF:FF:FF'

src_ip='10.9.8.7'
dst_ip='1.2.3.4'
multicast_ip='224.0.0.2'

eth_frame = Ether(dst=broadcast_mac,src=src_mac, type=0x0800)
ip_packet = IP(dst=multicast_ip,src=src_ip)

#Type 10 — Router Selection/Solicitation
icmp_payload= ICMP(type=10,code=0)
sendp(eth_frame/ip_packet/icmp_payload, iface=eth_inteface)

#Type 9 — Router Advertisement - Normal router advertisement	
eth_frame = Ether(dst=src_mac,src=dst_mac, type=0x0800)
ip_packet = IP(dst=src_ip,src=dst_ip,proto=1)
icmp_payload=ICMP(type=9,code=0)

sendp(eth_frame/ip_packet/icmp_payload, iface=eth_inteface)


