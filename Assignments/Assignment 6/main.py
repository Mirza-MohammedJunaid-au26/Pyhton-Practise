# """
# Q1. Count no occurrences of each number in a list.
# list = [ 1, 2, 1, 4, 5, 9, 10, 4, 1, 10, 5, 4] 
# """
# def occurence(l,occ):
#     for i in range(len(l)-1):
#         x=l[i]
#         c=0
#         for j in range(i,len(l)):
#             if l[j]==l[i]:
#                 c=c+1
#         count=dict({x:c})
#         if x not in occ.keys():
#             occ.update(count)
#     return occ
 
# list1 = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# occ = {}
# print(occurence(list1,occ))


# """
# Q2. Print the pattern for a given integer N, where input for N is user taken:
# """

# inp = int(input("Enter :"))

# for i in range(1,inp+1):
#     for j in range(i,0,-1):
#         print("."*i,"*"*j)

a = [1,2,1,3,4,1,6,3]
count = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
       if a[i] == a[j]:
           count +=1
    print(a[i],":",count)
