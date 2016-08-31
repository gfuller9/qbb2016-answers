#!/usr/bin/env python
#Usage: ./day2-homework-2.py {filename map} {filename target} {-options}
#options:
# d     replaces empty mappings with a "." (dot)
# e     replaces empty mappings with nothing (empty)
# can only use one option, must have a "-" before option
import sys
# open arguements

mapping = open(sys.argv[1])
target = open(sys.argv[2])
option = sys.argv[3] 

#make empty dict
prot_map = {}
#add stuff to dictionary
for i, line in enumerate (mapping):
    lines = line.rstrip("\r\n").split("\t")


    prot_map[lines[0].strip()]=lines[1]



# enumerate through the ctab file 

for i, line in enumerate (target):
    if i == 0:
        continue
    
    #split lines of ctab file
    lines = line.rstrip("\r\n").split("\t")
    name = lines[8].strip()
    #check if FlyBase name in dictionary

    if name in prot_map:
        lines[8]=prot_map[name]
        print "\t".join(lines)
    #if not in dictionary, replacing the different ones with options    
    elif name not in prot_map: 
        if option == "d":
            lines[8]=sys.argv[4]
            print "\t".join(lines)
        elif option == "e":
            lines[8] == None
            print "\t".join(lines)
        


