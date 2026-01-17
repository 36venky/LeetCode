class Solution:
    def isPalindrome(self,x:int)->bool:
        if x < 0:
            return False
        div = 1
        while x > 10 * div:
            div *= 10
        #print(div)                       # div contains the n-1 zeros preceded with 1
        while x :
            if x // div != x % 10:        # x // 10 first digit , x % 10 last digit 
                return False
            x = (x % div) // 10           # Removing the first and last compared digits 
            #print(x,div)
            div /= 100                    # As tow digits r removed every iteration , Reduce the size of div by 2
        return True

x=Solution().isPalindrome(1221)  
print(x)
