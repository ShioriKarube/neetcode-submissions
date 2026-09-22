class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        時間計算量: O(n)
        空間計算量: O(1)
        """
        profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price

            curr_profit = price - min_price
            profit = max(profit, curr_profit)

        return profit