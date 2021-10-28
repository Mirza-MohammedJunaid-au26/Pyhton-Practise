# Sum of Unique Elements: 

def unique(arr):
    dict1 = {}
    sum = 0

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] != arr[j]:
                dict1[arr[i]] = 1
            else:
                dict1.pop(arr[i])
    
    for k in dict1.keys():
        sum = sum+k
    
    return sum

    print(dict1)
arr = [1,2,3,1]
print(unique(arr))  


# Longest Common Prefix

def Commom_Prefix(arr):
    result = ""
    for i in range(len(arr[0])):
        if arr[0][i] == arr[-1][i]:
            result += arr[0][i]
        else:
            break
    return result

arr = ["flower","flow","flight"]
print("Longest Common Prefix :",Commom_Prefix(arr))