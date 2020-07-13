def top(s):
        return s[len(s)-1]
def isValid( s):
        
        
        stack=[]
        
        for i in s:
            print(stack,i)
            
                
            
            if(i=='('):
                stack.append('(')
                #print(stack)
                continue
                
                
            elif(i=='['):
                stack.append('[')

                continue
                
                
                
            elif(i=='{'):
                stack.append('{')
                continue
                
              
                
            elif(i==')' and (top(stack)=='(' or len(stack)==0)):
                
                
                
                stack.pop()
                
                
                
             
            
                
            elif(i==']' and (top(stack)=='[' or len(stack)==0)):
                
                
                
                stack.pop()
                
                
                
            
                
            elif(i=='}' and (top(stack)=='{' or len(stack)==0)):
                
                
                
                
                stack.pop()
                
                
               
            else:
                
                return 0
                
        return 1
                
print(isValid('(){}[]'))
        
            
