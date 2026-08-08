class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s = list(s)

        if len(s) < 2:
            return False

        for x in s:
            if len(stack) == 0:
                stack.append(x)
            else:
                if x == '(' or x == '{' or x == '[':
                    stack.append(x)

                elif stack[-1] == '(' and x == ')':
                    stack.pop()

                elif stack[-1] == '[' and x == ']':
                    stack.pop()

                elif stack[-1] == '{' and x == '}':
                    stack.pop()

                else:
                    return False

        return len(stack) == 0