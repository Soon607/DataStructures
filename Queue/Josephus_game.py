class Queue:
    def __init__(self):
        self.items=[]
        self.first_index=0
    def enqueue(self,val):
        self.items.append(val)
    def dequeue(self):
        if self.first_index==len(self.items):
            print('Queue is empty')
        else:
            x=self.items[self.first_index]
            self.first_index+=1
            return x
    def front(self):
        return self.items[self.first_index]
    def lenQ(self):
        return len(self.items)-self.first_index

def Josephus(n,k): # n:the number of table k:th
    Q=Queue()
    
    for i in range(1,n+1):
        Q.enqueue(i)
        
    
    while (Q.lenQ!=1):
        for j in range(1,k):
            Q.enqueue(Q.dequeue)
        Q.dequeue
    return Q.dequeue

        