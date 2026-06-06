# Name: Christopher A. Lee
# Date: 03/10/2026
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

# Libraries
from Bio import SeqIO

# Problem 2
with open('hw6_2.txt', 'r') as f:
    seq2 = list(SeqIO.parse(f, "fasta"))

    for i in range(len(seq2)):
        for j in range(len(seq2)):
            if i == j:
                continue
                
            if seq2[i].seq[-3:] == seq2[j].seq[:3]:
                print(seq2[i].id, seq2[j].id)
    print()

# Problem 3
with open('hw6_3.txt', 'r') as f:
    nodes = int(f.readline())
    edges = 0
    for i in f.readlines():
        edges += 1
    
    print(nodes - 1 - edges, nodes - 2, "\n")

# Problem 4
with open('hw6_4.txt', 'r') as f:
    seq4 = [str(fasta_seq.seq) for fasta_seq in SeqIO.parse(f, "fasta")]

    matrix = []
    for i in range(len(seq4)):
        row = []
        for j in range(len(seq4)):
            mismatches = 0

            for k in range(len(seq4[0])):
                if seq4[i][k] != seq4[j][k]:
                    mismatches += 1

            row.append(mismatches / len(seq4[0]))

        matrix.append(row)

    for row in matrix:
        for value in row:
            print(f"{value:.5f} ", end="")
        print()