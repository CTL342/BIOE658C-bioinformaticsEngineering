# Name: Christopher A. Lee
# Date: 04/28/2026
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

# Libraries
from Bio import SeqIO

# Problem 1
with open('hw11_1.txt', 'r') as f:
    contigs = [str(i.strip()) for i in f.readlines()]
    contigs_lengths = [len(contig) for contig in contigs]
    contigs_sorted = sorted(contigs_lengths, reverse=True)

    N = 0
    N50 = 0
    N75 = 0
    total = sum(contigs_sorted)

    for i in contigs_sorted:
        N += i
        if N50 == 0 and N >= (total * 0.5):
            N50 = i
        if N75 == 0 and N >= (total * 0.75):
            N75 = i
            break

    print(N50, N75)
