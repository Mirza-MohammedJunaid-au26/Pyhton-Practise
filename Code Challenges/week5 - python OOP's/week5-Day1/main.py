# Q1. Write a program to find the count of all even no’s and odd no’s in an array / list
                            #and
# Q2. Write a program to create a dictionary for above program


list1 = [1,2,3,4,5,6,7,8,9,10]
dict1 = {}

def even_or_odd(l,d):
    even_count = 0
    odd_count = 0
    for i in range(1,len(l)+1):
        if i%2==0:
            even_count=even_count+1
        else:
            odd_count=odd_count+1

    d["Odd"]=odd_count
    d["Even"]=even_count

    print("Q.1")
    print("Even Number Count : ",even_count)
    print("Odd Number Count : ",odd_count)
    print()
    print("Q.2")
    print(d)

even_or_odd(list1,dict1)


# Q3. Write a program to find the count of every vowel in a string

word = input("Enter Word : ")
vowel_dict = {}

def vowels(w):
    a_count=0
    e_count=0
    i_count=0
    o_count=0
    u_count=0
    
    for i in w:
        if i=="a":
            a_count = a_count+1
        elif i=="e":
            e_count = e_count+1
        elif i=="i":
            i_count = i_count+1
        elif i=="o":
            o_count = o_count+1
        elif i=="u":
            u_count = u_count+1

    vowel_dict["a"]=a_count
    vowel_dict["e"]=e_count
    vowel_dict["i"]=i_count
    vowel_dict["o"]=o_count
    vowel_dict["u"]=u_count
    return vowel_dict

print("Q.3")
print(vowels(word))
