from __future__ import print_function
from netmiko import ConnectHandler
import sys
import time
import select
import paramiko
import re
#fd = open(r'C:\Users\Administrateur\Desktop\Rslt.txt','w') # Where you want the file to save to.
#old_stdout = sys.stdout   
#sys.stdout = fd 
platform = 'cisco_ios'
username = 'admin' # edit to reflect
password = 'Pr0xySn@ke' # edit to reflect

ip_add_file = open(r'C:\IPAddressList.txt','r') # a simple list of IP addresses you want to connect to each one on a new line


print(username)


for host in ip_add_file:
    host = host.strip()
    print(host)
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    #output = device.send_command('terminal length 0')
    #output = device.send_command('enable') #Editable to be what ever is needed
    print('##############################################################\n')
    print('...................CISCO COMMAND SHOW RUN OUTPUT......................\n')
    output = device.send_command('sh version')
    print(output)
    print('##############################################################\n')
    print('...................CISCO COMMAND SHOW IP INT BR OUTPUT......................\n')
    output = device.send_command('sh ip int br')
    print(output) 
    print('##############################################################\n')

fd.close()
