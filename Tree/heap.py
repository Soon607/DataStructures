# Heap Class

class Heap:
    def __init__(self):
        self.heap=[]
        
    def parent(self,i): # returns the parent index of the element at index i.
        return (i-1)//2
    
    def left_child(self,i): # returns the left child index of the element
        return 2*i+1    
        
    def right_child(self,i): # returns the right child index of the element
        return 2*i+2
    
    def swap(self,i,j): # swaps the elements at indices i and j in the heap
        self.heap[i],self.heap[j]=self.heap[j],self.heap[i]
        
    def insert(self,val): # Insert a value while maintaining the heap property
        
        self.heap.append(val)
        i=len(self.heap)-1 # the index of the val
        while i!=0 and self.heap[i]>self.heap[self.parent(i)]:
            self.swap(i,self.parent(i))
            i=self.parent(i)
            
    def heapify_down(self,i,heap_size): # Performs the heapify-down operation starting at the given index
        
        largest=i
        left=self.left_child(i)
        right=self.right_child(i)
        
        if left<heap_size and self.heap[left]>self.heap[largest]:
            largest=left
            
        if right<heap_size and self.heap[right]>self.heap[largest]:
            largest=right
            
        if largest!=i: # if there any changes in values
            self.swap(i,largest)
            self.heapify_down(largest,heap_size)
            
    def delete_max(self): # removing and returning the maximum element
        if len(self.heap)==0:
            return None
        
        key=self.heap[0] # the maximum value
        self.swap(0,len(self.heap-1))
        self.heap.pop()
        self.heapify_down(0,len(self.heap))
        return key
    
    def make_heap(self,_list): # Building a heap from a given list of values
        self.heap=_list
        for i in range(len(self.heap)//2-1,-1,-1):
            self.heapify_down(i,len(self.heap))
            
    def heap_sort(self): #Sorts the heap in non-decreasing order 
        n=len(self.heap)
        for i in range(n-1,0,-1):
            self.swap(0,i)
            self.heapify_down(0,i)
        
            
        