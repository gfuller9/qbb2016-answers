#!/usr/bin/env python

"""Calculates number of contigs, minimum, maximum and average length and the N50

usage: ./assembly_stats.py <filename 1> <outname>"""

import sys


infile = open(sys.argv[1])
counter = 0
contigs = {}
#make a dictionary of the contigs
for line in infile:
    line.rstrip("\r\n")
    
    if line.startswith(">"):
        contigs[line] = []
        worker = line
    else:
        contigs[worker].append(line)

# figure out the shortest and the largest
for entry in contigs:
    contigs[entry]= ''.join(contigs[entry])
min_len = 10000000000000000000000
max_len = 0   
lengths = []
for entry in contigs:
    counter = counter + 1
    if len(contigs) == 1:
        min_len = len(contigs[entry])
        max_len = len(contigs[entry])
        lengths.append(len(contigs[entry]))
        
    else:
        if len(contigs[entry]) < min_len:
            min_len = len(contigs[entry])
        elif len(contigs[entry]) > max_len:
            max_len = len(contigs[entry])
            lengths.append(len(contigs[entry]))
print "Statistics for ", sys.argv[2]
print "Number of contigs: ", counter
print "min length: ", min_len
print "max length", max_len
total = 0
#get total length
for item in lengths:
    total = total + item
#calculate the average
lengths = sorted(lengths)
print len(lengths)

print "average length: ", total/counter
n50_counter = 0
n50 = 0
if len(lengths) == 1:
    print "N50 = 1"
else:
    for i, item in enumerate(lengths):
        n50_counter = n50_counter + int(item)
        if n50 == 0:
            if n50_counter >= total/2:
                n50 = i
            else:
                continue
                print "N50 = ", n50
    

    
    
    
    
    

        
        
        
    



