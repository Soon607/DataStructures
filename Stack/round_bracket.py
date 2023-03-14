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
            print('Stack is empty')
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print('Stack is Empty')
    def len_stack(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items)==0
    
def parChecker(preseq):
    S=Stack()
    for i in preseq:
        if i=='(':
            S.push(i)
        else:
            if S.is_empty():
                return False
            else:
                S.pop()
    if S.is_empty():
        return True
    else:
        return False
    
a=input('Enter:')
print(parChecker(a))


   
            