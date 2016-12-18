#!/usr/bin/env python

import sys
import scipy.stats as stats
import itertools

my_data = open(sys.argv[1])

data = []

early = []

late = []

for i, item in enumerate(my_data):
	if i == 0:
		continue
	else:
		lines = item.rstrip("\r\n").split("\t")
		data.append([lines[0],lines[1],lines[5],lines[2],lines[3]])
        late.append([lines[2],lines[3]])

enriched = []

deenriched = []
        
for item in data:
    a = float(item[1]) + float(item[2])
    b = float(item[3]) + float(item[4])
    ava = float(a)/2
    avb = float(b)/2
    if avb/ava > 2:
        item.append(avb/ava)
        enriched.append(item)
    if avb/ava < 0.5:
        item.append(avb/ava)
        deenriched.append(item)

enriched_significant = []

deenriched_significant = []

for item in enriched:
     a = [float(item[1]),float(item[2])]
     b = [float(item[3]),float(item[4])]
     p = stats.ttest_ind(a,b)
     if p[1] < 0.05:
         item.append(p[1])
         
         enriched_significant.append(item) 

for item in deenriched:
     a = [float(item[1]),float(item[2])]
     b = [float(item[3]),float(item[4])]
     p = stats.ttest_ind(a,b)
     if p[1] < 0.05:
         item.append(p[1])
         
         deenriched_significant.append(item) 

counter = 0
most_enriched = 0
for i, item in enumerate(enriched_significant):
    if i==0:
        counter = item[5]
        most_enriched = item
        continue
    elif float(item[5]) > counter:
        counter = item[5]
        most_enriched = item
        continue
    else:
        continue

print "enrichment\tgene\tp-value(ttest)\tenrichment(late/early)"
print 'most_enriched:\t' + str(most_enriched[0]) + "\t" + str(most_enriched[6]) + "\t" + str(most_enriched[5])
for item in enriched_significant:
    print 'enriched:\t' + str(item[0]) +"\t" + str(item[6]) + "\t" + str(item[5])
for item in deenriched_significant:
    print 'deenriched:\t' + str(item[0]) + "\t" + str(item[6]) + "\t" + str(item[5])
