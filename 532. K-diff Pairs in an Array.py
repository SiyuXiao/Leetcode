#这是我最开始写的代码，超时了，时间复杂度为n2
'''
def findPairs(nums, k):
    nums.sort()
    nums1 = set()
    for i in range(len(nums) - 1):
        if nums[i] + k in nums[i+1:] and (nums[i], nums[i] + k) not in nums1:
            nums1.add((nums[i], nums[i] + k))
    return len(nums1)
result = findPairs([3, 1, 4, 1, 5], 2)
print(result)
'''

#这种分类讨论的方法击败了其余百分之一百的选手
'''
def findPairs(nums, k):
    if k < 0:
        return 0
    if k == 0:
        sorted_nums = sorted(nums)
        a = set()
        for i in range(len(nums) - 1):
            if sorted_nums[i] == sorted_nums[i+1] and (sorted_nums[i], sorted_nums[i+1]) not in a:
                a.add((sorted_nums[i], sorted_nums[i+1]))
        return len(a)
    nums_set = set(nums) 
    cnt = 0
    for element in nums_set:
        if (element+k) in nums_set:
            cnt += 1
    return cnt
result = findPairs([3, 1, 4, 1, 5], 2)
print(result)
'''
#我正常不喜欢用这种调包解决问题的方法，但是我见过这个包太多次了，就当认识一下吧，其实也挺好理解的

import collections
def findPairs(nums, k):
    res = 0
    c = collections.Counter(nums)
    for i in c:
        if k > 0 and i + k in c or k == 0 and c[i] > 1:
            res += 1
    return res
result = findPairs([3, 1, 4, 1, 5], 2)
print(result)
