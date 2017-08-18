#!/usr/bin/env python
#Python Nework Programming Cookbook -- Chapter-1
# This program is optimized for Python 2.7. It may run on
# any Python version with/without modifications.

import socket

def find_service_name():
   protocolname = 'tcp'
   for port in [80, 25, 22, 8080, 21]:
        print "Port: %s => service name: %s" %(port, socket.getservbyport(port, protocolname))
   print "Port: %s => service name: %s" %(53, socket.getservbyport(53, 'udp'))

if __name__ == '__main__':
   find_service_name()
