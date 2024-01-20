def isPalindrome(s):
	Palindrome = s[::-1]
	test1 = ''.join([x for x in s if x.isalnum()])
	test2 = ''.join([x for x in Palindrome if x.isalnum()])
	if test1.lower() == test2.lower():
		return True
	else:
		return False
result = isPalindrome("OP")
print(result)


'''
a = "A man, 2a plan, a canal: Panama"
b = a[::-1]
c = ''.join([x for x in a if x.isalnum()])#从字符串中提取字母和数字
d = ''.join([x for x in b if x.isalpha()])#从字符串中提取字母
e = ''.join([x for x in b if x.isnumeric()])#从字符串中提取数字
print(c)
print(d)
print(e)
'''