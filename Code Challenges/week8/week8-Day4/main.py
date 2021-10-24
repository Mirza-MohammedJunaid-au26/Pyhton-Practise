# Q.1)

# Ans :

def intersection_array(n1,n2):
    l1 = len(n1)
    l2 = len(n2)
    list1 = []

    for i in range(l1-1):
        for j in range(l2-1):
            if n1[i] == n2[j]:
                list1.append(n1[i])
    return list1


num1 = [1,2,2,1]
num2 = [2,2]
print(intersection_array(num1,num2))


# Q.2)

# Ans :

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

# Ans :

def mergeSort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        mergeSort(left)
        mergeSort(right)

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

list2 = [2,0,2,1,1,0]
print(mergeSort(list2))


