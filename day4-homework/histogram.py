#!/usr/bin/env python

"""
Makes a histogram of data from a ctab file
NEED TO CHANGE THE TITLE OF THE GRAPH IN LINE 24
usage: ./histogram.py <ctab file>
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

df = pd.read_table(sys.argv[1])
df_fp = df["FPKM"]>0
dflog = np.log10(df[df_fp]["FPKM"].values)
print dflog

plt.figure
plt.hist(dflog, bins = 30)

plt.xlabel("log FPKM")
plt.ylabel("Counts")
plt.title("Transcripts in SRR072893")
plt.savefig("histogram.png")
plt.close()

