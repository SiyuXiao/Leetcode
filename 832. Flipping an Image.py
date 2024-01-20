#我在想这个数据要是很大的话这个时间复杂度是不是也很大啊？ 因为图像的数据量本来就很大
def flipAndInvertImage(A):
    for i in range(len(A)):
        A[i] = A[i][::-1]
        for j in range(len(A[i])):
            A[i][j] = 1 - A[i][j]
    return A
result = flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]])
print(result)