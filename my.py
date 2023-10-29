from collections import deque

class Solution:
    def evalRPN(self,a):
        stack=deque()
        for i in a:
            if i.replace('-','').isdigit():
                stack.append(int(i))
            else:
                if len(stack)>1:
                    t,p=stack.pop(),stack.pop()
                    s=eval(f'{p}{i}{t}')
                    if i=='/':
                        s=int(s)
                    stack.append(s)
        return stack[-1]


s=Solution()

print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+", "5","+"]))