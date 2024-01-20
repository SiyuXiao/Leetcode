#方法一
'''
def lengthOfLastWord(s):
	return 0 if len(s.split()) == 0 else len(s.split()[-1]) 
result = lengthOfLastWord("Hello World")
print(result)
'''
#上面的程序和下面这个是同一个意思：
'''
def lengthOfLastWord(s):
	if len(s.split()) == 0:
		return 0 
	else:
		return len(s.split()[-1]) 
result = lengthOfLastWord("Hello World")
print(result)
'''
#方法二
'''
def lengthOfLastWord(s):
	return 0 if not s.split() else len(s.split()[-1])
result = lengthOfLastWord("Hello World")
print(result)
'''

