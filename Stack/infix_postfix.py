class Stack:
    def __init__(self):
        self.items=[]
    def push(self,val):
        self.items.append(val)
        return self.items
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print('Stack is Empty')
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print('Stack is empty')
    def len_stack(self):
        return len(self)
    def isEmpty(self):
        return len(self)==0

# tokenization
def get_token_list(expr):
    temp=[]
    result=[]
    num=str()
    for i in expr:
        if i=='*' or i=='/' or i=='+' or i=='-' or i=='^' or i=='(' or i==')':
            for j in temp:
                num+=j
            if num!='':
                result.append(float(num))
            result.append(i)
            temp=[]
            num=''
        else:
            temp.append(i)
    for k in temp:
        num+=k
    result.append(float(num))
    return result
      
# infix_to_postfix
def infix_to_postfix(token_list,opStack,outStack):
    for i in token_list:
        if i=='*' or i=='/' or i=='(':
            opStack.push(i)
        elif i=='+' or i=='-':
            if opStack.len_stack()==0:
                opStack.push(i)
            else:
                while(opStack.len_stack()):
                    if opStack.top()=='*' or opStack.top()=='/':
                        outStack.append(opStack.top())
                        opStack.pop()
                    opStack.push(i)
            
        elif i==')':
            while(opStack.top()!='('):
                outStack.append(opStack.top())
                opStack.pop()
            opStack.pop()
        else:
            outStack.append(i)
    while(opStack.len_stack()!=0):
        outStack.append(opStack.top())
        opStack.pop()
            
                
            
# computation
def compute_profix(outStack):
    s=Stack()
    for i in outStack:
        if (i!='+' or i!='-' or i!='*' or i!='/' or i!='^'):
            s.push(i)
        else:
            operand1=s.top()
            s.pop()
            operand2=s.top()
            s.pop()
            if (i=='+'):
                s.push(operand2+operand1)
            elif(i=='-'):
                s.push(operand2-operand1)
            elif(i=='*'):
                s.push(operand2*operand1)
            elif(i=='/'):
                s.push(operand2/operand1)
    return s.top()

a='2+3*5'
print(get_token_list(a))           