class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #convert all stones to -ve values, create minheap
        #while there are more than one stone, heappop first and second, 
        #if second> first then append the difference
        #append a 0 just in case no elements are presemt, return the abs of the 0th element
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            first = heapq.heappop(stones)
            second=heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones,first-second)
        stones.append(0)
        return abs(stones[0])
        