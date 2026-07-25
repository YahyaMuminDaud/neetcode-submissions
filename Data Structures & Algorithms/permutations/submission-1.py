class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        store = []

        def dfs():

            if len(store) == len(nums):
                res.append(store.copy())
                return

            for i in range(len(nums)):

                if nums[i] not in store:
                    store.append(nums[i])
                    dfs()
                    store.pop()
            

        dfs()

        return res
