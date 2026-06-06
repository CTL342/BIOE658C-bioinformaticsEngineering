# Name: Christopher A. Lee
# Date: 03/30/2026
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

# Libraries
from Bio import SeqIO

# Problem 3
with open('hw8_3.txt', 'r') as f:
    num = int(f.readline())
    A = [int(x.strip()) for x in f.readline().strip("{}\n").split(",")]
    B = [int(x.strip()) for x in f.readline().strip("{}\n").split(",")]

    print("A U B")
    set_union = A.copy()
    for i in B:
        if i not in A:
            set_union.append(i)
    print(set_union)

    print("\nA ∩ B")
    set_inter = []
    for i in B:
        if i in A:
            set_inter.append(i)
    print(set_inter)

    print("\nA - B")
    set_AB = A.copy()
    for i in B:
        if i in A:
            set_AB.remove(i)
    print(set_AB)

    print("\nB - A")
    set_BA = B.copy()
    for i in A:
        if i in B:
            set_BA.remove(i)
    print(set_BA)

    print("\nA^C")
    set_AC = []
    for i in range(1, num + 1):
        if i not in A:
            set_AC.append(i)
    print(set_AC)
    
    print("\nB^C")
    set_BC = []
    for i in range(1, num + 1):
        if i not in B:
            set_BC.append(i)
    print(set_BC)
    print()

# Problem 4
def merge_strings(s1, s2):
    max_overlap = min(len(s1), len(s2))

    for i in range(max_overlap, 100, -1):
        if s1[-i:] == s2[:i]:
            return s1 + s2[i:]
            
    for i in range(max_overlap, 100, -1):
        if s2[-i:] == s1[:i]:
            return s2 + s1[i:]
            
    return ""

with open('hw8_4.txt', 'r') as f:
    reads = [str(seq.seq) for seq in SeqIO.parse(f, "fasta")]

while len(reads) > 1:
    merged_this_round = False
    
    for i in range(len(reads)):
        for j in range(i + 1, len(reads)):
            combined = merge_strings(reads[i], reads[j])
            
            if combined:
                s1, s2 = reads[i], reads[j]
                reads.remove(s1)
                reads.remove(s2)
                reads.append(combined)
                merged_this_round = True
                break
                
        if merged_this_round:
            break
            
    if not merged_this_round:
        break

super_string = reads[0]
print(super_string)