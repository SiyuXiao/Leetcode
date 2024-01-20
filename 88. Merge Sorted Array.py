#方法一
#这个方法放leetcode里面跑不出来，leetcode里面输出的nums1仍然是输入时的nums1，而不是改变后的nums1
#而且这个答案时间复杂度太高了，sort()函数的时间复杂度是n2,外面的for循环遍历时间复杂度是n,整体时间复杂度是n3
'''
def merge(nums1, m, nums2, n):
	a = len(nums2)
	b = len(nums1)
	nums1 = nums1[0: b-a]
	for i in nums2:
		nums1.append(i)
		nums1.sort()
	return nums1
result = merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(result)
'''


def merge(nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            print(nums1, m, n)
        if n > 0:
            nums1[:n] = nums2[:n]
        return(nums1)
result = merge([1,2,3,0,0,0], 3, [2,5,6], 3)
print(result)

