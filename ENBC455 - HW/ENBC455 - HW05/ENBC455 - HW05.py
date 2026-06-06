# Name: Christopher A. Lee
# Date: 02/28/2025
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

from Bio import SeqIO
from Bio import Align
from Bio import SeqUtils
import subprocess
# Problem 1
with open('hw5_1.txt', 'r') as f:
    seq1 = [str(fasta_seq.seq) for fasta_seq in SeqIO.parse(f, "fasta")]

    aligner1 = Align.PairwiseAligner()
    aligner1.substitution_matrix = Align.substitution_matrices.load("BLOSUM62")
    aligner1.open_gap_score = -5
    aligner1.extend_gap_score = -5
    
    max_score = aligner1.score(seq1[0], seq1[1])

    print(f"Problem 1\nMaximum Alignment Score: {max_score}\n")

# Problem 2
with open('hw5_2.txt', 'r') as f:
    seq2 = [str(fasta_seq.seq) for fasta_seq in SeqIO.parse(f, "fasta")]

    aligner2 = Align.PairwiseAligner()
    aligner2.substitution_matrix = Align.substitution_matrices.load("PAM250")
    aligner2.mode = 'local'
    aligner2.open_gap_score = -5
    aligner2.extend_gap_score = -5

    alignments = aligner2.align(seq2[0], seq2[1])
    print(f"Problem 2\n{alignments[0].score}\n{alignments[0][0].replace('-', '')}\n{alignments[0][1].replace('-', '')}\n")

# Problem 3
subprocess.run()

# Problem 4
with open('hw5_4.txt', 'r') as f:
    seq3 = [fasta_seq for fasta_seq in SeqIO.parse(f, "fasta")]
    seqs = [str(fasta_seq.seq) for fasta_seq in seq3]

    most_gc_content = 0
    most_gc_content_index = 0
    for i, seq in enumerate(seqs):
        temp = SeqUtils.gc_fraction(seq)
        if temp > most_gc_content:
            most_gc_content = temp
            most_gc_content_index = i

    print("Problem 4")
    print(seq3[most_gc_content_index].id)
    print(f"{most_gc_content * 100:.6f}%")