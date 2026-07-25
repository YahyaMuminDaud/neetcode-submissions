class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if nums == []:
            return [[]]

        store = []
        res = []
        def dfs(i):


            if len(store) == len(nums):
                res.append(store.copy())
                return

            for j in range(len(nums)):
                if nums[j] not in store:
                    store.append(nums[j])
                    dfs(i + 1)
                    store.pop()  
            
            

        dfs(0)
                
            
        return res