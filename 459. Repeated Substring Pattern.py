def repeatedSubstringPattern(str):
    ss = (str*2)[1:-1]
    return str in ss
result = repeatedSubstringPattern("abab")
print(result)