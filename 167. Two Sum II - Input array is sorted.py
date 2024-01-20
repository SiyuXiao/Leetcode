#字典的时间复杂度最低，用for加字典代替了之前的双重for循环
def twoSum(numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target-num in dic:
            return [dic[target-num] + 1, i + 1]
        dic[num] = i
result = twoSum([11,15,2,7,], 9)
print(result)