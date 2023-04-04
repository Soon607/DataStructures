class ChainingHashTable:
    def __init__(self,capacity):
        self.capacity=capacity
        self.table=[[] for _ in range(self.capacity)]
        
    def _hash(self,key):
        return hash(key)%self.capacity
    
    def insert(self,key,value):
        index=self._hash(key)
        for item in self.table[index]:
            if item[0]==key:
                item[1]=value
                return
        self.table[index].append((key,value))
        
    def delete(self,key):
        index=self._hash(key)
        for i , item in enumerate(self.table[index]):
            if item[0]==key:
                del self.table[index][i]
                return
    
    def search(self,key):
        index=self._hash(key)
        for item in self.table[index]:
            if item[0]==key:
                return item[1]
        return None