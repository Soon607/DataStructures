class Node: # Node class
    def __init__(self,key):
        self.key=key # key
        self.next=None # link
        
    def __str__(self):
        return str(self.key)
    
class SinglyLinkedList:
    def __init__(self):
        self.head=None # The first node
        self.size=0 # the number of node
        
    def __str__(self):
        s=""
        v=self.head # setting key value
        while v:
            s+=str(v.key)
            v=v.next
        s+='None'
        return s
    
    def __len__(self):
        return self.size # return the number of node
    
    # appending at the beggining of list
    def pushfront(self,key):
        new_node=Node(key) # creating a new node with key value
        new_node.next=self.head
        self.head=new_node
        self.size+=1
        return True
    
    # appending at the end of list
    def pushback(self,key):
        new_node=Node(key)
        if self.size==0: # when linkedlist is empty
            self.head=new_node # new_node become head_node
        else:
            tail=self.head  # to find tail node
            while tail.next!=None: # if tail.next isn't None
                tail=tail.next # tail.next will become tail and iterate again
            tail.next=new_node # after ending of while function  connecting new node to the last node
        self.size+=1
        
    # removing first element of list and returning
    def popfront(self):
        if self.size==0:
            return None  # return None when it's empty
        else:
            X=self.head
            key=X.key
            self.head=X.next
            del X # deleting object
            self.size-=1
            return key
    
    # removing the last element of list and returning key value
    def popback(self):
        if self.size==0:
            return None
        else:
            prev,tail=None,self.head
            while tail.next!=None:
                prev=tail
                tail=tail.next
            
            if prev==None: # only one node in the list
                self.head==None
            else:
                prev.next==None 
            
            key=tail.key
            del tail
            self.size-=1
            return key
        
    # search - searching key value and returning
    
    # using while loop
    def search(self,key):
        x=self.head
        while x!=None:
            if x.key==key:
                return x
            x=x.next
        return x # None
    
    # remove
    def remove(self,key):
        if self.size==0:
            return None
        
        elif self.head.key==key:
            self.popfront()
           
        else:
           prev,tail=None,self.head
           while tail.next!=None:
               prev=tail
               tail=tail.next
               if tail.key==key:
                   prev.next=tail.next
                   del tail
                   self.size-=1
                   break
                
            
    # reverse
    def reverse(self):
        a,b=None,self.head
        while b:
            if b:
                c=b.next
                b.next=a # reversing link
            a=b
            b=c      
    
        
                
    