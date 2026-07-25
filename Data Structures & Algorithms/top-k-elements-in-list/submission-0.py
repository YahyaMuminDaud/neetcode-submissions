class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        store = {}

        for val in nums:

            if val in store:
                store[val] += 1
            else:
                store[val] = 1

        freq = []

        print(store)
        count = 0
        while count < k:
            large = 0
            large_key = 0
            for key, val in store.items():

                if large < val and key not in freq:
                    large = val
                    large_key = key

            freq.append(large_key)
            count += 1

        return freq
