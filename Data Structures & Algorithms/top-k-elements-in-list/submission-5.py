class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        store = {}

        for val in nums:

            if val in store:
                store[val] += 1
            else:
                store[val] = 1

        heap = []

        for key, val in store.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res


    