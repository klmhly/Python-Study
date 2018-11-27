# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
# find方法：如果是字串，返回下标。否则，返回-1。
'''
输入: haystack = "hello", needle = "ll"
输出: 2
'''


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len1 = len(haystack)
        len2 = len(needle)
        if len2 == 0:
            return 0
        else:
            return haystack.find(needle)


test = Solution()
a = test.strStr('asdf','e')
b = test.strStr('asdf','s')
print(a)
print(b)