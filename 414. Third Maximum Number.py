def thirdMax(nums):
    new = list(set(nums))
    new.sort()
    if len(new) >= 3:
        return new[::-1][2]
    else:
        return new[-1]
result = thirdMax([2, 2, 3, 1])
print(result)