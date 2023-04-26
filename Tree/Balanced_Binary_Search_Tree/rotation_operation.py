# maintain the balance of the tree

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
# right rotation

def rotateRight(Node):
    if Node==0:
        return 
    if Node.left==None:
        return
    
    b=Node.left.right
    
    Node.left.parent=Node.parent
    if Node.parent:
        if Node.parent.left==Node:
            Node.parent.left=Node.left
        else:
            Node.parent.right=Node.left
            
    Node.left.right=Node
    Node.parent=Node.left
    
    Node.left=b
    
    if b:
        b.parent=Node
        
    if Node.root==Node:
        Node.root