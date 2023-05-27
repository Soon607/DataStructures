class disjointSet:
    def __init__(self,n):
        self.data=[i for i in range(n)]
        self.size=n
        
    def find(self,idx):
        return self.data[idx]
    
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x==y:
            return 
        for i in range(len(self.data)):
            if self.data[i]==y:
                self.data[i]=x
        self.size-=1
        