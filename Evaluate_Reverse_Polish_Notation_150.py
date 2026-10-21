class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = [] #stack is apended 
        operand = ["*","+","-","/"]
        for i, tok in enumerate(tokens):
            #when we come across a operand in the stack we pop 2 elements and do the operation in between
            if tok in operand:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if tok == "*":
                    calc = num2 * num1
                elif tok == "+":
                    calc = num2 + num1
                elif tok == "-":
                    calc = num2 - num1
                else:
                    calc = num2/num1
                stack.append(calc)

            else:
                stack.append(tok)
        return int(stack.pop())