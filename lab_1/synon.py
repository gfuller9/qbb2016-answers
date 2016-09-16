#!/usr/bin/env python

"""
Count synonymous and nonsynonymous mutations
usage: rev_trans <nucleotide alignments> <reference>
"""

import sys
import itertools
from itertools import islice
import matplotlib.pyplot as plt

def chunk_str(str, chunk_size):
    return [str[i:i+chunk_size] for i in range(0, len(str), chunk_size)]
#from Mike Lewis: http://stackoverflow.com/questions/5711452/how-do-i-slice-a-string-every-3-indices
codon_table = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W',
    }
queries = open(sys.argv[1])
reference = open(sys.argv[2])
refs = []
ref_full = []
#make list of codons in the reference
for line in reference:
    line = line.rstrip("\r\n")
    if line.startswith(">"):
        continue
        
    else:
        refs.append(line)

        refs_full = ''.join(refs)
        ref_full = chunk_str(refs_full,3)

elements = len(ref_full)
num = 0
#make empty lists with slot for each position
syn = [num]*elements
non = [num]*elements
#compare the sequences with the reference
#ignore deletions (only looking at SNPs)
for item in queries:
    seq = []
    item = item.rstrip("\r\n")
    if item.startswith("ATG"):
        seq = chunk_str(item,3)
        for i, line in enumerate(ref_full):
            if seq[i] in codon_table:
                if codon_table[seq[i]] == codon_table[ref_full[i]]:
                    
                    syn[i] = syn[i] + 1
                else:
                    non[i] = non[i] + 1
            else:
                #non[i] = non [ i ] + 1
                continue
    else:
        continue
#calcutlate ratio for each position and dn-ds
ratio = [num]*elements
d = [num]*elements
for i, item in enumerate(syn):
    d[i] = non[i]-syn[i]
    if syn[i] > 0:
        ratio[i] = float(non[i])/float(syn[i])
#this part is to calculate averages
av = 0
avrat = 0
variance = 0
for i, item in enumerate(d):
    av = av + d[i]
    avrat = avrat + ratio[i]

    
av = av/3431
avrat = avrat/3431
#calculate variance: average square of difference from mean
for i, item in enumerate(d):
    variancei = float(d[i]) - float(av) 
    variance = float(variancei**2) + variance
#stdev is sq route of variance

variance = variance / 3431

stdev = variance**0.5
#calculate standard error, stdev / sq route of N
sterror = stdev / (len(d)**0.5)
possig = []
sig = []
for i, item in enumerate(d):
    if (d[i] - av)/stdev > 1.96 or (d[i] - av)/stdev < -1.96:
        sig.append(ratio[i])
        possig.append(i)
position = []
for i in range(0,len(d)):
    position.append(i)
    

plt.figure
plt.scatter(position, ratio)
plt.scatter(possig, sig, color = "red")
plt.title("Distribution of Synonymous and NonSynonymous Mutations By Codon")
plt.xlabel("position")
plt.ylabel("Ratio of dN/dS")
plt.savefig("plot.png")
plt.close()


        

                
            
        