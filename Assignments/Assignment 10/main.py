# Q.1) 

class Pascal:
    def generate(self, numRows):
        result = []
        
        if numRows < 1:
            return result
 
        for i in range(0, numRows):            
            row = []
            
            if i == 0:
                row.append(1)
            else:   
                row.insert(0, 1)
                row.insert(i, 1)
                
                for j in range(1, i):
                    left_above = result[i - 1][j  - 1]
                    right_above = result[i - 1][j]
                    row.insert(j, left_above + right_above)
                
            result.append(row)
                    
        return result

obj = Pascal()
print(obj.generate(5))


# Q.2) 

class Pascal_Two:
    def getRow(self, rowIndex):
        res = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                res[j] += res[j - 1]
            res.append(1)
        return res

obj1 = Pascal_Two()
print(obj1.getRow(5))


# Q.3)

class Stocks(object):
    def BestTime(self, prices):
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for p in prices[1:]:
            if p < min_price:
                min_price = p
            elif max_profit < p - min_price:
                max_profit = p - min_price
        return max_profit

obj2 = Stocks()
chart = [7,1,5,3,6,4]
print(obj2.BestTime(chart)) 
