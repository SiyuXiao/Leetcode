def searchInsert(nums, target):
	for i, x in enumerate(nums):
		if len(nums) == 1:
			if target <= x:
				return 0
			elif target > x:
				return 1
		elif target == x:
			return i
		elif nums[i] < target < nums[i+1]:
			return i+1
		elif target > nums[-1]:
			return len(nums)
	else:
		return 0
result = searchInsert([1], 2)
print(result)