#这是我最开始的想法，但是超时了
'''
def fairCandySwap(A, B):
    sumA = sum(A)
    sumB = sum(B)
    for a in A:
        for b in B:
            if a + sumB - b == b + sumA - a:
                return [a, b]
print(fairCandySwap([1,1], [2,2]))
'''
#答案给的做法，我觉得这个想法很巧妙
#Calculate dif = (sum(A) - sum(B)) / 2
#We want find a pair (a, b) with a = b + dif
def fairCandySwap(A, B):
    dif = (sum(A) - sum(B)) // 2
    A = set(A)
    for b in set(B):
        if dif + b in A:
            return [dif + b, b]
print(fairCandySwap([1,2,5], [2,4]))
