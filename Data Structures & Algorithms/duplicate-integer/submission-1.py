class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        store = {}

        for val in nums:

            if val in store:
                return True
            else:
                store[val] = 1

        return False