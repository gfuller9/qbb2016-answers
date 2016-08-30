#!/usr/bin/env python
import sys
right_lines = []
file = open (sys.argv[1])
for line in file.readlines():
    
    
    if line.startswith("@"):
        continue
    else:
        lines = line.rstrip("\r\n").split("\t")
        if lines[2] == "*":
            continue
        else:
            right_lines.append(str(line))
        
        

print len(right_lines)

file.close()
