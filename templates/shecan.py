#!/bin/python
## python web scraping script
### Automating Changing resolv config for docker installation
import os
import requests

import socket
from bs4 import BeautifulSoup

# get ips from shecan DNS ip addresses
proxy={} # use proxy if needed
response = requests.get('https://shecan.ir' , proxies=proxy)
    #get html of the site
result = BeautifulSoup(response.text ,'html.parser' )
    #use Beautifull soup to read htmls
res = result.find_all('span' , attrs={'class':'shecan-dns-ips'}) 
for dns in res:
    DnsAddress = dns.text
    try:
        socket.inet_aton(DnsAddress)
        # pass output into bash command 
        os.system(f'''sudo echo 'nameserver {DnsAddress}' >> /etc/resolv.conf''')
        print("correct")
    except socket.error:
        print("Cant change resolv config file")
print("Done!")
