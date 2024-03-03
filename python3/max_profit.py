# 121
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit


tests = [
    (
        # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        # Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
        ([7,1,5,3,6,4],),   # Input
        (5),  # Output
    ),
    (
        # Explanation: In this case, no transactions are done and the max profit = 0.
        ([7,6,4,3,1],),
        (0),
    ),
    (
        # Explanation: In this case, no transactions are done and the max profit = 0.
        ([1,2,4,2,5,7,2,4,9,0,9],),
        (9),
    ),
]