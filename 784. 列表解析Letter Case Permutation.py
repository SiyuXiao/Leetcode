#Discuss用列表解析做的
'''
def letterCasePermutation(S):
    res = ['']
    for ch in S:
        if ch.isalpha():
            res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
        else:
            res = [i+ch for i in res]
    return res
result = letterCasePermutation("a1b2")
print(result)
'''
#我尝试着把列表里的for循环拿出来
def letterCasePermutation(S):
    res = ['']
    for ch in S:
        if ch.isalpha():
            c = []
            for a in res:
                for b in [ch.upper(), ch.lower()]:
                    c.append(a+b)  
            res = c  
        else:
            for i in range(len(res)):
                res[i] = res[i] + ch
    return res
result = letterCasePermutation("a1b2")
print(result)