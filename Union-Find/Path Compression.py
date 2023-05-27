# Path Compression
class disjointSet:
    def __init__(self,n):
        self.data=[-1 for _ in range(n)]
        self.size=n
        
    def upward(self,buf,idx):
        parent=self.data[idx]
        if parent<0:
            return idx
        buf.append(idx)
        return self.upward(buf,parent)
    
    def find(self,idx):
        buf=[]
        result=self.upward(buf,idx)
        for i in buf:
            self.data[i]=result
        return result
    
    def union(self,x,y):
        x,y=self.find(x),self.find(y)
        if x==y:
            return
        if self.data[x]<self.data[y]:
            self.data[y]=x
        elif self.data[x]>self.data[y]:
            self.data[x]=y
        else:
            self.data[x]-=1
            self.data[y]=x
        self.size-=1
        
disjoint = disjointSet(10)

disjoint.union(0, 1)
disjoint.union(1, 2)
disjoint.union(2, 3)
disjoint.union(4, 5)
disjoint.union(5, 6)
disjoint.union(6, 7)
disjoint.union(8, 9)

print(disjoint.data)
print(disjoint.size)
