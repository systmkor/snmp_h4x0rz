import pcapy
import socket
import os
from impacket import ImpactDecoder, ImpactPacket
def my_fun(hdr, data):
  decoder = ImpactDecoder.LinuxSLLDecoder()
  eth = decoder.decode(data)
  ip = eth.child()
  udp = ip.child()
  if udp.get_uh_dport() == 161:
    print "snmp found."
    snmpd = udp.child()
    print snmpd.get_packet()
#    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    print ip.get_ip_dst()
#    sock.sendto(snmpd.get_packet(), (ip.get_ip_dst(), 161)) 

def main():
  
  cap = pcapy.open_live('any', 2000, True, 1000)
  cap.setfilter('ip proto \\udp')
  cap.loop(-1, my_fun)
if __name__ == "__main__":
  main()
