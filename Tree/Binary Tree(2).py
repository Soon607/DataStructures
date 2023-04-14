# making Node
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        
# making BinaryTree
class BinaryTree:
    def __init__(self):
        self.root=Node(None)
        
        self.preorder_list=[]
        self.inorder_list=[]
        self.postorder_list=[]
        
     # adding values in the binary tree           
    def add(self,item):
        # when there is no value in the root node
        if self.root.key is None:
            self.root.key=item
        
        # if the root node has no value, inserting that node's left or right child node
        else:
            self._add_node(self.root,item)
            
    def _add_node(self,parent,item):
        print('parent:',parent.key,'child',item)
        # if root(parent)>item, locate at the left child
        if parent.key>item:
            if parent.left is not None:
                self._add_node(parent.left,item)
            else:
                parent.left=Node(item)
                
        else:
            if parent.right is not None:
                self._add_node(parent.right,item)
            else:
                parent.right=Node(item)
             
    # search the binary tree
    def search(self,item):
        if self.root.key is None:
            return False
        else:
            return self._search_node(self.root,item)
        
    def _search_node(self,cur,item):
        print(cur.key,item)
        if cur.key==item:
            return True
        else:
            if cur.key>item:
                if cur.left is not None:
                    return self._search_node(cur.left,item)
                else:
                    return False
                
            else:
                if cur.right is not None:
                    return self._search_node(cur.right,item)
                else:
                    False
                    
    # delete function
    def remove(self,item):
        if self.root.key==item:
            # has no child nodes
            if self.root.left==None and self.root.right==None:
                self.root.key=None
            # has one child node
            elif self.root.left==None and self.root.right!=None:
                self.root=self.root.right
            elif self.root.left!=None and self.root.right==None:
                self.root=self.root.left
            # has both child nodes
            else:
                self.root.key=self._most_left(self.root.right)
        else:
            if self.root.key>item:
                self._remove(self.root,self.root.left,item)
            else:
                # print(self.root.key,self.root.right.key,item)
                self._remove(self.root,self.root.right,item)
                
    def _remove(self,parent,cur,item):
        print(parent.key,cur.key,item)
        if cur is None:
            print('No item',item)
            
        if cur.key==item:
            # has no child nodes
            if cur.left==None and cur.right==None:
                print('here')
                if parent.left==cur:
                    parent.left=None
                else:
                    parent.right=None
            # has one child node
            elif cur.left==None and cur.right!=None:
                if parent.left==cur:
                    parent.left=cur.right
                else:
                    parent.right=cur.right
            
            elif cur.left!=None and cur.right==None:
                if parent.left==cur:
                    parent.left=cur.left
                else:
                    parent.right=cur.left
            # has both child nodes
            if cur.left!=None and cur.right!=None:
                cur.key=self._most_left(cur.right).key
                self._removeitem(cur,cur.right,cur.key)
            
        else:
            if cur.key>item:
                self._remove(cur,cur.left,item)
            else:
                self._remove(cur,cur.right,item)
                
    # finds the leftmost child node of the righ child node
    def _most_left(self,cur):
        if cur.left==None:
            return cur
        else:
            return self._most_left(cur.left)
            
    # when has both child, remove and move the leftmost child
    def _removeitem(self,parent,cur,item):
        if cur.key==item:
            if parent.left==cur:
                parent.left=None
            else:
                parent.right=None
        else:
            if cur.val>item:
                self._removeitem(cur,cur.left,item)
            else:
                self._removeitem(cur,cur.right,item)
    
            
            
    
    # traversal function
    # 1. preorder_traversal
    def preorder_traverse(self):
        if self.root is not None:
            self._preorder(self.root)
            
    def _preorder(self,cur):
        self.preorder_list.append(cur.key)
        print(cur.key)
        if cur.left is not None:
            self._preorder(cur.left)
        if cur.right is not None:
            self._preorder(cur.right)
            
    #2. inorder_traversal
    def inorder_traverse(self):
        if self.root is not None:
            self._inorder(self.root)
            
    def _inorder(self,cur):
        if cur.left is not None:
            self._inorder(cur.left)
            
        self.inorder_list.append(cur.key)
        print(cur.key)
        
        if cur.right is not None:
            self._inorder(cur.right)
    
    #3. postorder_traverse        
    def postorder_traverse(self):
        if self.root is not None:
            self._postorder(self.root)
            
    def _postorder(self,cur):
        if cur.left is not None:
            self._postorder(cur.left)
        
        if cur.right is not None:
            self._postorder(cur.right)
            
        self.postorder_list.append(cur.key)
        print(cur.key)
