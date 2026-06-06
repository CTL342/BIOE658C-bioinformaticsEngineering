# Name: Christopher A. Lee
# Date: 12/30/2025
# Prof: Dr. Callura
# Course: Bioinformatics - ENBC 455

# Problem 1
with open('hw1_1.txt', 'r') as file:
    string = file.read()
    A = 0
    C = 0
    G = 0
    T = 0
    for char in string:
        if char == 'A':
            A += 1
        elif char == 'C':
            C += 1
        elif char == 'G':
            G += 1
        elif char == 'T':
            T += 1
    print(A, C, G, T)
    print()

# Problem 2
with open('hw1_2.txt', 'r') as file:
    string = file.read()
    for char in string:
        if char == 'T':
            char = 'U'
        print(char, end='')
    print()

# Problem 3
with open('hw1_3.txt', 'r') as file:
    string = file.read()
    reversed_string = string[::-1]
    for char in reversed_string:
        if char == 'A':
            print('T', end="")
        elif char == 'C':
            print('G', end="")
        elif char == 'G':
            print('C', end="")
        elif char == 'T':
            print('A', end="")
    print("\n")

# Problem 4
from Bio.Seq import Seq
with open('hw1_4.txt', 'r') as file:
    seq = Seq(file.read().replace('\n', '').strip())
    print(seq.translate())