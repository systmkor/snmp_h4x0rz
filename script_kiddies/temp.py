
import socket
UDP_IP="127.0.0.1"
UDP_PORT=161
f = open ('/home/ramrod/get_data', 'r')
print f
parts = list()
for line in f:
  for word in line.split():
    print word
    parts.append(int(word, 16))
MESSAGE = bytearray(parts)
sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
sock.sendto( MESSAGE, ( UDP_IP, UDP_PORT ) )
print MESSAGE
