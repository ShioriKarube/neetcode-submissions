class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        時間計算量: O(n)
        空間計算量: O(n)
        """
        seen = {}

        for i, num in enumerate(nums):
            corresponding = target - num
            if corresponding in seen:
                return [seen[corresponding], i]
            else:
                seen[num] = i