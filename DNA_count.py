def CountDNA(s):
    o = []
    o.append(s.count('A'))
    o.append(s.count('C'))
    o.append(s.count('G'))
    o.append(s.count('T'))
    for i in o:
        print(i, end=" ")