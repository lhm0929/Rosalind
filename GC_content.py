
from operator import index


path = r"C:\Users\88698\Downloads\rosalind_gc_2_dataset.txt"

f = open(path, "r")
lines = f.readlines()

id = []
seq = []
gc_cont = []
subseq = ""
for i in range(len(lines)):
    if lines[i].startswith('>'):
        if len(subseq) != 0:
            seq.append(subseq)
            subseq = ""
        id.append(lines[i].replace('\n', ''))
    else:
        subseq += lines[i].replace('\n', '')
seq.append(subseq)

for s in seq:
    gc_num = 0
    for c in s:
        if c == 'C' or c == 'G':
            gc_num += 1
    gc_cont.append(gc_num / len(s))
max_gc_index = gc_cont.index(max(gc_cont))
print(id[max_gc_index])
print(max(gc_cont))