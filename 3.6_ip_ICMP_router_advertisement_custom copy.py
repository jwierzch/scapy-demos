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

icmp_type=b'\x09'
icmp_code=b'\x00'
icmp_checksum=b'\xf1\xf5'

# Advertisement count. 8 bits.
# The number of router advertisements in this message. Each advertisement contains one router address/preference level pair.
advertisement_count=b'\x01'

# Address Entry size. 8 bits.
# The number of 32-bit words of information for each router address entry in the list. The value is normally set to 2 (router address + preference level).
address_entry_size=b'\x02'

# Lifetime. 16 bits.
# The maximum number of seconds that the router addresses in this list may be considered valid.
lifetime=b'\x00\x01'

# Router address. 32 bits.
# The IPv4 address of the advertised router.
router_address=b'\x01\x02\x03\x04'

# Preference level. 32 bits, signed.
# The preferability of the router address as a default router address, relative to other router addresses on the same subnet. This is a twos-complement value where higher values indicate that the route is more preferable.
preference=b'\x00\x00\x00\x01'

icmp_payload=icmp_type+icmp_code+icmp_checksum+advertisement_count+address_entry_size+lifetime+router_address+preference
sendp(eth_frame/ip_packet/icmp_payload, iface=eth_inteface)


