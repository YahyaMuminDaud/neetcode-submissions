class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def back(i, store):

            # BASE CASE: you're done deciding
            if i == len(nums):
                res.append(store.copy())  # you wrote store.append(nums[i]) here — wrong, you're past the end
                                        # you also forgot .copy() — without it every entry in res is the same list
                return                    # you had recursive calls after return — dead code, same bug as Invert Tree

            # INCLUDE nums[i] — these were inside your if block, they should be outside it
            store.append(nums[i])
            back(i + 1, store)            # you wrote back(store, i+1) — args were flipped

            # BACKTRACK then SKIP — you had this after a return so it never ran
            store.pop()                   # you wrote res.pop() — wrong list
            back(i + 1, store)

        back(0, [])                       # you never called back() to start things off
        return res
