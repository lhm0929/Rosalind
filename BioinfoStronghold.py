def CountDNA(s):
    o = []
    o.append(s.count('A'))
    o.append(s.count('C'))
    o.append(s.count('G'))
    o.append(s.count('T'))
    for i in o:
        print(i, end=" ")


def DNAtoRNA(t):
    s = []
    for n in t:
        if n == 'T':
            s.append('U')
        else:
            s.append(n)
    for i in s:
        print(i, end='')


def reverse_DNA(s):
    r = []
    for n in s[::-1]:
        if n == 'A':
            r.append('T')
        elif n == 'T':
            r.append('A')
        elif n == 'C':
            r.append('G')
        else:
            r.append('C')
    for i in r:
        print(i, end='')


# def RabitRecurrence(n, k):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return (RabitRecurrence(n - 2, k) * k) + RabitRecurrence(n - 1, k)

# # GC content
# def GCcont(seq):
#     GC = seq.count('G') + seq.count('C')
#     return GC / len(seq)

# f = open("C:\\Users\88698\Downloads\\rosalind_gc.txt", "r")
# # read fasta file
# info = []
# seq = []
# seq_GC = []
# temp_seq = ""
# i = 0
# for line in f.readlines():
#     if line.startswith('>'):
#         if i != 0:
#             info.append(line)
#             seq.append(temp_seq)
#             temp_seq = ""
#         else:
#             info.append(line)
#         i += 1
#     else:
#         temp_seq = temp_seq + line.replace('\n', '')
# seq.append(temp_seq) # last sequence

# for s in seq:
#     seq_GC.append(GCcont(s))

# print(info[seq_GC.index(max(seq_GC))].replace('>', ''), end = '')
# print(max(seq_GC) * 100)
# f.close()

# Hamming distance
def Dh(s, t):
    n = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            n += 1
    print(n)

s = "TGCTGAGTCTTTCACCATAGCTTCCTGTGCTTTTTGTTGCCCAAAACTGGACCCAGCGAGCGAGCTCGTTCCCATGTGCGTAGATGCTCTCTGTAAACGTTGTGTATATGAGTAGCAAGTTTCTATTGTCATGACTACTACCGGCATAATCACCTCATCGGAATGGGGCTGTCGTCCACAGAGGGTTAGGCTCAATAGCAGGTTCGAAGGAAACGGCTACTGCACCGCTGAATGGTAAGTTGTGAGACTGGTCATATGGTACTTAGGCGTAAGTTTATTCTATATAAATTGCTGAGGGCGGGCTTATCCACCTCCAGCCGAGTTCATGCTGCAGTATGTTGGTCCCTTGGGGCCAAGACCAGGAAGCCTGACGCGCAACGCCCGGCAGCCCACGCCACTGTGATCCTGGCCTGCCTTACTCGGGTATGTAGGTTGGTGGCGCGCGTGTGTTTCATCTCTCACGATACCCGATGGTGCGCCGCGGTAAGAAGCCTAGGCAACCGGGGAATGTCGCAAGTGCCTCCTAATTTTATGTGGCTTGCTTAAGCATCTATCCGTTTGGAACTGCAAAATAGCGAGGTATAGGGCTCGTGAGTTTAATCGCCCAATCTTCAAAGGGTATCTGAGTAATCGTAGGTTGCTTACTGGGGCTAGGGGCCATGTTGGTCGGGAGGGATAGTTATGACCGAAATCTATTATAGACCATATTTATGCATGTTCCTCCGATCTTGGGCTACAAATTTAATCTCCGAGAGCCGACCTGCGCTCACCAGCTGTTTGTGGCATTACCATCTTTCGTCAAGGACTCCGGCAGATTTCCGAATCTCAAGCTGGCAGATTAGAAGAGTTATCTTCGGGGTGATGGGGGGATCATAAGTCCGGGGGAGGAGATCTCACCACGTAATATGGGACTCTGCTCAATAGCGTAACGCTACCAACAGACAGGCAGACTCCTA"
t = "CGGTGCGTCTTACAATATCGCTTTCTGGTAGCTCTAGTGCGTAAATTTATATTGCTCCGCGACATTCGCCACCCAGTGCATAGAAGGTTTTACTCAGCTCTGGGGACACGTGAAGGTTATTTGAATATGCACGATTACGAAGACTACTACAGACGCAGCAGAAGCAGGTGGACGTGCGCGTAGGGTAAAACCCTATAGTTAGAGCGAAAGGGCCAGGTAATGGTACTACCGGTGATTAGTATGGAGACATGTCGTAAATGTCATAGGATCACGTCTTAACTTTACGATTTGGCCCGAGGATGTGTAAGTGACCCCAGCTTAATACAAGTTACAGCACGTTGGTCCCTTGGCGCATCTACCAGAAAAGCAGACCCTGGGCACACTGAGGCTCGGGCTACTGGGAAAATGGCAGGTGTCAAGCGTTACGTTAGAGTGAGGGAAGGGTGGTATCTCATCTGTCAGGCCCACTGAGAGTCCAGGGCGGTCAGCACGGTATGGAATTGGGGTGCATGTCAAGGGGCATCCTAGGTATTGTATCTTGTGAGGTCTCCTACCCTTGTCGCAATGCAAGGTAGCGATAGCGCAGAGTCGGCAGTATGAACGCGCTGCCTGTGCAGGGGGGGTGCTCTCCTTTATATTAATCTCTATCATCGAGAGCGAGATTGATCCCTTGGGTACCTTCTCCCGGAGTTCTTTACCAGACCATATGTGTCTAACTCACACGTACTAAGGGAGAGTAAATTCACATCACATTGTGGAGGTGCGATCACACTTCGCTTGTGTTAATTCCATCCTGCTTCACCACACATGGATCACTAATGCAACTAAAAAACCCACTTTTAAACAAATCGCATGCGCGAGATGCGCGCCTAACTTGACAGGTACCCGGCACCCCGGTCCCTCAGAGGGTTGTACCTTCAACTTCTTCTGAAGAACAACATACAAGTCCTGCTTAG"

Dh(s, t)