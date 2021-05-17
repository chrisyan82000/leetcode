def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for s in S:
            if s == '(':
                stack.append(s)
            else:
                m = stack.pop()
                if m == '(': stack.append(1)
                else:
                    tmp = 0
                    while m != '(':
                        tmp+=m
                        m = stack.pop()
                    stack.append(2*tmp)
        return sum(stack)
