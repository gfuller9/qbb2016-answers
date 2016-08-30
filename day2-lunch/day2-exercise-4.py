#!/usr/bin/env python
import sys
right_lines = []
file = open (sys.argv[1])
lnum = 0
for line in file:
    
    
    if line.startswith("@"):
        continue
    else:
        lines = line.rstrip("\r\n").split("\t")
      
        if lines[2] != "*":
            print (lines[2])
            lnum = lnum + 1
            if lnum == 11:
                break
            
                  
        



file.close()