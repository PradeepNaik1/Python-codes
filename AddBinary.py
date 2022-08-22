class Solution:
    
    def addBinaryLogic(self, n, a, b):
        res = ""
        i = n-1
        carry = "0"
        while i >= 0:
            if a[i] == b[i] and carry == "1":
                if a[i] == "1":
                    res = "1" + res
                else:
                    res = "1" + res
                    carry = "0"      
            elif a[i] == b[i] and carry == "0":
                if a[i] == "1":
                    res = "0" + res
                    carry = "1"
                else:
                    res = "0" + res      
            elif a[i] != b[i]:
                if carry == "1":
                    res = "0" + res
                    carry = "1"
                else:
                    res = "1" + res
            i -= 1
        if carry == "1":
            res = "1" + res
        return res
      
    #logic starts here
    def addBinary(self, a: str, b: str) -> str:
        n = len(list(a))
        m = len(list(b))
        if n > m:
            for i in range(n-m):
                b = "0" + b     
            res = self.addBinaryLogic(n,a,b)
            return res
        n = len(list(b))
        m = len(list(a))
        if n > m:
            for i in range(n-m):
                a = "0" + a            
            res = self.addBinaryLogic(n,a,b)
            return res
        if n == m:
            res = self.addBinaryLogic(n,a,b)
            return res
    
    
