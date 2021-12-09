# Q.1) 

def validIPAddress(IP):

        def isIPv4(IP):
            ip = IP.split('.')
            for s in ip:
                if len(s) == 0 or len(s) > 3:
                    return 'Neither'
                if ((s[0] == '0' and len(s) != 1) or not s.isdigit() or int(s) > 255):
                    return 'Neither'
            return 'IPv4'

        def isIPv6(IP: str) -> str:
            ip = IP.split(':') 
            for s in ip:
                if len(s) == 0 or len(s) > 4:
                    return "Neither"
                for c in s:
                     if c not in '0123456789abcdef':
                        return "Neither"
            return 'IPv6'

        if len(IP.split('.'))-1 == 3:
            return isIPv4(IP)
        elif len(IP.split(':'))-1 == 7:
            return isIPv6(IP.lower())
        return "Neither"

inp = input()
print(validIPAddress(inp))


# Q.2)

def letterCombinations(digits):
    if len(digits) == 0:
        return []
    characters = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    result = []
    solve(digits,characters,result)
    return result
def solve(digits, characters, result, current_string="",current_level = 0):
    if current_level == len(digits):
        result.append(current_string)
        return
    for i in characters[int(digits[current_level])]:
        solve(digits,characters,result,current_string+i,current_level+1)
inp = input()
print(letterCombinations(inp))


# Q.3)

def uniquePathsIII(grid):
    startx = starty = empty = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            cell = grid[row][col] 
            if cell >= 0:
                empty += 1
            if cell == 1:
                startx, starty = row, col
    return dfs(grid, startx, starty, empty)
        
def dfs(grid, x, y, step):
    if grid[x][y] == 2: 
        return step == 1
    ret = 0
    cur = grid[x][y]
    grid[x][y] = -2
    for dirx, diry in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        tx, ty = x + dirx, y + diry
        if 0 <= tx < len(grid) and 0 <= ty < len(grid[0]) and grid[tx][ty] >= 0:
            ret += dfs(grid, tx, ty, step - 1)
    grid[x][y] = cur
    return ret

lis = list(map(int,input().split()))
print(uniquePathsIII(lis))

