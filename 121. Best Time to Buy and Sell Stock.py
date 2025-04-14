"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

#Attempt 1 (Failed - Time Limit Exceeded):

class Solution(object):
    def maxProfit(self, prices):
        maxProfit = 0

        for day, price in enumerate(prices):
            for upcomingprice in prices[day:]:
                currentProfit = upcomingprice - price
                if currentProfit > maxProfit:
                    maxProfit = currentProfit
              
        return maxProfit      



#Attempt 2:

class Solution(object):
    def maxProfit(self, prices):
        #Utilizing a TwoPointer method
        l,r = 0,1
        maxProfit = 0

        while r<len(prices):
            if prices[l] < prices[r]:
                 currentProfit = prices[r] - prices[l]
                 maxProfit = max(currentProfit, maxProfit)
            else:
                 l = r
    
            r += 1
        return maxProfit