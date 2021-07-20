#!/usr/bin/python
from scapy.all import *


eth_inteface = "Intel(R) Ethernet Connection (13) I219-LM"
src_mac='00:50:56:AA:AA:AA'  
dst_mac='00:50:56:FF:FF:FF'

eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x0800)
ip_packet = IP(dst='1.2.3.4',src='10.9.8.7')

sendp(eth_frame/ip_packet, iface=eth_inteface)

eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x86DD)
ip6_packet = IPv6(dst='0123:4567:89ab:cdef:0123:4567:89ab:cdef',src='0123::cdef')

sendp(eth_frame/ip6_packet, iface=eth_inteface)
