class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = []

        store = {}

        for val in strs:

            a = sorted(val)
            b = ''.join(a)            
            if b in store:

                store[b].append(val)
            else:
                store[b] = [val]

        for key, val in store.items():

            res.append(val)
        return res