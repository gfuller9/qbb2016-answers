#!/usr/bin/env python

"""
finds matching kmers between a single query sequence and a database of targets
usage: ./day3-homework-1.py <target.fa> <source.fa> k-mer

How to keep track of position of target (subset.fa)???
keys should be kmers from source
values should be positions
do second pass, take kmer as query and see if match in target dictionary
should have kept track of query because enumerating along

Second part is extend only if match exactly
extend each end, one after the other using a while loop
"""
#this is making a count of kmers in the target
import sys, fasta

target = open(sys.argv[1])
source = open(sys.argv[2])
lengths = []


k = int(sys.argv[3])
#make a query dictionary
kmer_source = {}
for ident, sequence in fasta.FASTAReader(source):
    sequence = sequence.upper()
    for i in range(0, len(sequence)-k):
        kmer = sequence[i : i + k]
        if kmer not in kmer_source:
            kmer_source[kmer] = []

        kmer_source[kmer].append(i)

#make target dictionaries

kmer_position = {}
for ident, sequence in fasta.FASTAReader(target):
    sequence = sequence.upper()
    
    #lets you have empty kmer_counts at start of each sequence
    kmer_position = {}
    #makes each dictionary
    
    for i in range(0, len(sequence)-k):
        kmer = sequence[i : i + k]
        if kmer not in kmer_position:
            kmer_position[kmer] = []
 
        kmer_position[kmer].append(i)
    #checks dictionaries against each other and prints out the corresponding values

    for kmer in kmer_position:

        if kmer in kmer_source:
            print "---target sequence name: " + ident + "---\t" + "target starts:\t" + str(kmer_position[kmer]) + "\tquery starts:\t" + str(kmer_source[kmer]) + "\tkmer:\t" + kmer


