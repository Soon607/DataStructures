# left rotation
def left_rotation(node):
    new_root=node.right
    node.right=new_root.left
    new_root.left=node
    return new_root
    
# right rotation
def right_rotatioin(node):
    new_root=node.left
    node.left=new_root.right
    new_root.right=node
    return new_root