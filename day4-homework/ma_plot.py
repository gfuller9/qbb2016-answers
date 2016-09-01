#!/usr/bin/env python

"""
Usage: ./ma_plot.py <ctab file 1> <ctab file 2>
"""
#import that stuff to use later
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


#read the data frames for the files
df1 = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

#pull out the FPKM values
#since they are organized the same, transcript id's line up :D
data1 = df1["FPKM"].values 
data2 = df2["FPKM"].values

#print type(data2)


#take logs of these data frames
logdf1 = np.log2(data1)
logdf2 =np.log2(data2)
#calculate M and A statistics (note M is y, A is x)
y = logdf1-logdf2
x = 0.5 * (logdf1 + logdf2)

#make the figure
plt.figure
plt.scatter(x,y)
plt.xlabel("A")
plt.title("MA Plot Comparing SRR072893, SRR072915")
plt.ylabel("M")
plt.savefig("maplot.png")

