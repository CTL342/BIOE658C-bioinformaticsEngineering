# Name: Christopher A. Lee
# Date: 04/22/2026
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

# Libraries
from Bio import SeqIO
from collections import defaultdict

# Problem 1
with open("hw10_1.txt", "r") as f:
    reads = [line.strip() for line in f.readlines() if line.strip()]
    adj = {}
    for read in reads:
        prefix = read[:-1]
        suffix = read[1:]
        adj[prefix] = suffix
        
    current_node = reads[0][:-1]
    superstring = []
    
    for i in range(len(reads)):
        superstring.append(current_node[0])
        current_node = adj[current_node]
        
    print("".join(superstring))