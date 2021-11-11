# Q.1)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
def printList(head):
    cur = head
    while cur != None:
        print(cur.data,end = " ")
        cur = cur.next

new_head = None

def reverse_LL_rec(head,prev):
    global new_head
    if head is None:
        return
    if head.next is None:
        head.next = prev
        return head

    new_head = reverse_LL_rec(head.next,head)
    head.next = prev
    return new_head

head = Node(5)
head.next = Node(15)
head.next.next = Node(25)
head.next.next.next = Node(35)

printList(head)
print()
head_rev = reverse_LL_rec(head,None)
printList(head_rev)
print()

# Q,2) and Q.3) Not Taught in Lecture