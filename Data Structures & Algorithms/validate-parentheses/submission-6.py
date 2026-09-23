class Solution:
    def isValid(self, s: str) -> bool:
        """
        時間計算量: O(n)
        空間計算量: O(n)
        """
        parentheses = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stack = []
        for ch in s:
            if ch in parentheses:
                if not stack:
                    return False
                if stack.pop() != parentheses[ch]:
                    return False
            else:
                stack.append(ch)
        
        return not stack