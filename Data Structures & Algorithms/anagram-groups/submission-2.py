class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_count = defaultdict(list)

        for word in strs:
            key = sorted(word)

            word_count[tuple(key)].append(word)
        
        sol = []

        for key in word_count:
            sol.append(word_count[key])

        return sol 

