class Stack:
    def __init__(self):
        self.items=[]
    def push(self,val):
        self.items.append(val)
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('Stack is empty')
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print('Stack is empty')
    def __len__(self):
        return len(self.items)
    def isEmpty(self):
        return len(self)==0
    
# tokenisation

def tokenisation(expr):
    tokens=[]
    valprocessing=False # whether is number or not. number-True
    value=0
    
    for val in expr:
        if val==" ":   # examining blank
            continue
        
        if val in '0123456789': # when val is number
            value=value*10+int(val)
            valprocessing=True
        else: # when val is not number
            if valprocessing==True:
                tokens.append(value)
                value=0 
            valprocessing=False
            tokens.append(val)
            
    if valprocessing:
        tokens.append(value)
    return tokens

#infix to postfix

def infix_postfix(token_list):
    prio={
        '*':3,
        '/':3,
        '+':2,
        '-':2,
        '(':1
    }
    
    opstack=Stack()
    outstack=[]
    
    for token in token_list:
        if type(token) is int:
            outstack.append(token)
        elif token==')':
            while opstack.top()!='(':
                outstack.append(opstack.pop())
            opstack.pop()
        else:
            if opstack.isEmpty()==0:
                opstack.push(token)
            else:
                while len(opstack)>0:
                    if prio[opstack.top()]>=prio[token]:
                        outstack.append(opstack.pop())
                    else:
                        break
                opstack.push(token)
                
    while not opstack.isEmpty():
        outstack.append(opstack.pop())
    
    return outstack

# computation

def computation(token_list):
    intstack=Stack()
    
    for token in token_list:
        if type(token)==int:
            intstack.push(token)
         
        elif token=='*':
            token_a=intstack.pop()
            token_b=intstack.pop()
            intstack.push(token_b*token_a)
        
        elif token=='/':
            token_a=intstack.pop()
            token_b=intstack.pop()
            intstack.push(token_b/token_a)
            
        elif token=='+':
            token_a=intstack.pop()
            token_b=intstack.pop()
            intstack.push(token_b+token_a)   
         
        elif token=='-':
            token_a=intstack.pop()
            token_b=intstack.pop()
            intstack.push(token_b-token_a)
            
    return intstack.pop()


                    
            
                