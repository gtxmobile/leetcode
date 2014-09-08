def evalRPN(tokens):
        stack=[]
        for i in tokens:
            try:
                stack.append(float(i))
            except:
                if i=='+':
                    stack.append(stack.pop(-2)+stack.pop())
                elif i=='-':
                    stack.append(stack.pop(-2)-stack.pop())
                elif i=='*':
                    stack.append(stack.pop(-2)*stack.pop())
                else:
                    stack.append(int(stack.pop(-2)/stack.pop()))
        return int(stack[0])
print evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
