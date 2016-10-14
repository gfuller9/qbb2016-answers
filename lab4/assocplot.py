#!/usr/bin/env Python
#Usage: ./assocplot.py <input file> <plotname>
import sys
import matplotlib.pyplot as plt
import math

assoc = open(sys.argv[1])

pos = []
pos_sig = []
log_sig = []
log = []


for i, line in enumerate(assoc):
    if i > 0:
        fields = line.rstrip("\r\n").split()
        try:
            float(fields[8])
            if float(fields[8])<0.00001:
                pos_sig.append(fields[2])
                log_sig.append(math.log10(float(fields[8]))*-1)
                
            else:
                pos.append(fields[2])
                log.append((math.log10(float(fields[8])))*(-1))

        except ValueError:
            continue

plt.figure()
plt.scatter(pos,log, s = 20, alpha = 0.1)
plt.scatter(pos_sig,log_sig, color = 'red', s=20, alpha = 0.5)
plt.xlabel("Chromosome Position")
plt.xlim(0,1700000)
plt.ylabel("-log10 (P)")
plt.title(sys.argv[2])
plt.savefig(sys.argv[2]+".png")