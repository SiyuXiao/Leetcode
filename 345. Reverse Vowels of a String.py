#方法一：这是光头写的，调用的re包，我觉得这个程序可读性差，不通用
'''
import re
def reverseVowels(s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
result = reverseVowels("hello")
print(result)
'''

#方法二, 我觉得这个写法很好，容易理解，有通用性

def reverseVowels(s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        L = list(s)
        i = 0
        j = len(L) - 1
        while i < j:
            while i < j and L[i] not in vowels:
                i += 1
            while i < j and L[j] not in vowels:
                j -= 1
            L[i], L[j] = L[j], L[i] #这个交换值的写法好奇妙啊
            i += 1
            j -= 1
        return ''.join(L)
result = reverseVowels("lol")
print(result)