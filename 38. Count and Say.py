def countAndSay(n):
    a = '1'
    A = []
    B = [0]
    C = []
    l = 1
    if n == 1:
        return '1'
    else:
        while l <= n-1:
            a = a + '0'
            for i in range(len(a) - 1):
                if a[i] != a[i+1]:
                    A.append(a[i])
                    B.append(i+1)
            for j in range(len(B) - 1):
                C.append(B[j+1] - B[j])
            a = ''
            for k in range(len(A)):
                a = a + str(C[k])
                a = a + A[k]
            l += 1
            A = []
            B = [0]
            C = []
        return a
result = countAndSay(3)
print(result)