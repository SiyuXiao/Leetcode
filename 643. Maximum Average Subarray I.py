#这个算法时间复杂度不满足要求，这个算法时间复杂度相当于n*k
'''
def findMaxAverage(nums, k):
    a = []
    for i in range(len(nums) - k + 1):
        b = (sum(nums[i:i + k]))/k
        a.append(b)
    return max(a)
result = findMaxAverage([1,12,-5,-6,50,3], 4)
print(result)
'''
#这个算法的时间复杂度是n
def findMaxAverage(nums, k):
    sums=0
    sums=sum(nums[:k])
    res=sums
    for i in range(k,len(nums)):
        sums+=(nums[i]-nums[i-k])
        if res<sums:
            res=sums
    return res/k
result = findMaxAverage([1,12,-5,-6,50,3], 4)
print(result)    