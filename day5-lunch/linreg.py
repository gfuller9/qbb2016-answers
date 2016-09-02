#!/usr/bin/env python

import numpy as np
import statsmodels.api as sm
import sys
import matplotlib.pyplot as plt

data1 = open(sys.argv[1])
ctab = open(sys.argv[2])

d1 = {}
d2 = {}

for line in ctab:
    fields = line.rstrip("\r\n").split("\t")
    d1[fields[5]] = fields[10]



for line in data1:
    fields = line.rstrip("\r\n").split("\t")
    if fields[0] in d1:
        d2[fields[0]] = [float(fields[4]),float(d1[fields[0]])]

aver = []
fpkm = []

for item in d2:
    aver.append(d2[item][0])
    fpkm.append(d2[item][1])
aver = np.asarray(aver)
fpkm = np.asarray(fpkm)
plt.figure()
plt.scatter(aver,fpkm)
plt.show()
model = sm.OLS(aver,fpkm)
results = model.fit()
print results.summary()







