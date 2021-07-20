#!/usr/bin/python
from scapy.all import *


eth_inteface = "Intel(R) Ethernet Connection (13) I219-LM"
src_mac='00:50:56:AA:AA:AA'  
dst_mac='00:50:56:FF:FF:FF'
broadcast_mac='FF:FF:FF:FF:FF:FF'

src_ip='10.10.10.10'
dst_ip='20.20.20.20'

user_seq = 1000000 #random num starting the seq
server_seq = 2000000 #random num starting the seq


############# Handshake #############
#USER: SYN
eth_frame_src = Ether(dst=dst_mac,src=src_mac, type=0x0800)
ip_packet_src = IP(dst=dst_ip,src=src_ip)

src_port = 1025
dst_port = 80
seq=user_seq
ack = 0 #no ack yet were just starting
# FIN = 0x01
# SYN = 0x02
# RST = 0x04
# PSH = 0x08
# ACK = 0x10
# URG = 0x20
# ECE = 0x40
# CWR = 0x80
flags = 0x02
tcp_src= TCP(sport=src_port, dport=dst_port, seq=seq, ack=ack,flags=flags)
sendp(eth_frame_src/ip_packet_src/tcp_src, iface=eth_inteface)

#SERVER: SYN-ACK
eth_frame_rsp = Ether(dst=src_mac,src=dst_mac, type=0x0800)
ip_packet_rsp = IP(dst=src_ip,src=dst_ip)

src_port = 80
dst_port = 1025
seq=server_seq
user_seq=user_seq+1
ack = user_seq
flags = 0x12

tcp_resp = TCP(sport=src_port, dport=dst_port, seq=seq, ack=ack,flags=flags)
sendp(eth_frame_rsp/ip_packet_rsp/tcp_resp, iface=eth_inteface)

#USER: ACK
eth_frame_src = Ether(dst=dst_mac,src=src_mac, type=0x0800)
ip_packet_src = IP(dst=dst_ip,src=src_ip)

src_port = 1025
dst_port = 80
seq=user_seq
server_seq=server_seq+1
ack = server_seq #sender seq+1
flags = 0x10
tcp_src= TCP(sport=src_port, dport=dst_port, seq=seq, ack=ack,flags=flags)

sendp(eth_frame_src/ip_packet_src/tcp_src, iface=eth_inteface)

############# Data Transmission #############
#USER: Data request
eth_frame_src = Ether(dst=dst_mac,src=src_mac, type=0x0800)
ip_packet_src = IP(dst=dst_ip,src=src_ip)

src_port = 1025
dst_port = 80
seq=user_seq
ack = server_seq 
flags = 0x10
tcp_src= TCP(sport=src_port, dport=dst_port, seq=seq, ack=ack,flags=flags)

sendp(eth_frame_src/ip_packet_src/tcp_src/"give me data please.", iface=eth_inteface)

#SERVER: Data given
eth_frame_rsp = Ether(dst=src_mac,src=dst_mac, type=0x0800)
ip_packet_rsp = IP(dst=src_ip,src=dst_ip)

src_port = 80
dst_port = 1025
seq=server_seq
user_seq=user_seq+20
ack = user_seq
flags = 0x10

tcp_resp = TCP(sport=src_port, dport=dst_port, seq=seq, ack=ack,flags=flags)
sendp(eth_frame_rsp/ip_packet_rsp/tcp_resp/"here is some data", iface=eth_inteface)

#USER: Data Ack
eth_frame_src = Ether(dst=dst_mac,src=src_mac, type=0x0800)
ip_packet_src = IP(dst=dst_ip,src=src_ip)

src_port = 1025
dst_port = 80
seq=user_seq
server_seq = server_seq+17
ack = server_seq
flags = 0x10
tcp_src= TCP(sport=src_port, dport=dst_port, seq=seq, ack=ack,flags=flags)

sendp(eth_frame_src/ip_packet_src/tcp_src, iface=eth_inteface)

#SERVER: FIN
eth_frame_rsp = Ether(dst=src_mac,src=dst_mac, type=0x0800)
ip_packet_rsp = IP(dst=src_ip,src=dst_ip)

src_port = 80
dst_port = 1025
seq=server_seq
user_seq=user_seq
ack = user_seq
flags = 0x01

tcp_resp = TCP(sport=src_port, dport=dst_port, seq=seq, ack=ack,flags=flags)
sendp(eth_frame_rsp/ip_packet_rsp/tcp_resp, iface=eth_inteface)

#USER: FIN + ACK
eth_frame_src = Ether(dst=dst_mac,src=src_mac, type=0x0800)
ip_packet_src = IP(dst=dst_ip,src=src_ip)

src_port = 1025
dst_port = 80
seq=user_seq
server_seq = server_seq + 1
ack = server_seq
flags = 0x11
tcp_src= TCP(sport=src_port, dport=dst_port, seq=seq, ack=ack,flags=flags)

sendp(eth_frame_src/ip_packet_src/tcp_src, iface=eth_inteface)

#SERVER: ACK
eth_frame_rsp = Ether(dst=src_mac,src=dst_mac, type=0x0800)
ip_packet_rsp = IP(dst=src_ip,src=dst_ip)

src_port = 80
dst_port = 1025
seq=server_seq
user_seq=user_seq +1
ack = user_seq
flags = 0x10

tcp_resp = TCP(sport=src_port, dport=dst_port, seq=seq, ack=ack,flags=flags)
sendp(eth_frame_rsp/ip_packet_rsp/tcp_resp, iface=eth_inteface)