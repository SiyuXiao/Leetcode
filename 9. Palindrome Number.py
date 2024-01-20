def isPalindrome(x):
	b=0
	y=x
	while x>0:
		a=x%10
		b=10*b+a
		x=x//10
	return b==y
c=isPalindrome(121)
print(c)