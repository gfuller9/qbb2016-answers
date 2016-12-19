#!/usr/bin/env python

import h5py
import sys
import numpy as np

file= h5py.File(sys.argv[1])

print file[u'0.expected']
print file[u'0.counts']
print file[u'0.positions']
print file[u'regions']

mystuff = open(sys.argv[1])

counts = file['0.counts'][...]
expected = file['0.expected'][...]
positions = file['0.positions'][...]
regions = file['regions'][...]

counts[counts < 1.0] = 0.00000001
expected[expected < 1.0] = 0.00000001

enrich = counts/expected
logenrich = np.log(enrich)
#logexpected = np.log(expected)
#np.set_printoptions(threshold=np.nan)
#enrichment = logcounts/logexpected

numbers = []
#set enrichment threshold of 2

enrichpos = []
#iterate through the array
for i, item in enumerate(enrich):
    #iterate through each subarray
    for n, value in enumerate(enrich[i]):
        #check to see if enriched, if so, add the coordinates to a list
        if value > 2:
            
            enrichpos.append([i,n,value])
   
#translate that list into our coordinates

print len(positions)
firstcoords = []
secondcoords = []

for item in positions:
    firstcoords.append(item[0])
    secondcoords.append(item[1])

#for i, item in enrichpos:
#    if item
enriched_positions = []

for i, item in enumerate(enrichpos):
    a= item[0]
    b = item[1]
    val = item[2]
    enriched_positions.append([firstcoords[a],secondcoords[b],val])

already = []
for item in positions:
    already.append([item[0],item[1],0])
already2 = []

for item in enriched_positions:
    for i, thing in enumerate(already):       
        if item[0] == thing[0]:
            if item[2] > thing[2]:
                already[i] = [item[0],item[1],item[2]]
            if item[2] < thing[2]:
                continue
        elif item[1] == thing[1]:
            if item[2] > thing[2]:
                already[i] = [item[0],item[1],item[2]]
            if item[2] < thing[2]:
                continue
                
for item in already:
    print item



