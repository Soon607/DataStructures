max_size=int(input('max size is:'))
class CircleQueue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.queue=[None]*max_size
        
    def isEmpty(self):
        if self.front==self.rear:
            return True
        else:
            return False
    
    def isFull(self):
        if (self.rear+1)%max_size==self.front:
            print('Queue is full')
    
    def enqueue(self,val):
        if not self.isFull():
            self.rear=(self.rear+1)%max_size
            self.queue[self.rear]=val
            
    def dequeue(self):
        if not self.isEmpty():
            self.front=(self.front+1)%max_size
            return self.queue[self.front]
        
    def peek(self):
        if not self.isEmpty():
            return self.queue[(self.front+1)%max_size]
    
    def dequeue_print(self):
        i=self.front
        if self.isEmpty():
            print('Empty Queue')
            return
        while True:
            i=(i+1)%max_size
            print(self.queue[i],' ')
            if i==self.rear or i==self.front:
                break

circle=CircleQueue()
circle.enqueue(1)
circle.enqueue(2)
circle.enqueue(3)
circle.enqueue(4)
print(circle.queue)
circle.dequeue_print()