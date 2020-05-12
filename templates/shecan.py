#!/bin/python
###
import os
import requests

import socket
from bs4 import BeautifulSoup

proxy={}
response = requests.get('https://shecan.ir' , proxies=proxy)
    #get html of the site
result = BeautifulSoup(response.text ,'html.parser' )
    #use Beautifull soup to read htmls
res = result.find_all('span' , attrs={'class':'shecan-dns-ips'}) 
for dns in res:
    DnsAddress = dns.text
    try:
        socket.inet_aton(DnsAddress)
        os.system(f'''sudo echo 'nameserver {DnsAddress}' >> /etc/resolv.conf''')
        print("correct")
    except socket.error:
        print("Error")
print("Done!")
