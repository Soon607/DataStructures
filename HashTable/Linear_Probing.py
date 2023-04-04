class LinearProbingHashTable:
    def __init__(self,capacity):
        self.capacity=capacity
        self.table=[None]*self.capacity
        
    def _hash(self,key):
        return hash(key)%self.capacity
    
    def insert(self,key,value):
        index=self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0]==key:
                self.table[index]=(key,value)
                return
            index=(index+1)%self.capacity
        self.table[index]=(key,value)
        
    def delete(self,key):
        index=self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0]==key:
                self.table[index]=None
                next_index=(index+1)%self.capacity
                while self.table[next_index] is not None:
                    next_key,next_value=self.table[next_index]
                    self.table[next_index]=None
                    self.insert(next_key,next_value)
                    next_index=(next_index+1)%self.capacity
                return
            index=(index+1)%self.capacity
            
    def search(self,key):
        index=self._hash(key)
        while self.table[index] is not None:
            if self.table[index][0]==key:
                return self.table[index][1]
            index=(index+1)%self.capacity
        return None