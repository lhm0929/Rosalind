def DNAtoRNA(t):
    s = []
    for n in t:
        if n == 'T':
            s.append('U')
        else:
            s.append(n)
    for i in s:
        print(i, end='')