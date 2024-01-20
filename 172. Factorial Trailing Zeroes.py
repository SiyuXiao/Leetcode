#我这个算法的超时了
def trailingZeroes(n):
    nfactorial = 1
    cnt = 0
    for a in range(1, n+1):
        nfactorial *= a
    nfactorialstr = str(nfactorial)
    for b in nfactorialstr[::-1]:
        if b == '0':
            cnt += 1
        else:
            return cnt
result = trailingZeroes(5)
print(result)


