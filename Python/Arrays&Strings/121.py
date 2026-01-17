class Solution():
    def maxProfit(self,prices):
        min_p = float('inf')
        max_p = 0

        for price in prices:                # Iterate through the list , keeping track of max profit and min price !!

            if price < min_p:
                min_p = price

            profit = price - min_p

            if profit > max_p:
                max_p = profit
        
        return max_p

x = Solution().maxProfit([1,4,1,1,1,5])     # **Imp**
print(x)