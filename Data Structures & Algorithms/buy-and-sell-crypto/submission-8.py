class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        時間計算量: O(n)
        空間計算量: O(1)
        """
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price

            max_profit = max(max_profit, profit)

        return max_profit