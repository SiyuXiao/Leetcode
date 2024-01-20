#最开始的思路，这个算法超时了
'''
def findShortestSubArray(nums):
    D = {}
    A = []
    B = []
    for a in nums:
        if a not in D:
            D[a] = 1
        else:
            D[a] += 1
    degree = max(D.values())
    for b in D.keys():
        if D[b] == degree:
            for i in range(len(nums)):
                if nums[i] == b:
                    A.append(i)
            B.append(max(A) - min(A))
            A = []      
    return min(B) + 1
result = findShortestSubArray([1, 2, 2, 3, 1])
print(result)
'''
#这是我受一个答案的启发写的，不过那个答案又是调包，又是调函数的
#篇幅还比我长不少，我啥包都没调
def findShortestSubArray(nums):
    D = {}
    A = []
    for a in nums:
        if a not in D:
            D[a] = 1
        else:
            D[a] += 1
    degree = max(D.values())
    for b in D.keys():
        if D[b] == degree:
            A.append(len(nums) - nums.index(b) - nums[::-1].index(b))#这一步替换了之前的循环，时间复杂度一下子下来了    
    return min(A)
result = findShortestSubArray([1, 2, 2, 3, 1])
print(result)