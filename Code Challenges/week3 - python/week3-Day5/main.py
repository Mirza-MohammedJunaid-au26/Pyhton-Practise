#   Q1. What will be the output ? (Easy)	(5 marks)

i = 2
p = 1

while i <= 10 :
   p = p*i
   i =  i + 1
print(p)

# Output : 3628800


#    Q2. What will be the output ? (Easy)	(5 marks)

Sum1 = 0
Sum2 = 0

i = 1

while i < 10 :

    if i%2 == 0 :
       #Sum1 = sum1+ i  # sum1 is not defined
        Sum1 = Sum1+i  # changes
    else :
       #Sum2 = sum2 + i  # sum2 is not defined
       Sum2 = Sum2+i   # changes
    i = i + 1   
print( Sum1, Sum2 )


# Case 1 : 
# Output : sum1 and sum2 is not defined

# Case 2 :
# if sum1 = Sum1 & sum2 = Sum2
# Output : 20 25



#   Q3. Print the product of first 10 even numbers.

# Ans :

product = 1
for i in range(1,21):
    if i%2==0:
        product=product*i
print(product)
        
