"""Leetcode 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing
a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""


class Solution:
    def max_profit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        res = 0

        for _ in range(len(prices) - 1):
            if prices[right] <= prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                res = max(profit, res)
            right += 1

        return res


# class Solution:
#     def max_profit(self, prices: list[int]) -> int:
#         max_profit = 0
#         min_buy = prices[0]
#         for sell in prices:
#             max_profit = max(max_profit, sell - min_buy)
#             min_buy = min(min_buy, sell)
#         return max_profit