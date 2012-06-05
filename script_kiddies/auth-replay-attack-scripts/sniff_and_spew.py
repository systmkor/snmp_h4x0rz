import pysnmp
import pcapy
import sys
import string
import time
import socket
UDP_IP="127.0.0.1"
UDP_PORT=161
f = open ('/home/ramrod/get_data', 'r')
parts = list()
parts = f.read()
MESSAGE = bytearray(parts)

sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
sock.sendto( MESSAGE, ( UDP_IP, UDP_PORT ) )
(newdata, fromAddr) = sock.recvfrom(10000)
tempstr =  ''
prevcar = ' '
for car in newdata:
  if car.isalpha() :
    tempstr += car
  elif prevcar.isalpha():
    print tempstr
    tempstr = ''
  prevcar = car
print tempstr
#return_message = bytearray(newdata)
