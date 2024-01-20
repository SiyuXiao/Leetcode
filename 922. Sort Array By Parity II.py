#我最开始写的这个算法，只击败了0.97%的对手
def sortArrayByParityII(A):
    new = []
    new1 = []
    new2 = []
    for a in A:
        if a%2 == 0:
            new.append(a)
        else:
            new1.append(a)
    for i, j in zip(new, new1):
        b = (i, j)
        new2 = new2 + list(b)
    return new2
result = sortArrayByParityII([4,2,5,7])
print(result)