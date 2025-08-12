prices = [6,5,4,3,2] #[9,5,4,3,2,7,1]

maxProfit = 0
minBuy = prices[0]
for price in prices:
    
    profit = price - minBuy
    maxProfit = max(profit, maxProfit)
    minBuy = min(minBuy, price)

print(maxProfit)