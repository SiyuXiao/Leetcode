def repeatedStringMatch(A, B):
    if not set(B).issubset(set(A)): return -1
    elif B in A: return 1   
    max_times = len(B)//len(A) + 2
    for i in range(len(B)//len(A),max_times+1):
        if B in A*i:
            return i   
    return -1
result = repeatedStringMatch()