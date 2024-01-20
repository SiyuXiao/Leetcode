#符合题目要求的答案，题目的意思就是当有多个结果的时候输出一个结果就行
def twoSum(nums, target):
	for i,x in enumerate(nums):
		for j,y in enumerate(nums):
			if x+y==target and i!=j:
				a=[i,j]
				return a
b=twoSum([1,2,3,4,5],7)
print(str(b).replace(' ',''))

#题目只要求输出一个结果，我想把所以结果全部输出出来
'''def twoSum(nums, target):
	for i,x in enumerate(nums):
		for j,y in enumerate(nums):
			if x+y==target and i!=j:
				a=[i,j]
				print(str(a).replace(' ',''))
twoSum([1,2,3,4,5],7)'''

#先定义一个空表，然后把符合要求的列表添加到这个空列表里
'''def twoSum(nums, target):
	c=[]
	for i,x in enumerate(nums):
		for j,y in enumerate(nums):
			if x+y==target and i!=j:
				a=[i,j]
				c.append(a)
	print(str(c).replace(' ',''))
twoSum([1,2,3,4,5],7)'''