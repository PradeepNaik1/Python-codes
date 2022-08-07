class Solution:
    def reverse(self, x: int) -> int:
        
        res = 0
        if x > 0:
            while x >0:
                rem = x % 10
                res = (res*10)+rem
                x = x//10

            if  res >= -2 ** 31 and res <= (2**31)-1:
                return res
            else:
                return 0
        elif x == 0: return 0
        elif x < 0 :
            x = abs(x)
            while x > 0:
                rem = x % 10
                res = (res*10)+rem
                x = x//10

            if  res >= -2 ** 31 and res <=(2**31)-1:
                return -res
            else:
                return 0
s = Solution()
x = int(input())
print(s.reverse(x))
