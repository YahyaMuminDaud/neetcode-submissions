class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        store = {}
        ans = []
        for val in strs:

            a = sorted(val)
            b = ""
            for vals in a:
                b += vals
   

            if b in store:
                store[b].append(val)
            else:
                store[b] = [val]
           
        for key, val in store.items():

            ans.append(val)

        return ans