class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        a = ""

        for val in s:

            if val.isalpha() or val.isdigit():
                a += val
            

        b = a.lower()


        l = 0
        r = len(b) - 1

        while l < r:

            if b[l] != b[r]:
                return False
            
            l += 1
            r -= 1

        return True