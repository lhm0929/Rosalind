# Hamming distance
def Dh(s, t):
    n = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            n += 1
    print(n)