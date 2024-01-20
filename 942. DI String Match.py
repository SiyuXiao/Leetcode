def diStringMatch(S):
    S1 = list(range(len(S)+1))
    S2 = []
    cnt1 = 0
    cnt2 = -1
    for a in S:
        if a == 'I':
            S2.append(S1[cnt1])
            cnt1 += 1
        else:
            S2.append(S1[cnt2])
            cnt2 -= 1
    S2.append(sum(S1) - sum(S2))
    return S2
result = diStringMatch("IDID")
print(result)