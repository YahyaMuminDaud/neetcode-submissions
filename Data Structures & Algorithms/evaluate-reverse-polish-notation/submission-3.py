class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for val in tokens:

            if val == "+":

                a = stack.pop()
                b = stack.pop()

                c = b + a
                stack.append(c)

            elif val == "-":

                a = stack.pop()
                b = stack.pop()

                c = b - a
                stack.append(c)
            elif val == "*":

                a = stack.pop()
                b = stack.pop()

                c = b * a
                stack.append(c)

            elif val == "/":

                a = stack.pop()
                b = stack.pop()

                c = int(b / a)
                stack.append(c)
            else:
                stack.append(int(val))

        return stack[0]