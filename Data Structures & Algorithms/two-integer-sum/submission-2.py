class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}
        i = 0
        for val in nums:
            a = target - val
            if a in store:
                return [store[a], i]
            else:
                store[val] = i
            
            i += 1

        return []