class Node:
    def __init__(self,key,value,left,right):
        self.key=key
        self.value=value
        self.left=left
        self.right=right
        
    def __str__(self):
        return str(self.key,self.value)
    
class BinaryTree:
    def __init__(self):
        self.root=None
        

    def search(self,key):
        node=self.root
        while True:
            if node is None: # fail to search
                return -1
            if key==node.key:
                return node.value
            elif key<node.key:
                node=node.left
            else:
                node=node.right
    
    # inserts a node and value into the binary tree.
    def insert(self,key,value):
        def insert_node(node,key,value):
            if key==node.key: 
                return False
            
            elif key<node.key:
                if node.left is None:
                    node.left=Node(key,value,None,None)
                else:
                    insert_node(node.left,key,value)
            
            else:
                if node.right is None:
                    node.right=Node(key,value,None,None)
                else:
                    insert_node(node.right,key,value)
                    
        if self.root is None:
            self.root=Node(key,value,None,None)
            return True
        else:
            return insert_node(self.root,key,value)
        
    # deletes a value from the binary tree
    def delete(self,key):
        node=self.root
        parent=None
        left_child=True # whether node is a parent's right or left child
        
        while True:
            if node is None:
                return False
            if key==node.key:
                break
            else:
                parent=node
                if key<node.key:
                    node=node.left
                    left_child=True
                    
                else:
                    node=node.right
                    left_child=False
                    
        #After finding a key and if the key has no child or one child
        if node.left is None:
            if node is self.root:
                self.root=node.right
            elif left_child:
                parent.left=node.right
            else:
                parent.right=node.right
                
        elif node.right is None:
            if node is self.root:
                self.root=node.left
            elif left_child:
                parent.left=node.left
            else:
                parent.right=node.left
                
        # delete a node that has both child nodes
        else:
            parent=node
            node_max_left=node.left
            left_child=True
            
            while node_max_left.right is not None:
                parent=node_max_left
                node_max_left=node_max_left.right
                left_child=False
                
            node.key=node_max_left.key # replace key node with node_max_left
            node.value=node_max_left.value
            
            if left_child:
                parent.left=node_max_left.left
            else:
                parent.right=node_max_left.left
        return True
    

                
    
