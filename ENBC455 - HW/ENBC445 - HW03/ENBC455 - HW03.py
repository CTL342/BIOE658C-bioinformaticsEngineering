# Name: Christopher A. Lee
# Date: 02/01/2025
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

# Problem 1
with open('hw3_1.txt') as file:
    months, litter_mul = file.readline().split()    
    adults = 1
    babies = 0
    newborns = 0

    for i in range(3, int(months) + 1):
        adults += babies
        babies = newborns
        newborns = adults * int(litter_mul)
        
    print(adults + babies + newborns, "\n")

from Bio.Seq import Seq
# Problem 2
with open('hw3_2.txt') as file:
    # Filter all sequences from the file into a list
    seqs = []
    temp = ""
    for line in file.readlines():
        if '>' not in line:
            temp += line.strip()
        else:
            if temp:
                seqs.append(temp)
            temp = ""
    if temp:
        seqs.append(temp)
    
    # Remove all of the introns within the original sequence
    raw_seq = seqs.pop(0)
    for seq in seqs:
        raw_seq = raw_seq.replace(seq, "")
    
    # Translate sequence into protein string
    dna_seq = Seq(raw_seq)
    protein_string = dna_seq.translate()
    print(protein_string, "\n")

# Problem 3
with open('hw3_3.txt') as file:
    # Filter all sequences from the file into a list
    seqs = []
    temp = ""
    for line in file.readlines():
        if '>' not in line:
            temp += line.strip()
        else:
            if temp:
                seqs.append(temp)
            temp = ""
    if temp:
        seqs.append(temp)

    # Identify subsequence indexes
    target = 0
    for i in range(len(seqs[0])):
        if target == len(seqs[1]):
            break
            
        if seqs[0][i] == seqs[1][target]:
            print(i + 1, end=" ")
            target += 1
    print("\n")

# Problem 4
with open('hw3_4.txt') as file:
    # Filter all sequences from the file into a list
    seqs = []
    temp = ""
    for line in file.readlines():
        if '>' not in line:
            temp += line.strip()
        else:
            if temp:
                seqs.append(temp)
            temp = ""
    if temp:
        seqs.append(temp)

    # Identify shortest sequence 
    seqs.sort(key=len)
    shortest_seq = seqs[0]
    other_seqs = seqs[1:]
    cond = False

    # Loops through possible lengths of substring backwards to have the
    # longest common subsequence guarenteed later on
    for length in range(len(shortest_seq), 0, -1):
        # Acts as a sliding window
        for i in range(len(shortest_seq) - length + 1):
            candidate = shortest_seq[i:i+length]

            # Checks if current candidate sequence exists in all other 
            # sequences
            cond = True
            for seq in other_seqs:
                if candidate not in seq:
                    cond = False
                    break
        # If condition is met and the longest common subsequence is found
        # in all of the sequences, than it is printed out
            if cond:
                print(candidate)
                break
        if cond:
            break