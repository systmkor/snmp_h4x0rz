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

def dict_krak(msg='', digest='', pass_dict=''):
  for line in open(pass_dict, 'r')
    if hmac.new(key=line, msg).hexdigest() == digest:
      print line

def print_password(passwd='', pathname='', stdout=True):
  
  if stdout:
    print(passwd)

