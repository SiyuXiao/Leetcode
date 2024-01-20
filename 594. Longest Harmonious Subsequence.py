#我这个算法超时了
'''
def findLHS(nums):
    nums.sort()
    none = []
    for i in range(len(nums) - 1):
        if nums[i+1] - nums[i] == 1:
            none.append(nums.count(nums[i]) + nums.count(nums[i+1]))
    return max(none) if none else 0
result = findLHS([1,3,2,2,5,2,3,7])
print(result)
'''
#这个算法对字典的使用真是太值得我学习了
def findLHS(nums):
    mp={}
    for i in nums:
        if i not in mp:
            mp[i]=1
        else: mp[i]+=1 
    ln=0;
    for i in mp:
        if mp.get(i+1):#字典 get() 函数返回指定键的值，如果值不在字典中返回默认值
            ln=max(ln,mp[i]+mp[i+1])
    return ln 
result = findLHS([1,3,2,2,5,2,3,7])
print(result)