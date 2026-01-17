class Solution():
    def isSubsequence(self,s:str,t:str)->bool:
        S = len(s)
        T = len(t)
        j = 0

        for i in range(T):
            if t[i] == s[j]:
                if j == S-1:        # If the Substring is satisfied "in Order" return True
                    return True
                j += 1

        return False

x = Solution().isSubsequence("Alic","Alics")
print(x)