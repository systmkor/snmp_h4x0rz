####
#
# KRAK
#
# Description: An extremely basic hmac dictionary cracker. Just used
#   for test purpose for this project.
#
# Author: Orion Miller
#

#!/usr/bin/pythin

import hmac
pass_dict = ''
msg = ''
digest = ''
curr_digest = ''

#libpcap


for line in open(pass_dict, 'r')
  a = hmac.new(key=line, msg)
  if a.hexdigest() == digest:
    print line
#compare keys
#if keys are identical
#print the original and the dictionary key
#print the dictionary password
