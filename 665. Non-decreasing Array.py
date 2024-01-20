#这是我最开始写的算法，这种算法不适用于这个样例：[3,4,2,3]，这个样例应该输出false
'''
def checkPossibility(nums):
    count = 0
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i+1]:
            count += 1
    return count < 2
result = checkPossibility([4,2,3])
print(result)
'''
#符合题目要求的答案，这个思想非常好
#遇到降序的pair，要么改pair里的第一个变成第二个看是否变成非降序，要么改pair里的第二个变成第一个看是否变成非降序
def checkPossibility(nums):
    one, two = nums[:], nums[:]
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            one[i] = nums[i + 1]
            two[i + 1] = nums[i]
            break
    return one == sorted(one) or two == sorted(two)
result = checkPossibility([3,4,2,3])
print(result)

