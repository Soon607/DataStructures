# union by rank
class disjointSet:
    def __init__(self,n):
        self.data=[-1 for _ in range(n)] # indicating its own parent(representing a separate set)
        self.size=n # the total number of disjoint sets initially
        
    def find(self,idx): # finding the representative of the set(parent)
        parent=self.data[idx]
        if parent<0:
            return idx
        return self.find(parent)
    
    def union(self,x,y): # merging the sets
        x,y=self.find(x),self.find(y)
        if x==y: # elements are already in the same set
            return
        
        # comparing size the sizes of the sets
        # the absolute value of the negative number represents the rank or height of the set
        # smaller rank is attached to the set with a larger rank
        if self.data[x]<self.data[y]:            
            self.data[y]=x 
        elif self.data[x]>self.data[y]:
            self.data[x]=y 
        else: # choosing one representative as the parent
            self.data[x]-=1 # decreasing its size by 1
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
disjoint.union(0,8)
print(disjoint.data)
print(disjoint.size)

        

        