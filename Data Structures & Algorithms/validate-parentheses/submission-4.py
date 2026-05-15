class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for char in s:
            #add to stack if opening brackets
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            
            #if it's closing check the opening for it from stack pop
            elif char == ')':
             
                if stack[-1] == '(':
                    stack.pop()  
                else:
                    return False #wrong mathcing
            
            elif char == '}':
                
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
            
            elif char == ']':
                if len(stack) == 0:
                    return False
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        
        
        return len(stack) == 0