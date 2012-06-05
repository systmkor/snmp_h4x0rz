So:

capture_snmp has some base functionality for parsing a file.
Despite being only a few lines, this took me several hours to hack
together. The libraries are poorly documented.

http://code.google.com/p/impacket/source/browse/trunk/impacket/ImpactPacket.py?r=183
Contains the packet format, though its ugly.

This is the function you will be interested in for gaining info
def get_byte(self, index):
        "Return byte at 'index'"
at specific indides within the snmp packet.

Other than that, I wish you all the best of luck. I am sorry, its 2 am.