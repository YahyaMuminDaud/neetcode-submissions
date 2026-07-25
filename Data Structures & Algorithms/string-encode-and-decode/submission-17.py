class Solution:


    def encode(self, strs: List[str]) -> str:
        
        string = ""
        
        for val in strs:
            string += val
            string += "-"
        
        return string

    def decode(self, s: str) -> List[str]:

        res = []
        strings = ""
        for val in s:
            
            if val == "-":
                res.append(strings)
                strings = ""
                continue
            strings += val
        
        
        return res