#!/usr/bin/env python
"""
Usage: ./linreg.py <bigwig output file (tab)> <ctab file>
"""

import numpy as np
import statsmodels.api as sm
import sys
import matplotlib.pyplot as plt

data1 = open(sys.argv[1])
ctab = open(sys.argv[2])

d1 = {}
d2 = {}
#enumerate through the ctab file 
for i, line in enumerate(ctab):
    #skip header
    if i == 0:
        continue
    #split open lines and tab separate
    else:    
        fields = line.rstrip("\r\n").split("\t")
        #convert fpkm values to floats and append to a dictionary
        fields[10]=float(fields[10])
        d1[fields[5]] = fields[10]
   



#extract values from the tab files to the dictionary; average from tab and then fpkm from the ctab as values for key of txnscript name
for line in data1:
    fields = line.rstrip("\r\n").split("\t")
    if fields[0] in d1:
        d2[fields[0]] = [float(fields[3]),d1[fields[0]]]
#make lists for averages and the fpkm
aver = []
fpkm = []
#append to those lists
for item in d2:
    aver.append(d2[item][0])
    fpkm.append(d2[item][1])
#convert data to arrays
aver = np.asarray(aver)
fpkm = np.asarray(fpkm)
#figure options to see what the coverage looks like plotted against fpkm
#plt.figure()
#plt.scatter(aver,fpkm)
#plt.show()
#make the model with linear regression
model = sm.OLS(aver,fpkm)
results = model.fit()
print results.summary()







