#唉我去，python里貌似没有一次只能删除字符串中一个字符的函数，那个strip函数一次把所有一样的全删除了
#所以我把字符串转化成列表，利用列表中remove函数一次只删除一个的特点，防止出现像strip那样一次把所有一样的字符全删除了
def findTheDifference(s, t):
	s1 = []
	t1 = []
	for a in s:
		s1.append(a)
	for b in t:
		t1.append(b)
	for c in s1:
		t1.remove(c)
	return ''.join(t1)#把列表转化成字符串
result = findTheDifference('a', 'aa')
print(result)