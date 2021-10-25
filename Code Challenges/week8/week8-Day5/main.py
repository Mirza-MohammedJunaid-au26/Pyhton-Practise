
# Q.1)

def reverse_string(s):

    rev = []
    print("Before Reversing :",s)
    for i in range(len(s)-1,-1,-1):
        rev.append(s[i])
    return rev

inp = list(map(str,input("Enter String :")))
print("After Reversing :",reverse_string(inp))


# Q.2)

def merge(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        merge(left)
        merge(right)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:

              l[k] = left[i]

              i += 1
            else:
                l[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k]=right[j]
            j += 1
            k += 1
    return l

list2 = [2,5,6,3,7,8,1]
print(merge(list2)) 


# Q.3)
def order(arr):
 
    a = 0
 
    for i in arr:
        if i:
            arr[a] = i
            a = a + 1
 
    for i in range(a, len(arr)):
        arr[i] = 0
 
arr = [0,1,0,3,12] 
print("Before : ",arr)
order(arr)
print("After : ",arr)
