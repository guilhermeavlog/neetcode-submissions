from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        l = 0
        counter_t = Counter(t)
        counter_s = Counter()
        shortest_substring = ""
        required = len(counter_t)
        formed = 0



        for r in range(len(s)):
            counter_s[s[r]] = 1 + counter_s.get(s[r], 0) 

            if counter_s[s[r]] == counter_t[s[r]]:
                formed += 1

            while formed ==required and counter_s.get(s[l], 0) > counter_t.get(s[l], 0): 
                counter_s[s[l]] -= 1
                if counter_s[s[l]] == 0:
                    del counter_s[s[l]]
                l += 1
                

            if r-l+1 < len(shortest_substring) or len(shortest_substring)==0: # check if window is smaller
                if formed == required:
                    shortest_substring = s[l:r+1]


        return shortest_substring


    

        