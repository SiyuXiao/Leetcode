#这题跟我耍赖，题目里明明说的是输入二维数组，结果测试样例里面几维的都有
def matrixReshape(nums, r, c):
    number = []
    for b in nums:
        number += b
    newnums = []
    if len(number) != r*c:
        return nums
    else:
        for a in range(0, r):
            newnums.append(number[a*c:a*c + c])
    return newnums
result = matrixReshape([[1,2], [3,4]], 1, 4)
print(result)