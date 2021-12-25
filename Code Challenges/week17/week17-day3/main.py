# Q.1) Minimum Moves to Equal Array Elements

# Code :

class Solution:

    steps = 0

    def minMoves(self, nums):

        cur = nums[0]

        for i in range(1,len(nums)):
            
            if cur > nums[i]:
                ans = cur - nums[i]
                nums[i] = ans + nums[i]
                self.steps += 1

            elif cur < nums[i]:
                ans = nums[i] - cur
                nums[0] = ans + cur
                self.steps += 1
                return self.minMoves(nums)

        return self.steps          
obj=Solution()
nums = [1,2,3]
print(obj.minMoves(nums))


# Q.2) Longest Substring Without Repeating Characters

# Code :

class Solution(object):
   def lengthOfLongestSubstring(self, s):
      i =0
      j = 0
      d={}
      ans = 0
      while j < len(s):
         if s[j] not in d or i>d[s[j]]:
            ans = max(ans,(j-i+1))
            d[s[j]] = j
         else:
            i = d[s[j]]+1
            ans = max(ans,(j-i+1))
            j-=1
         #print(ans)
         j+=1
      return ans

obj = Solution()
s = "abcabcbb"
print(obj.lengthOfLongestSubstring(s))


# Q.3) 

class Solution:
    def minOperations(self, nums,x):

        x = sum(nums) - x
        
        ptr1 = 0
        ptr2 =0
        d = 0
        ans =-1

        for i in range(len(nums)):
            if d < x:
                if ptr2!= len(nums):


                    d+= nums[ptr2]
                    ptr2+=1

            if d== x:
                ans = max(ans, ptr2-ptr1)
                if ptr2!=len(nums):

                    d+= nums[ptr2]
                    ptr2+=1

            while d> x and ptr1 != ptr2:
                d-= nums[ptr1]
                ptr1+=1
        
        if d == x:
            ans = max(ans, ptr2-ptr1)

        if ans == -1:
            return -1
        
        return len(nums) -ans

obj = Solution()
nums = [1,1,4,2,3]
x = 5
print(obj.minOperations(nums,x))

