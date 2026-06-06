# Name: Christopher A. Lee
# Date: 02/18/2025
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

from Bio import SeqIO
import Levenshtein
# Problem 3
with open('hw4_3.txt', 'r') as f:
    seq1 = f.readline().strip()
    seq2 = f.readline().strip()
    
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count += 1
        
    print("Problem 3\nHamming Distance:", count, "\n")

# Problem 4
with open('hw4_4.txt', 'r') as f:
    seq = [str(fasta_seq.seq) for fasta_seq in SeqIO.parse(f, "fasta")]

    dist = Levenshtein.distance(seq[0], seq[1])
    print("Problem 4\nEdit Distance:", dist)