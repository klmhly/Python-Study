class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [[] for i in range(numRows)]
        lens = len(s)
        rows = min(numRows, len(s))
        down = False
        curRow = 0
        for i in range(lens):
            res[curRow]+=s[i]
            if curRow == 0 or curRow == numRows - 1:
                down = not down
            if down:
                curRow = curRow + 1
            else:
                curRow = curRow - 1
        return res

test = Solution()
t = test.convert("PAYPALISHIRING",3)
print(''.join(t[0]+t[1]+t[2]))
print(''.join(t))