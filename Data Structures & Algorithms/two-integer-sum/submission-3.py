class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        storage = {}
        i = 0
        for val in nums:

            a = target - val

            if a in storage:
                return [storage[a], i]
            else:
                storage[val] = i
            
            i += 1

        return []
            