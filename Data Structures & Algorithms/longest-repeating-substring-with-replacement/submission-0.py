class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window 
        # count characters in window
        # replace other characters to match most frequent
        # keep count of longest string size
        # if different character becomes most frequent flip those instead

        count = {}
        l = 0
        max_freq = 0
        res = 0

        for r in range(len(s)):
            if s[r] not in count: # add new character to count
                count[s[r]] = 1 
            else:
                count[s[r]] += 1
            
            if count[s[r]] > max_freq: # update max freq 
                max_freq = count[s[r]]

            while (r - l + 1 ) - max_freq > k: # shrink window if flipping not enough 
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res


            
            

        