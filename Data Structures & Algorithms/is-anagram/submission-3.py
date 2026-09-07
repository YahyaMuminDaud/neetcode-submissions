class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    

        store1 = {}

        store2 = {}

        for val in s:

            if val in store1:
                
                store1[val] += 1
            else:
                store1[val] = 1

        for val in t:

            if val in store2:
                store2[val] += 1
            else:
                store2[val] = 1

        return store1 == store2