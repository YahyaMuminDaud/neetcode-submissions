class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}

        for i in range(len(nums)):

            a = target - nums[i]

            if a in store:

                return [store[a], i]
            else:

                store[nums[i]] = i
