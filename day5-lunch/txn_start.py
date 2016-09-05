#!/usr/bin/env python
"""
Usage: ./txn_start.py <file>
"""
import sys


import matplotlib.pyplot as plt
#I need a list of chromosomes to be sure I can sort things not in chromosomes
chromosomes = ["X", "Y", "2L", "2R", "3L","3R", "4"]
#Open the file
data = open(sys.argv[1])

#print "chromosome" + "\t" + "start" +"\t"+ "end" + "\t"+ "t_name"
#Enumerate through the ctab file
for i, line in enumerate(data):
    #skip header
    if i == 0:
        continue
    #split up lines by tab
    fields = line.rstrip("\r\n").split("\t")
    #ignore reads that don't map to chromosomes
    if fields[1] not in chromosomes:
        continue
    #if they're on the negative strand, we need to use the end position to define the promoter region
    if fields[2] == "-":
        #adding 500 to either end of the end position and printing it out in the format for .bed file
        #also making sure if there is a transcript w/ end right at the start of chromosome it is handled differently
        if int(fields[4]) < 500:
            print fields[1] + "\t" + str(int(fields[4])+500) + "\t" + str(0) + "\t" + fields[5]
            
            continue
        else:   
                 
            print fields[1] + "\t" + str(int(fields[4])+500) + "\t" + str(int(fields[4])-500) + "\t" + fields[5]
    #if on + strand, use the start position       
    elif fields[2]== "+":
        if int(fields[3]) < 500:
            print fields[1]+ "\t" + str(0) + "\t" + str(int(fields[3])) + "\t" + fields[5]
        else:        
            print fields[1]+ "\t" + str(int(fields[3])-500) + "\t" + str(int(fields[3])+500) + "\t" + fields[5]

    else: 
        continue
        


    