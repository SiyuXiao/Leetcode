//这个是我最开始写的
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

//以后用这种写法最快在不用包的情况下：
def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    return [list(row) for row in zip(*matrix)]
