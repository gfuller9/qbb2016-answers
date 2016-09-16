#!/usr/bin/env python

"""
Turns a protein fasta file into a nucleotide file
usage: rev_trans <prot_fasta file> <nucleic acid fasta file>
"""

import sys
import itertools
from itertools import islice

def chunk_str(str, chunk_size):
    return [str[i:i+chunk_size] for i in range(0, len(str), chunk_size)]
# from Mike Lewis: http://stackoverflow.com/questions/5711452/how-do-i-slice-a-string-every-3-indices
aminos = ["A","C","D","E","F","G","I","H","K","L","M","N","P","Q","R","S","T","V","W","Y","*"]

protein = open(sys.argv[1])
nucleic = open(sys.argv[2])
sequence = []
proteins = {}
proteins_id = []
prot_seq = []
amino_acids = ["A","C","D","E","F","G","I","H","K","L","M","N","P","Q","R","S","T","V","W","Y","*"]
dnas = {}
dna_id = []

#make a dictionary, proteins, with ID and each residue from the alignment in  list as the value
for line in protein:
    line = line.rstrip("\r\n")
    
    #extracting the id for each protein
    if line.startswith(">"):
        minimal = line.strip(">")
        minimal = minimal[:-2]
        proteins_id.append(minimal)
        prot_seq_full = ''.join(prot_seq)
        prot_seq_full = chunk_str(prot_seq_full,1)
        proteins[proteins_id[-1]] = prot_seq_full
        prot_seq = []

    else:
        prot_seq_full = ''.join(prot_seq)
        prot_seq_full = chunk_str(prot_seq_full,1)
        prot_seq.append(line)
# makes a dictionary of the dna sequences with list of the codons as the value for the key        
for line in nucleic:
    codons = []
    
    line = line.rstrip("\r\n")
    
    if line.startswith(">"):
        minimal = line.split("|")
        
        dna_id.append(minimal[3])
        

    else:
        #removing the gaps in nucleotide sequences so we are only looking at the protein
        for char in line:
            if char == "-":
                line = line.replace(char, '')
        
        
        codons = chunk_str(line,3)        
        dnas[dna_id[-1]] = codons
#actually takes each codon and adds unless it's a gap, in which case it adds three -'s
for item in dnas:
    
    seq = []
    if item not in proteins:
        continue
    else:
        for i in range(0,len(proteins[item])):
            if proteins[item][i] in aminos:
                if i in range(0,len(dnas[item])):
                    seq.append(dnas[item][i])
                else:
                    seq.append("---")
            else:
                seq.append("---")
        seq = ''.join(seq)
        print item
        print seq
        

    