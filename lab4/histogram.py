#!/usr/bin/env Python

import sys
import matplotlib.pyplot as plt

freq = open(sys.argv[1])
frequencies = []

for i, line in enumerate(freq):
    if i > 0:
        fields = line.rstrip("\r\n").split("     ")
        try:
            float(fields[2])
            if float(fields[2]) == 2016:
                continue
            else:
                frequencies.append(float(fields[2]))
        except ValueError:
            frequencies.append(float(fields[3]))
            continue

    else:
        continue
    

plt.figure()
plt.hist(frequencies, bins = 100)
plt.xlabel("Frequency")
plt.ylabel("Number")
plt.title("Frequency of SNPs")
plt.savefig("frequency_histogram.png")

