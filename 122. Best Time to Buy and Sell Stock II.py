def maxProfit(prices):
    res = []
    for i in range(len(prices)-1) :
        if prices[i+1] > prices[i] :
            profit = prices[i+1] - prices[i]
            res.append (profit)
    return sum(res)
result = maxProfit([7,1,5,3,4,6])
print(result)