# Q.1) 

class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        min_sum, min_index, total = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if min_sum > total:
                min_sum, min_index = total, i + 1
        return -1 if total < 0 else min_index

obj = Solution()
gas = [1,2,3,4,5]
cost =  [3,4,5,1,2]
print(obj.canCompleteCircuit(gas,cost))


# Q.2) 

import heapq
from heapq import _heapify_max, _heappop_max
class Solutionn:
    def maximumUnits(self, boxTypes, truckSize):
        
        box_list = []
        for e in boxTypes:
            box_list.append([e[1], e[0]])
        _heapify_max(box_list)
        tot_units = 0
        while box_list and truckSize > 0:
            n_u, n_b = _heappop_max(box_list)
            n_b = min(truckSize, n_b)
            truckSize -= n_b
            tot_units += (n_u * n_b)
        return tot_units
        

obj = Solutionn()
print(obj.maximumUnits([[5,10],[2,5],[4,7],[3,9]],10))


# Q.3) 

class Solution:
    def canPartition(self, nums):
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        dp = [0 for _ in range(s + 1)]
        dp[0] = 1
        for num in nums:
            for i in range(s, -1, -1):
                if dp[i]:
                    dp[i+num] = 1
            if dp[s//2]:
                return True
        return False

obj = Solution()
print(obj.canPartition([1,5,11,5]))