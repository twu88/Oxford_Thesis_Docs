#!/usr/bin/env python
import os
import glob

from scapy.all import *
from subprocess import Popen


#import trimpcap
#from scapy.layers.inet import TCP, ICMP, IP, Ether

#open file upload file if pcapng process if not error 
#process pcap extract the payload then filter for tcp and udp write results to .dat file 
#Take the output .dat file to work out entropy 
#trimpcap 32,64,100kb		
#ent.py

#for every pcap file take the filename to create new .dat file

#Popen('python3 trimpcap.py 1000 *.pcapng')

#pcap = rdpcap("withings_monitor_merge.pcapng")

#for pkt in pcap:
#	if Raw in pkt:
#		out = open("out.dat", "wb")
#		out.write(pkt[Raw].load)
#		#print(pkt[Raw])
			

def handler(packet):
	print(f)
	f.write(str(packet.payload.payload.payload))

for filename in os.listdir(os.curdir):
	if filename.endswith(".pcapng"):		
		Popen('python3 trimpcap.py 500 filename')
		f = open((filename.rsplit(".", 1) [0] ) +".dat", "wb")
		sniff(offline=filename, prn=handler, filter='tcp or udp')
		
#Popen('python3 ent.py -t *.dat > results.txt')

	
