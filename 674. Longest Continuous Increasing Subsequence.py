def findLengthOfLCIS(nums):
    new = []
    new1 = []
    nums1 = nums + [0] #这题要是有负数的话就完了
    for i in range(0, len(nums1)-1):
        if nums1[i] < nums1[i+1]:
            new.append(nums1[i])
        else:
            new1.append(len(new)+1)
            new = []
    return max(new1) if new1 else len(nums)
result = findLengthOfLCIS([1,3,5,4,2,3,4,5])
print(result)