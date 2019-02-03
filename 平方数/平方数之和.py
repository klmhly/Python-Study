'''
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a**2 + b**2 = c。
示例1:
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5


示例2:
输入: 3
输出: False
'''

import math
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(math.sqrt(c))+1):
            x = math.sqrt(c - i ** 2)
            if x == int(x):
                return True
        return False