class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #ok if current element is lower than lowest than lowest is current 
        #then we calculate profit 
        lowest = prices[0]
        profit = 0
        for i, price in enumerate(prices):
            if price < lowest:
                lowest = price
            
            if lowest < price:
                currProfit = price - lowest
                if currProfit > profit:
                    profit = currProfit
        return profit
