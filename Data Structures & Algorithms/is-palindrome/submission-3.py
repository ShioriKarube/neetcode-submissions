class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        時間計算量: O(n)
        空間計算量: O(n)
        """
        letters = []
        for ch in s:
            if ch.isalnum():
                letters.append(ch.lower())

        length = len(letters)-1
        l, r = 0, length
        while l < r:
            if letters[l] == letters[r]:
                l += 1
                r -= 1
            else:
                return False
        return True