#!/usr/bin/python
# https://www.geeksforgeeks.org/python-how-to-create-an-arp-spoofer-using-scapy/
from scapy.all import *

src_mac =  '00:50:56:AA:AA:AA'
dst_mac =  '00:50:56:BB:BB:BB'

eth_inteface = "Intel(R) Ethernet Connection (13) I219-LM"

eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x08100)
vlan = Dot1Q(prio=0,vlan=105,id=0, type=0x800)
ip_packet = IP(dst='1.2.3.4',src='10.9.8.7')

sendp(eth_frame/vlan, iface=eth_inteface)
sendp(eth_frame/vlan/ip_packet, iface=eth_inteface)


