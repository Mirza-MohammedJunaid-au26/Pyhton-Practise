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

count=0
for i in range(len(nums)):
    if nums[i] != val:
        nums[count] = nums[i]
            count +=1
    return count