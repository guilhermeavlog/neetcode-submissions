class Solution:
    def isPalindrome(self, s: str) -> bool:
        right, left = len(s)-1, 0
        s = s.lower()

        while right > left:
            while not s[right].isalnum() and right > left:
                right -= 1
            while not s[left].isalnum() and right > left:
                left += 1
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1

        return True

        