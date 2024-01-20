#这个是我最开始写的，执行不通，后来发现题目要求是在原列表chars上改动，不能像我这样新建一个final列表
#而且题目里说的character也不一定只有字母
'''
def compress(chars):
	a = []
	b = []
	c = []
	d = ''
	final = []
	chars1 = chars + ['0']
	for i in range(len(chars1) - 1):
		if chars1[i] != chars1[i+1]:
			a.append(i+1)
			c.append(chars1[i])
	a = [0] + a
	for j in range(len(a) - 1):
		b.append(a[j+1] - a[j])
	for k in range(len(b)):
		d = d + c[k]
		d = d + str(b[k])
	d = d + 'a'
	for l in range(len(d) - 1):
		if d[l] == '1' and d[l+1].isalpha():
			continue
		else:
			final.append(d[l])
	chars = final
	return(chars)
result = compress(["a","a","b","b","c","c","c"])
print(result)
'''
#我改进的这个程序满足题目要求
'''
def compress(chars):
	a = []
	b = []
	c = []
	d = ''
	final = []
	chars1 = chars + ['0']
	for i in range(len(chars1) - 1):
		if chars1[i] != chars1[i+1]:
			a.append(i+1)
			c.append(chars1[i])
	a = [0] + a
	for j in range(len(a) - 1):
		b.append(a[j+1] - a[j])
	for k in range(len(b)):
		d = d + c[k]
		if b[k] != 1:
			d = d + str(b[k])
	for l in d:
		final.append(l)
	chars[:] = final[:]
	return(chars)
result = compress(["a","a","b","b","c","c","c"])
print(result)
'''
#Discuss里面给的算法，这个算法击败了其余百分之一百的选手，但不是特别好理解

def compress(chars):
    i = j = 0
    while j < len(chars):
        count, k = 1, j + 1
        while k < len(chars) and chars[j] == chars[k]:
            count, k = count + 1, k + 1
        chars[i] = chars[j]
        i += 1
        if count > 1:
            for c in str(count):
                chars[i] = c
                i += 1
        j = k
    return i
result = compress(["a","a","b","b","c","c","c"])
print(result)
