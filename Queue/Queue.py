class Queue:
    def __init__(self):
        self.items=[]
        self.first_index=0
        
    def enqueue(self,val):
        self.items.append(val)
        
    def dequeue(self):
        if self.first_index==len(self.items):
            print('Queue is empty')
            return None
        else:
            x=self.items[self.first_index]
            self.first_index+=1
            return x
    def front(self):
        return self.items[self.first_index]
    def lenQ(self):
        return len(self.items)-self.first_index
    