# Q - 1 ) Sort Array by Increasing Frequency

arr = [1,2,3,4,5,1,2,3,4,1,2,3,1,2,1]
new_arr = []
dict1 = {}
i = 0 
while i<len(arr):
    count = 0
    a = arr[i]
    for j in range(i,len(arr)):
        if arr[i]==arr[j]:
            count = count + 1
    up = dict({a:count})
    if a not in dict1.keys():
        dict1.update(up)
    i = i+1

for i in dict1.values():
    if i < i+1:
       new_arr.append(i)
print(new_arr)



# Q- 2 ) Average Salary Excluding the Minimum and Maximum Salary

def min_and_nax(arr):
    total = 0
    average = 0
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    arr.pop(0)
    n = len(arr)
    arr.pop(n-1)

    for k in range(n-1):
        total = total + arr[k]

    average = total//(n-1)
    return average

arr = [3000,4000,1000,2000,5000]
print(min_and_nax(arr))



# Q - 3 ) Valid Anagram

def anagram(str1,str2):
    n1 = len(str1)
    n2 = len(str2)
    
    if n1 != n2 :
        return 0
    
    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(n1):
        if str1[i] != str2[i]:
            return 0
    return 1

str1 = "anagram"
str2 = "nagaram"

if anagram(str1, str2):
    print("true")
else:
    print("false")