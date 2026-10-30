class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        # print('pre', heap)
        heapq.heapify(heap)
        # print('after', heap)
        while len(heap) > 1:
            max_stone1 = -heapq.heappop(heap)
            max_stone2 = -heapq.heappop(heap)
            if max_stone1 == max_stone2:
                continue
            remain = abs(max_stone1 - max_stone2) 
            heapq.heappush(heap, -remain)
            # print('new heap', heap)
        return 0 if len(heap) == 0 else -heap[0]