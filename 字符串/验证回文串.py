# 回文串：逆序的串和原串相等
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 通过滤波器筛选出满足要求的串并转换成列表
        t = list(filter(str.isalnum, s.lower()))
        if t == t[::-1]:
            return True
        else:
            return False
