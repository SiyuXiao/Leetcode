#这个题出的挺好，我刚开始没考虑负负得正的情况，比如下面的测试样例
def maximumProduct(nums):
    nums.sort()
    a = nums[-1]*nums[-2]*nums[-3]
    b = nums[-1]*nums[0]*nums[1]
    return max(a, b)
result = maximumProduct([-4,-3,-2,-1,60])
print(result)