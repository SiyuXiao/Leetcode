def firstUniqChar(s):
	a = []
	b = list(set(s))
	b.sort(key=s.index)
	for i in b:
		if s.count(i) == 1:
			a.append(i)
	return s.find(a[0]) if a else -1
result = firstUniqChar("leetcode")
print(result)
