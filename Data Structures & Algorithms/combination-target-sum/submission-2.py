class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        store = []

        def dfs(i, sums):

            if i >= len(nums):
                return

            if sums + nums[i] > target:
                pass
            elif sums + nums[i] == target:
                store.append(nums[i])
                res.append(store.copy())
                store.pop()
            else:
                store.append(nums[i])
                dfs(i, sums + nums[i])
                store.pop()
            dfs(i + 1, sums)

        dfs(0, 0)
        return res
