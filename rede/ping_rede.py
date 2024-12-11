import os, re, sys
from socket import *


pre = '10.0.0.'
for ip in range(10, 20): 
    # print (pre+str(ip))
    cmd = 'ping -c2 ' + (pre+str(ip))
    r = "".join(os.popen(cmd).readlines())
    if re.search(' ttl', r):
    	print ('HOST ON: ', pre+str(ip))
# cmd = 'ping -c2 ' + '10.0.0.7'
# r = "".join(os.popen(cmd).readlines())
# print (r)


"""
i=0
os.system("clear")
print "+----------------------+"
print '|By: Wickedpy          |'
print '|******* IPZork *******|'
print '+----------------------+' 
print '[+] Verificando ips na rede [+]'
while i < len(ips):
   cmd = 'ping -c1 ' + ips[i]
   r = "".join(os.popen(cmd).readlines())
   if re.search(' ttl',r):
      print '[+] HOST ON:' ,ips[i]
   i+=1
"""