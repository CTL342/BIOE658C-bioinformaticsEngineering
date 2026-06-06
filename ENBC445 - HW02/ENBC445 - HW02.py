# Name: Christopher A. Lee
# Date: 12/30/2025
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

# Problem 3
from Bio import Entrez
from Bio import SeqIO

Entrez.email = "clee363@terpmail.umd.edu"
handle = Entrez.efetch(db="nucleotide", id=["JX317645", "JQ011276", "NM_001265803", "HM595636", "JQ712981", "JX460804", "NM_013179", "JX491654", "JF927163", "JQ762396"], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
shortest_seq = min(records, key=lambda x: len(x.seq))
print(shortest_seq.format("fasta"))

# Problem 4
with open('hw2_4.txt', 'r') as file:
    seq = file.readline().strip()
    subseq = file.readline().strip()

    for i, char in enumerate(seq):
        if seq[i: i + len(subseq)] == subseq:
            print(i + 1, "", end="")