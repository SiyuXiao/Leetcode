#这是我自己写的程序，虽然有点曲折，但是我认为是通法
'''
def shortestCompletingWord(licensePlate, words):
    licensePlate1 = ''
    for a in licensePlate:
        if a.isalpha():
            licensePlate1 += a.lower()
    D = {}
    for a in licensePlate1:
        if a not in D:
            D[a] = 1
        else:
            D[a] += 1
    words2 = []
    for a in words:
        c = True
        for b in D:
            if a.count(b) < D[b]:
                c = False
                break
        if c == True:
            words2.append(a)
    words3 = []
    for a in words2:
        words3.append(len(a))
    return words2[words3.index(min(words3))]
result = shortestCompletingWord("Ah71752", ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"])
print(result)
'''
#Discuss的一个做法，值得我学习
#直接赋值，浅拷贝和深拷贝的区别：http://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html
def shortestCompletingWord(licensePlate, words):
    plate = [s.lower() for s in licensePlate if s.isalpha()]
    for word in sorted(words, key = len):#这个sorted的key用来给单词按字母长度排序
        temp = plate.copy()#这个copy的用法挺好，避免了指向同一个内存
        for c in word:
            if c in temp:
                del temp[temp.index(c)]
        if len(temp) == 0:
            return word
result = shortestCompletingWord("Ah71752", ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"])
print(result)