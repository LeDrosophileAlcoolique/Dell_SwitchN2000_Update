from __future__ import print_function
from netmiko import ConnectHandler

import sys
import time
import select
import paramiko
import re

import string



#Info switch
switch_new_version = "6.6.0.13"
switch_new_firmware = "N2000Stdv6.6.0.13.stk"
ip_tftp = "10.180.1.99"




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

    if (output.find(switch_new_version) > -1):
        print ("Switch à jour")
    else:
        print ("Switch pas à jour")

        print('##############################################################\n')
        print('...................MAJ du Bordel......................\n')
        print(device.enable(cmd='enable', pattern="ssword"))
        print (device.check_enable_mode())
        copy_cmd = "copy tftp://" + ip_tftp + "/" + switch_new_firmware + " backup"

        print(copy_cmd)
        #print(device.send_command(copy_cmd, expect_string="(y/n)", delay_factor=2, max_loops=500, auto_find_prompt=True, strip_prompt=True, strip_command=True, normalize=True, use_textfsm=False, use_genie=False))
        print(device.send_command(copy_cmd, expect_string="(y/n)", delay_factor=1))
        #time.sleep(20)
        print(device.send_command("y", delay_factor=))
        
        
    print('##############################################################\n')
    print('...................ENABLE......................\n')
    output = device.send_command('sh switch')
    print(2)
    print(output)
    print(device.enable(cmd='enable', pattern="ssword"))
    print(3)
    print('##############################################################\n')
    print('...................X......................\n')

    print (device.check_enable_mode())
    print(device.is_alive())

    print(device.send_command('sho run inter vla 99', expect_string='exit', delay_factor=1, max_loops=500, auto_find_prompt=True, strip_prompt=True, strip_command=True, normalize=True, use_textfsm=False, use_genie=False))
    #expected string seem important on Dell
    
    print('##############################################################\n')

#fd.close()
