class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = {"+", "-", "*", "/"}
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                e1 = stack.pop()
                e2 = stack.pop()
                if i == "+":
                    stack.append(e2+e1)
                elif i == "-":
                    stack.append(e2-e1)
                elif i == "*":
                    stack.append(e2*e1)
                else:
                    stack.append(int(float(e2)/e1))
        return stack[-1]


        