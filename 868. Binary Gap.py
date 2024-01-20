def binaryGap(N):
    pre = dist = 0
    for i, c in enumerate(bin(N)[2:]):
        if c == "1":
            dist = max(dist, i - pre)
            pre = i
    return dist
result = binaryGap(22)
print(result)
