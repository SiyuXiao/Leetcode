def moveZeroes(nums):
    new1 = []
    new2 = []
    for a in nums:
        if a != 0:
            new1.append(a)
        else:
            new2.append(a)
    return  new1 + new2
result = moveZeroes([0,1,0,3,12])
print(result)