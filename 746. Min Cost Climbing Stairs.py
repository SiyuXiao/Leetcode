#这题读明白就花好长时间，top指的不是最后一位数，是最后一位数的next place 
def minCostClimbingStairs(cost):
    pre = cost[0] 
    cur = cost[1]
    for i in range(2, len(cost)):
        pre, cur = cur, min(pre, cur) + cost[i]
        print(pre, cur)
    return min(pre,cur)
result = minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
#print(result)