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
            print('Stack is empty')
            
    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self)==0
    
s=Stack()
s.push(10)
s.push(2)
print(s.top())
print(s.pop())
print(len(s))
print(s.isEmpty())
