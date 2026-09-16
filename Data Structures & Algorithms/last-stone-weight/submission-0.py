class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = abs(heapq.heappop(stones))
            y = abs(heapq.heappop(stones))
            if x > y:
                heapq.heappush(stones, -1*(x-y))
            
        stones.append(0)
        return abs(stones[0])