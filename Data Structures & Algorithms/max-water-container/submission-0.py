class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1
        biggest = 0
        while l <= r:
            a = min(heights[l], heights[r])
            b = r - l
            curr = min(heights[l], heights[r]) * (r - l)

            if biggest < curr:
                biggest = curr

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return biggest         