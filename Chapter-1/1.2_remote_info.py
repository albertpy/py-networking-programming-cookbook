#!/usr/bin/env python
#Python Nework Programming Cookbook -- Chapter-1
# This program is optimized for Python 2.7. It may run on
# any Python version with/without modifications.
import socket

def get_remote_machine_info():
   remote_host = 'www.bacsitamviet.com'
   try:
        print "IP address: %s" %socket.gethostbyname(remote_host)
   except socket.error, err_msg:
        print "%s: %s" %(remote_host, err_msg)

if __name__ == '__main__':
   get_remote_machine_info()
