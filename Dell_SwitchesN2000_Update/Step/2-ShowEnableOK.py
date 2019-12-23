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
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password, secret=password)
    output = device.send_command('terminal length 0')
    print('##############################################################\n')
    print('...................COMMAND SHOW RUN OUTPUT......................\n')
    output = device.send_command('sh version')
    print(output)
    print('##############################################################\n')
    print('...................ENABLE......................\n')
    output = device.send_command('sh switch')
    print(2)
    print(output)
    print(device.enable(cmd='enable', pattern="ssword"))
    print(3)
    print('##############################################################\n')
    print('...................WRITE......................\n')

    print (device.check_enable_mode())
    print(device.is_alive())

    print(device.send_command('sho run inter vla 99', expect_string='exit', delay_factor=1, max_loops=500, auto_find_prompt=True, strip_prompt=True, strip_command=True, normalize=True, use_textfsm=False, use_genie=False))
    #expected string seem important on Dell
    
    print('##############################################################\n')

#fd.close()
