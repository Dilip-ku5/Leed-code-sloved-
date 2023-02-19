def maxprofit( a ):
    min_price = a[0]
    max_profit = 0
    for i in range(len(a)):
        min_price = min(min_price,a[i])
        profit = a[i]-min_price
        max_profit = max(max_profit,profit)
        return max_profit
    







a = [7,1,6,4,3,]
print(maxprofit(a))