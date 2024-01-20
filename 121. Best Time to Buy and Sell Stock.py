'''
def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
result = maxProfit([7, 1, 5, 3, 6, 4])
print(result)
'''

def maxProfit(prices):
    if not prices:
        return 0   
    max_profit = sell_price = 0
    for price in prices[::-1]:
        sell_price = max(sell_price, price)
        max_profit = max(max_profit, sell_price - price)
    return max_profit
result = maxProfit([7, 1, 5, 3, 6, 4])
print(result)