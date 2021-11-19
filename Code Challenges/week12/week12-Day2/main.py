# Q.1) and # Q.2) Not Taught in Lecture

# Q.3)

def Merge_Tree(r1,r2,r3):
    
    for i in range(len(r1)):
        if r1[i] != None and r2[i] != None:
            r3.append(r1[i]+r2[i])
        elif r1[i] == None or r2[i] == None:
            r3.append(r1[i]) 
            r3.append(r2[i])

    return r3 
    

root1 = [1,3,2,5,None,None,None]
root2 = [2,1,3,None,4,None,7]
root3 = []
print(Merge_Tree(root1,root2,root3))
