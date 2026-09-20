# 解法1: ハッシュマップ解法

# 解法2: ソート＋二点ポインタ
（値, 元のインデックス）というペアを先に作ることで元のリスト内での位置を保持する。今回の問題での二点ポインタは両端から中心に向かって狭めるパターンを使用。
時間計算量はpairsに値を追加していくのでO(n)、ソートでO(nlogn)、探すのにO(n)だから最終的にはO(n)。
空間計算量はpairsというリストを作成するためO(n)。

# 解法3: 二点ポインタ
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        元のnumsがソートされている場合のみ
        時間計算量: O(n)
        空間計算量: O(1)
        """
        l, r = 0, len(nums)-1

        while l < r:
            total = nums[l] + nums[r]
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l, r]
```
この解法はソート済みが前提のためNeetCodeの問題では使えない。ソートされていたなら左右にポインタを置いて、合計がtargetより大きければ右のを一つ左へ、小さければ左を右へ動かす。
捨てた要素は答えにはならないと保証できるため、時間O(n)、空間O(1)で解ける。
