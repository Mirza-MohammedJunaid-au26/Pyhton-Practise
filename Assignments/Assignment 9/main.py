# Q.1)

def Frequency(arr):
    
    freq = []
    dic = {}
    a = 0

    for i in arr:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    
    for k,v in dic.items():
        freq.append(k)

    return freq[0:2]    


arr = [1,1,1,2,2,3]
print(Frequency(arr))

# Q.2) 

class Node:
 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def lca(root, n1, n2):
     
    if root is None:
        return None
 
    if(root.data > n1 and root.data > n2):
        return lca(root.left, n1, n2)
 
    if(root.data < n1 and root.data < n2):
        return lca(root.right, n1, n2)
 
    return root
 
 
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
 
n1 = 10 ; n2 = 14
t = lca(root, n1, n2)
print (n1, n2, t.data)
 
n1 = 14 ; n2 = 8
t = lca(root, n1, n2)
print (n1, n2 , t.data)
 
n1 = 10 ; n2 = 22
t = lca(root, n1, n2)
print (n1, n2, t.data)
 

# Q.3)

def preOrder(root1,root2):
    ans = False
    if root1 == None or root2 == None:
        return 
    
    if root1.data != root2.data:
        return ans
    else:
        print(root1.data,root2.data)
        preOrder(root1.left,root2.left)
        preOrder(root1.right,root2.right)
        ans = True
    return ans

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

Node10 = Node(1)
Node11 = Node(2)
Node12 = Node(3)
Node13 = Node(4)
Node14= Node(5)
Node15= Node(6)
Node16 = Node(7)
Node17 = Node(8)
Node18 = Node(9)

Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node2.right = Node5
Node3.left = Node6
Node3.right = Node7
Node4.left = Node8
Node4.right = Node9

Node10.left = Node11
Node10.right = Node12
Node11.left = Node13
Node11.right = Node14
Node12.left = Node15
Node12.right = Node16
Node13.left = Node17
Node13.right = Node18

root1 = Node1
root2 = Node10

print("Ans :",preOrder(root1,root2))
