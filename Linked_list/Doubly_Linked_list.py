# Node
class Node:
    def __init__(self,key=None):
        self.key=key
        self.next=self
        self.prev=self
    def __str__(self):
        return str(self.key)
 
 # Doubly Linked List   
class DoublyLinkedList:
    def __init__(self):
        self.head=Node() # dummy node
        self.size=0
    
    def __iter__(self): # generator
        v=self.head.next
        while v!=self.head:
            yield v
            v=v.next
            
    def __str__(self):
        return "->".join(str(v) for v in str)
    
    def __len__(self):
        return self.size
    
    def splice(self,a,b,x):
        if a==None or b==None or x==None:
            return
        # cut [a.....b]
        ap=a.prev
        bn=b.next
        
        ap.next=bn
        bn.prev=ap
        
        # insert [a...b] after x
        xn=x.next
        x.next=a
        a.prev=x
        
        xn.prev=b
        b.next=xn
        
    # moving method
    def moveAfter(self,a,x): # moving a after x
        self.splice(a,a,x)
    
    def moveBefore(self,a,x): # moving a before x
        self.splice(a,a,x.prev)
        
    # inserting 
    def insertAfter(self,x,key): # creating and inseritng new node
        self.moveAfter(self,Node(key),x)
        
    def insertBefore(self,x,key):
        self.moveBefore(self,Node(key),x)
        
    # pushfront and pushback
    
    def pushfront(self,key):
        self.insertAfter(self,self.head,key)
        
    def pushback(self,key):
        self.insertBefore(self,self.head,key)
        
    # serach
    def serach(self,key):
        v=self.head
        while v.next!=self.head:
            if v.key==key:
                return v
            v=v.next
        return None
    
    # isempty
    def isEmpty(self):
        if self.size!=0:
            return False
        else:
            return True
    #first,last
    def first(self):
        ch=self.head
        return ch.next
    
    def last(self):
        ch=self.head
        return ch.prev
    
    # removing
    def remove(self,x): # removing node x
        if x==None or x==self.head:
            pass
        else:
            x.prev.next=x.next
            x.next.prev=x.prev
            del x
                     
    # popFront & popBack
    def popFront(self):
        if self.isEmpty():
            return None
        
        else:
            key=self.head.next.key
            self.remove(self.head.next)
            return key
        
    def popBack(self):
        if self.isEmpty():
            return None
        
        else:
            key=self.head.prev
            self.remove(self.head.prev)
            return key
    
    # join
    def join(self,list):
        if self.isEmpty():
            self=list
        elif list.isEmpty():
            self=self
        else:
            self.head.prev.next=list.head.next  # self 리스트의 마지막값의 링크는 추가하고자하는 list의 head노드 다음 값
            list.head.next.prev=self.head.prev  #추가하고자하는 리스트의 첫값의 prev링크는 self리스트의 마지막값
            list.head.prev.next=self.head #추가하고자하는 리스트의 마지막값의 다음값은 self리스트의 헤드값이되어 서로 원형 연결한다
            self.head.prev=list.head.prev #self.head의 prev링크는 list의 마지막값이되어야한다.
                    
        
        
        
