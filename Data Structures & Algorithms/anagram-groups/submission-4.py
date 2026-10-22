class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        storage = {}

        for val in strs:
            a = sorted(val)
            b = ""
            for val2 in a:
                b += val2
            
            if b in storage:
                storage[b].append(val)
            else:
                storage[b] = [val]

        
        res = []

        for key, val in storage.items():

            res.append(val)

        return res