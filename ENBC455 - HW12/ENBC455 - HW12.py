# Name: Christopher A. Lee
# Date: 04/28/2026
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

# Libraries
from Bio import SeqIO
from Bio.Seq import Seq

# Problem 1
with open("hw12_1.txt", "r") as f:
    reads = [line.strip() for line in f.readlines() if line.strip()]

    genome = reads[0]
    unused_reads = reads[1:]

    while unused_reads:
        best_overlap = -1
        best_idx = -1
        best_append = ""

        for i, r in enumerate(unused_reads):
            ov_forward = 0
            for j in range(min(len(genome), len(r)), 0, -1):
                if genome[-j:] == r[:j]:
                    ov_forward = j
                    break
            
            if ov_forward > best_overlap:
                best_overlap = ov_forward
                best_idx = i
                best_append = r[ov_forward:]

            r_rc = str(Seq(r).reverse_complement())
            ov_reverse = 0
            for j in range(min(len(genome), len(r_rc)), 0, -1):
                if genome[-j:] == r_rc[:j]:
                    ov_reverse = j
                    break
                    
            if ov_reverse > best_overlap:
                best_overlap = ov_reverse
                best_idx = i
                best_append = r_rc[ov_reverse:]

        genome += best_append
        unused_reads.pop(best_idx)

    read_length = len(reads[0])
    wrap_overlap = 0
    end_chunk = genome[-read_length:]
    start_chunk = genome[:read_length]
    
    for j in range(min(len(end_chunk), len(start_chunk)), 0, -1):
        if end_chunk[-j:] == start_chunk[:j]:
            wrap_overlap = j
            break
    
    if wrap_overlap > 0:
        genome = genome[:-wrap_overlap]

    print("Assembled Cyclic Superstring:")
    print(genome)