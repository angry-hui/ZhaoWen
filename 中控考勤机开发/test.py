import os
import re
import time
import sys
import subprocess
 
lifeline = re.compile(r"(\d) received")
report = ("No response","Partial Response","Alive")
 
print(time.ctime())
 
for host in range(1,10):
   ip = "192.168.1."+str(host)
   pingaling = subprocess.Popen(["ping","-q", "-c 2", "-r", ip], shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
   print("Testing ",ip,)
   ppywhile 1:
      pingaling.stdout.flush()
      line = pingaling.stdout.readline()
      if not line: break
      igot = re.findall(lifeline,line)
      if igot:
           #report[int(igot[0])]
           pass
 
print(time.ctime())