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
            print('Stack is Empty')
            
    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self)==0

# round_bracket

def parChecker(parSeq):
    S=Stack()
    for symbol in parSeq:
        if symbol == "(":
            S.push(symbol)
        else: # symbol==")"
            if len(S)==0: # if nothing matched
                return False
            else:
                S.pop()
    if len(S)==0:
        return True
    else:
        return False

list1=['(','(',')','(',')',')']
print(parChecker(list1))
       
    