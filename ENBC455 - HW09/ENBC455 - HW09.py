# Name: Christopher A. Lee
# Date: 04/12/2026
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

# Libraries
from Bio import SeqIO, Seq
import itertools
from collections import defaultdict

# Problem 1
with open('hw9_1.txt', 'r') as f:
    alph_str = f.readline().strip().split()
    n = int(f.readline().strip())

    print(alph_str)
    print(n)
    combos = itertools.product(alph_str, repeat=n)
    for combo in combos:
        print("".join(combo))
    print()

# Problem 2
with open('hw9_2.txt', 'r') as f:
    strands = [str(seq.seq) for seq in SeqIO.parse(f, "fasta")]
    kmers = defaultdict(int)
    for i in range(len(strands[0]) - 3):
        kmers[strands[0][i: i + 4]] += 1
    print(kmers, "\n")

# Problem 3
with open('hw9_3.txt', 'r') as f:
    kmers = set()
    for line in f:
        kmers.add(line.strip())
        kmers.add(str(Seq.Seq(line.strip()).reverse_complement()))
    
    edges = set()
    for k in kmers:
        edges.add((k[:-1], k[1:]))
    for edge in sorted(edges):
        print(f"({edge[0]}, {edge[1]})", end=" | ")
