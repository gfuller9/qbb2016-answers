#!/usr/bin/env python

"""
finds matching kmers between a single query sequence and a database of targets and extends by 1
usage: ./kmer_match_extender.py <target.fa> <source.fa> k-mer
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
    global sourcy
    sourcy = sequence.upper()
    
    for i in range(0, len(sequence)-k):
        kmer = sequence[i : i + k]
        if kmer not in kmer_source:
            kmer_source[kmer] = []

        kmer_source[kmer].append(i)

#open each target sequence and pass to FASTAReader

kmer_position = {}
key = []
length = []
for ident, sequence in fasta.FASTAReader(target):
    sequence = sequence.upper()
    
    #lets you have empty kmer_counts at start of each sequence
    kmer_position = {}
    #make empty list of exact matches for each target
    matches = []
    #iterate through the target and define the kmers
    for i in range(0, len(sequence)-k):
        kmer = sequence[i : i + k]
        #check if kmer in query dictionary
        if kmer in kmer_source:
            kmer2 = kmer
            print kmer2
            
            #checks each position the kmer is in the query
            for item in kmer_source[kmer2]:  
                #these are count variables for making sure I don't iterate through into nonexistant string indices   
                a = k
                #print item

                b=0
                #checks if the i+k+n position is in both the query and the target sequence and appends the matching base to each.  Want to be sure the position is in the sequence
                #There's still a bug at lower kmer values...
                while len(sequence)>i+a+1:
                    a +=1
                    
                    if sequence[(i+a)] == sourcy[(item+a)]:  
                       
                        kmer2 = kmer2 + sequence[i+a]
                        
                    else:
                        break
                #checks if the previous position (i-n) is a real index
                while i-b > 0:
                    b+=1
                    if sequence[i-b] == sourcy[item-b]:
                        kmer2 = sequence[i-b]+kmer2
                    else: 
                        break
                #appends the new kmer
                matches.append(kmer2)
                length.append(len(kmer2))
                
    #sorts the lengths
    #prints identity, then the sorted kmers
     
    matches.sort(key = len, reverse = True)
    print "___"+ident+"___"

           
    for value in range(0,len(matches)-1):
        print matches[value]

#could check how long the matches are and the longest: for fun, I could see how long average exact matches are...

#length.sort( reverse = True)

#print length[0]
    
                  