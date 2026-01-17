class Solution():
    def mergeStrings(self,s1:str,s2:str) -> str:
        A , B = len(s1) , len(s2)
        a , b = 0 , 0
        s = []
        word = 1

        while(a < A and b < B):         # A Part of merge Sort method !!
            if word == 1:
                s.append(s1[a])
                a += 1
                word = 2
            else:
                s.append(s2[b])
                b += 1
                word = 1

        while a < A:
            s.append(s1[a])
            a += 1

        while b < B:
            s.append(s2[b])
            b += 1 
        return ''.join(s)               # Strings r immutable chanf=ginf its value will be : O(n) , use list : O(1) !!

x = Solution().mergeStrings("Bob","Alice")
print(x)