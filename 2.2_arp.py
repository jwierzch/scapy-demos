#!/usr/bin/python
from scapy.all import *


eth_inteface = "Intel(R) Ethernet Connection (13) I219-LM"
requesting_mac='00:50:56:AA:AA:AA'
broadcast_mac='FF:FF:FF:FF:FF:FF'


### request
eth_frame = Ether(dst=broadcast_mac,src=requesting_mac, type=0x0806)
#sendp(frame, iface=eth_inteface)
arp_packet = ARP(
    hwtype=1,
    ptype=0x0800,
    hwlen=6,
    plen=4,
    op=1,
    hwsrc= requesting_mac,
    psrc= '10.1.1.10',
    hwdst= '00:00:00:00:00:00',
    pdst='8.8.8.8',
    )

sendp(eth_frame/arp_packet, iface=eth_inteface)



