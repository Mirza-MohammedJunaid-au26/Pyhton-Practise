from collections import deque

# Q.1) 

def fourSum(nums, target):
    sort_nums = sorted(nums)
    ls = len(nums)
    res = {}
    pairs = {}
    ans = []
    for i in range(ls - 3):
        for j in range(i + 1, ls - 2):
            res_2 = sort_nums[i] + sort_nums[j]
            try:
                pairs[target - res_2].append([i, j])
            except KeyError:
                pairs[target - res_2] = [[i, j]]
    for key, temp in pairs.items():
        for pair in temp:
            j = pair[1] + 1
            k = ls - 1
            while j < k:
                current = sort_nums[j] + sort_nums[k]
                if current == key:
                    result = (sort_nums[pair[0]], sort_nums[pair[1]], sort_nums[j], sort_nums[k])
                    res[result] = True
                    j += 1
                elif current < key:
                    j += 1
                else:
                    k -= 1
    ans = list(res.keys())
    return ans

list1 = list(map(int,input().split()))
target = int(input())
print(fourSum(list1,target))


# Q.2)
class UndirectedGraphNode():
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution():
    def cloneGraph(self, node):
        if not node:
            return node
        visited = {}
        first = UndirectedGraphNode(node.label)
        visited[node.label] = first
        stack = [node]
        while stack:
            top = stack.pop()
            for n in top.neighbors:
                if n.label not in visited:
                    visited[n.label] = UndirectedGraphNode(n.label)
                    stack.append(n)
                visited[top.label].neighbors.append(visited[n.label])
        return first



