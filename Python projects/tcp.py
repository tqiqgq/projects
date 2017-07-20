from scapy.all import *
import logging

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
destination  = "www.google.ru"
dport = 80
sport = 4444
my_seq = 2000

debug = True

pkt_ip = IP(dst=destination)
pkt_syn = pkt_ip/TCP(sport=sport, dport=dport, seq=my_seq, flags="S")
pkt_syn_ack = sr1(pkt_syn, verbose=0)


if pkt_syn_ack.ack != my_seq+1:
	print("Bad ACK number !")
remote_seq = pkt_syn_ack.seq
my_seq = my_seq+1


pkt_ack = pkt_ip/TCP(sport=sport, dport=dport, seq=my_seq, ack=remote_seq+1, flags="A")
send(pkt_ack)

if debug:
	print("######################### SYN ###############################")
	print("seq = %d, ack = %d" % (pkt_syn.seq, pkt_syn.ack))

	print("######################### SYN-ACK ############################")
	print("seq = %d, ack = %d" % (pkt_syn_ack.seq, pkt_syn_ack.ack))

	print("######################### ACK ###############################")
	print("seq = %d, ack = %d" % (pkt_ack.seq, pkt_ack.ack))
