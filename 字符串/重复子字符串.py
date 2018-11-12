class Solution():
    def ma(self,s):
        return s in (s*2)[1:-1]

test = Solution()
g = test.ma('abab')
print(g)
s = 'asd'
print(s[:-1])