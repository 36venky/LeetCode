class Solution():
    def longestCommonPrefix(self,str):
        minl = float('inf')
        for s in str:
            if len(s) < minl:
                minl = len(s)
        print(minl)                         # Get the length of min string !!
        i = 0
        while i < minl :
            for s in str:
                if s[i] != str[0][i]:       # Compare all the strings with any one string in it and store the common chars in s
                    return s[:i]
                
            i += 1
        return s[:i]
    
x = Solution().longestCommonPrefix(["Al","Alie","Aliec"])
print(x)
