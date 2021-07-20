#!/usr/bin/python
from scapy.all import *


eth_inteface = "Intel(R) Ethernet Connection (13) I219-LM"
requesting_mac='00:50:56:EE:EE:EE'
broadcast_mac='FF:FF:FF:FF:FF:FF'
destination_mac='00:50:56:BB:BB:BB'

requesting_ip= '10.1.10.10'
destination_ip='75.75.75.75'


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
    psrc= requesting_ip,
    hwdst= '00:00:00:00:00:00',
    pdst=destination_ip,
    )

sendp(eth_frame/arp_packet, iface=eth_inteface)

### response
eth_frame = Ether(dst=requesting_mac,src=destination_mac, type=0x0806)
#sendp(frame, iface=eth_inteface)
arp_packet = ARP(
    hwtype=1,
    ptype=0x0800,
    hwlen=6,
    plen=4,
    op=2,
    hwsrc= destination_mac,
    psrc= destination_ip,
    hwdst= requesting_mac,
    pdst= requesting_ip,
    )

sendp(eth_frame/arp_packet, iface=eth_inteface)


