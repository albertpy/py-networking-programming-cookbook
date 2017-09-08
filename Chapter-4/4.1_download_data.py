#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program requires Python 3.5.2 or any later version
# It may run on any other version with/without modifications.
#
# Follow the comments inline to make it run on Python 2.7.x.

import argparse

#import urllib.request
# Comment out the above line and uncomment the below for Python 2.7.x.
import urllib
import urllib2
from urllib import urlopen

REMOTE_SERVER_HOST = 'http://www.cnn.com'

class HTTPClient:

    def __init__(self, host):
        self.host = host

    def fetch(self):
        #response = urllib.request.urlopen(self.host)
        # Comment out the above line and uncomment the below for Python 2.7.x.
        response = urllib2.urlopen(self.host)

        data = response.read()
        text = data.decode('utf-8')
        return text

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HTTP Client Example')
    parser.add_argument('--host', action="store", dest="host", default=REMOTE_SERVER_HOST)

    given_args = parser.parse_args()
    host = given_args.host
    client = HTTPClient(host)
    print client.fetch()
[root@python learn]# more 4.1_download_data.py
#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter - 4
# This program is optimized for Python 2.7.
# It may run on any other version with/without modifications.

import argparse
import httplib

REMOTE_SERVER_HOST = 'www.python.org'
REMOTE_SERVER_PATH = '/'

class HTTPClient:

    def __init__(self, host):
        self.host = host

    def fetch(self, path):
        http = httplib.HTTP(self.host)

        # Prepare header
        http.putrequest("GET", path)
        http.putheader("User-Agent", __file__)
        http.putheader("Host", self.host)
        http.putheader("Accept", "*/*")
        http.endheaders()

        try:
            errcode, errmsg, headers = http.getreply()

        except Exception, e:
                print "Client failed error code: %s message:%s headers:%s" %(errcode, errmsg, headers)
        else:
            print "Got homepage from %s" %self.host

        file = http.getfile()
        return file.read()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='HTTP Client Example')
    parser.add_argument('--host', action="store", dest="host",  default=REMOTE_SERVER_HOST)
    parser.add_argument('--path', action="store", dest="path",  default=REMOTE_SERVER_PATH)
    given_args = parser.parse_args()
    host, path = given_args.host, given_args.path
    client = HTTPClient(host)
    print client.fetch(path)
    
    *******************
    
    Use command: 
    # python 4.1_download_data.py --host=http://cnn.com
    
