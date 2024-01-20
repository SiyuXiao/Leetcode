def findRestaurant(list1, list2):
    nums = {}
    nums1 = []
    for i, a in enumerate(list1):
        for j, b in enumerate(list2):
            if a == b:
                nums[a] = i + j
    c = min(nums.values())
    for b in nums:
        if nums[b] == c:
            nums1.append(b)
    return nums1
result = findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"],
["KFC","Burger King","Tapioca Express","Shogun"])
print(result)