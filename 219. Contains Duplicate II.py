#这个写法超时了
'''
def containsNearbyDuplicate(nums, k):
    for i, a in enumerate(nums):
        for j, b in enumerate(nums):
            if a == b and i != j:
                diff = abs(i - j)
                if diff <= k:
                    return True
    return False
result = containsNearbyDuplicate([1,2,3,1,2,3], 2)
print(result)
'''

def containsNearbyDuplicate(nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False
result = containsNearbyDuplicate([1,0,1,1], 1)
print(result)
