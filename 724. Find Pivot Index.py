#这题我用的第697题的解题思想
'''
def pivotIndex(nums):
    nums = nums + [0]
    sum1 = 0
    sum2 = sum(nums[1:])
    for i in range(0, len(nums)-1):
        if sum1 == sum2:
            return i
        else:
            sum1 += nums[i]
            sum2 -= nums[i+1]
    return -1
result = pivotIndex([1, 7, 3, 6, 5, 6])
print(result)
'''
