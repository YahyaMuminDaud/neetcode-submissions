class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if s == "":
            return 0
        i = 0
        count = 1
        while i < len(s):
            
            j = i + 1
            check = set()
            check.add(s[i])
            while j < len(s):

                if s[j] in check:
                    break
                a = len(s[i : j + 1])
                if count < a:
                    count = a
                check.add(s[j])
                j += 1

            i += 1
        return count