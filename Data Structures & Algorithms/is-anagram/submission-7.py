class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = defaultdict(int)

        for c in s:
            counter_s[c] = 1 + counter_s.get(c, 0)
        
        counter_t = defaultdict(int)

        for c in t:
            counter_t[c] = 1 + counter_t.get(c, 0)

        for c in s:
            if not counter_t[c] == counter_s[c]:
                return False

        for c in t:
            if not counter_t[c] == counter_s[c]:
                return False
            
        return True 



        