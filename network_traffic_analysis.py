# nmap - network mapper
# pcap - to capture packets (all or filtered)
# netstat - network stats
# Wireshark - comprehensive analysis of the network
# analysis can be an attack


from scapy.all import *
 
for pkt in sniff(iface='en0', count=5):
    print('Packet: ' + str(pkt.summary()) + '\n')
    
# Remediation: disabling ports and services, e.g. default FTP protected (updates) or disabled; firewall; encrypted traffic (point-to-point)
