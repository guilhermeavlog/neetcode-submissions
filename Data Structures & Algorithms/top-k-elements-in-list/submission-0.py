class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        
        for n in nums:
            if n in dictionary:
                dictionary[n] += 1
            else:
                dictionary[n] = 1

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        
        for key in dictionary:
            buckets[dictionary[key]].append(key)
        
        answer = []
        for i in range(n, -1, -1):
            for z in range(len(buckets[i])):
                answer.append(buckets[i][z])
                k -= 1
                if k == 0:
                    return answer
             

        return answer
            

        
                

        