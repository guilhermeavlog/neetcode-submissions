from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = Counter(s1)
        count_s2 = {}
        l = 0

        if len(s1) > len(s2):
            return False

        for r in range(len(s2)):
            count_s2[s2[r]] = 1 + count_s2.get(s2[r], 0)

            while count_s2.get(s2[r], 0) > count_s1.get(s2[r], 0):
                count_s2[s2[l]] -= 1
                if count_s2[s2[l]] == 0:
                    del count_s2[s2[l]]      # (3) drop zero keys so == works
                l += 1

            if count_s2 == count_s1:
                return True




        return False
        