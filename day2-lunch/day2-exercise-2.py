#!/usr/bin/env python
import sys

no_mismatch = []
file = open (sys.argv[1])
for line in file.readlines():
    
    
    if line.startswith("@"):
        continue
    elif "NM:i:0" in line:
        no_mismatch.append(str(line))
    else:
        continue
        
        
        


print len(no_mismatch)

file.close()
