class Node:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.left=None
        self.right=None
        self.color='Red' # Initial color
        
class RedBlackTree:
    def __init__(self):
        self.root=None
        self.inserted_node=None
        
    def find(self,data):
        return self._find_data(self.root,data)
    
    def _find_data(self,root,data):
        if root is None or root.data==data:
            return root
        elif root.data>=data:
            return self._find_data(root.left,data)
        elif root.data<data:
            return self._find_data(root.right,data)
            
    def insert(self,data):
        self.root=self._insert_node(self.root,data,None)
        self._balancing(self.inserted_node)
        return
    
    def _insert_node(self,cur,data,parent):
        if cur is None:
            cur=Node(data)
            cur.parent=parent
            self.inserted_node=cur
        else:
            if data<cur.data:
                cur.left=self._insert_node(cur.left,data,cur)
            elif data>cur.data:
                cur.right=self._insert_node(cur.right,data,cur)
        return cur
    
    def _balancing(self,node):
        P=node.parent
        if P is None: #if node is root node
            node.color='Black'
        else:
            if P.color=='Red':
                G=P.parent # grandparent must exist
                U=None
            if G.left==P:
                U=G.right
            elif G.right==P:
                U=G.left
                
            if U is not None and U.color=='Red':
                # parent,uncle-Black, grandparend-Red
                P.color,U.color="Black","Black"
                G.color="Red"
                # rebalancing from grandparent
                self._balancing(G)
                
            else: # Uncle is None or uncle.color is black
                if P==G.left and P.left==node: # LL case
                    G.color,P.color=P.color,G.color
                    self._right_rotate(G)
                    
                elif P==G.left and P.right==node: #LR case
                    self._left_rotate(P)
                    G.color,node.color=node.color,G.color
                    self._right_rotate(G)
                    
                elif P==G.right and P.right==node: #RR case
                    G.color,P.color=P.color,G.color
                    self._left_rotate(G)
                    
                elif P==G.right and P.left==node: #RL case
                    self._right_rotate(P)
                    G.color,node.color=node.color,G.color
                    self._left_rotate(G)
                    
    def _find_min_successor(self,node):
        if node.left is None:
            return node
        else:
            return self._find_min_successor(node.left)
        
    def delete(self,data):
        node=self._get_delete_node(self.root,data)
        if node is None:
            return False
        self._delete_node(node)
        return True
    
    def _get_delete_node(self, node, data):
        if node.data > data:
            return self._get_delete_node(node.left, data)
        elif node.data < data:
            return self._get_delete_node(node.right, data)
        elif node.data == data:
            # check left, right child
            left = node.left
            right = node.right
            if left is not None and right is not None:
                # delete node has both child
                # swap value of minimum successor and delete node
                min_successor = self._find_min_successor(node.right)
                node.data, min_successor.data = min_successor.data, node.data
                return min_successor
            else:
                return node