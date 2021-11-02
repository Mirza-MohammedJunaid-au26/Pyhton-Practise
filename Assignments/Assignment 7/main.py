# Q.1)

def RomanToInt(s):
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            num+=roman[s[i]]
            i+=1
      return num

st = "MCMXCIV"
print(RomanToInt(st))


# Q.2) 

def removeElement(nums, val):
   count = 0
   for i in range(len(nums)):
      if nums[i] != val:
         nums[count] = nums[i]
         count += 1
   return count

nums = [1,2,2,3,3,4,4,5]
val = 4
print(removeElement(nums,val))

# Q.3)

def maxDepth(s):
   stack = []     
   max_depth = 0
   for c in s:
      if c == '(':
         stack.append(c)                
         max_depth = max(max_depth, len(stack))
      elif c == ')':
         stack.pop()
   return max_depth

s = "(1+(2*3)+((8)/4))+1"
print(maxDepth(s))