class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_count = defaultdict(list)

        for word in strs:
            arr = [0] * 26

            for c in word:
                arr[ord(c) - ord('a')] += 1

            key = arr

            word_count[tuple(key)].append(word)
        
        sol = []

        for key in word_count:
            sol.append(word_count[key])

        return sol 

