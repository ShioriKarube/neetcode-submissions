class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        時間計算量: O(n)
        空間計算量: O(1)
        """
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            r += 1
        
        return max_profit