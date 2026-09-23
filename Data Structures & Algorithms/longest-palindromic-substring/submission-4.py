class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        

        max_length = 1
        ans_l, ans_r = 0, 0

        for i in range(len(s)):
            l, r = i - 1, i + 1 # in case odd
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    max_length = r - l + 1
                    ans_l = l
                    ans_r = r
                l -= 1
                r += 1

            l, r = i - 1, i # in case even

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    max_length = r - l + 1
                    ans_l = l
                    ans_r = r
                l -= 1
                r += 1

        return s[ans_l : ans_r+1]
        
        