#这个算法真是太帅了，我原来没有想到这个
def isToeplitzMatrix(matrix):
    m = matrix
    for i in range(len(m) - 1):
        for j in range(len(m[0]) - 1):
            if m[i][j] != m[i + 1][j + 1]:
                return False
    return True
result = isToeplitzMatrix([
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
])
print(result)