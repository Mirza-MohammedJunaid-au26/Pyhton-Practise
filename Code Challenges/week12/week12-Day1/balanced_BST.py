def inOrder(root,arr):

    if root == None:
        return
    
    else:
        inOrder(root.left,arr)
        arr.append(root.data)
        inOrder(root.right,arr)   

    return arr

def check_BST(root,arr):

    r = arr.index(root.data)
    
    left = arr[0:r]
    max_left = max(left)

    right = arr[r+1 : len(arr)+1]
    min_right = min(right)

    if max_left < root.data and min_right > root.data:
        print("It is a BST")
    else:
        print("It is Not a BST")


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)
Node7 = Node(7)
Node8 = Node(8)
Node9 = Node(9)

root = None
Node5.left = Node4
Node4.left = Node3
Node3.left = Node2
Node2.left = Node1
Node5.right = Node6
Node6.right = Node7
Node7.right = Node8
Node8.right = Node9
root = Node5
arr = []
inOrder(root,arr)
check_BST(root,arr)


"""
                5
            4       6
        3               7
    2                       8
1                               9
"""