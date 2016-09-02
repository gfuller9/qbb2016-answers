#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

chromosomes = ["X", "Y", "2L", "2R", "3L","3R", "4"]
data = open(sys.argv[1])

#print "chromosome" + "\t" + "start" +"\t"+ "end" + "\t"+ "t_name"

for i, line in enumerate(data):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    if fields[1] not in chromosomes:
        continue
    
    if fields[2] == "-":

        if int(fields[4]) < 500:
            print fields[1] + "\t" + str(int(fields[4])+500) + "\t" + str(0) + "\t" + fields[5]
            
            continue
        else:        
            print fields[1] + "\t" + str(int(fields[4])+500) + "\t" + str(int(fields[4])-500) + "\t" + fields[5]
           
    elif fields[2]== "+":
        if int(fields[3]) < 500:
            print fields[1]+ "\t" + str(0) + "\t" + str(int(fields[3])) + "\t" + fields[5]
        else:        
            print fields[1]+ "\t" + str(int(fields[3])-500) + "\t" + str(int(fields[3])+500) + "\t" + fields[5]

    else: 
        continue
        

#for _, _, chro, strand, start, end, t_name, _, _, _, _, _, _ in df.itertuples():
#   if strand == "-":

#        d[chro] = (int(pd.read_table(sys.argv[1], index_col = "chr")["start"])-500, int(pd.read_table(sys.argv[1], index = "chr")["start"])+500,pd.read_table(sys.argv[1], index = "chr")["t_name"])
#    else: 
#        d[chro] = (int(pd.read_table(sys.argv[1], index_col = "chr")["end"])+500, int(pd.read_table(sys.argv[1], index = "chr")["end"])-500,pd.read_table(sys.argv[1], index = "chr")["t_name"])

#df = pd.DataFrame( d )
#df.to_csv (sys.stdout)
    