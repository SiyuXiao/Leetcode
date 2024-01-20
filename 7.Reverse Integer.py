#如何把一个数字中每一位的数字表示成列表中的一个元素
'''number = 12345
a=list(map(int,str(number)))
print(a)'''

#如何将一个列表中的每一个元素倒序
'''number = 12345
a=list(map(int,str(number)))
a.reverse()
print(a)'''

#使用了列表解析对正数和末尾为0的数可以倒置，这个代码能跑得通真是我蒙的,用map把字符串变成数字，用列表解析把数字又变回了字符串，真是多余
'''def reverse(x):
	a=list(map(int,str(x)))#str(x)表示把数字转化成了字符串，map表示把字符串转化成了整数
	a.reverse()
	b = int("".join([str(y) for y in a]))#列表解析，for：把a中的数字遍历一遍，str：把数字变成字符串，join：把字符添加到同一个字符串里，间隔为空
	return b
c=reverse(123450)
print(str(c).replace(', ',''))'''

#符合题目要求的答案
def reverse(x):
	sign=x<0
	x=list(str(abs(x)))
	y=x.reverse()
	z=(-1) ** sign * int(''.join(x))
	if z>=(-2**31) and z<=(2**31-1):
		return z
	else:
		return 0
a=reverse(120)
print(a)
