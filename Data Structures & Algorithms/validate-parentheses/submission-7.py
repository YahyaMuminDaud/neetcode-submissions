class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for val in s:
            if val == "[" or val == "{" or val == "(":
                stack.append(val)

            elif val == "]":
                if len(stack) == 0 or stack[-1] != "[":
                    return False
                stack.pop(-1)

            elif val == "}":
                if len(stack) == 0 or stack[-1] != "{":
                    return False
                stack.pop(-1)

            elif val == ")":
                if len(stack) == 0 or stack[-1] != "(":
                    return False
                stack.pop(-1)

        if len(stack) > 0:
            return False
        return True
