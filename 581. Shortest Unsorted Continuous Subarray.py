#我最开始用这种方法做的，但是没法处理比如[1, 3, 2, 2]这种情况，因为我正在方法局限在3后面只有一个比3小的数
'''
def findUnsortedSubarray(nums):
    test = nums[:]
    test.sort()
    if test == nums:
        return 0
    else:
        a = []
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                a.append(i)
        return a[-1] - a[0] + 2
result = findUnsortedSubarray([2, 1])
print(result)
'''
#这种方法就克服了上面那个算法的弊端
def findUnsortedSubarray(nums):
    test = nums[:]
    test.sort()
    if test == nums:
        return 0
    else:
        new = []
        new1 = list(zip(nums, test))
        for i in range(0, len(new1)):
            if new1[i][0] != new1[i][1]:
                new.append(i)
        return new[-1] - new[0] + 1
result = findUnsortedSubarray([2,6,4,8,10,9,15])
print(result)
