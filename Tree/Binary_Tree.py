class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self):
        self.root=Node(None)
        
        self.preorder_list=[]
        self.inorder_list=[]
        self.postorder_list=[]
        
    def add(self,item):
        if self.root.key is None:
            self.root.key=item
            
        else:
            self._add_node(self.root,item)
            
    def _add_node(self,parent,item):
        print('parent:',parent.key,'child',item)
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
                if cur.key<item:
                    if cur.right is not None:
                        return self._search_node(cur.right,item)
                    else:
                        return False
                    
    def delete(self,key):
        self._delete_node(self.root,key)
        
    def _delete_node(self,cur,key):
        if not cur:
            return False
        elif cur==self.root and cur.key==key:
            if cur.left and cur.right:
                pre_key=self._find_predecessor(cur.left)
                self._delete_node(cur,pre_key)
                cur.key=pre_key
            elif cur.left or cur.right:
                if cur.left:
                    self.root=cur.left
                elif cur.right:
                    self.root=cur.right
            else:
                self.root=None
        
        elif cur.left and cur.left.key==key:
            if cur.left.left and cur.right.right:
                pre_key=self._find_predecessor(cur.left.left)
                self._delete_node(cur,pre_key)
                cur.left.key=pre_key
            elif cur.left.left or cur.left.right:
                if cur.left.left:
                    cur.left=cur.left.left
                elif cur.left.right:
                    cur.left=cur.left.right
            else:
                cur.left=None
                
        elif cur.right and cur.right.key==key:
            if cur.right.left and cur.right.right:
                pre_key=self._find_predecessor(cur.right.left)
                self._delete_node(cur,pre_key)
                cur.right.key=pre_key
            elif cur.right.left or cur.right.right:
                if cur.right.left:
                    cur.right=cur.right.left
                elif cur.right.right:
                    cur.right=cur.right.right
            else:
                cur.right=None
        elif cur.key>key:
            return self._delete_node(cur.left,key)
        elif cur.key<key:
            return self._delete_node(cur.right,key)
        
    def _find_predecessor(self,cur):
        if cur.right:
            return self._find_predecessor(cur.right)
        if not cur.right:
            return cur.val
        
    # traversal 
    # preorder_traversal
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
            
    # inorder_traversal
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
            
    # postorder_traverse
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
        

            
    
    
