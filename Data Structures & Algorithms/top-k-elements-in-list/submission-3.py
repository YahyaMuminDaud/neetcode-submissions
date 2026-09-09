class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        storage = {}

        for val in nums:

            if val in storage:
                storage[val] += 1
            else:
                storage[val] = 1

        

        i = k

        while i > 0:

            a = 0
            b = 0
            for key,val in storage.items():

                if a < val:
                    a = val
                    b = key

            res.append(b)
            del storage[b]
            i -= 1
            

        return res