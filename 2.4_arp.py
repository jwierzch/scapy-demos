#!/usr/bin/python
from scapy.all import *


eth_inteface = "Intel(R) Ethernet Connection (13) I219-LM"
src_mac='AA:AA:AA:AA:AA:AA'
dst_mac='FF:FF:FF:FF:FF:FF'

eth_frame = Ether(dst=dst_mac,src=src_mac, type=0x0806)

arp_packet = ARP(
    hwtype=1,
    ptype=0x0800,
    hwlen=6,
    plen=4,
    op=1,
    hwsrc= 'BB:BB:BB:BB:BB:BB',
    psrc= '10.1.10.10',
    hwdst= 'EE:EE:EE:EE:EE:EE',
    pdst= '75.75.75.75'
    )

sendp(eth_frame/arp_packet, iface=eth_inteface)

arp_packet = ARP(
    hwtype=1,
    ptype=0x0806,
    hwlen=6,
    plen=4,
    op=1,
    hwsrc= 'BB:BB:BB:BB:BB:BB',
    psrc= b'\x0a\x01\x0a\x0a',
    hwdst= 'EE:EE:EE:EE:EE:EE',
    pdst= b'\x4b\x4b\x4b\x4b'
    )


sendp(eth_frame/arp_packet, iface=eth_inteface)

arp_packet = ARP(
    hwtype=2,
    ptype=0x0842,
    hwlen=6,
    plen=4,
    op=1,
    hwsrc= 'BB:BB:BB:BB:BB:BB',
    psrc= b'\x0a\x01\x0a\x0a',
    hwdst= 'EE:EE:EE:EE:EE:EE',
    pdst= b'\x4b\x4b\x4b\x4b'
    )

sendp(eth_frame/arp_packet, iface=eth_inteface)

arp_packet = ARP(
    hwtype=4,
    ptype=0x22F0,
    hwlen=6,
    plen=4,
    op=1,
    hwsrc= 'BB:BB:BB:BB:BB:BB',
    psrc= b'\x0a\x01\x0a\x0a',
    hwdst= 'EE:EE:EE:EE:EE:EE',
    pdst= b'\x4b\x4b\x4b\x4b'
    )

sendp(eth_frame/arp_packet, iface=eth_inteface)

arp_packet = ARP(
    hwtype=5,
    ptype=0x3600,
    hwlen=6,
    plen=4,
    op=1,
    hwsrc= '00:50:56:BB:BB:BB',
    psrc= b'\x0a\x01\x0a\x0a',
    hwdst= 'EE:EE:EE:EE:EE:EE',
    pdst= b'\x4b\x4b\x4b\x4b'
    )

sendp(eth_frame/arp_packet, iface=eth_inteface)