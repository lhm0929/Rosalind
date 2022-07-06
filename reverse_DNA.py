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
