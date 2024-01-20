def findDisappearedNumbers(nums):
    if not nums:
        return []
    else:
        new = list(set(nums))
        new.sort()
        compare = []
        result = []
        newlist = {}
        for c in new:
            newlist[c] = 1#把new列表转化成newlist字符串
        for a in range(1, (len(nums)+1)):
            compare.append(a)
        for b in compare:
            if b not in newlist:
                result.append(b)
        return result
result = findDisappearedNumbers([4,3,2,7,8,2,3,1])
print(result)