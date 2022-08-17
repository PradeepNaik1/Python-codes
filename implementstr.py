class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(list(haystack))
        n = len(list(needle))
        if n > 0:
            for i in range((m-n)+1):
                count = 0
                for j in range(n):

                    if haystack[j+i] != needle[j] :
                        break
                    else:
                        count+= 1
                if count == n:
                    return i
            return -1
        else:
            return 0
