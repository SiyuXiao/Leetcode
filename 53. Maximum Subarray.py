#方法一：把所有的连续组合都列出来，然后比较所有的组合里面哪个组合的和最大
'''
L = [1,2,3]
print([L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1)])
'''
#上面这个程序和下面这个程序是一个意思
'''
L = [1,2,3]
for i in range(0,len(L)):
	for j in range(1,len(L)-i+1):
		print(L[i:i+j])
'''

'''
def maxSubArray(nums):
	b = []
	for i in range(0, len(nums)):
		for j in range(1, len(nums)-i+1):
			a = sum(nums[i:i+j])
			b.append(a)
	return(max(b))
result = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(result)
'''
#这个方法虽然也可以完成功能，但是leetcode上跑完显示超时了

#方法二：

def maxSubArray(nums):
	curSum = maxSum = nums[0]
	for num in nums[1:]:
		curSum = max(num, curSum + num)
		maxSum = max(maxSum, curSum)
		print(num, curSum, maxSum)
	return maxSum
result = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#print(result)
