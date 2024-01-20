def transpose(A):
    B = []
    C = []
    for j in range(len(A[0])):
        for i in range(len(A)):
            B.append(A[i][j])
        C.append(B)
        B = []
    return C
result = transpose([[1,2,3],[4,5,6],[7,8,9]])
print(result)

