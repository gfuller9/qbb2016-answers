#!/usr/bin/env Python

import sys
import matplotlib.pyplot as plt

pca = open(sys.argv[1])
x = []
y = []
ident = []
snp = []
sample = []
counter = ""
for i, line in enumerate(pca):
    fields = line.rstrip("\r\n").split(" ")
    if fields[0] != sample:
        counter = fields[0]
        sample.append(fields[0])
    else:
        continue
    
    x.append(fields[2])
    y.append(fields[3])

print str(x) + str(y)

plt.figure()
plt.scatter(x,y, label = ["PC1", "PC2"])
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Principle Components of Genotype")
plt.savefig("PCA.png")
