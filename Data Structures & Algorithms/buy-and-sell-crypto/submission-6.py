class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        時間計算量: O(n)
        空間計算量: O(1)
        """
        l, r = 0, 1
        profit = 0

        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                curr_profit = prices[r] - prices[l]
                profit = max(profit, curr_profit)
            r += 1

        return profit
