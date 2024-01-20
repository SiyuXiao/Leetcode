#这人做法很聪明，很好理解
def backspaceCompare(S, T):
    def bsString(string):
        res = []
        for c in string:
            if c != '#':
                res.append(c)
            else:
                res = res[:-1]#取这个字母之前的所有字母
        return res
    return bsString(S) == bsString(T)
result = backspaceCompare("ab##", "c#d#")
print(result)