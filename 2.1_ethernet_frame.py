#!/usr/bin/python
from scapy.all import *

eth_inteface = "Intel(R) Ethernet Connection (13) I219-LM"
src_mac='00:50:56:CC:CC:CC'
dst_mac='00:50:56:DD:DD:DD'



eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x9000)
sendp(eth_frame, iface=eth_inteface)

eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x9000)/"Hello ethernet"
sendp(eth_frame, iface=eth_inteface)

eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x9000)/"beep boop beep beep boop boop"
sendp(eth_frame, iface=eth_inteface)

eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x8808)
sendp(eth_frame, iface=eth_inteface)

eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x80F3)
sendp(eth_frame, iface=eth_inteface)

eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x0842)
sendp(eth_frame, iface=eth_inteface)

eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x0806)
sendp(eth_frame, iface=eth_inteface)