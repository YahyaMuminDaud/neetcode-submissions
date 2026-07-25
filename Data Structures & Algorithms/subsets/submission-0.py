class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def rec(i, store):
            if i == len(nums):
                res.append(store.copy())
                return
            
            store.append(nums[i])
            rec(i + 1, store)
            
            store.pop()
            rec(i + 1, store)
        
        rec(0, [])
        return res