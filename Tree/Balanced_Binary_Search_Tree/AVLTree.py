# AVL Tree

# Node class
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        self.height=1 # default=1
        
# AVL Tree class
class AVLTree:
    def __init__(self,val):
        self.root=TreeNode(val)
        
    def get_height(self,cur):
        if not cur:
            return 0
        return cur.height
    
    def get_balance(self,cur):
        if not cur:
            return 0
        return self.get_height(cur.left)-self.get_height(cur.right)
        
    # rotation
    def left_rotate(self,cur): # balance the right-heavy subtree
        v=cur
        w=cur.right
        t=w.left
        cur=w
        w.left=v
        v.right=t
        v.height=1+max(self.get_height(v.left),self.get_height(v.right))
        w.height=1+max(self.get_height(w.left),self.get_height(w.right))
        return cur
    
    def right_rotate(self,cur): # balance the left-heavy subtree
        v=cur
        w=cur.left
        t2=w.right
        cur=w
        w.right=v
        v.left=t2
        v.height=1+max(self.get_height(v.left),self.get_height(v.right))
        w.height=1+max(self.get_height(w.left),self.get_height(w.right))
        return cur
    
    def insert(self,val):
        self.root=self.insert_node(self.root,val)
        
    def insert_node(self,cur,val):
        if not cur:
            return TreeNode(val)
        elif val<cur.val:
            cur.left=self.insert_node(cur.left,val)
        elif val>cur.val:
            cur.right=self.insert_node(cur.right,val)
            
        cur.height=1+max(self.get_height(cur.left),self.get_height(cur.right))
        balance=self.get_balance(cur) # yeild bf value
        
        if balance>1 and val<cur.left.val: #left-left
            cur=self.right_rotate(cur)
        elif balance>1 and val>cur.left.val: #left-right
            cur.left=self.left_rotate(cur.left)
            cur=self.right_rotate(cur)
        elif balance<-1 and val>cur.right.val: #right-right
            cur=self.left_rotate(cur)
        elif balance<-1 and val<cur.right<val: #right-left
            cur.right=self.right_rotate(cur.right)
            cur=self.left_rotate(cur)
        return cur
    
    def delete(self,val):
        self.root=self.delete_node(self.root,val)
        
    def find_predecessor(self,cur):
        if cur.right:
            return self.find_predecessor(cur.right)
        else:
            return cur.val
        
    def delete_node(self,cur,val):
        if not cur:
            return False
        elif cur==self.root and cur.val==val:
            if cur.left and cur.right:
                pre_val=self.find_predecessor(cur.left)
                self.delete_node(cur,pre_val)
                cur.val=pre_val
            elif cur.left or cur.right:
                if cur.left:
                    self.root=cur.left
                elif cur.right:
                    self.root=cur.right
            else:
                self.root=None
                
        elif cur.left and cur.left==val:
            if cur.left.left and cur.left.right:
                pre_val=self.find_predecessor(cur.left.left)
                self.delete_node(cur,pre_val)
                cur.left.val=pre_val
                cur.left.height=1+\
                    max(self.get_height(cur.left.left),self.get_height(cur.left.right))
            elif cur.left.left or cur.left.right:
                if cur.left.left:
                    cur.left=cur.left.left
                elif cur.left.right:
                    cur.left=cur.left.right
                cur.left.height=1+\
                    max(self.get_height(cur.left.left),self.get_height(cur.left.right))
            else:
                cur.left=None
            cur.height=1+max(self.get_height(cur.left),self.get_height(cur.right))
        
        elif cur.right and cur.right.val == val:
            if cur.right.left and cur.right.right:
                 pre_val = self._find_predecessor(cur.right.left)
                 self._delete_node(cur, pre_val)
                 cur.right.val = pre_val
                 cur.right.height = 1 + \
                     max(self._get_height(cur.right.left),
                        self._get_height(cur.right.right))
            elif cur.right.left or cur.right.right:
                if cur.right.left:
                    cur.right = cur.right.left
                elif cur.right.right:
                    cur.right = cur.right.right
                cur.right.height = 1 + \
                    max(self._get_height(cur.right.left),
                        self._get_height(cur.right.right))
            else:
                cur.right = None
            cur.height = 1 + max(self._get_height(cur.left),
                                 self._get_height(cur.right))
            
        elif cur.val>val:
            cur.left=self.delete_node(cur.left,val)
            
        elif cur.val<val:
            cur.right=self.delete_node(cur.right,val)
            
        balance=self.get_balance(cur)
        
        if balance>1 and self.get_balance(cur.left)>=0:
            cur=self.right_rotate(cur) #left-left
            
        elif balance>1 and self.get_balance(cur.left)<0:
            cur.left=self.left_rotate(cur.left)
            cur=self.right_rotate(cur) #left-right
            
        elif balance<-1 and self.get_balance(cur.right)>0:
            cur.right=self.right_rotate(cur.right)
            cur=self.left_rotate(cur) # right-left
            
        elif balance<-1 and self.get_balance(cur.right)<=0:
            cur=self.left_rotate(cur) #right-right
            
        return cur
    
    def traverse(self):
        return self._print(self.root,[])
    
    def _print(self,cur,result):
        if cur:
            self._print(cur.left,result)
            result.append(cur.val)
            self._print(cur.right,result)
        return result
    
avl=AVLTree(10)
avl.insert(5)
avl.insert(15)
avl.insert(2)
avl.insert(7)
avl.insert(11)
avl.insert(30)
avl.insert(4)
avl.insert(25)
avl.insert(40)
print(f'root balance: {avl.get_balance(avl.root)}, path: {avl.traverse()}')
        