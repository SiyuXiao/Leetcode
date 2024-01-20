def canConstruct(ransomNote, magazine):
    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True
result = canConstruct("aa", "aab")
print(result)