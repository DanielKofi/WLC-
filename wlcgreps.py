import csv
import getpass
from netmiko import ConnectHandler
import time
import sys
import re

conn = ConnectHandler(device_type='cisco_wlc_ssh'
                ,ip = '10.10.10.10'
                ,username='admin'
                ,password='letmein'
                ,secret='now')
        #print(ap)
conn.enable() 


with open('aps1.csv', 'r') as f:
     readCSV = csv.reader(f, delimiter=',')
     for row in readCSV:
        ap = row[0]
        building = row[1]
        floor = row[2]
        
       
        output = conn.send_command("show ap config gen {}".format(ap))

        if 'invalid.' in output:
            print('could not log onto ap',ap)

       

        #print(output)

       # pat1 = pat.group(0)
        for line in output.splitlines():
            if 'AP LWAPP Up Time' in line:
                print(ap, '-',building,floor)
            
                print(line)
                print('---------')
               # print(pat1)
     
     