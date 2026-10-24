class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        prefix = 0
        seen = {0:1}

        for i in range(len(nums)):

            prefix += nums[i]
            a = prefix - k

            if a in seen:
                count += seen[a]

            if prefix in seen:
                seen[prefix] += 1
            else:
                seen[prefix] = 1

        return count