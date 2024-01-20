#这个代码直接放leetcode里跑不通，leetcode里调用的是初始的nums,所以我新赋值的nums没有调用
'''
def rotate(nums, k):
    n = len(nums) - k  
    nums = nums[n:] + nums[:n]
    return nums
result = rotate([1,2,3,4,5,6,7], 3)
print(result)
'''
#如果改成下面这个，就只改变了原来的nums，而没有新建nums
def rotate(nums, k):
    n = len(nums) - k  
    nums[:] = nums[n:] + nums[:n]
    return nums
result = rotate([1,2,3,4,5,6,7], 3)
print(result)