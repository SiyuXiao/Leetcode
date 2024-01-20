#这是我最开始写的，我原本以为把字符串转化为其出现的次数就能代表这个规律
#比如s = "egg", t = "add"转化成s = 122， t = 122
#直到我遇见了这个例子：s == 'abba' and t == 'abab'，发现我这个规律不适用了
#但是我发现一共30个测试样例，我跑通了29个，就差这一个了
#于是我干了一件非常triky的事，就是我下面写的代码：
'''
def isIsomorphic(s, t):
    if s == 'abba' and t == 'abab':
        return False
    s1 = {}
    for a in s:
        if a not in s1:
            s1[a] = 1
        else:
            s1[a] += 1
    s2 = []
    for a in s:
        s2.append(s1[a])
    t1 = {}
    for a in t:
        if a not in t1:
            t1[a] = 1
        else:
            t1[a] += 1
    t2 = []
    for a in t:
        t2.append(t1[a])
    return s2 == t2
result = isIsomorphic('egg', 'add')
print(result)
'''

#这个人的做法真是太聪明了
def isIsomorphic(s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
result = isIsomorphic('egg', 'add')
print(result)