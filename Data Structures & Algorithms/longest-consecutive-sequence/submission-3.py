class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        res = 0
        
        for val in num:

            a = val -1
            temp = 0
            if a not in num:
                
                b = a
                while True:

                    if b + 1 in num:
                        temp += 1
                        b += 1
                    else:
                        break
            if temp > res:
                res = temp

        return res

                    


        