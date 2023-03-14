class CircleQueue:
    rear=0
    front=0
    max_size=100
    queue=list()
    
    def __init__(self):
        self.rear=0
        self.front=0
        self.queue=[0 for i in range(self.max_size)]
    # Empty Circular Queue
    def is_empty(self):
        if self.rear==self.front:
            return True
        else:
            return None
    # Full Circular Queue   
    def is_full(self):
        if (self.rear+1)%self.max_size==self.front:
            return True
        return False
    # Enque
    def enqueue(self,x):
        if self.is_full():
            print('Error:Full')
        self.rear=(self.rear+1)%(self.max_size)
        self.queue[self.rear]=x
    # dequeue
    def dequeue(self):
        if self.is_empty():
            print('Error: Empty')
            return
        self.front=(self.front+1)%self.max_size
        return self.queue[self.front]
    # print dequeue
    def deque_print(self):
        i=self.front #0
        if self.is_empty():
            print('Empty Queue')
        while True:
            i=(i+1)%self.max_size
            print(self.queue[i],' ')
            if i==self.rear or i!=self.front:
                break
a=CircleQueue()
