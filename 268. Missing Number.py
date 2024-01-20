#我觉得这个题的测试样例有毛病，我这个程序输入[0]的时候跑不了，但是输入0应该出来啥我也不知道
'''
def missingNumber(nums):
    nums.sort()
    for i in range(0, len(nums)):
        if nums[i+1] - nums[i] != 1:
            return nums[i] + 1
result = missingNumber([3,0,1])
print(result)
'''
#原来题的意思是这个数组一定是从0开始的，所以下面这个程序才正确
'''
def missingNumber(nums):
    return sum(range(len(nums)+1)) - sum(nums)
result = missingNumber([0])
print(result)
'''