# 可以删除一个元素，因此遇到不等的两个元素时，就可以跳过那个元素判断剩余的串是不是回文串
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 双指针
        # 当左右不等的时候，就判断i++的串，或者j--的串是不是回文串，如果是，则删除一个可以构成回文串，否则不可以
        left = 0
        right = len(s)-1
        while left<right:
            if s[left]!=s[right]:
                # 跳过左边元素
                s1 = s[left+1:right+1]
                # 跳过右边元素
                s2 = s[left:right]
                # 这两种情况满足一种即可
                if s1==s1[::-1] or s2==s2[::-1]:
                    return True
                else:
                    return False
            left = left+1
            right = right-1
        if left>=right:
            return True