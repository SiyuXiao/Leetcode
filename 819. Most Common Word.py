def mostCommonWord(paragraph, banned):
    paragraph0 = ''
    for a in paragraph:
        if a == ',':
            paragraph0 += a + ' '
        else:
            paragraph0 += a
    paragraph0 = paragraph0.lower()
    paragraph1 = paragraph0.split()
    for a in paragraph1:
        for b in a:
            if b.isalpha() == False:
                paragraph0 = paragraph0.replace(b, '')
    #以上是为了去掉非字母符号
    paragraph11 = []
    paragraph12 = paragraph0.split()
    for a in paragraph12:
        if a not in set(banned):#我把banned变成集合，这样的话能快点
            paragraph11.append(a)
    #以上是为了去掉paragraph里banned有的元素
    D = {}
    for a in paragraph11:
        if a not in D:
            D[a] = 1
        else:
            D[a] += 1
    for a in D:
        if D[a] == max(D.values()):
            return a
result = mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
print(result)
#"Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
#"a, a, a, a, b,b,b,c, c", ["a"]
#"abc abc? abcd the jeff!", ["abc","abcd","jeff"]