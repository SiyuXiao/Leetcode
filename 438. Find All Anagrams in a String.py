#这是我最开始的想法，我觉得没毛病，但是一跑超时了
#这个问题的核心是判断两个字符串所含有的字符是否一样，我用的是排序比较的方法
#排序比较的时间复杂度是：排序：nlogn 比较：n 外面的while循环：n， 所以总体的时间复杂度是n*n*nlogn
#原来如此，我不超时就奇怪了
'''
def findAnagrams(s, p):
    p1 = sorted(p)
    cnt = 0
    none = []
    while cnt <= (len(s) - len(p) + 1):
        if sorted(s[cnt:cnt+len(p)]) == p1:
            none.append(cnt)
        cnt += 1
    return none
result = findAnagrams("cbaebabacd", "abc")
print(result)
'''
#王警剑刚开始写的，也超时了
'''
def find(s, p):
    y = []
    for i in range(len(s)-len(p)+1):
        d = {}
        for j in range(len(p)):
            if p[j] not in d:
                d[p[j]] = 1
            else:
                d[p[j]] += 1
        for j in range(len(p)):
            if s[i+j] not in d:
                d[s[i+j]] = 1
            elif d[s[i+j]] == 1:
                del(d[s[i+j]])
            else:
                d[s[i+j]] -= 1
        if len(d) == 0:
            y.append(i)
    return y

print(find('cbaebabacd', 'abc'))
'''

#Discuss中的一种做法，我觉得这个做法很巧妙

def findAnagrams(s, p):
    res = []
    n, m = len(s), len(p)
    if n < m: return res
    phash, shash = [0]*123, [0]*123
    for x in p:
        phash[ord(x)] += 1
    for x in s[:m-1]:
        shash[ord(x)] += 1
    for i in range(m-1, n):
        shash[ord(s[i])] += 1
        if i-m >= 0:
            shash[ord(s[i-m])] -= 1#这一步保证了s中比较的字母数目和p字母的数目一样多
        if shash == phash:
            res.append(i - m + 1)
    return res
result = findAnagrams("cbaebabacd", "abc")
print(result)

#王警剑的时间复杂度为1的做法，dp自始至终不变，dd代表s和p之间的差异
'''
def findAnagrams(s, p):
    dp = {}
    for i in range(len(p)):
        if p[i] not in dp:
            dp[p[i]] = 1
        else:
            dp[p[i]] += 1
    y = []
    for i in range(len(s)-len(p)+1):
        if i == 0:
            dd = {}
            for j in range(len(p)):
                if p[j] not in dd:
                    dd[p[j]] = 1
                else:
                    dd[p[j]] += 1
            for j in range(len(p)):
                if s[j] not in dd:
                    dd[s[j]] = 1
                else:
                    if s[j] not in dp:#这一步真是经典啊，我和王警剑讨论很长时间
                        dd[s[j]] += 1
                    else:
                        if dd[s[j]] > 1:
                            dd[s[j]] -= 1
                        else:
                            del dd[s[j]]
        else:
            if s[i-1] not in dd:
                dd[s[i-1]] = 1
            else:
                if dd[s[i-1]] > 1:
                    dd[s[i-1]] -= 1
                else:
                    del dd[s[i-1]]
            if s[i+len(p)-1] not in dd:
                dd[s[i+len(p)-1]] = 1
            else:
                if s[i+len(p)-1] not in dp:
                    dd[s[i+len(p)-1]] += 1
                else:
                    if dd[s[i+len(p)-1]] > 1:
                        dd[s[i+len(p)-1]] -= 1
                    else:
                        del dd[s[i+len(p)-1]]
        if len(dd) == 0:
            y.append(i)
    return y
print(findAnagrams('cbaebabacd', 'abc'))
'''