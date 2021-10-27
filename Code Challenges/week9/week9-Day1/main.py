# Q-1 ) Number of Good Pairs: 

def good_pair(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                print("(",i,",",j,")")

arr1 = [1,2,3,1,2,3,1,2,3]
good_pair(arr1)

# Q - 2) Longest Substring Without Repeating Characters

def longestSubString(s):

    i=0
    n = len(s)
    dic = {}
    max_lenght = 0

    while i < n:
        j = i
        while j < n:
            if s[j] not in dic.keys():
                dic[s[j]] = 1
                j = j+1
            else:
                if max_lenght < j-i:
                    max_lenght = j-i
                while s[i] != s[j]:
                    dic.pop(s[i]) 
                    i = i+1
                dic.pop(s[i])
                i = i+1
                break

        if j == n:
            if max_lenght < j-1:
                max_lenght = j-1
            break

    return max_lenght

s = "aabcdefg"
print(longestSubString(s))


#  Q - 3) Two Sum

def function1(arr,t):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == t:
                return i,j

arr = [1,2,3,4,5]
target = 5
print(function1(arr,target))

