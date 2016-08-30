#!/usr/bin/env python
import sys

file = open (sys.argv[1])
mapq = 0
lines = []
for line in file:
    
    
    if line.startswith("@"):
        continue
    else:
        mapq = mapq + int(line[4])
        lines.append(line)

print float(mapq/len(lines))
        
                  
        



file.close()