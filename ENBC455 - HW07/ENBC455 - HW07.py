# Name: Christopher A. Lee
# Date: 03/17/2026
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

# Libraries
from Bio import SeqIO

# Problem 2
for seq in SeqIO.parse("hw7_2.fasta", "fasta"):
    print(seq.id)
    print(seq.seq)

# Problem 3
with open("hw7_3.txt", "r") as f:
    threshold = int(f.readline().strip())
    count = 0

    for seq in SeqIO.parse(f, "fastq"):
        quality_scores = seq.letter_annotations['phred_quality']
        avg_quality = sum(quality_scores) / len(quality_scores)
        if avg_quality < threshold:
            count += 1
        
    print()
    print(count, "\n")

# Problem 4
with open("hw7_4.txt", "r") as f:
    first_line = f.readline().split()
    q_threshold = int(first_line[0])
    p_percentage = int(first_line[1])
    count = 0

    for seq in SeqIO.parse(f, "fastq"):
        quality_scores = seq.letter_annotations["phred_quality"]
        bases_above_q = sum(1 for score in quality_scores if score >= q_threshold)
        current_p = (bases_above_q / len(quality_scores)) * 100

        if current_p >= p_percentage:
            count += 1

    print(count) 
        