class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        i = 0
        j = 1
        currmax = 0
        while i  < j and j < len(prices):

            if prices[i] >= prices[j]:
                i += 1
                j = i + 1
            elif prices[i] < prices[j]:

                a = abs(prices[i] - prices[j])
                if currmax < a:
                    
                    currmax = a
                
                j += 1
        
        return currmax