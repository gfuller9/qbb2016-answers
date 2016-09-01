#!/usr/bin/env python


import sys

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_table(sys.argv[1])

df2 = pd.read_table(sys.argv[2])

df1main2l = df1["chr"] == "2L"
df2main2l = df2["chr"] == "2L"
df1main2r = df1["chr"]=="2R" 
df2main2r = df2["chr"]=="2R"
df1main3l = df1["chr"]=="3L" 
df2main3l = df2["chr"]=="3L"
df1main3r = df1["chr"]=="3R" 
df2main3r = df2["chr"]=="3R"
df1main4 = df1["chr"]=="4"
df2main4 = df2["chr"]=="4"
df1mainx = df1["chr"]=="X"
df2mainx = df2["chr"]=="X"

data_frames = [df1main2l,df2main2l,df1main2r,df2main2r,df1main3l,df2main3l,df1main3r,df2main3r,df1main4,df2main4,df1mainx,df2mainx]
chromosome = ['2R','2L','3R','3L','4','X']

for item in chromosome:
    dfroi1 = df1["chr"] == item
    dfroi2 = df2["chr"] == item
    dfmain = df1[dfroi1]
    dfmain2 = df2[dfroi2]
    smoothed =dfmain["FPKM"].rolling(int(sys.argv[3])).mean()
    smoothed2 = dfmain2["FPKM"].rolling(200).mean()
    plotty = (smoothed, smoothed2)
    plt.figure()
    plt.plot(smoothed, label = "Sample 1")
    plt.plot(smoothed2, label = "Sample 2")
    plt.title("Chromosome " + item)
    plt.savefig(item)
    plt.close

#for item in range(0, len(data_frames),2):
 #   print item
  #  smoothed = data_frames[item]["FPKM"].rolling(200).mean()
   # smoothed2 = data_frames[item+1]["FPKM"].rolling(200).mean()