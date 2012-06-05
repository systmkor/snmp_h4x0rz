#!/usr/bin/python

####
#
# KRAK
#
# Description: An extremely basic hmac dictionary cracker. Just used
#   for test purpose for this project.
#
# Author: Orion Miller
#


class cli_options:
  passwd_out_path=''
  stdout = True
  pass_dict_path = ''

class snmp_info:
  snmp_filepath =''
  snmp_file = None
  msg = ''
  digest = ''

  def get_info(self):
    self.snmp_file = open(self.snmp_filepath, 'rb')
    self.digest = self.snmp_file.read(24)
    self.snmp_file.read(1) #passed the delim
    self.msg = self.snmp_file.read(1024) #crappy way of reading msg

import hmac

def main():
   cli_opt = cli_options()
   cli_opt.pass_dict_path = raw_input("Password Dictionary File Path: ") 
   info = snmp_info()
   info.snmp_filepath = raw_input("SNMP information file path: ")
   info.get_info()
   print(info.digest)
   print(info.msg)
   dict_krak(info.msg, info.digest, cli_opt.pass_dict_path)


def dict_krak(msg='', digest='', pass_dict=''):
  for line in open(pass_dict, 'r'):
    #print line,
    #print hmac.new(line[:-1], msg).hexdigest()[0:24]
    #print digest
    if hmac.new(line[:-1], msg).hexdigest()[0:24] == digest:
      print line

def print_password(passwd='', pathname='', stdout=True):
  if pathname is not '':
    f = open(pathname, 'w')
    f.write(passwd)
    f.close()

  if stdout:
    print(passwd)


if __name__ == "__main__":
  main()

