#我这个程序只能满足等于1的情况
'''
def isHappy(n):
    while n != 1:
        n1 = str(n)
        n2 = 0
        for i in range(len(n1)):
            n2 += int(n1[i])**2
        n = n2
    else:
        return True
result = isHappy(19)
print(result)
'''
#这个人写的这个算法没有说这个set是否形成了一个loop
def isHappy(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(x) **2 for x in str(n)])
    return n == 1
result = isHappy(2)
print(result)