class Solution():
    def romenToInterger(self,s:str)->int:
        d = {'I':1,                             
             'V':5,                               # Pre-defined Roman Values !! 
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000}
        sum = 0
        n = len(s)
        i = 0
 
        while i < n:
            if i < n-1 and d[s[i]] < d[s[i-1]]:  # If the value of next ele is greater then,add the diff of it to the sum else 
                sum += d[s[i+1]] - d[s[i]]       #  add its value to the sum , with an edge case of (n-1)
                i += 2
            else:
                sum += d[s[i]]
                i += 1
        return sum

x = Solution().romenToInterger("V")
print(x)