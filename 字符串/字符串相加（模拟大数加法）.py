class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s = ''
        result = ''
        len1 = len(num1)
        len2 = len(num2)
        carry = 0
        while len1 > 0 or len2 > 0 or carry:
            if len1 > 0:
                x = int(num1[len1 - 1])
                len1 = len1 - 1
            else:
                x = 0
            if len1 > 0:
                y = int(num2[len1 - 1])
                len2 = len2 - 1
            else:
                y = 0
            s = s + str((x + y + carry) % 10)
            carry = (x + y + carry) // 10
        return s



test = Solution()
rst = test.addStrings('0','0')
print(rst)