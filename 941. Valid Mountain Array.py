#唉我去，这题乍看上去要求挺简单，但实际做起来很难啊
#做了一个多小时，这个程序还跑超时了
'''
def validMountainArray(A):
    if len(A) < 3 or A == sorted(A):
        return False
    else:
        for i in range(len(A) - 1):
            if A[i] < A[i+1]:
                if A[i+1:][::-1] == sorted(A[i+1:]) and len(A[i+1:]) == len(set(A[i+1:])):
                    return True
            else:
                return False
result = validMountainArray([0,3,2,1])
print(result)
'''

#这个人用的应该是two pointer的思想，太帅了
def validMountainArray(A):
    i, j, n = 0, len(A) - 1, len(A)
    while i + 1 < n and A[i] < A[i + 1]: i += 1
    while j > 0 and A[j - 1] > A[j]: j -= 1
    return 0 < i == j < n - 1
result = validMountainArray([0, 1, 2, 0])
print(result)

