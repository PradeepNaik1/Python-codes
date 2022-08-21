class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        res = []
        carry = 1
        if digits[-1]+1 < 10:
            digits[-1] += carry
            return digits
        for i in range(n-1,-1,-1):
            sums = digits[i] + carry
            if  sums >= 10:
                res.append(sums%10)
                carry = sums//10
            else:
                res.append(sums)
                carry = 0
        if carry:
            res.append(carry)
        return res[::-1]  
