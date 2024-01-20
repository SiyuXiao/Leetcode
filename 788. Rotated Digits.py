#这个题题意本身就没说明白，我这个写法的理解是如果一个数只有2569中的数那么这个数就满足要求
def rotatedDigits(N):
    numbers = 0
    for i in range(1, N+1):
        a = str(i) 
        b = set(a)
        if b.issubset('2569'):
            numbers += 1
    return numbers
result = rotatedDigits(22)
print(result)