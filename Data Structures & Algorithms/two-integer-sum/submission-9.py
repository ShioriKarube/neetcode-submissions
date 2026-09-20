class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        ペアを作ってソートし、two pointerで解く
        時間計算量: O(nlogn)
        空間計算量: O(n)
        """
        pairs = []

        for i, num in enumerate(nums):
            pairs.append((num, i))
        pairs.sort()

        l, r = 0, len(pairs)-1

        while l < r:
            total = pairs[l][0] + pairs[r][0]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                i, j = pairs[l][1], pairs[r][1]
                return [min(i, j), max(i, j)]
