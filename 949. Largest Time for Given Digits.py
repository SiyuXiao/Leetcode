#哎，服了，写了这么一堆，当我看到这个测试样例的时候：[2,0,6,6]我发现我的逻辑从头开始就错了，这里面我C1是[20]，导致后面直接输出空了
def largestTimeFromDigits(A):
    B = []
    C = []
    D = []
    for a in A:
        B.append(a*10)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if a + b < 24 and i != j:
                C.append(a+b)
    if C == []:
        return ''
    else:
        C1 = max(C)
        A0 = C1 // 10 
        A1 = C1 % 10
        A.remove(A0)
        A.remove(A1)
        if (A[0]*10 + A[1]) <60:
            D.append(A[0]*10 + A[1])
        if (A[1]*10 + A[0]) <60:
            D.append(A[1]*10 + A[0])
        if D == []:
            return ''
        else:
            D1 = max(D)
            if len(str(C1)) == 1:
                C1 = '0' + str(C1)
            if len(str(D1)) == 1:
                D1 = '0' + str(D1)
            return str(C1) + ':' + str(D1)
result = largestTimeFromDigits([1,2,3,4])
print(result)